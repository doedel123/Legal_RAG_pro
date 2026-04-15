#!/usr/bin/env python3
"""
RAGIE-Adapter
=============
Duenner Wrapper um das RAGIE Python SDK, der die gleiche API liefert
wie ``retrieve.JuristischerRetriever`` — damit der Benchmark beide Systeme
einheitlich ansprechen kann.

Nutzung:
    from ragie_client import RagieRetriever
    r = RagieRetriever(partition="strafrecht")
    results = r.search("Konkludente Taeuschung § 263", top_k=10)
"""

import os
import logging
from typing import Optional

from dotenv import load_dotenv
from ragie import Ragie

from retrieve import SearchResult

log = logging.getLogger(__name__)


class RagieRetriever:
    """
    Minimaler RAGIE-Client, kompatibel zur SearchResult-Struktur von retrieve.py.

    Parameters
    ----------
    partition : str
        RAGIE-Partition (bei uns ``strafrecht``).
    rerank : bool
        Server-seitiges Reranking von RAGIE aktivieren.
    env_file : str
        Pfad zur .env-Datei mit ``RAGIE_API_KEY``.
    """

    def __init__(self, partition: str = "strafrecht",
                 rerank: bool = True,
                 env_file: str = ".env.local"):
        load_dotenv(env_file, override=True)
        api_key = os.getenv("RAGIE_API_KEY")
        if not api_key:
            raise ValueError("RAGIE_API_KEY nicht in env-Datei gesetzt")

        self.client = Ragie(auth=api_key)
        self.partition = partition
        self.rerank = rerank
        log.info(f"RagieRetriever bereit (partition={partition}, rerank={rerank})")

    def search(self, query: str, top_k: int = 10) -> list[SearchResult]:
        """Fuehrt eine Retrieval-Anfrage an RAGIE aus und mappt das Ergebnis
        auf ``SearchResult``-Objekte.
        """
        response = self.client.retrievals.retrieve(request={
            "query": query,
            "top_k": top_k,
            "partition": self.partition,
            "rerank": self.rerank,
        })

        results: list[SearchResult] = []
        for chunk in response.scored_chunks:
            # Metadata: Dokument-Infos ins SearchResult-Metadata mappen
            meta = {
                "source_type": "fachliteratur",
                "document_id": chunk.document_id,
                "document_name": chunk.document_name,
                "chunk_index": chunk.index,
                "source_file": chunk.document_name,
            }
            # RAGIE document_metadata & chunk metadata mergen
            if chunk.document_metadata:
                meta.update({f"doc_{k}": v for k, v in chunk.document_metadata.items()})
            if chunk.metadata:
                meta.update(chunk.metadata)

            results.append(SearchResult(
                text=chunk.text,
                score=chunk.score,
                collection=f"ragie:{self.partition}",
                metadata=meta,
            ))
        return results
