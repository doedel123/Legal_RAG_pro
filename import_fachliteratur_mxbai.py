#!/usr/bin/env python3
"""
Direct-Mxbai Import fuer Fachliteratur (alle Rechtsgebiete)
============================================================
Walkt ``data/fachliteratur/<Rechtsgebiet>/...`` und lastet alle .md-Dateien
direkt mit ``mixedbread-ai/deepset-mxbai-embed-de-large-v1`` in die Qdrant-
Collection ``fachliteratur_mxbai``. Keine Zwischen-Collection, kein E5.

Dispatch nach Dateityp:
  - Kommentare (Regelfall) → FachliteraturChunker
    (erkennt §, Randnummern, Gliederungsebenen — generalisiert auf beliebige
    Gesetz-Suffixe, nicht nur StGB/StPO)
  - Ratgeber / Fachbuecher → RatgeberChunker
    (Headings-basiert, groessere Chunks, ohne Randnummer-Heuristik)

Welche Dateien Ratgeber sind, wird ueber eine kleine Pattern-Liste erkannt
(``_is_ratgeber``). Default = Kommentar.

Usage:
    python import_fachliteratur_mxbai.py --recreate
    python import_fachliteratur_mxbai.py --domains strafrecht,mietrecht
    python import_fachliteratur_mxbai.py --dry-run
"""

from __future__ import annotations

import argparse
import logging
import os
import re
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from qdrant_client import models
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

from import_tool import (
    Chunk,
    FachliteraturChunker,
    RatgeberChunker,
    QdrantManager,
    compute_sparse_vector,
)

COLLECTION = "fachliteratur_mxbai"
MXBAI_MODEL = "mixedbread-ai/deepset-mxbai-embed-de-large-v1"
EMBED_BATCH = 32
UPLOAD_BATCH = 100

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Dispatch-Logik: welcher Chunker + welche Meta pro Datei
# ---------------------------------------------------------------------------

# Ratgeber/Fachbuch-Marker im Dateinamen (alles andere → Kommentar).
RATGEBER_PATTERNS = (
    re.compile(r"[Mm]ieter", re.IGNORECASE),           # "Mieter"-Ratgeber
    re.compile(r"[Nn]ebenkosten"),
    re.compile(r"[Mm]essverfahren"),
    re.compile(r"[Ff]ehlerquell"),
)

# Gesetz + Kommentar-Label pro Datei-Pattern. Default wird aus Pfad abgeleitet.
# Erweiterung: neuer Eintrag (regex, (gesetz, kommentar)).
KOMMENTAR_META: list[tuple[re.Pattern, tuple[str, str]]] = [
    (re.compile(r"StGB_Kommentar", re.IGNORECASE),
        ("StGB", "Fischer/Anstoetz/Lutz StGB")),
    (re.compile(r"StPO_Kommentar|Strafprozess", re.IGNORECASE),
        ("StPO", "Schmitt/Koehler StPO")),
    (re.compile(r"erfurter", re.IGNORECASE),
        ("ArbR", "Erfurter Kommentar")),
    (re.compile(r"abgabenordnung", re.IGNORECASE),
        ("AO", "Abgabenordnung-Kommentar")),
    (re.compile(r"Mietrecht\.md$", re.IGNORECASE),
        ("BGB/Miet", "Mietrecht-Kommentar")),
    (re.compile(r"OwigRecht\.md$", re.IGNORECASE),
        ("OWiG", "OWiG-Kommentar")),
    (re.compile(r"Strassenverkehrsrecht\.md$", re.IGNORECASE),
        ("StVG/StVO", "Strassenverkehrsrecht-Kommentar")),
]


def _is_ratgeber(path: Path) -> bool:
    name = path.name
    return any(pat.search(name) for pat in RATGEBER_PATTERNS)


def _kommentar_meta(path: Path) -> tuple[str, str]:
    s = str(path)
    for pat, meta in KOMMENTAR_META:
        if pat.search(s):
            return meta
    # Fallback: Gesetz = Dateistem, Kommentar = Dateistem
    stem = path.stem
    return stem, stem


def _domain_from_path(data_root: Path, path: Path) -> str:
    """Liefert das Top-Level-Fachgebiet (lowercase)."""
    rel = path.relative_to(data_root)
    return rel.parts[0].lower() if rel.parts else "unbekannt"


def _buch_name(path: Path) -> str:
    """Menschenlesbarer Buchname fuer Metadata (ohne .md)."""
    return path.stem


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--data-dir", default="data")
    parser.add_argument("--env-file", default=".env.local")
    parser.add_argument("--recreate", action="store_true")
    parser.add_argument("--domains", default="",
                        help="Komma-Liste, nur diese Fachgebiete importieren "
                             "(default: alle)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Nur Chunking, kein Upload")
    args = parser.parse_args()

    load_dotenv(args.env_file, override=True)
    data_root = Path(args.data_dir) / "fachliteratur"
    if not data_root.exists():
        log.error("Verzeichnis nicht gefunden: %s", data_root)
        sys.exit(1)

    md_files = sorted(data_root.rglob("*.md"))
    if not md_files:
        log.error("Keine .md-Dateien in %s", data_root)
        sys.exit(1)

    # Optional: Fachgebiet-Filter
    domain_filter = {d.strip().lower() for d in args.domains.split(",") if d.strip()}
    if domain_filter:
        md_files = [f for f in md_files
                    if _domain_from_path(data_root, f) in domain_filter]
        log.info("Filter: %s → %d Dateien", domain_filter, len(md_files))

    log.info("Gefunden: %d Fachliteratur-Datei(en)", len(md_files))

    kommentar_chunker = FachliteraturChunker()
    ratgeber_chunker = RatgeberChunker()

    all_chunks: list[Chunk] = []
    stats: dict[str, int] = {}

    for fp in md_files:
        domain = _domain_from_path(data_root, fp)
        is_ratgeber = _is_ratgeber(fp)

        if is_ratgeber:
            chunks = ratgeber_chunker.chunk_file(
                str(fp), domain=domain, buch=_buch_name(fp))
            typ = "ratgeber"
        else:
            gesetz, kommentar = _kommentar_meta(fp)
            chunks = kommentar_chunker.chunk_file(
                str(fp),
                gesetz_override=gesetz,
                kommentar_override=kommentar,
                domain=domain,
            )
            typ = f"kommentar({gesetz})"

        key = f"{domain}/{typ}"
        stats[key] = stats.get(key, 0) + len(chunks)
        log.info("  %-50s → %4d chunks  [%s/%s]",
                 fp.name[:50], len(chunks), domain, typ)
        all_chunks.extend(chunks)

    log.info("Gesamt: %d Chunks aus %d Dateien", len(all_chunks), len(md_files))
    log.info("Verteilung: %s",
             ", ".join(f"{k}={v}" for k, v in sorted(stats.items())))

    if args.dry_run:
        log.info("Dry-run: Kein Upload.")
        return

    # --- Embedding ---
    log.info("Lade Embedding-Modell: %s", MXBAI_MODEL)
    model = SentenceTransformer(MXBAI_MODEL)
    log.info("Modell geladen (Device: %s, Dim: %d)",
             model.device, model.get_sentence_embedding_dimension())

    qurl = os.getenv("QDRANT_ENDPOINT")
    qkey = os.getenv("QDRANT_API_KEY")
    if not (qurl and qkey):
        log.error("QDRANT_ENDPOINT / QDRANT_API_KEY fehlen")
        sys.exit(1)

    qdrant = QdrantManager(qurl, qkey)
    qdrant.setup_collection(COLLECTION, recreate=args.recreate)

    texts = [c.text for c in all_chunks]
    t0 = time.time()
    dense = model.encode(
        texts,
        batch_size=EMBED_BATCH,
        normalize_embeddings=True,
        show_progress_bar=True,
    ).tolist()
    log.info("Embedding fertig in %.1fs", time.time() - t0)

    # --- Upload ---
    points = []
    for chunk, vec in zip(all_chunks, dense):
        sp_idx, sp_val = compute_sparse_vector(chunk.text)
        points.append(models.PointStruct(
            id=chunk.point_id,
            vector={
                "dense": vec,
                "bm25": models.SparseVector(indices=sp_idx, values=sp_val),
            },
            payload={"text": chunk.text, **chunk.metadata},
        ))

    for i in tqdm(range(0, len(points), UPLOAD_BATCH),
                  desc=f"Upload → {COLLECTION}"):
        qdrant.client.upsert(
            collection_name=COLLECTION,
            points=points[i:i + UPLOAD_BATCH],
        )

    log.info("Fertig: %d Punkte in '%s'", len(points), COLLECTION)


if __name__ == "__main__":
    main()
