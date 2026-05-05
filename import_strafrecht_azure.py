#!/usr/bin/env python3
"""
Import Strafrecht-Markdowns nach Azure AI Search (Index 'fachliteratur')
=========================================================================
Apples-to-apples-Variante zu Qdrant:
  - GLEICHER Chunker wie unser bestehendes RAG (FachliteraturChunker aus
    import_tool.py) → identische Chunk-Cuts wie in fachliteratur_mxbai
  - Embedding: OpenAI ``text-embedding-3-large`` (3072d) — funktional
    identisch zu Azure OpenAI ``text-embedding-3-large``, kein separates
    Azure-OpenAI-Resource-Setup noetig
  - Index mit:
      * Hybrid-faehig (BM25 + Vector)
      * Deutsche Tokenisierung via ``de.microsoft`` Analyzer (Komposita-Split)
      * INT8 Scalar Quantization auf den Vektoren (analog zu unserem Qdrant-SQ)
      * Semantic-Configuration fuer optionalen Server-Side-Rerank (Bench: an/aus)
      * Filterbare Felder: paragraph, gesetz, randnummer, domain, source_type

Usage:
    python import_strafrecht_azure.py               # idempotent, upsert
    python import_strafrecht_azure.py --recreate    # Index loeschen + neu
    python import_strafrecht_azure.py --dry-run     # nur Chunking-Stats
"""

import argparse
import logging
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SearchableField,
    SimpleField,
    SearchField,
    SearchFieldDataType,
    VectorSearch,
    VectorSearchProfile,
    HnswAlgorithmConfiguration,
    HnswParameters,
    ScalarQuantizationCompression,
    ScalarQuantizationParameters,
    VectorSearchCompressionTarget,
    RescoringOptions,
    SemanticConfiguration,
    SemanticPrioritizedFields,
    SemanticField,
    SemanticSearch,
    LexicalAnalyzerName,
)
from tqdm import tqdm

from import_tool import FachliteraturChunker

INDEX_NAME = "fachliteratur"
DEFAULT_ENDPOINT = "https://legalrag.search.windows.net"
EMBED_MODEL = "text-embedding-3-large"
EMBED_DIM = 3072
EMBED_BATCH = 100
UPLOAD_BATCH = 500

FILES_TO_IMPORT = [
    {
        "path": "data/fachliteratur/Strafrecht/StGB_Kommentar/StGB_Kommentar.md",
        "gesetz": "StGB",
        "kommentar": "Fischer/Anstoetz/Lutz StGB",
        "domain": "strafrecht",
    },
    {
        "path": "data/fachliteratur/Strafrecht/StPO_Kommentar/Strafprozessordnung.md",
        "gesetz": "StPO",
        "kommentar": "Schmitt/Koehler StPO",
        "domain": "strafrecht",
    },
]

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Index-Schema
# ---------------------------------------------------------------------------

def build_index_definition() -> SearchIndex:
    fields = [
        # Schluessel (deterministisch via uuid5 → idempotente Upserts)
        SimpleField(
            name="id", type=SearchFieldDataType.String,
            key=True, filterable=False, retrievable=True,
        ),

        # Volltext, deutsche Tokenisierung mit Komposita-Split
        SearchableField(
            name="text", type=SearchFieldDataType.String,
            analyzer_name=LexicalAnalyzerName.DE_MICROSOFT,
            retrievable=True,
        ),

        # Dense-Vektor (3072d) mit HNSW + INT8 Quantization
        SearchField(
            name="text_vector",
            type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
            searchable=True,
            retrievable=False,
            vector_search_dimensions=EMBED_DIM,
            vector_search_profile_name="hnsw-int8",
        ),

        # Filterbare Metadata
        SimpleField(name="paragraph", type=SearchFieldDataType.String,
                    filterable=True, retrievable=True),
        SimpleField(name="gesetz", type=SearchFieldDataType.String,
                    filterable=True, retrievable=True),
        SimpleField(name="domain", type=SearchFieldDataType.String,
                    filterable=True, retrievable=True),
        SimpleField(name="source_type", type=SearchFieldDataType.String,
                    filterable=True, retrievable=True),
        SimpleField(name="randnummer", type=SearchFieldDataType.Int32,
                    filterable=True, retrievable=True),
        SimpleField(name="page", type=SearchFieldDataType.Int32,
                    filterable=False, retrievable=True),

        # Retrievable-only (fuer Response-Schema und Semantic-Ranker)
        SearchableField(name="kommentar", type=SearchFieldDataType.String,
                        retrievable=True, analyzer_name=LexicalAnalyzerName.DE_MICROSOFT),
        SearchableField(name="breadcrumb", type=SearchFieldDataType.String,
                        retrievable=True, analyzer_name=LexicalAnalyzerName.DE_MICROSOFT),
        SimpleField(name="source_file", type=SearchFieldDataType.String,
                    filterable=False, retrievable=True),
    ]

    vector_search = VectorSearch(
        profiles=[
            VectorSearchProfile(
                name="hnsw-int8",
                algorithm_configuration_name="hnsw-default",
                compression_name="scalar-int8",
            )
        ],
        algorithms=[
            HnswAlgorithmConfiguration(
                name="hnsw-default",
                parameters=HnswParameters(m=4, ef_construction=400, ef_search=500),
            )
        ],
        compressions=[
            ScalarQuantizationCompression(
                compression_name="scalar-int8",
                rescoring_options=RescoringOptions(
                    enable_rescoring=True,
                    default_oversampling=2.0,
                ),
                parameters=ScalarQuantizationParameters(
                    quantized_data_type=VectorSearchCompressionTarget.INT8,
                ),
            )
        ],
    )

    semantic_search = SemanticSearch(configurations=[
        SemanticConfiguration(
            name="default",
            prioritized_fields=SemanticPrioritizedFields(
                title_field=SemanticField(field_name="breadcrumb"),
                content_fields=[SemanticField(field_name="text")],
                keywords_fields=[
                    SemanticField(field_name="paragraph"),
                    SemanticField(field_name="gesetz"),
                    SemanticField(field_name="kommentar"),
                ],
            ),
        )
    ])

    return SearchIndex(
        name=INDEX_NAME,
        fields=fields,
        vector_search=vector_search,
        semantic_search=semantic_search,
    )


# ---------------------------------------------------------------------------
# Embedding helper
# ---------------------------------------------------------------------------

def embed_batch(openai_client: OpenAI, texts: list[str]) -> list[list[float]]:
    resp = openai_client.embeddings.create(model=EMBED_MODEL, input=texts)
    return [d.embedding for d in resp.data]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--recreate", action="store_true",
                        help="Index vor dem Upload loeschen + neu anlegen")
    parser.add_argument("--dry-run", action="store_true",
                        help="Nur chunken, kein Embedding/Upload")
    parser.add_argument("--env-file", default=".env.local")
    args = parser.parse_args()

    load_dotenv(args.env_file, override=True)
    endpoint = os.getenv("AZURE_SEARCH_ENDPOINT", DEFAULT_ENDPOINT)
    admin_key = os.getenv("AZURE_PRIMARY_API_KEY")
    openai_key = os.getenv("OPENAI_API_KEY")

    if not admin_key:
        log.error("AZURE_PRIMARY_API_KEY fehlt in %s", args.env_file); sys.exit(1)
    if not openai_key:
        log.error("OPENAI_API_KEY fehlt in %s", args.env_file); sys.exit(1)

    log.info("Endpoint: %s", endpoint)

    # --- 1. Chunking ---
    chunker = FachliteraturChunker()
    all_chunks = []
    for cfg in FILES_TO_IMPORT:
        path = Path(cfg["path"])
        if not path.exists():
            log.error("Datei nicht gefunden: %s", path); sys.exit(1)
        chunks = chunker.chunk_file(
            str(path),
            gesetz_override=cfg["gesetz"],
            kommentar_override=cfg["kommentar"],
            domain=cfg["domain"],
        )
        log.info("  %s → %d chunks", path.name, len(chunks))
        all_chunks.extend(chunks)
    log.info("Gesamt: %d Chunks", len(all_chunks))

    if args.dry_run:
        log.info("Dry-run: kein Upload."); return

    # --- 2. Index anlegen / aktualisieren ---
    cred = AzureKeyCredential(admin_key)
    idx_client = SearchIndexClient(endpoint=endpoint, credential=cred)
    existing = [i.name for i in idx_client.list_indexes()]
    if args.recreate and INDEX_NAME in existing:
        log.info("Loesche bestehenden Index '%s'", INDEX_NAME)
        idx_client.delete_index(INDEX_NAME)
        existing.remove(INDEX_NAME)

    log.info("Erstelle/aktualisiere Index '%s'", INDEX_NAME)
    idx_client.create_or_update_index(build_index_definition())

    # --- 3. Documents bauen + Embeddings rechnen + uploaden ---
    openai = OpenAI(api_key=openai_key)
    sc = SearchClient(endpoint=endpoint, index_name=INDEX_NAME, credential=cred)

    # Azure-Search-Dokumente vorbereiten (ohne Vektor — kommt im Embed-Step)
    docs = []
    for c in all_chunks:
        m = c.metadata
        docs.append({
            "id": c.point_id,
            "text": c.text,
            "paragraph": (m.get("paragraph") or "") or None,
            "gesetz": (m.get("gesetz") or "") or None,
            "kommentar": (m.get("kommentar") or "") or None,
            "domain": (m.get("domain") or "") or None,
            "source_type": (m.get("source_type") or "fachliteratur"),
            "randnummer": m.get("randnummer"),
            "page": int(m.get("page") or 0),
            "breadcrumb": (m.get("breadcrumb") or "") or None,
            "source_file": (m.get("source_file") or "") or None,
        })

    # Embed in Batches (OpenAI hat token-Limit pro Request, 100 Chunks ist sicher)
    log.info("Embedding %d Chunks mit %s ...", len(docs), EMBED_MODEL)
    t0 = time.time()
    for i in tqdm(range(0, len(docs), EMBED_BATCH), desc="embed"):
        batch = docs[i:i + EMBED_BATCH]
        texts = [d["text"] for d in batch]
        try:
            vecs = embed_batch(openai, texts)
        except Exception as e:
            log.error("Embedding-Fehler bei Batch %d: %s", i, e); raise
        for d, v in zip(batch, vecs):
            d["text_vector"] = v
    log.info("Embedding fertig in %.0fs", time.time() - t0)

    # Upload in Azure-Search Batches
    log.info("Upload %d Documents in Batches von %d ...", len(docs), UPLOAD_BATCH)
    t0 = time.time()
    failed = 0
    for i in tqdm(range(0, len(docs), UPLOAD_BATCH), desc="upload"):
        batch = docs[i:i + UPLOAD_BATCH]
        # None-Werte raus, Azure mag sie nicht in nicht-nullable Feldern
        clean = [{k: v for k, v in d.items() if v is not None} for d in batch]
        try:
            results = sc.upload_documents(documents=clean)
            failed += sum(1 for r in results if not r.succeeded)
        except Exception as e:
            log.error("Upload-Fehler bei Batch %d: %s", i, e); raise
    log.info("Upload fertig in %.0fs (failed: %d)", time.time() - t0, failed)

    # Stats
    count = sc.get_document_count()
    log.info("Index '%s' enthaelt jetzt %d Dokumente", INDEX_NAME, count)


if __name__ == "__main__":
    main()
