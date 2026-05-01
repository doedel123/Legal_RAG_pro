#!/usr/bin/env python3
"""
PageIndex-Adapter
=================
Duenner Wrapper um den PageIndex-Tree (donkredito_structure.json), der die
gleiche ``search(query, top_k) -> list[SearchResult]``-API liefert wie unsere
anderen Retriever. So laeuft PageIndex im Benchmark neben ours-mxbai / RAGIE /
Vectara ohne Sonderbehandlung.

Retrieval-Strategie (single-call ranking):
    1. Tree in kompakten Katalog serialisieren (node_id + title + summary-Snippet)
    2. gpt-4o sieht Katalog + Query, liefert Top-K node_ids als JSON
    3. Fuer jede ID: Knoten-Text als SearchResult verpacken

Das ist eine Vereinfachung des agentischen Tool-Loops von PageIndex
(get_document_structure → get_page_content), laesst sich aber fair am gleichen
Top-K-Judge messen.
"""

from __future__ import annotations

import json
import logging
import os
import re
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
import litellm

from retrieve import SearchResult

log = logging.getLogger(__name__)

DEFAULT_TREE_PATH = Path(__file__).parent / "PageIndex" / "results" / "donkredito_structure.json"
DEFAULT_MODEL = "gpt-4o-2024-11-20"
SUMMARY_SNIPPET_CHARS = 280
COLLECTION_LABEL = "pageindex:donkredito"


def _flatten(nodes: list[dict], parent_path: tuple[str, ...] = ()) -> list[dict]:
    flat = []
    for n in nodes:
        title = (n.get("title") or "").strip()
        breadcrumb = " > ".join(parent_path + (title[:60],))
        flat.append({
            "node_id": n.get("node_id", ""),
            "title": title,
            "breadcrumb": breadcrumb,
            "line_num": n.get("line_num"),
            "text": n.get("text") or "",
            "summary": (n.get("summary") or n.get("prefix_summary") or "").strip(),
        })
        if n.get("nodes"):
            flat.extend(_flatten(n["nodes"], parent_path + (title[:60],)))
    return flat


def _build_catalog(flat_nodes: list[dict]) -> str:
    lines = []
    for n in flat_nodes:
        snippet = n["summary"][:SUMMARY_SNIPPET_CHARS].replace("\n", " ")
        lines.append(f'[{n["node_id"]}] {n["breadcrumb"]}  ::  {snippet}')
    return "\n".join(lines)


class PageIndexRetriever:
    """PageIndex-Retrieval auf einem vorgebauten Tree via single-call LLM-Ranking."""

    def __init__(self,
                 tree_path: str | Path = DEFAULT_TREE_PATH,
                 model: str = DEFAULT_MODEL,
                 env_file: str = ".env.local"):
        load_dotenv(env_file, override=True)
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OPENAI_API_KEY fehlt fuer PageIndex-Retrieval")
        path = Path(tree_path)
        if not path.exists():
            raise FileNotFoundError(f"PageIndex-Tree nicht gefunden: {path}")
        with path.open() as f:
            self.tree = json.load(f)
        self.model = model
        self.doc_name = self.tree.get("doc_name", "doc")
        self.nodes = _flatten(self.tree.get("structure", []))
        self.by_id = {n["node_id"]: n for n in self.nodes}
        self.catalog = _build_catalog(self.nodes)
        log.info("PageIndexRetriever bereit (%d Knoten, Modell=%s)",
                 len(self.nodes), self.model)

    def search(self, query: str, top_k: int = 10) -> list[SearchResult]:
        prompt = (
            "Du erhaelst einen Katalog von Abschnitten eines Ermittlungsakte-Dokuments. "
            "Jede Zeile: [node_id] Breadcrumb :: Zusammenfassung-Snippet.\n\n"
            f"KATALOG:\n{self.catalog}\n\n"
            f"ANFRAGE: {query}\n\n"
            f"Gib die {top_k} relevantesten node_ids zurueck als JSON-Liste, sortiert "
            "von relevantest nach weniger relevant. Nur ein JSON-Array, keine Erklaerung. "
            'Beispiel: ["0042", "0113", "0007"]'
        )

        try:
            resp = litellm.completion(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
            )
            raw = resp.choices[0].message.content or ""
        except Exception as e:
            log.error("PageIndex-LLM-Call fehlgeschlagen: %s", e)
            return []

        ids = _parse_id_list(raw)
        results: list[SearchResult] = []
        for rank, nid in enumerate(ids[:top_k], start=1):
            n = self.by_id.get(nid)
            if not n or not n["text"]:
                continue
            results.append(SearchResult(
                text=n["text"],
                score=1.0 / rank,
                collection=COLLECTION_LABEL,
                metadata={
                    "source_type": "ermittlungsakte",
                    "heading": n["title"],
                    "breadcrumb": n["breadcrumb"],
                    "line_num": n["line_num"],
                    "node_id": nid,
                    "rank": rank,
                },
            ))
        return results


def _parse_id_list(raw: str) -> list[str]:
    raw = raw.strip()
    m = re.search(r"\[[^\[\]]*\]", raw, flags=re.DOTALL)
    if m:
        try:
            arr = json.loads(m.group(0))
            return [str(x).strip().strip('"') for x in arr if str(x).strip()]
        except json.JSONDecodeError:
            pass
    return re.findall(r'"?(\d{3,4})"?', raw)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    r = PageIndexRetriever()
    for q in [
        "Wer ist die Geschaedigte in diesem Fall?",
        "Welche Firmen sind in den Betrugsfall verwickelt?",
    ]:
        print(f"\n=== {q} ===")
        for res in r.search(q, top_k=3):
            print(f"[{res.score:.3f}] {res.metadata.get('breadcrumb')}")
            print(f"    {res.text[:200].replace(chr(10), ' ')}...")
