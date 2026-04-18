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
"""

import argparse
import concurrent.futures
import os
import re
import sys
import tempfile
import time
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types

UPLOAD_PARALLELISM = 4   # parallele Uploads (Server-seitiges Indexing dauert ~1-3 min/File)

STORE_DISPLAY_NAME = "strafrecht"
FILES_TO_UPLOAD = [
    "data/fachliteratur/Strafrecht/StGB_Kommentar/StGB_Kommentar.md",
    "data/fachliteratur/Strafrecht/StPO_Kommentar/Strafprozessordnung.md",
]
PAGE_MARKER = re.compile(r"^## Seite (\d+)\s*$", re.MULTILINE)
DEFAULT_MAX_MB = 1.0


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


def wait_for_operation(client, op, label: str, poll_sec: int = 5):
    """Pollt die Long-Running-Operation bis sie abgeschlossen ist."""
    start = time.time()
    while not op.done:
        elapsed = int(time.time() - start)
        print(f"  {label}: {elapsed}s…", end="\r", flush=True)
        time.sleep(poll_sec)
        op = client.operations.get(op)
    print(f"  {label}: fertig nach {int(time.time() - start)}s.        ")
    return op


def main():
    parser = argparse.ArgumentParser(description="Gemini File Search Store einrichten")
    parser.add_argument("--reuse", action="store_true",
                        help="Bestehenden Store (gleicher display_name) weiterverwenden")
    parser.add_argument("--recreate", action="store_true",
                        help="Bestehenden Store loeschen und neu anlegen")
    parser.add_argument("--max-mb", type=float, default=DEFAULT_MAX_MB,
                        help=f"Ziel-Groesse pro Teil-File in MB (default: {DEFAULT_MAX_MB})")
    parser.add_argument("--env-file", default=".env.local")
    args = parser.parse_args()

    load_dotenv(args.env_file, override=True)
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY fehlt in", args.env_file)
        sys.exit(1)

    client = genai.Client(api_key=api_key)

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
                  f"({len(upload_tasks)} Files, {UPLOAD_PARALLELISM} parallel) ...")
            print(f"  Server-seitiges Indexing dauert typisch 1-3 min pro File.\n")
            t0 = time.time()
            done = 0
            failed_uploads = []

            def upload_one(task, retries: int = 3):
                display_name, out_path = task
                started = time.time()
                for attempt in range(retries):
                    try:
                        op = client.file_search_stores.upload_to_file_search_store(
                            file=str(out_path),
                            file_search_store_name=store.name,
                            config={"display_name": display_name},
                        )
                        while not op.done:
                            time.sleep(5)
                            op = client.operations.get(op)
                        return display_name, time.time() - started
                    except Exception as e:
                        if attempt < retries - 1:
                            wait = 2 ** attempt * 5  # 5s, 10s, 20s
                            print(f"  ⚠ Retry {attempt+1}/{retries-1} in {wait}s: {display_name}")
                            time.sleep(wait)
                        else:
                            raise

            with concurrent.futures.ThreadPoolExecutor(
                    max_workers=UPLOAD_PARALLELISM) as ex:
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
