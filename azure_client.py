#!/usr/bin/env python3
"""
Azure AI Search Adapter
========================
Wrapper um Azure AI Search, kompatibel zur ``SearchResult``-API der anderen
Retriever. Liefert zwei Varianten:

  - ``AzureHybridRetriever``    BM25 + Vector (RRF), kein Server-Reranker
  - ``AzureSemanticRetriever``  Hybrid + Microsoft Semantic Ranker (L2-Rerank)

Beide nutzen den deutschen ``de.microsoft``-Analyzer (Komposita-Split,
Stemming) und INT8-Scalar-Quantization mit Rescoring auf Volltext-Vektoren
(siehe Index-Schema in ``import_strafrecht_azure.py``).

Embedding der Query: OpenAI ``text-embedding-3-large`` (3072d, gleiches
Modell wie beim Index-Build).
"""

import logging
import os
from typing import Optional

from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery
from openai import OpenAI

from retrieve import SearchResult

log = logging.getLogger(__name__)

DEFAULT_ENDPOINT = "https://legalrag.search.windows.net"
INDEX_NAME = "fachliteratur"
EMBED_MODEL = "text-embedding-3-large"
SEMANTIC_CONFIG = "default"

# Felder, die wir aus dem Index zurueckbekommen wollen (text + metadata)
SELECT_FIELDS = [
    "id", "text", "breadcrumb", "domain", "source_type",
    "paragraph", "gesetz", "kommentar", "randnummer", "page", "source_file",
]


class _AzureBase:
    """Gemeinsame Logik fuer beide Azure-Retriever-Varianten."""

    def __init__(self,
                 endpoint: Optional[str] = None,
                 index: str = INDEX_NAME,
                 env_file: str = ".env.local",
                 expand: bool = False):
        load_dotenv(env_file, override=True)

        ep = endpoint or os.getenv("AZURE_SEARCH_ENDPOINT") or DEFAULT_ENDPOINT
        admin_key = os.getenv("AZURE_QUERY_KEY") or os.getenv("AZURE_PRIMARY_API_KEY")
        if not admin_key:
            raise ValueError("AZURE_QUERY_KEY oder AZURE_PRIMARY_API_KEY fehlt")
        openai_key = os.getenv("OPENAI_API_KEY")
        if not openai_key:
            raise ValueError("OPENAI_API_KEY fehlt (fuer Query-Embedding)")

        self.client = SearchClient(
            endpoint=ep, index_name=index,
            credential=AzureKeyCredential(admin_key),
        )
        self.openai = OpenAI(api_key=openai_key)
        self.endpoint = ep
        self.index = index

        # Optionale Claude-Query-Expansion (gleicher Pfad wie ours-api)
        self.expander = None
        if expand:
            from retrieve import QueryExpander
            self.expander = QueryExpander()
            log.info("Query Expansion aktiviert (Claude)")

    def _embed(self, text: str) -> list[float]:
        resp = self.openai.embeddings.create(model=EMBED_MODEL, input=text)
        return resp.data[0].embedding

    def _maybe_expand(self, query: str) -> str:
        if not self.expander:
            return query
        try:
            ex = self.expander.expand(query)
            return ex.expanded or query
        except Exception as e:
            log.warning("Query Expansion fehlgeschlagen: %s", e)
            return query

    def _to_results(self, hits, label: str) -> list[SearchResult]:
        out: list[SearchResult] = []
        for h in hits:
            # Semantic-Rerank-Score wenn vorhanden, sonst Suchscore
            score = h.get("@search.reranker_score") or h.get("@search.score") or 0.0
            md = {k: h.get(k) for k in SELECT_FIELDS if k != "text" and h.get(k) is not None}
            out.append(SearchResult(
                text=h.get("text", ""),
                score=float(score),
                collection=label,
                metadata=md,
            ))
        return out


class AzureHybridRetriever(_AzureBase):
    """Hybrid: BM25 (de.microsoft Analyzer) + Vector (HNSW INT8) ueber RRF."""

    def search(self, query: str, top_k: int = 10,
               domain: Optional[str] = None) -> list[SearchResult]:
        sq = self._maybe_expand(query)
        qv = self._embed(sq)
        vq = VectorizedQuery(
            vector=qv,
            k_nearest_neighbors=top_k * 4,
            fields="text_vector",
        )
        kwargs = dict(
            search_text=sq,
            vector_queries=[vq],
            top=top_k,
            select=SELECT_FIELDS,
        )
        if domain:
            kwargs["filter"] = f"domain eq '{domain.lower()}'"
        try:
            hits = list(self.client.search(**kwargs))
        except Exception as e:
            log.warning("Azure-Hybrid-Aufruf fehlgeschlagen: %s", e); return []
        return self._to_results(hits, label=f"azure-hybrid:{self.index}")


class AzureSemanticRetriever(_AzureBase):
    """Hybrid + Microsoft Semantic Ranker (Cross-Encoder L2-Rerank)."""

    def search(self, query: str, top_k: int = 10,
               domain: Optional[str] = None) -> list[SearchResult]:
        qv = self._embed(query)
        vq = VectorizedQuery(
            vector=qv,
            k_nearest_neighbors=top_k * 4,
            fields="text_vector",
        )
        kwargs = dict(
            search_text=query,
            vector_queries=[vq],
            top=top_k,
            select=SELECT_FIELDS,
            query_type="semantic",
            semantic_configuration_name=SEMANTIC_CONFIG,
        )
        if domain:
            kwargs["filter"] = f"domain eq '{domain.lower()}'"
        try:
            hits = list(self.client.search(**kwargs))
        except Exception as e:
            log.warning("Azure-Semantic-Aufruf fehlgeschlagen: %s", e); return []
        return self._to_results(hits, label=f"azure-semantic:{self.index}")
