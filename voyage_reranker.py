#!/usr/bin/env python3
"""
Standalone Voyage-Reranker (ohne Abhaengigkeit zu sentence-transformers).
Wird von ours_mxbai_voyage_client.py (Dev) und ours_mxbai_api_client.py
(Produktion) gemeinsam genutzt.
"""

import time
import logging

import requests

from retrieve import SearchResult, DEFAULT_TOP_K

log = logging.getLogger(__name__)

VOYAGE_RERANK_URL = "https://api.voyageai.com/v1/rerank"
VOYAGE_RERANK_MODEL = "rerank-2.5"


class VoyageReranker:
    """
    Duck-Type-kompatibel zu CohereReranker/LocalReranker. Ruft Voyage's
    Rerank-API auf mit Retry/Backoff bei 429/5xx.
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
