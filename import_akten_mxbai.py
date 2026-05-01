#!/usr/bin/env python3
"""
Direct-Mxbai Import fuer Ermittlungsakten
==========================================
Chunked alle .md-Dateien unter data/ermittlungsakten/ mit dem existierenden
ErmittlungsaktenChunker (aus import_tool.py) und embedded sie direkt mit
``mixedbread-ai/deepset-mxbai-embed-de-large-v1`` in die Qdrant-Collection
``ermittlungsakten_mxbai``. Kein E5-Zwischenschritt.

Usage:
    python import_akten_mxbai.py
    python import_akten_mxbai.py --recreate
"""

import argparse
import logging
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

from import_tool import (
    ErmittlungsaktenChunker,
    QdrantManager,
    compute_sparse_vector,
)

COLLECTION = "ermittlungsakten_mxbai"
MXBAI_MODEL = "mixedbread-ai/deepset-mxbai-embed-de-large-v1"
EMBED_BATCH = 32
UPLOAD_BATCH = 100

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", default="data")
    parser.add_argument("--env-file", default=".env.local")
    parser.add_argument("--recreate", action="store_true",
                        help="Collection vor dem Import neu anlegen")
    args = parser.parse_args()

    load_dotenv(args.env_file, override=True)
    qurl = os.getenv("QDRANT_ENDPOINT")
    qkey = os.getenv("QDRANT_API_KEY")
    if not (qurl and qkey):
        log.error("QDRANT_ENDPOINT / QDRANT_API_KEY fehlen in %s", args.env_file)
        sys.exit(1)

    akten_dir = Path(args.data_dir) / "ermittlungsakten"
    md_files = sorted(akten_dir.rglob("*.md"))
    if not md_files:
        log.error("Keine .md-Dateien in %s", akten_dir)
        sys.exit(1)
    log.info("%d Ermittlungsakten-Datei(en) gefunden", len(md_files))

    chunker = ErmittlungsaktenChunker()
    all_chunks = []
    for fp in md_files:
        chunks = chunker.chunk_file(str(fp))
        log.info("  %s → %d Chunks", fp.name, len(chunks))
        all_chunks.extend(chunks)
    log.info("Gesamt: %d Chunks", len(all_chunks))

    log.info("Lade Embedding-Modell: %s", MXBAI_MODEL)
    model = SentenceTransformer(MXBAI_MODEL)
    log.info("Modell geladen (Device: %s, Dim: %d)",
             model.device, model.get_sentence_embedding_dimension())

    qdrant = QdrantManager(qurl, qkey)
    qdrant.setup_collection(COLLECTION, recreate=args.recreate)

    # Embed in Batches (keine Prefixe — mxbai-de braucht fuer Passages keinen)
    texts = [c.text for c in all_chunks]
    start = time.time()
    dense = model.encode(
        texts,
        batch_size=EMBED_BATCH,
        normalize_embeddings=True,
        show_progress_bar=True,
    ).tolist()
    log.info("Embedding fertig in %.1fs", time.time() - start)

    # Upload
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

    for i in tqdm(range(0, len(points), UPLOAD_BATCH), desc=f"Upload → {COLLECTION}"):
        qdrant.client.upsert(
            collection_name=COLLECTION,
            points=points[i:i + UPLOAD_BATCH],
        )

    log.info("Fertig: %d Punkte in '%s'", len(points), COLLECTION)


if __name__ == "__main__":
    main()
