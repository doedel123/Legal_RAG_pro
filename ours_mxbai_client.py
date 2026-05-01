#!/usr/bin/env python3
"""
Ours-with-Mxbai-DE-Embeddings Adapter
=====================================
Variante unserer eigenen Pipeline, die E5-large durch das deutsch-optimierte
``mixedbread-ai/deepset-mxbai-embed-de-large-v1`` ersetzt. Sucht in der
parallelen Qdrant-Collection ``fachliteratur_mxbai`` (via reindex_mxbai.py
befuellt). Query Expansion, BM25-Hybrid-Suche und Cohere-Reranking bleiben
identisch.

Empfohlener Query-Prompt laut Modell-Karte:
    "Represent this sentence for searching relevant passages: {query}"
Passagen ohne Prefix.
"""

import logging
from typing import Optional

from sentence_transformers import SentenceTransformer

from retrieve import JuristischerRetriever, SearchResult

log = logging.getLogger(__name__)

MXBAI_MODEL = "mixedbread-ai/deepset-mxbai-embed-de-large-v1"
MXBAI_COLLECTION = "fachliteratur_mxbai"
QUERY_PROMPT = "Represent this sentence for searching relevant passages: "


class _MxbaiEmbedder:
    """
    Duck-Type-kompatibler Ersatz fuer die E5-SentenceTransformer-Instanz in
    ``JuristischerRetriever``. Entfernt die E5-Prefixe ``query:`` / ``passage:``
    und ersetzt sie durch das fuer mxbai-de empfohlene Query-Prompt (nur bei
    Queries; Passagen brauchen keinen Prefix).
    """

    def __init__(self, model_name: str = MXBAI_MODEL):
        self.model = SentenceTransformer(model_name)

    def encode(self, text: str, normalize_embeddings: bool = True):
        if text.startswith("query:"):
            raw = text[len("query:"):].strip()
            prompt = QUERY_PROMPT + raw
        elif text.startswith("passage:"):
            prompt = text[len("passage:"):].strip()
        else:
            prompt = text
        return self.model.encode(prompt, normalize_embeddings=normalize_embeddings)


class OursMxbaiRetriever:
    """
    Unsere eigene Pipeline (Query Expansion + Hybrid + Cohere-Rerank), aber
    mit mxbai-de-Embeddings auf einer parallelen Qdrant-Collection.
    """

    def __init__(self, collection: str = MXBAI_COLLECTION,
                 env_file: str = ".env.local"):
        self._retriever = JuristischerRetriever(env_file=env_file)
        # E5-Model durch mxbai-de-Wrapper ersetzen (isolierte Instanz)
        self._retriever.model = _MxbaiEmbedder()
        self.collection = collection
        log.info(f"OursMxbaiRetriever bereit (collection={collection})")

    def search(self, query: str, top_k: int = 10,
               domain: Optional[str] = None) -> list[SearchResult]:
        """Sucht in der mxbai-Collection; ``domain`` filtert auf Fachgebiet
        (z.B. ``"strafrecht"``, ``"mietrecht"``). None = cross-domain."""
        results, _ = self._retriever.search(
            query,
            collections=[self.collection],
            top_k=top_k,
            domain=domain,
        )
        for r in results:
            r.collection = f"ours-mxbai:{self.collection}"
        return results
