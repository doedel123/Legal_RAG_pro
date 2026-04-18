import re
import sys
from pathlib import Path

PAGE_MARKER = re.compile(r"^## Seite (\d+)\s*$", re.MULTILINE)


def split_at_pages(text: str) -> list[str]:
    """Zerlegt den Text in Seiten (jede Seite startet mit '## Seite N')."""
    parts = PAGE_MARKER.split(text)
    pages = []
    if parts[0].strip():
        pages.append(parts[0])
    for i in range(1, len(parts), 2):
        page_num = parts[i]
        body = parts[i + 1] if i + 1 < len(parts) else ""
        pages.append(f"## Seite {page_num}\n{body}")
    return pages


def split_into_n(md_path: Path, n: int) -> list[tuple[Path, str]]:
    """Splittet md_path in n möglichst gleich große Teile an Seitengrenzen."""
    text = md_path.read_text(encoding="utf-8")
    pages = split_at_pages(text)
    if not pages:
        return []

    sizes = [len(p.encode("utf-8")) for p in pages]
    total = sum(sizes)
    target = total / n

    chunks: list[list[str]] = [[] for _ in range(n)]
    chunk_sizes = [0] * n
    idx = 0
    for page, size in zip(pages, sizes):
        # Letzten Chunk nicht überlaufen lassen; sonst Seite in aktuellen Chunk,
        # und zum nächsten wechseln, wenn Target für aktuellen überschritten.
        if idx < n - 1 and chunk_sizes[idx] + size > target and chunks[idx]:
            idx += 1
        chunks[idx].append(page)
        chunk_sizes[idx] += size

    base = md_path.stem
    width = len(str(n))
    out = []
    for i, pieces in enumerate(chunks, 1):
        if not pieces:
            continue
        name = f"{base}_part{i:0{width}d}.md"
        out.append((md_path.parent / name, "\n".join(pieces)))
    return out


def main():
    base_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/fachliteratur")
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 2

    if not base_dir.exists():
        print(f"Verzeichnis nicht gefunden: {base_dir}")
        sys.exit(1)

    md_files = sorted(
        p for p in base_dir.rglob("*.md")
        if not re.search(r"_part\d+\.md$", p.name)
    )
    if not md_files:
        print(f"Keine .md-Dateien in {base_dir} gefunden.")
        sys.exit(0)

    print(f"Splitte {len(md_files)} Datei(en) in je {n} Teile ...\n")
    for md in md_files:
        size_mb = md.stat().st_size / 1024 / 1024
        print(f"• {md.relative_to(base_dir)}  ({size_mb:.1f} MB)")
        parts = split_into_n(md, n)
        if not parts:
            print("    (keine Seiten-Marker gefunden, übersprungen)")
            continue
        for out_path, content in parts:
            out_path.write_text(content, encoding="utf-8")
            part_mb = len(content.encode("utf-8")) / 1024 / 1024
            print(f"    → {out_path.relative_to(base_dir)}  ({part_mb:.1f} MB)")
        print()


if __name__ == "__main__":
    main()
