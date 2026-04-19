#!/usr/bin/env python3
"""
Ours-Mixedbread-API + Voyage-Rerank (Produktions-Stack)
========================================================
Produktionstaugliche Variante: statt mxbai-de lokal via SentenceTransformer
zu laden, wird die **Mixedbread Embedding-API** genutzt. Modell-Identitaet
ist garantiert (``mxbai-embed-de-large-v1``), Vektoren damit kompatibel zur
bestehenden ``fachliteratur_mxbai``-Collection — **kein Re-Index noetig**.

Reranker: Voyage ``rerank-2.5`` (bester Reranker aus den Benchmarks).

Vorteil: Server braucht kein lokales Modell, keine GPU, kein MPS.
Latenz-Aufschlag: ~100–200 ms fuer den Embedding-API-Call.

Env (.env.local):
    MIXEDBREAD_API_KEY = Mixedbread API Key
    VOYAGE_API_KEY     = Voyage API Key (fuer Reranker)
    MIXEDBREAD_API_BASE = https://api.mixedbread.com/v1  (optional, Default)
"""

import os
import logging

import numpy as np
import requests
from dotenv import load_dotenv

from retrieve import SearchResult
from ours_mxbai_client import MXBAI_COLLECTION, MXBAI_MODEL, QUERY_PROMPT
from ours_mxbai_voyage_client import _VoyageReranker

log = logging.getLogger(__name__)


class _MxbaiApiEmbedder:
    """
    Duck-Type-kompatibler Ersatz fuer die lokale SentenceTransformer-Instanz.
    Ruft die Mixedbread Embedding-API auf (OpenAI-kompatibles Schema).
    """

    def __init__(self, api_key: str, model: str = MXBAI_MODEL,
                 api_base: str = "https://api.mixedbread.com/v1",
                 timeout: int = 30):
        self.api_key = api_key
        self.model = model
        self.url = f"{api_base.rstrip('/')}/embeddings"
        self.timeout = timeout
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

    def encode(self, text: str, normalize_embeddings: bool = True):
        # Gleiche Prompt-Logik wie lokaler Client:
        # mxbai-de Queries profitieren von einem Representation-Prompt.
        if text.startswith("query:"):
            raw = text[len("query:"):].strip()
            prompt = QUERY_PROMPT + raw
        elif text.startswith("passage:"):
            prompt = text[len("passage:"):].strip()
        else:
            prompt = text

        payload = {"model": self.model, "input": prompt}
        resp = requests.post(self.url, headers=self.headers,
                             json=payload, timeout=self.timeout)
        resp.raise_for_status()
        data = resp.json()
        vec = np.array(data["data"][0]["embedding"], dtype=np.float32)
        if normalize_embeddings:
            n = np.linalg.norm(vec)
            if n > 0:
                vec = vec / n
        return vec


class OursApiRetriever:
    """
    Voll-API-basierter Produktions-Retriever:
      - Query Expansion via Anthropic
      - Query Embedding via Mixedbread API (mxbai-embed-de-large-v1)
      - Hybrid Search gegen bestehende Qdrant-Collection ``fachliteratur_mxbai``
      - Rerank via Voyage rerank-2.5

    Kein lokales Modell noetig — deploybar als schlanker FastAPI-Container
    auf Cloud Run / Fly.io.
    """

    def __init__(self, collection: str = MXBAI_COLLECTION,
                 env_file: str = ".env.local"):
        load_dotenv(env_file, override=True)
        mxbai_key = os.getenv("MIXEDBREAD_API_KEY") or os.getenv("MXBAI_API_KEY")
        voyage_key = os.getenv("VOYAGE_API_KEY")
        if not mxbai_key:
            raise ValueError("MIXEDBREAD_API_KEY nicht gesetzt")
        if not voyage_key:
            raise ValueError("VOYAGE_API_KEY nicht gesetzt")

        api_base = os.getenv("MIXEDBREAD_API_BASE") or \
                   os.getenv("MXBAI_API_BASE") or \
                   "https://api.mixedbread.com/v1"

        # Wir re-usen die gesamte Retriever-Pipeline (Expansion + Hybrid)
        # und tauschen nur Embedder und Reranker aus. lazy_model=True spart
        # sentence-transformers/torch in Produktions-Containern.
        from retrieve import JuristischerRetriever
        self._retriever = JuristischerRetriever(env_file=env_file, lazy_model=True)
        self._retriever.model = _MxbaiApiEmbedder(api_key=mxbai_key, api_base=api_base)
        self._retriever.reranker = _VoyageReranker(api_key=voyage_key)
        self.collection = collection
        log.info(f"OursApiRetriever bereit "
                 f"(mxbai-api + voyage-rerank-2.5, collection={collection})")

    def search(self, query: str, top_k: int = 10) -> list[SearchResult]:
        results, _ = self._retriever.search(
            query,
            collections=[self.collection],
            top_k=top_k,
        )
        for r in results:
            r.collection = f"ours-api:{self.collection}"
        return results
