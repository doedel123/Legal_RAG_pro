import os
import sys
import time
import re
import tempfile
from pathlib import Path
from dotenv import load_dotenv
from google import genai

PAGE_MARKER = re.compile(r"^## Seite (\d+)\s*$", re.MULTILINE)
MAX_MB = 1
MAX_RETRIES = 3
RETRY_WAIT = 15
# Pause zwischen Uploads (Free-Tier ist strikt; zu aggressiv führt zu 429 und API-Key-Sperre).
UPLOAD_PAUSE = 16
# Polling-Intervall für Indexierungsstatus.
POLL_INTERVAL = 15
# Maximale Retries bei 429/ResourceExhausted pro Upload-Aufruf (mit exp. Backoff).
RATE_LIMIT_RETRIES = 5

def split_markdown_at_pages(md_path: Path, max_bytes: int) -> list[tuple[str, str]]:
    text = md_path.read_text(encoding="utf-8")
    parts = PAGE_MARKER.split(text)
    
    pages = []
    if parts[0].strip():
        pages.append((0, parts[0]))
    for i in range(1, len(parts), 2):
        page_num = int(parts[i])
        content = f"## Seite {page_num}\n{parts[i + 1] if i + 1 < len(parts) else ''}"
        pages.append((page_num, content))

    chunks = []
    cur_parts = []
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

    base = md_path.stem
    width = len(str(len(chunks)))
    return [
        (f"{base}_part{idx+1:0{width}d}.md", content)
        for idx, content in enumerate(chunks)
    ]

def main():
    load_dotenv(".env.local", override=True)
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Fehler: GEMINI_API_KEY nicht in .env.local gefunden.")
        sys.exit(1)

    client = genai.Client(api_key=api_key)
    
    base_dir = Path("data/fachliteratur")
    if not base_dir.exists():
        print(f"Fehler: Verzeichnis {base_dir} nicht gefunden.")
        sys.exit(1)

    md_files = sorted(base_dir.rglob("*.md"))
    if not md_files:
        print(f"Keine Markdown-Dateien in {base_dir} gefunden.")
        sys.exit(0)

    print(f"\nGefundene Markdown-Dateien in {base_dir}:")
    for i, f in enumerate(md_files, 1):
        size_mb = f.stat().st_size / 1024 / 1024
        print(f"  [{i}] {f.relative_to(base_dir)}  ({size_mb:.1f} MB)")

    sel = input(
        "\nWelche Dateien hochladen? "
        "(Nummern kommasepariert, z.B. '1,3' oder 'all' für alle) [all]: "
    ).strip().lower() or "all"

    if sel == "all":
        selected = md_files
    else:
        try:
            idxs = [int(x) for x in re.split(r"[,\s]+", sel) if x]
            selected = [md_files[i - 1] for i in idxs]
        except (ValueError, IndexError):
            print(f"Ungültige Auswahl: {sel}")
            sys.exit(1)

    if not selected:
        print("Keine Dateien ausgewählt.")
        sys.exit(0)

    print(f"\nAusgewählt: {len(selected)} Datei(en)")
    for f in selected:
        print(f"  - {f.relative_to(base_dir)}")
    md_files = selected

    print(f"\nErstelle neuen Gemini Filestore...")
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    
    try:
        store = client.file_search_stores.create(
            config={"display_name": f"fachliteratur-{timestamp}"}
        )
        filestore_id = store.name
        print(f"Filestore erfolgreich erstellt!")
        print(f"Filestore-ID: {filestore_id}")
    except Exception as e:
        print(f"Fehler beim Erstellen des Filestores: {e}")
        sys.exit(1)

    max_bytes = int(MAX_MB * 1024 * 1024)

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)

        # display_name -> lokaler Pfad, für eventuelle Retries
        file_map: dict[str, Path] = {}
        # display_name -> Anzahl Retry-Versuche
        retry_counts: dict[str, int] = {}

        def upload_one(display_name: str, path: Path) -> bool:
            print(f"  -> Lade hoch: {display_name} ... ", end="", flush=True)
            backoff = 30
            for attempt in range(1, RATE_LIMIT_RETRIES + 1):
                try:
                    client.file_search_stores.upload_to_file_search_store(
                        file=str(path),
                        file_search_store_name=filestore_id,
                        config={"display_name": display_name}
                    )
                    print("✓")
                    time.sleep(UPLOAD_PAUSE)
                    return True
                except Exception as e:
                    msg = str(e)
                    is_rate_limit = (
                        "429" in msg
                        or "RESOURCE_EXHAUSTED" in msg
                        or "Too Many Requests" in msg
                        or "quota" in msg.lower()
                    )
                    is_server_error = (
                        "500" in msg
                        or "INTERNAL" in msg
                        or "503" in msg
                        or "UNAVAILABLE" in msg
                        or "502" in msg
                        or "504" in msg
                        or "DEADLINE_EXCEEDED" in msg
                    )
                    if (is_rate_limit or is_server_error) and attempt < RATE_LIMIT_RETRIES:
                        label = "429/Rate-Limit" if is_rate_limit else "5xx/Server-Fehler"
                        print(f"\n    {label} — warte {backoff}s (Versuch {attempt}/{RATE_LIMIT_RETRIES}) ...")
                        time.sleep(backoff)
                        backoff = min(backoff * 2, 300)
                        print(f"  -> Lade hoch: {display_name} ... ", end="", flush=True)
                        continue
                    print(f"✗ Fehler: {e}")
                    return False
            return False

        # Dateien aufteilen, speichern und initial hochladen
        for fpath in md_files:
            size_mb = fpath.stat().st_size / 1024 / 1024
            print(f"Splitte {fpath.name} ({size_mb:.1f} MB) in ~{MAX_MB} MB Teile ...")
            pieces = split_markdown_at_pages(fpath, max_bytes=max_bytes)
            print(f"  -> {len(pieces)} Teile generiert.")

            for display_name, content in pieces:
                out = tmp / display_name
                out.write_text(content, encoding="utf-8")
                file_map[display_name] = out
                if not upload_one(display_name, out):
                    retry_counts[display_name] = retry_counts.get(display_name, 0)

        expected = len(file_map)
        print(f"\nWarte auf Indexierung von {expected} Dokumenten-Teilen (Fortschrittsanzeige)...")

        start_time = time.time()
        # display_names, die wir final aufgegeben haben
        abandoned: set[str] = set()
        # resource-names bereits verarbeiteter FAILED-Dokumente (damit wir jede
        # einzelne Fehlschlag-Instanz nur genau einmal retryen)
        handled_failed: set[str] = set()

        def try_delete(doc) -> bool:
            # Ohne force schlägt das Löschen mit "Cannot delete non-empty Document" fehl.
            for kwargs in ({"name": doc.name, "config": {"force": True}},
                           {"name": doc.name, "force": True},
                           {"name": doc.name}):
                try:
                    client.file_search_stores.documents.delete(**kwargs)
                    return True
                except TypeError:
                    continue
                except Exception as e:
                    print(f"  (konnte altes FAILED-Dokument nicht löschen: {e})")
                    return False
            return False

        while True:
            try:
                docs = list(client.file_search_stores.documents.list(parent=filestore_id))
            except Exception:
                docs = []

            status_counts: dict[str, int] = {}
            failed_docs = []
            pending = False
            # display_name -> hat mindestens ein nicht-FAILED Dokument
            active_names: set[str] = set()

            for d in docs:
                state = str(getattr(d, "state", "UNKNOWN")).split(".")[-1]
                status_counts[state] = status_counts.get(state, 0) + 1
                dn = getattr(d, "display_name", "") or ""
                if state in ("STATE_PENDING", "STATE_UNSPECIFIED", "UNKNOWN"):
                    pending = True
                    active_names.add(dn)
                elif state == "STATE_ACTIVE":
                    active_names.add(dn)
                elif state == "STATE_FAILED":
                    failed_docs.append(d)

            # Nur neue (noch nicht behandelte) FAILED-Dokumente retryen
            new_failed = [d for d in failed_docs if d.name not in handled_failed]
            for d in new_failed:
                handled_failed.add(d.name)
                dn = getattr(d, "display_name", "") or ""
                if dn not in file_map or dn in abandoned:
                    continue
                attempts = retry_counts.get(dn, 0)
                if attempts >= MAX_RETRIES:
                    abandoned.add(dn)
                    continue

                retry_counts[dn] = attempts + 1
                print(f"\n[Retry {attempts + 1}/{MAX_RETRIES}] FAILED: {dn} — warte {RETRY_WAIT}s und lade erneut hoch ...")
                time.sleep(RETRY_WAIT)
                try_delete(d)
                upload_one(dn, file_map[dn])

            missing = [dn for dn in file_map if dn not in active_names and dn not in abandoned]
            if missing:
                status_counts["NOT_YET_REGISTERED"] = len(missing)

            status_str = ", ".join(f"{k}: {v}" for k, v in status_counts.items())
            elapsed = int(time.time() - start_time)
            print(f"\rZeit: {elapsed}s | Status: {status_str} (erwartet: {expected})   ", end="", flush=True)

            # Fertig, wenn nichts pending ist, keine unbehandelten FAILED und
            # jeder erwartete display_name entweder aktiv oder aufgegeben ist.
            unhandled_failed = [d for d in failed_docs if d.name not in handled_failed]
            accounted = sum(1 for dn in file_map if dn in active_names or dn in abandoned)
            if not pending and not unhandled_failed and accounted >= expected:
                print("\n\nAlle Dokumenten-Teile wurden verarbeitet!")
                print("-" * 60)
                print("ZUSAMMENFASSUNG:")
                print(f"Filestore-ID: {filestore_id}")

                # Frische Liste aller aktuell im Filestore vorhandenen Dokumente holen
                try:
                    final_docs = list(client.file_search_stores.documents.list(parent=filestore_id))
                except Exception as e:
                    print(f"(konnte finale Liste nicht holen: {e})")
                    final_docs = docs

                by_state: dict[str, list] = {}
                for d in final_docs:
                    st = str(getattr(d, "state", "UNKNOWN")).split(".")[-1]
                    by_state.setdefault(st, []).append(d)

                print(f"\nFilestore-Inhalt ({len(final_docs)} Dokumente):")
                for st in sorted(by_state):
                    print(f"\n  [{st}] {len(by_state[st])} Dokument(e):")
                    for d in sorted(by_state[st], key=lambda x: getattr(x, "display_name", "") or ""):
                        dn = getattr(d, "display_name", "") or "(ohne display_name)"
                        print(f"    - {dn}   ({d.name})")

                active_count = len(by_state.get("STATE_ACTIVE", []))
                failed_count = len(by_state.get("STATE_FAILED", []))
                print(f"\nErwartet: {expected} | Aktiv: {active_count} | Fehlgeschlagen: {failed_count}")
                if abandoned:
                    print(f"Nach {MAX_RETRIES} Retries aufgegeben: {sorted(abandoned)}")
                print("-" * 60)
                break

            time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    main()
