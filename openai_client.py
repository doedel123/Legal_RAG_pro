#!/usr/bin/env python3
"""
OpenAI-Adapter
==============
Duenner Wrapper um die OpenAI Vector Stores Search API, der dieselbe API
wie ``retrieve.JuristischerRetriever`` und ``ragie_client.RagieRetriever`` liefert
— damit der Benchmark drei Systeme einheitlich ansprechen kann.

Nutzung:
    from openai_client import OpenAIRetriever
    r = OpenAIRetriever()
    results = r.search("Konkludente Taeuschung § 263", top_k=10)
"""

import os
import logging
from typing import Optional

from dotenv import load_dotenv
from openai import OpenAI

from retrieve import SearchResult

log = logging.getLogger(__name__)


class OpenAIRetriever:
    """
    Adapter fuer OpenAI Vector Stores.

    Parameters
    ----------
    vector_store_id : str
        ID des OpenAI Vector Stores (sonst ``OPENAI_VECTOR_STORE_ID`` aus .env).
    rewrite_query : bool
        Laesst OpenAI die Query serverseitig umformulieren
        (eigene Variante von Query-Expansion). Default False — damit der Benchmark
        fair bleibt und unsere Expansion nicht doppelt passiert.
    env_file : str
        Pfad zur .env-Datei mit ``OPENAI_API_KEY`` (+ optional ``OPENAI_VECTOR_STORE_ID``).
    """

    def __init__(self, vector_store_id: Optional[str] = None,
                 rewrite_query: bool = False,
                 env_file: str = ".env.local"):
        load_dotenv(env_file, override=True)

        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY nicht in env-Datei gesetzt")

        self.client = OpenAI(api_key=api_key)
        self.vector_store_id = vector_store_id or os.getenv("OPENAI_VECTOR_STORE_ID")
        if not self.vector_store_id:
            raise ValueError("OPENAI_VECTOR_STORE_ID weder als Argument noch in env gesetzt")

        self.rewrite_query = rewrite_query
        log.info(f"OpenAIRetriever bereit (vs={self.vector_store_id[:15]}..., "
                 f"rewrite_query={rewrite_query})")

    def search(self, query: str, top_k: int = 10) -> list[SearchResult]:
        """Fuehrt eine Vector-Store-Suche gegen OpenAI aus und mappt das Ergebnis
        auf ``SearchResult``-Objekte.
        """
        response = self.client.vector_stores.search(
            vector_store_id=self.vector_store_id,
            query=query,
            max_num_results=top_k,
            rewrite_query=self.rewrite_query,
        )

        results: list[SearchResult] = []
        for item in response.data:
            # OpenAI-Content ist eine Liste von Blocks (type='text'); hier mergen
            texts = [c.text for c in item.content if getattr(c, "type", None) == "text"]
            text = "\n".join(texts).strip()

            meta = {
                "source_type": "fachliteratur",
                "document_id": item.file_id,
                "document_name": item.filename,
                "source_file": item.filename,
            }
            if getattr(item, "attributes", None):
                meta.update({f"attr_{k}": v for k, v in item.attributes.items()})

            results.append(SearchResult(
                text=text,
                score=item.score,
                collection=f"openai:{self.vector_store_id[:15]}",
                metadata=meta,
            ))
        return results
