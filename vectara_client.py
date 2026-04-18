#!/usr/bin/env python3
"""
Vectara-Adapter
===============
Duenner Wrapper um die Vectara v2 Query-API, der die gleiche Schnittstelle
liefert wie ``retrieve.JuristischerRetriever`` — damit der Benchmark alle
Systeme einheitlich ansprechen kann.

Nutzung:
    from vectara_client import VectaraRetriever
    r = VectaraRetriever(corpus_key="strafrecht")
    results = r.search("Konkludente Taeuschung § 263", top_k=10)

Env (.env.local):
    VECTARA_API_KEY    = personal API key
    VECTARA_CORPUS_KEY = key des Corpus (Default: "strafrecht")
"""

import os
import logging
from typing import Optional

import requests
from dotenv import load_dotenv

from retrieve import SearchResult

log = logging.getLogger(__name__)

VECTARA_BASE_URL = "https://api.vectara.io"


class VectaraRetriever:
    """
    Minimaler Vectara-Client, kompatibel zur SearchResult-Struktur von retrieve.py.

    Parameters
    ----------
    corpus_key : str
        Vectara-Corpus-Key (vom User beim Corpus-Anlegen vergeben,
        oder aus der Vectara-Console ablesbar).
    rerank : bool
        Server-seitiges Reranking (MMR) aktivieren.
    env_file : str
        Pfad zur .env-Datei mit ``VECTARA_API_KEY``.
    timeout : int
        Request-Timeout in Sekunden.
    """

    def __init__(self, corpus_key: Optional[str] = None,
                 rerank: bool = False,
                 env_file: str = ".env.local",
                 timeout: int = 30):
        load_dotenv(env_file, override=True)
        api_key = os.getenv("VECTARA_API_KEY")
        if not api_key:
            raise ValueError("VECTARA_API_KEY nicht in env-Datei gesetzt")

        self.corpus_key = corpus_key or os.getenv("VECTARA_CORPUS_KEY") or "strafrecht"
        self.rerank = rerank
        self.timeout = timeout
        self.headers = {
            "x-api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        log.info(f"VectaraRetriever bereit (corpus={self.corpus_key}, rerank={rerank})")

    def search(self, query: str, top_k: int = 10) -> list[SearchResult]:
        """Fuehrt eine Retrieval-Anfrage an Vectara aus und mappt das Ergebnis
        auf ``SearchResult``-Objekte.
        """
        url = f"{VECTARA_BASE_URL}/v2/corpora/{self.corpus_key}/query"
        search_cfg: dict = {"limit": top_k}
        if self.rerank:
            # MMR diversifiziert die Top-K, ohne zusätzliche Kosten
            search_cfg["reranker"] = {"type": "mmr", "diversity_bias": 0.1}

        payload = {
            "query": query,
            "search": search_cfg,
            # kein Summarizer — wir wollen nur die Chunks für den Benchmark
            "generation": None,
        }

        resp = requests.post(url, headers=self.headers, json=payload,
                             timeout=self.timeout)
        if resp.status_code != 200:
            raise RuntimeError(
                f"Vectara-Query fehlgeschlagen ({resp.status_code}): {resp.text[:500]}"
            )
        data = resp.json()

        results: list[SearchResult] = []
        for hit in data.get("search_results", []):
            doc_meta = hit.get("document_metadata") or {}
            part_meta = hit.get("part_metadata") or {}
            meta = {
                "source_type": "fachliteratur",
                "document_id": hit.get("document_id", ""),
                "document_name": doc_meta.get("title") or hit.get("document_id", ""),
                "source_file": doc_meta.get("title") or hit.get("document_id", ""),
            }
            if doc_meta:
                meta.update({f"doc_{k}": v for k, v in doc_meta.items()})
            if part_meta:
                meta.update(part_meta)

            results.append(SearchResult(
                text=hit.get("text", ""),
                score=float(hit.get("score", 0.0)),
                collection=f"vectara:{self.corpus_key}",
                metadata=meta,
            ))
        return results
