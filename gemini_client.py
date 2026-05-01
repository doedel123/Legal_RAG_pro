#!/usr/bin/env python3
"""
Gemini File Search Adapter
==========================
Wrapper um Gemini's File Search Tool, der die gleiche API liefert wie
``retrieve.JuristischerRetriever`` — damit der Benchmark einheitlich
mit unserem RAG / RAGIE / OpenAI vergleichen kann.

Pipeline:
  1. ``generate_content`` mit FileSearch-Tool aufrufen
  2. Die zurueckgegebenen ``grounding_chunks`` (Top-K Chunks) extrahieren
  3. Da Gemini keine expliziten Scores ausliefert, nutzen wir den Rang
     als Proxy-Score (1.0, 0.95, 0.90, ...).

Das LLM-Antwort-Generieren wird auf ein Minimum reduziert (max_output_tokens=64),
damit die Latenz nicht ins Bodenlose faellt — wir wollen nur die Chunks.

Nutzung:
    from gemini_client import GeminiRetriever
    r = GeminiRetriever()
    results = r.search("Konkludente Taeuschung § 263", top_k=10)
"""

import os
import logging
from typing import Optional

from dotenv import load_dotenv
from google import genai
from google.genai import types

from retrieve import SearchResult

log = logging.getLogger(__name__)

# Schnelles, guenstiges Modell — wir wollen nur die Chunks, nicht die Antwort
GEMINI_MODEL = "gemini-2.5-flash"
# Hoch genug, damit Gemini den File-Search-Tool-Call ueberhaupt ausloest.
# Niedrigere Werte (z.B. 64) führen dazu, dass das Modell direkt eine Antwort
# beginnt, in MAX_TOKENS laeuft und das Tool nie aufruft → leere
# grounding_metadata. 1024 reicht zuverlaessig fuer Tool-Use + Kurz-Antwort.
MAX_OUTPUT_TOKENS = 1024


class GeminiRetriever:
    """
    Gemini File Search-Client, kompatibel zur SearchResult-Struktur.

    Parameters
    ----------
    store_name : str | None
        Vollqualifizierter Name des File Search Stores
        (z.B. ``fileSearchStores/strafrecht-8l3wgktjduks``).
        Wenn None: aus env-Variable ``GEMINI_FILE_SEARCH_STORE``.
    model : str
        Gemini-Modell fuer die generate_content-Anfrage.
    env_file : str
        Pfad zur .env-Datei mit ``GEMINI_API_KEY``.
    """

    def __init__(self, store_name: Optional[str] = None,
                 model: str = GEMINI_MODEL,
                 env_file: str = ".env.local"):
        load_dotenv(env_file, override=True)
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY nicht in env-Datei gesetzt")

        self.store_name = store_name or os.getenv("GEMINI_FILE_SEARCH_STORE")
        if not self.store_name:
            raise ValueError(
                "GEMINI_FILE_SEARCH_STORE nicht gesetzt. "
                "Erst `python setup_gemini.py` laufen lassen und "
                "den ausgegebenen Store-Namen in .env.local eintragen."
            )

        self.client = genai.Client(api_key=api_key)
        self.model = model
        log.info(f"GeminiRetriever bereit (model={model}, store={self.store_name})")

    def search(self, query: str, top_k: int = 10) -> list[SearchResult]:
        """Fuehrt eine Retrieval-Anfrage an Gemini File Search aus."""
        config = types.GenerateContentConfig(
            tools=[
                types.Tool(
                    file_search=types.FileSearch(
                        file_search_store_names=[self.store_name],
                        top_k=top_k,
                    )
                )
            ],
            max_output_tokens=MAX_OUTPUT_TOKENS,
            temperature=0.0,
        )

        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=query,
                config=config,
            )
        except Exception as e:
            log.warning(f"Gemini-Aufruf fehlgeschlagen: {e}")
            return []

        # Chunks aus grounding_metadata extrahieren
        candidates = getattr(response, "candidates", None) or []
        if not candidates:
            return []
        grounding = getattr(candidates[0], "grounding_metadata", None)
        if not grounding:
            return []
        gchunks = getattr(grounding, "grounding_chunks", None) or []

        results: list[SearchResult] = []
        for rank, gc in enumerate(gchunks):
            ctx = getattr(gc, "retrieved_context", None)
            if not ctx:
                continue
            text = getattr(ctx, "text", None) or ""
            if not text:
                continue
            doc = (getattr(ctx, "title", None)
                   or getattr(ctx, "document_name", None)
                   or "Gemini-Doc")

            # Rang-basierter Proxy-Score (1.0 → 1/(N+1)), monoton fallend
            proxy_score = 1.0 - (rank / max(len(gchunks), 1)) * 0.5

            results.append(SearchResult(
                text=text,
                score=proxy_score,
                collection=f"gemini:{self.store_name.split('/')[-1]}",
                metadata={
                    "source_type": "fachliteratur",
                    "document_name": doc,
                    "source_file": doc,
                    "chunk_rank": rank + 1,
                    "score_kind": "proxy_rank",
                },
            ))
        return results
