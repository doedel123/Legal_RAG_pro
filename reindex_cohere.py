#!/usr/bin/env python3
"""
Reindex Fachliteratur mit Cohere-Embeddings
============================================
Liest alle Chunks aus der Qdrant-Collection ``fachliteratur`` (E5-Vektoren),
embedded den Text mit Cohere ``embed-multilingual-v3.0`` und schreibt die
Chunks in eine neue Collection ``fachliteratur_cohere``. BM25-Sparse-Vektoren
werden aus dem Text neu berechnet. Payload und IDs bleiben identisch.

Usage:
    python reindex_cohere.py               # legt fachliteratur_cohere an
    python reindex_cohere.py --recreate    # loescht bestehende Cohere-Collection und neu
"""

import argparse
import os
import sys
import time

from dotenv import load_dotenv
import cohere
from qdrant_client import QdrantClient, models
from tqdm import tqdm

from retrieve import _compute_sparse_vector

SRC_COLLECTION = "fachliteratur"
DST_COLLECTION = "fachliteratur_cohere"
COHERE_MODEL = "embed-multilingual-v3.0"
COHERE_DIM = 1024
COHERE_BATCH = 96  # Cohere v3 Batch-Limit


def ensure_collection(qc: QdrantClient, name: str, recreate: bool):
    if qc.collection_exists(name):
        if recreate:
            print(f"Loesche existierende Collection '{name}' ...")
            qc.delete_collection(name)
        else:
            print(f"Collection '{name}' existiert bereits — "
                  "mit --recreate neu aufbauen.")
            sys.exit(1)

    print(f"Erstelle Collection '{name}' ...")
    qc.create_collection(
        collection_name=name,
        vectors_config={
            "dense": models.VectorParams(
                size=COHERE_DIM,
                distance=models.Distance.COSINE,
                on_disk=True,
            ),
        },
        sparse_vectors_config={
            "bm25": models.SparseVectorParams(modifier=models.Modifier.IDF),
        },
    )
    for f in ["source_type", "gesetz", "paragraph", "kommentar",
              "aktenzeichen", "fall", "dokument_typ"]:
        try:
            qc.create_payload_index(
                collection_name=name, field_name=f,
                field_schema=models.PayloadSchemaType.KEYWORD,
            )
        except Exception:
            pass
    try:
        qc.create_payload_index(
            collection_name=name, field_name="randnummer",
            field_schema=models.PayloadSchemaType.INTEGER,
        )
    except Exception:
        pass
    try:
        qc.create_payload_index(
            collection_name=name, field_name="text",
            field_schema=models.TextIndexParams(
                type=models.TextIndexType.TEXT,
                tokenizer=models.TokenizerType.WORD,
                min_token_len=3, lowercase=True,
            ),
        )
    except Exception:
        pass


def iter_source(qc: QdrantClient, batch_size: int = 256):
    """Alle Punkte aus der Quell-Collection scrollen (nur Payload + ID)."""
    offset = None
    while True:
        points, offset = qc.scroll(
            collection_name=SRC_COLLECTION,
            with_payload=True,
            with_vectors=False,
            limit=batch_size,
            offset=offset,
        )
        if not points:
            break
        for p in points:
            text = p.payload.get("text", "") if p.payload else ""
            if not text:
                continue
            yield p.id, text, p.payload
        if offset is None:
            break


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--recreate", action="store_true",
                        help="Cohere-Collection vorher loeschen und neu aufbauen")
    parser.add_argument("--env-file", default=".env.local")
    args = parser.parse_args()

    load_dotenv(args.env_file, override=True)
    qurl = os.getenv("QDRANT_ENDPOINT")
    qkey = os.getenv("QDRANT_API_KEY")
    ckey = os.getenv("COHERE_API_KEY") or os.getenv("CO_API_KEY")
    if not (qurl and qkey):
        print("QDRANT_ENDPOINT / QDRANT_API_KEY fehlen."); sys.exit(1)
    if not ckey:
        print("COHERE_API_KEY fehlt."); sys.exit(1)

    qc = QdrantClient(url=qurl, api_key=qkey, timeout=60)
    co = cohere.ClientV2(api_key=ckey)

    if not qc.collection_exists(SRC_COLLECTION):
        print(f"Quell-Collection '{SRC_COLLECTION}' nicht vorhanden."); sys.exit(1)

    src_info = qc.get_collection(SRC_COLLECTION)
    total = src_info.points_count
    print(f"Quelle: '{SRC_COLLECTION}' mit {total} Punkten")

    ensure_collection(qc, DST_COLLECTION, recreate=args.recreate)

    # Sammeln, batchen, embedden, uploaden
    buffer: list[tuple[int, str, dict]] = []
    uploaded = 0
    start = time.time()

    def flush():
        nonlocal uploaded
        if not buffer:
            return
        texts = [t for _, t, _ in buffer]
        # Cohere v3: input_type="search_document" fuer Passagen
        resp = co.embed(
            texts=texts,
            model=COHERE_MODEL,
            input_type="search_document",
            embedding_types=["float"],
        )
        embs = resp.embeddings.float_
        points = []
        for (pid, text, payload), emb in zip(buffer, embs):
            sp_idx, sp_val = _compute_sparse_vector(text)
            points.append(models.PointStruct(
                id=pid,
                vector={
                    "dense": emb,
                    "bm25": models.SparseVector(indices=sp_idx, values=sp_val),
                },
                payload=payload,
            ))
        qc.upsert(collection_name=DST_COLLECTION, points=points, wait=True)
        uploaded += len(points)
        buffer.clear()

    with tqdm(total=total, desc="Reindex") as bar:
        for pid, text, payload in iter_source(qc):
            buffer.append((pid, text, payload))
            if len(buffer) >= COHERE_BATCH:
                flush()
                bar.update(COHERE_BATCH)
        if buffer:
            remaining = len(buffer)
            flush()
            bar.update(remaining)

    elapsed = time.time() - start
    print(f"\n✓ {uploaded} Punkte nach '{DST_COLLECTION}' geschrieben ({elapsed:.1f}s)")


if __name__ == "__main__":
    main()
