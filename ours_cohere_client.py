#!/usr/bin/env python3
"""
Ours-with-Cohere-Embeddings Adapter
====================================
Variante unserer eigenen Pipeline, die E5-large durch Cohere
``embed-multilingual-v3.0`` ersetzt. Sucht in der parallelen
Qdrant-Collection ``fachliteratur_cohere`` (via reindex_cohere.py befuellt).
Query Expansion, BM25-Hybrid-Suche und Cohere-Reranking bleiben identisch.

Nutzung:
    from ours_cohere_client import OursCohereRetriever
    r = OursCohereRetriever()
    results = r.search("Konkludente Taeuschung § 263", top_k=10)
"""

import os
import logging

import numpy as np
import cohere
from dotenv import load_dotenv

from retrieve import JuristischerRetriever, SearchResult

log = logging.getLogger(__name__)

COHERE_EMBED_MODEL = "embed-multilingual-v3.0"
COHERE_COLLECTION = "fachliteratur_cohere"


class _CohereEmbedder:
    """
    Duck-Type-kompatibler Ersatz fuer ``SentenceTransformer``.
    Nutzt Cohere Embed API und gibt ein Array mit ``.tolist()`` zurueck
    — genau was ``JuristischerRetriever.search()`` erwartet.
    """

    def __init__(self, client: "cohere.ClientV2",
                 model: str = COHERE_EMBED_MODEL):
        self.client = client
        self.model = model

    def encode(self, text: str, normalize_embeddings: bool = True):
        # E5-Prefixe entfernen; fuer Cohere ist `input_type` entscheidend
        if text.startswith("query:"):
            raw = text[len("query:"):].strip()
            input_type = "search_query"
        elif text.startswith("passage:"):
            raw = text[len("passage:"):].strip()
            input_type = "search_document"
        else:
            raw = text
            input_type = "search_query"

        resp = self.client.embed(
            texts=[raw],
            model=self.model,
            input_type=input_type,
            embedding_types=["float"],
        )
        vec = np.array(resp.embeddings.float_[0], dtype=np.float32)
        if normalize_embeddings:
            n = np.linalg.norm(vec)
            if n > 0:
                vec = vec / n
        return vec


class OursCohereRetriever:
    """
    Unsere eigene Pipeline (Query Expansion + Hybrid + Rerank), aber
    mit Cohere-Embeddings auf einer parallelen Qdrant-Collection.
    """

    def __init__(self, collection: str = COHERE_COLLECTION,
                 env_file: str = ".env.local"):
        load_dotenv(env_file, override=True)
        api_key = os.getenv("COHERE_API_KEY") or os.getenv("CO_API_KEY")
        if not api_key:
            raise ValueError("COHERE_API_KEY nicht gesetzt")

        # Wrapped retriever mit identischer Hybrid-/Rerank-Logik
        self._retriever = JuristischerRetriever(env_file=env_file)
        # E5-Model durch Cohere-Wrapper ersetzen (monkey-patch,
        # aber die Instanz ist isoliert vom ``ours``-Retriever im Benchmark)
        self._retriever.model = _CohereEmbedder(cohere.ClientV2(api_key=api_key))
        self.collection = collection
        log.info(f"OursCohereRetriever bereit (collection={collection})")

    def search(self, query: str, top_k: int = 10) -> list[SearchResult]:
        results, _ = self._retriever.search(
            query,
            collections=[self.collection],
            top_k=top_k,
        )
        # Kennzeichne Collection im Ergebnis
        for r in results:
            r.collection = f"ours-cohere:{self.collection}"
        return results
