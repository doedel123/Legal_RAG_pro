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
import time
import logging

import requests
from dotenv import load_dotenv

from retrieve import SearchResult, DEFAULT_TOP_K
from ours_mxbai_client import OursMxbaiRetriever, MXBAI_COLLECTION

log = logging.getLogger(__name__)

VOYAGE_RERANK_URL = "https://api.voyageai.com/v1/rerank"
VOYAGE_RERANK_MODEL = "rerank-2.5"


class _VoyageReranker:
    """
    Duck-Type-kompatibel zu CohereReranker/LocalReranker: ``rerank(query, results, top_k)``
    liefert eine gefilterte Liste von SearchResults.
    """

    def __init__(self, api_key: str, model: str = VOYAGE_RERANK_MODEL,
                 timeout: int = 30):
        self.api_key = api_key
        self.model = model
        self.timeout = timeout
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        log.info(f"VoyageReranker ({model}) bereit.")

    def rerank(self, query: str, results: list[SearchResult],
               top_k: int = DEFAULT_TOP_K) -> list[SearchResult]:
        if not results:
            return results

        documents = []
        for r in results:
            t = r.text
            # Breadcrumb-Prefix (`[... ]\n`) entfernen – konsistent mit CohereReranker
            if t.startswith("["):
                idx = t.find("]\n")
                if idx > 0:
                    t = t[idx + 2:]
            documents.append(t)

        payload = {
            "query": query,
            "documents": documents,
            "model": self.model,
            "top_k": min(top_k, len(documents)),
        }

        # Retry mit exponential Backoff bei 429 / 5xx
        max_attempts = 5
        backoff = 4
        data = None
        for attempt in range(1, max_attempts + 1):
            try:
                resp = requests.post(VOYAGE_RERANK_URL, headers=self.headers,
                                     json=payload, timeout=self.timeout)
                status = resp.status_code
                if status == 200:
                    data = resp.json()
                    break
                if status in (429, 500, 502, 503, 504) and attempt < max_attempts:
                    log.info(f"Voyage {status} — warte {backoff}s "
                             f"(Versuch {attempt}/{max_attempts}) ...")
                    time.sleep(backoff)
                    backoff = min(backoff * 2, 60)
                    continue
                resp.raise_for_status()
            except requests.exceptions.RequestException as e:
                if attempt < max_attempts:
                    log.info(f"Voyage Fehler ({e}) — Retry in {backoff}s ...")
                    time.sleep(backoff)
                    backoff = min(backoff * 2, 60)
                    continue
                log.warning(f"Voyage Reranking endgueltig fehlgeschlagen: {e}")
                return results[:top_k]

        if data is None:
            log.warning("Voyage Reranking fehlgeschlagen (alle Retries erschoepft)")
            return results[:top_k]

        reranked = []
        for item in data.get("data", []):
            idx = item.get("index")
            if idx is None or idx >= len(results):
                continue
            original = results[idx]
            reranked.append(SearchResult(
                text=original.text,
                score=float(item.get("relevance_score", 0.0)),
                collection=original.collection,
                metadata=original.metadata,
            ))
        return reranked


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
