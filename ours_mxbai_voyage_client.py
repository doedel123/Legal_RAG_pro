#!/usr/bin/env python3
"""
Ours-Mxbai-Embeddings + Voyage-Reranker Adapter
================================================
Variante unserer Pipeline: identisch zu ``OursMxbaiRetriever`` (mxbai-de
Embeddings + bestehende Hybrid-Suche in ``fachliteratur_mxbai``), aber der
Cohere-Reranker wird durch ``voyage-rerank-2.5`` ersetzt. Ziel: isoliert
messen, wie viel Qualitaet der Reranker-Swap bringt.

Env (.env.local):
    VOYAGE_API_KEY = ...
"""

import os
import logging

from dotenv import load_dotenv

from retrieve import SearchResult
from ours_mxbai_client import OursMxbaiRetriever, MXBAI_COLLECTION
from voyage_reranker import VoyageReranker

log = logging.getLogger(__name__)

# Backward-Compat Alias fuer alten Namen (falls andere Module darauf referenzieren)
_VoyageReranker = VoyageReranker


class OursMxbaiVoyageRetriever:
    """
    Unser RAG mit mxbai-de-Embeddings + Voyage rerank-2.5 statt Cohere.
    Alles andere (Query Expansion, Hybrid-Suche, Collection) identisch zu
    ``OursMxbaiRetriever``.
    """

    def __init__(self, collection: str = MXBAI_COLLECTION,
                 env_file: str = ".env.local"):
        load_dotenv(env_file, override=True)
        api_key = os.getenv("VOYAGE_API_KEY")
        if not api_key:
            raise ValueError("VOYAGE_API_KEY nicht gesetzt")

        # Re-use existierende mxbai-Retriever-Infrastruktur
        self._retriever = OursMxbaiRetriever(collection=collection, env_file=env_file)
        # Cohere-Reranker durch Voyage-Reranker ersetzen
        self._retriever._retriever.reranker = _VoyageReranker(api_key=api_key)
        self.collection = collection
        log.info(f"OursMxbaiVoyageRetriever bereit "
                 f"(mxbai-de + voyage-rerank-2.5, collection={collection})")

    def search(self, query: str, top_k: int = 10) -> list[SearchResult]:
        results = self._retriever.search(query, top_k=top_k)
        for r in results:
            r.collection = f"ours-mxbai-voyage:{self.collection}"
        return results
