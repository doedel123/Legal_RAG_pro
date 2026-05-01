#!/usr/bin/env python3
"""
Einmalige Einrichtung eines Gemini File Search Stores
======================================================
  1. Legt einen File Search Store an (Name: 'strafrecht')
  2. Splittet die grossen Markdowns an ## Seite-Grenzen in ~1 MB Stuecke
     (Gemini bricht bei sehr grossen Single-Files mit STATE_FAILED ab)
  3. Laedt jedes Teil-File hoch und wartet auf serverseitige Indexierung
  4. Gibt die Store-Resource-ID aus, die in .env.local eingetragen wird:
        GEMINI_FILE_SEARCH_STORE=<id>

Nutzung:
    python setup_gemini.py
    python setup_gemini.py --reuse           # existierenden Store mit gleichem Namen weiterverwenden
    python setup_gemini.py --recreate        # existierenden Store loeschen + neu anlegen
    python setup_gemini.py --max-mb 1.5      # Ziel-Groesse pro Teil-File in MB (default: 1.0)
    python setup_gemini.py --method import   # Files API + import_file (default)
    python setup_gemini.py --method direct   # JS-kompatibel: nur display_name
    python setup_gemini.py --method direct-config  # mit mime_type + chunking_config
"""

import argparse
import concurrent.futures
import json
import os
import re
import sys
import tempfile
import time
from pathlib import Path
from urllib import error as urlerror
from urllib import parse, request

from dotenv import load_dotenv
from google import genai
from google.genai import types

# Gemini File Search indexing is sensitive to bursty uploads. Default to one
# in-flight operation; increase with --parallel only when quota is known.
DEFAULT_UPLOAD_PARALLELISM = 1

STORE_DISPLAY_NAME = "strafrecht"
FILES_TO_UPLOAD = [
    "data/fachliteratur/Strafrecht/StGB_Kommentar/StGB_Kommentar.md",
    "data/fachliteratur/Strafrecht/StPO_Kommentar/Strafprozessordnung.md",
]
PAGE_MARKER = re.compile(r"^## Seite (\d+)\s*$", re.MULTILINE)
DEFAULT_MAX_MB = 1.0
DEFAULT_POLL_SEC = 15
DEFAULT_PAUSE_SEC = 20
DEFAULT_RETRIES = 6
MAX_BACKOFF_SEC = 300
MARKDOWN_MIME_TYPE = "text/markdown"
MAX_GEMINI_CHUNK_TOKENS = 512
DEFAULT_CHUNK_TOKENS = 512
DEFAULT_CHUNK_OVERLAP = 100
DEFAULT_UPLOAD_METHOD = "direct"


class ImportAuthenticationError(RuntimeError):
    """Raised when Gemini importFile rejects otherwise valid API-key auth."""


def split_markdown_at_pages(md_path: Path, max_bytes: int) -> list[tuple[str, str]]:
    """Splittet eine Markdown-Datei an ## Seite-Grenzen in ~max_bytes grosse Stuecke.

    Returns: Liste von (display_name, content) Tupeln.
    """
    text = md_path.read_text(encoding="utf-8")

    # Spalte am Page-Marker, behalte Marker im Folge-Stueck
    parts = PAGE_MARKER.split(text)
    # parts = [pre, page1_num, page1_content, page2_num, page2_content, ...]
    pages: list[tuple[int, str]] = []
    if parts[0].strip():
        pages.append((0, parts[0]))
    for i in range(1, len(parts), 2):
        page_num = int(parts[i])
        content = f"## Seite {page_num}\n{parts[i + 1] if i + 1 < len(parts) else ''}"
        pages.append((page_num, content))

    # Greedy zu Stuecken zusammenfuehren bis max_bytes erreicht
    chunks: list[str] = []
    cur_parts: list[str] = []
    cur_size = 0
    for _, content in pages:
        size = len(content.encode("utf-8"))
        if cur_parts and cur_size + size > max_bytes:
            chunks.append("\n".join(cur_parts))
            cur_parts, cur_size = [], 0
        cur_parts.append(content)
        cur_size += size
    if cur_parts:
        chunks.append("\n".join(cur_parts))

    # Deterministische Namen mit Teil-Index (Seitenzahlen sind wegen
    # Merge aus Teil-Files nicht monoton und nicht eindeutig)
    base = md_path.stem
    width = len(str(len(chunks)))
    return [
        (f"{base}_part{idx+1:0{width}d}.md", content)
        for idx, content in enumerate(chunks)
    ]


def find_existing_store(client):
    for store in client.file_search_stores.list():
        if getattr(store, "display_name", None) == STORE_DISPLAY_NAME:
            return store
    return None


def is_transient_error(err: Exception | str) -> bool:
    msg = str(err)
    transient_markers = (
        "429",
        "500",
        "502",
        "503",
        "504",
        "INTERNAL",
        "RESOURCE_EXHAUSTED",
        "UNAVAILABLE",
        "DEADLINE_EXCEEDED",
        "Too Many Requests",
        "quota",
    )
    return any(marker.lower() in msg.lower() for marker in transient_markers)


def operation_error_text(op) -> str | None:
    err = getattr(op, "error", None)
    if not err:
        return None
    code = getattr(err, "code", None)
    message = getattr(err, "message", None)
    status = getattr(err, "status", None)
    details = getattr(err, "details", None)
    parts = [str(v) for v in (code, status, message) if v]
    if details:
        parts.append(str(details))
    return " | ".join(parts) or str(err)


def wait_for_operation(client, op, label: str, poll_sec: int = DEFAULT_POLL_SEC):
    """Pollt die Long-Running-Operation bis sie abgeschlossen ist."""
    start = time.time()
    while not op.done:
        elapsed = int(time.time() - start)
        print(f"  {label}: {elapsed}s…", end="\r", flush=True)
        time.sleep(poll_sec)
        op = client.operations.get(op)
    op_error = operation_error_text(op)
    if op_error:
        raise RuntimeError(f"{label}: Operation fehlgeschlagen: {op_error}")
    print(f"  {label}: fertig nach {int(time.time() - start)}s.        ")
    return op


def chunking_config(args) -> dict:
    return {
        "white_space_config": {
            "max_tokens_per_chunk": args.chunk_tokens,
            "max_overlap_tokens": args.chunk_overlap,
        }
    }


def rest_chunking_config(args) -> dict:
    return {
        "whiteSpaceConfig": {
            "maxTokensPerChunk": args.chunk_tokens,
            "maxOverlapTokens": args.chunk_overlap,
        }
    }


def upload_direct(client, store_name: str, display_name: str, path: Path, args):
    return client.file_search_stores.upload_to_file_search_store(
        file=str(path),
        file_search_store_name=store_name,
        config={"display_name": display_name},
    )


def upload_direct_config(client, store_name: str, display_name: str, path: Path, args):
    return client.file_search_stores.upload_to_file_search_store(
        file=str(path),
        file_search_store_name=store_name,
        config={
            "display_name": display_name,
            "mime_type": MARKDOWN_MIME_TYPE,
            "chunking_config": chunking_config(args),
        },
    )


def import_file_rest(client, store_name: str, file_name: str, args):
    api_key = getattr(getattr(client, "_api_client", None), "api_key", None)
    if not api_key:
        raise RuntimeError("REST import_file Fallback ohne API-Key nicht moeglich")
    body = json.dumps({
        "fileName": file_name,
        "chunkingConfig": rest_chunking_config(args),
    }).encode("utf-8")
    query = parse.urlencode({"key": api_key})
    url = (
        "https://generativelanguage.googleapis.com/v1beta/"
        f"{store_name}:importFile?{query}"
    )
    req = request.Request(
        url,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": api_key,
        },
    )
    try:
        with request.urlopen(req, timeout=120) as resp:
            payload = json.loads(resp.read().decode("utf-8") or "{}")
    except urlerror.HTTPError as e:
        details = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"REST import_file fehlgeschlagen: HTTP {e.code} {details}") from e
    except urlerror.URLError as e:
        raise RuntimeError(f"REST import_file fehlgeschlagen: {e}") from e
    return types.ImportFileOperation.from_api_response(payload)


def upload_via_file_import(client, store_name: str, display_name: str, path: Path, args):
    uploaded = None
    try:
        uploaded = client.files.upload(
            file=str(path),
            config={
                "display_name": display_name,
                "mime_type": MARKDOWN_MIME_TYPE,
            },
        )
    except Exception as e:
        raise RuntimeError(f"files.upload fehlgeschlagen: {e}") from e
    try:
        return client.file_search_stores.import_file(
            file_search_store_name=store_name,
            file_name=uploaded.name,
            config={"chunking_config": chunking_config(args)},
        )
    except Exception as e:
        if "401" in str(e) or "UNAUTHENTICATED" in str(e):
            try:
                return import_file_rest(client, store_name, uploaded.name, args)
            except Exception as rest_error:
                try:
                    client.files.delete(name=uploaded.name)
                except Exception as delete_error:
                    print(
                        f"  (konnte temporaere Datei {uploaded.name} "
                        f"nicht loeschen: {delete_error})"
                    )
                raise ImportAuthenticationError(
                    "import_file SDK und REST-Fallback fehlgeschlagen "
                    f"fuer {uploaded.name}: SDK={e}; REST={rest_error}"
                ) from rest_error
        raise RuntimeError(
            f"import_file fehlgeschlagen fuer {uploaded.name}: {e}"
        ) from e


def patch_resumable_upload_auth(client) -> None:
    """Work around SDK upload calls that can omit x-goog-api-key on final POST."""
    api_client = getattr(client, "_api_client", None)
    api_key = getattr(api_client, "api_key", None)
    if not api_client or not api_key:
        return
    original_upload_file = api_client.upload_file

    def upload_file_with_api_key(file_path, upload_url, upload_size, *, http_options=None):
        if http_options is None:
            http_options = types.HttpOptions()
        elif isinstance(http_options, dict):
            http_options = types.HttpOptions(**http_options)
        headers = dict(http_options.headers or {})
        headers.setdefault("x-goog-api-key", api_key)
        http_options.headers = headers
        return original_upload_file(
            file_path,
            upload_url,
            upload_size,
            http_options=http_options,
        )

    api_client.upload_file = upload_file_with_api_key


def main():
    parser = argparse.ArgumentParser(description="Gemini File Search Store einrichten")
    parser.add_argument("--reuse", action="store_true",
                        help="Bestehenden Store (gleicher display_name) weiterverwenden")
    parser.add_argument("--recreate", action="store_true",
                        help="Bestehenden Store loeschen und neu anlegen")
    parser.add_argument("--max-mb", type=float, default=DEFAULT_MAX_MB,
                        help=f"Ziel-Groesse pro Teil-File in MB (default: {DEFAULT_MAX_MB})")
    parser.add_argument("--env-file", default=".env.local")
    parser.add_argument("--parallel", type=int, default=DEFAULT_UPLOAD_PARALLELISM,
                        help=f"Parallele Uploads (default: {DEFAULT_UPLOAD_PARALLELISM})")
    parser.add_argument("--pause-sec", type=int, default=DEFAULT_PAUSE_SEC,
                        help=f"Pause nach erfolgreichem Upload (default: {DEFAULT_PAUSE_SEC})")
    parser.add_argument("--poll-sec", type=int, default=DEFAULT_POLL_SEC,
                        help=f"Polling-Intervall fuer Operationen (default: {DEFAULT_POLL_SEC})")
    parser.add_argument("--retries", type=int, default=DEFAULT_RETRIES,
                        help=f"Retries pro Teil-File bei 429/5xx (default: {DEFAULT_RETRIES})")
    parser.add_argument("--chunk-tokens", type=int, default=DEFAULT_CHUNK_TOKENS,
                        help=f"Gemini Chunk-Groesse in Tokens (default: {DEFAULT_CHUNK_TOKENS})")
    parser.add_argument("--chunk-overlap", type=int, default=DEFAULT_CHUNK_OVERLAP,
                        help=f"Gemini Chunk-Overlap in Tokens (default: {DEFAULT_CHUNK_OVERLAP})")
    parser.add_argument("--method", choices=("direct", "direct-config", "import"), default=DEFAULT_UPLOAD_METHOD,
                        help="Upload-Methode: direct=JS-kompatibel, direct-config=mit MIME/Chunking, import=Files API + import_file")
    args = parser.parse_args()
    if not 0 <= args.chunk_tokens <= MAX_GEMINI_CHUNK_TOKENS:
        parser.error(
            f"--chunk-tokens muss zwischen 0 und {MAX_GEMINI_CHUNK_TOKENS} liegen"
        )
    if args.chunk_overlap < 0:
        parser.error("--chunk-overlap darf nicht negativ sein")
    if args.chunk_overlap > args.chunk_tokens:
        parser.error("--chunk-overlap darf nicht groesser als --chunk-tokens sein")

    load_dotenv(args.env_file, override=True)
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY fehlt in", args.env_file)
        sys.exit(1)

    client = genai.Client(api_key=api_key)
    patch_resumable_upload_auth(client)

    # --- Store erstellen / holen ---
    existing = find_existing_store(client)
    if existing:
        if args.recreate:
            print(f"▶ Loesche bestehenden Store: {existing.name}")
            client.file_search_stores.delete(name=existing.name, config={"force": True})
            existing = None
        elif args.reuse:
            print(f"▶ Verwende bestehenden Store: {existing.name}")
            store = existing
        else:
            print(f"Ein Store mit display_name='{STORE_DISPLAY_NAME}' existiert bereits:")
            print(f"  {existing.name}")
            print("Nutze --reuse zum Weiterverwenden oder --recreate zum Neu-Anlegen.")
            sys.exit(1)

    if not existing:
        print(f"▶ Erstelle File Search Store: display_name='{STORE_DISPLAY_NAME}'")
        store = client.file_search_stores.create(
            config={"display_name": STORE_DISPLAY_NAME},
        )
        print(f"  → {store.name}")

    # --- Failed Documents loeschen + erkennen welche Teil-Files schon ACTIVE sind ---
    existing_docs = list(client.file_search_stores.documents.list(parent=store.name))
    failed = [d for d in existing_docs
              if str(getattr(d, "state", "")).endswith("STATE_FAILED")]
    for d in failed:
        print(f"▶ Loesche FAILED Dokument: {d.display_name}")
        client.file_search_stores.documents.delete(name=d.name, config={"force": True})

    # PENDING & ACTIVE ueberspringen — die sind schon unterwegs oder fertig
    skip_names = {d.display_name for d in existing_docs
                  if str(getattr(d, "state", "")).split(".")[-1]
                  in ("STATE_ACTIVE", "STATE_PENDING")}

    # --- Dateien splitten und (nur fehlende) parallel uploaden ---
    max_bytes = int(args.max_mb * 1024 * 1024)
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)

        # Alle Teil-Files erst auf Disk schreiben
        upload_tasks: list[tuple[str, Path]] = []
        for fpath in FILES_TO_UPLOAD:
            src = Path(fpath)
            if not src.exists():
                print(f"Datei nicht gefunden: {fpath}")
                sys.exit(1)
            size_mb = src.stat().st_size / 1024 / 1024
            print(f"▶ Splitte {src.name} ({size_mb:.1f} MB) in ~{args.max_mb} MB Teile ...")
            pieces = split_markdown_at_pages(src, max_bytes=max_bytes)
            print(f"  → {len(pieces)} Teile")
            for display_name, content in pieces:
                if display_name in skip_names:
                    print(f"  ↷ Skip (bereits aktiv/pending): {display_name}")
                    continue
                out = tmp / display_name
                out.write_text(content, encoding="utf-8")
                upload_tasks.append((display_name, out))

        if not upload_tasks:
            print("\nAlle Teil-Files bereits aktiv. Nichts zu tun.")
        else:
            print(f"\n▶ Starte parallel Upload + Indexing "
                  f"({len(upload_tasks)} Files, {args.parallel} parallel) ...")
            print(f"  Methode: {args.method}")
            print("  Server-seitiges Indexing dauert typisch 1-3 min pro File.")
            print("  Bei 500/503/429 wird mit exponentiellem Backoff wiederholt.\n")
            t0 = time.time()
            done = 0
            failed_uploads = []

            def upload_one(task):
                display_name, out_path = task
                started = time.time()
                backoff = 30
                for attempt in range(1, args.retries + 1):
                    try:
                        if args.method == "direct":
                            op = upload_direct(
                                client, store.name, display_name, out_path, args
                            )
                        elif args.method == "direct-config":
                            op = upload_direct_config(
                                client, store.name, display_name, out_path, args
                            )
                        else:
                            op = upload_via_file_import(
                                client, store.name, display_name, out_path, args
                            )
                        wait_for_operation(
                            client,
                            op,
                            display_name,
                            poll_sec=args.poll_sec,
                        )
                        if args.pause_sec:
                            time.sleep(args.pause_sec)
                        return display_name, time.time() - started
                    except Exception as e:
                        if not is_transient_error(e) or attempt >= args.retries:
                            raise
                        print(
                            f"  ⚠ Retry {attempt}/{args.retries} in {backoff}s: "
                            f"{display_name} ({str(e)[:120]})"
                        )
                        time.sleep(backoff)
                        backoff = min(backoff * 2, MAX_BACKOFF_SEC)

            with concurrent.futures.ThreadPoolExecutor(
                    max_workers=max(1, args.parallel)) as ex:
                futures = {ex.submit(upload_one, t): t for t in upload_tasks}
                for fut in concurrent.futures.as_completed(futures):
                    task = futures[fut]
                    try:
                        name, dur = fut.result()
                        done += 1
                        elapsed = int(time.time() - t0)
                        print(f"  [{done}/{len(upload_tasks)}] ✓ {name}  "
                              f"(file: {dur:.0f}s, gesamt: {elapsed}s)")
                    except Exception as e:
                        failed_uploads.append((task[0], str(e)))
                        print(f"  ✗ {task[0]}: {e}")
                        if isinstance(e, ImportAuthenticationError):
                            print(
                                "\nAbbruch: importFile akzeptiert diesen API-Key "
                                "nicht. Weitere Files wuerden nur temporaer "
                                "hochgeladen und dann beim Import scheitern."
                            )
                            for pending in futures:
                                pending.cancel()
                            break

            print(f"\n✔ Uploads abgeschlossen in {int(time.time() - t0)}s")
            if failed_uploads:
                print(f"\nFehlgeschlagene Uploads:")
                for name, err in failed_uploads:
                    print(f"  - {name}: {err[:150]}")

    # --- Status ausgeben ---
    print()
    print("=" * 60)
    print("✔ File Search Store bereit.")
    print()
    print("In deine .env.local eintragen:")
    print(f"  GEMINI_FILE_SEARCH_STORE={store.name}")
    print()
    docs = list(client.file_search_stores.documents.list(parent=store.name))
    print(f"Enthaltene Dokumente: {len(docs)}")
    for d in docs:
        state = getattr(d, "state", "?")
        dn = getattr(d, "display_name", d.name)
        print(f"  - {dn}  [{state}]")
    print("=" * 60)


if __name__ == "__main__":
    main()
