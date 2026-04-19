#!/usr/bin/env python3
"""
RAG-Benchmark
=============
Vergleicht unser Qdrant-basiertes RAG mit RAGIE anhand einer YAML-Liste
von Test-Queries. Bewertet Ergebnisqualitaet per LLM-as-Judge (Claude).

Pipeline pro Query:
  1. Beide Systeme liefern Top-K Chunks
  2. Claude bewertet jeden Chunk 0-3 (Relevanz)
  3. Metriken: nDCG@K, Relevance@K, Top-1-Score, Latenz

Usage:
    python benchmark.py                              # Standard-Queries, volle Pipeline
    python benchmark.py --queries my.yaml --top-k 5
    python benchmark.py --skip-judge                 # nur Latenz-Vergleich
    python benchmark.py --systems ours               # nur ein System (dry-run)
"""

import os
import re
import sys
import json
import math
import time
import argparse
import logging
import concurrent.futures
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Optional

import yaml
from dotenv import load_dotenv
from tqdm import tqdm

from retrieve import JuristischerRetriever, SearchResult, FACHLITERATUR_COLLECTION
from ragie_client import RagieRetriever
from openai_client import OpenAIRetriever
from gemini_client import GeminiRetriever
from vectara_client import VectaraRetriever
from ours_cohere_client import OursCohereRetriever
from ours_mxbai_client import OursMxbaiRetriever
from ours_mxbai_voyage_client import OursMxbaiVoyageRetriever
from ours_mxbai_api_client import OursApiRetriever

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

DEFAULT_TOP_K = 10
JUDGE_MODEL = "claude-sonnet-4-20250514"
JUDGE_MAX_TOKENS = 150

logging.basicConfig(
    level=logging.WARNING,  # quiet by default; tqdm handles progress
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)
logging.getLogger("httpx").setLevel(logging.WARNING)

# ---------------------------------------------------------------------------
# LLM-as-Judge Prompt
# ---------------------------------------------------------------------------

JUDGE_SYSTEM_PROMPT = """\
Du bist ein erfahrener Strafrechtsexperte, der die Relevanz von Textauszuegen
aus juristischen Kommentaren (Fischer StGB, Schmitt/Koehler StPO) fuer eine
konkrete Suchanfrage bewertet.

Bewerte auf einer Skala von 0 bis 3:
  3 = Direkt relevant: beantwortet die Frage oder enthaelt die zentralen
      Rechtsbegriffe/Tatbestandsmerkmale
  2 = Thematisch relevant: nuetzlicher Kontext zur Frage, behandelt das
      gleiche Rechtsgebiet
  1 = Tangential: gleiches Thema, aber andere Aspekte (z.B. Nachbarparagraph)
  0 = Irrelevant: beantwortet die Frage nicht, anderes Rechtsgebiet

Antworte AUSSCHLIESSLICH mit einem JSON-Objekt ohne Markdown:
{"score": <0-3>, "reason": "<max 10 Worte Begruendung>"}
"""


def build_judge_user_prompt(query: str, context: str, chunk_text: str) -> str:
    return (
        f"Suchanfrage: {query}\n"
        f"Kontext der Anfrage: {context}\n\n"
        f"Textauszug:\n{chunk_text[:2000]}"
    )


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class QueryCase:
    id: str
    category: str
    query: str
    context: str = ""


@dataclass
class JudgedChunk:
    rank: int
    text: str
    score: float           # retrieval score
    judge_score: int       # 0-3
    judge_reason: str
    metadata: dict = field(default_factory=dict)


@dataclass
class SystemRun:
    system: str
    query_id: str
    latency_sec: float
    chunks: list[JudgedChunk] = field(default_factory=list)

    def ndcg_at_k(self, k: int = 10) -> float:
        rels = [c.judge_score for c in self.chunks[:k]]
        if not rels:
            return 0.0
        dcg = sum(r / math.log2(i + 2) for i, r in enumerate(rels))
        ideal = sorted(rels, reverse=True)
        idcg = sum(r / math.log2(i + 2) for i, r in enumerate(ideal))
        return dcg / idcg if idcg > 0 else 0.0

    def relevance_at_k(self, k: int = 10, threshold: int = 2) -> float:
        top = self.chunks[:k]
        if not top:
            return 0.0
        return sum(1 for c in top if c.judge_score >= threshold) / len(top)

    def top_1_score(self) -> int:
        return self.chunks[0].judge_score if self.chunks else 0

    def mean_score(self) -> float:
        if not self.chunks:
            return 0.0
        return sum(c.judge_score for c in self.chunks) / len(self.chunks)


# ---------------------------------------------------------------------------
# LLM Judge
# ---------------------------------------------------------------------------

class LLMJudge:
    def __init__(self):
        import anthropic
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY fehlt")
        self.client = anthropic.Anthropic(api_key=api_key)

    def judge(self, query: str, context: str, chunk_text: str) -> tuple[int, str]:
        """Bewertet einen Chunk. Returns (score 0-3, reason)."""
        try:
            resp = self.client.messages.create(
                model=JUDGE_MODEL,
                max_tokens=JUDGE_MAX_TOKENS,
                system=JUDGE_SYSTEM_PROMPT,
                messages=[{
                    "role": "user",
                    "content": build_judge_user_prompt(query, context, chunk_text),
                }],
            )
            text = resp.content[0].text.strip()
            if text.startswith("```"):
                text = re.sub(r"^```(?:json)?\s*", "", text)
                text = re.sub(r"\s*```$", "", text)
            data = json.loads(text)
            score = int(data.get("score", 0))
            reason = str(data.get("reason", ""))[:150]
            return max(0, min(3, score)), reason
        except Exception as e:
            log.warning(f"Judge-Fehler: {e}")
            return 0, f"judge-error: {e}"


# ---------------------------------------------------------------------------
# Runners
# ---------------------------------------------------------------------------

def run_our_rag(retriever: JuristischerRetriever, query: str,
                top_k: int) -> tuple[list[SearchResult], float]:
    start = time.time()
    # Nur Fachliteratur vergleichen, volle Pipeline (Expansion + Reranking)
    results, _ = retriever.search(
        query=query,
        collections=[FACHLITERATUR_COLLECTION],
        top_k=top_k,
        expand=True,
        rerank=True,
    )
    return results, time.time() - start


def run_ragie(retriever: RagieRetriever, query: str,
              top_k: int) -> tuple[list[SearchResult], float]:
    start = time.time()
    results = retriever.search(query, top_k=top_k)
    return results, time.time() - start


def run_openai(retriever: OpenAIRetriever, query: str,
               top_k: int) -> tuple[list[SearchResult], float]:
    start = time.time()
    results = retriever.search(query, top_k=top_k)
    return results, time.time() - start


def run_gemini(retriever: GeminiRetriever, query: str,
               top_k: int) -> tuple[list[SearchResult], float]:
    start = time.time()
    results = retriever.search(query, top_k=top_k)
    return results, time.time() - start


def run_vectara(retriever: VectaraRetriever, query: str,
                top_k: int) -> tuple[list[SearchResult], float]:
    start = time.time()
    results = retriever.search(query, top_k=top_k)
    return results, time.time() - start


def run_ours_cohere(retriever: OursCohereRetriever, query: str,
                    top_k: int) -> tuple[list[SearchResult], float]:
    start = time.time()
    results = retriever.search(query, top_k=top_k)
    return results, time.time() - start


def run_ours_mxbai(retriever: OursMxbaiRetriever, query: str,
                   top_k: int) -> tuple[list[SearchResult], float]:
    start = time.time()
    results = retriever.search(query, top_k=top_k)
    return results, time.time() - start


def run_ours_mxbai_voyage(retriever: OursMxbaiVoyageRetriever, query: str,
                          top_k: int) -> tuple[list[SearchResult], float]:
    start = time.time()
    results = retriever.search(query, top_k=top_k)
    return results, time.time() - start


def run_ours_api(retriever: OursApiRetriever, query: str,
                 top_k: int) -> tuple[list[SearchResult], float]:
    start = time.time()
    results = retriever.search(query, top_k=top_k)
    return results, time.time() - start


# ---------------------------------------------------------------------------
# Report helpers
# ---------------------------------------------------------------------------

def strip_breadcrumb(text: str) -> str:
    if text.startswith("["):
        idx = text.find("]\n")
        if idx > 0:
            return text[idx + 2:]
    return text


def location_str(res: SearchResult) -> str:
    """Kurze Ortsangabe (fuer Reports)."""
    bc = res.metadata.get("breadcrumb", "")
    if bc:
        return bc[:80]
    doc = res.metadata.get("document_name", "")
    if doc:
        return doc[:80]
    return res.collection


def aggregate(runs: list[SystemRun], system: str, k: int) -> dict:
    sys_runs = [r for r in runs if r.system == system]
    if not sys_runs:
        return {}
    return {
        "count": len(sys_runs),
        "ndcg@k": sum(r.ndcg_at_k(k) for r in sys_runs) / len(sys_runs),
        "relevance@10": sum(r.relevance_at_k(10) for r in sys_runs) / len(sys_runs),
        "relevance@3": sum(r.relevance_at_k(3) for r in sys_runs) / len(sys_runs),
        "top1_score": sum(r.top_1_score() for r in sys_runs) / len(sys_runs),
        "mean_score": sum(r.mean_score() for r in sys_runs) / len(sys_runs),
        "latency_sec": sum(r.latency_sec for r in sys_runs) / len(sys_runs),
    }


def print_cli_report(query_cases: list[QueryCase],
                      runs_by_query: dict[str, dict[str, SystemRun]],
                      top_k: int):
    """Kompakter CLI-Report mit Tabelle."""
    print()
    print("═" * 78)
    print(f"  BENCHMARK REPORT  ({len(query_cases)} Queries, Top-{top_k})")
    print("═" * 78)

    for case in query_cases:
        qruns = runs_by_query.get(case.id, {})
        print(f"\n[{case.id} / {case.category}]  {case.query}")
        for sys_name, run in qruns.items():
            ndcg = run.ndcg_at_k(top_k)
            rel10 = run.relevance_at_k(10) * 100
            rel3 = run.relevance_at_k(3) * 100
            t1 = run.top_1_score()
            print(f"  {sys_name:8s}  nDCG={ndcg:.2f}  Rel@10={rel10:4.0f}%  "
                  f"Rel@3={rel3:4.0f}%  Top1={t1}  Latenz={run.latency_sec:.1f}s")

    # Aggregat
    all_runs = [r for qr in runs_by_query.values() for r in qr.values()]
    systems = sorted({r.system for r in all_runs})

    print()
    print("─" * 78)
    print("  GESAMT-DURCHSCHNITT")
    print("─" * 78)
    print(f"  {'Metrik':<14} | " + " | ".join(f"{s:<10}" for s in systems))
    print(f"  {'-'*14} | " + " | ".join(f"{'-'*10}" for _ in systems))

    aggs = {s: aggregate(all_runs, s, top_k) for s in systems}

    for label, key, fmt in [
        ("nDCG@10",      "ndcg@k",       "{:.3f}"),
        ("Relevance@10", "relevance@10", "{:.1%}"),
        ("Relevance@3",  "relevance@3",  "{:.1%}"),
        ("Top-1-Score",  "top1_score",   "{:.2f}"),
        ("Mean-Score",   "mean_score",   "{:.2f}"),
        ("Latenz (s)",   "latency_sec",  "{:.2f}"),
    ]:
        row = f"  {label:<14} | "
        row += " | ".join(f"{fmt.format(aggs[s].get(key, 0)):<10}" for s in systems)
        print(row)
    print()


def write_markdown_report(path: Path, query_cases: list[QueryCase],
                           runs_by_query: dict, top_k: int):
    all_runs = [r for qr in runs_by_query.values() for r in qr.values()]
    systems = sorted({r.system for r in all_runs})
    aggs = {s: aggregate(all_runs, s, top_k) for s in systems}

    lines: list[str] = []
    lines.append(f"# RAG Benchmark Report\n")
    lines.append(f"_Generiert: {datetime.now().isoformat(timespec='seconds')}_\n")
    lines.append(f"\n- Queries: **{len(query_cases)}**")
    lines.append(f"- Top-K: **{top_k}**")
    lines.append(f"- Systeme: {', '.join(systems)}\n")

    lines.append("## Gesamtvergleich\n")
    lines.append("| Metrik | " + " | ".join(systems) + " |")
    lines.append("|--------|" + "|".join("--------" for _ in systems) + "|")
    for label, key, fmt in [
        ("nDCG@10",      "ndcg@k",       "{:.3f}"),
        ("Relevance@10", "relevance@10", "{:.1%}"),
        ("Relevance@3",  "relevance@3",  "{:.1%}"),
        ("Top-1-Score",  "top1_score",   "{:.2f}"),
        ("Mean-Score",   "mean_score",   "{:.2f}"),
        ("Latenz (s)",   "latency_sec",  "{:.2f}"),
    ]:
        vals = " | ".join(fmt.format(aggs[s].get(key, 0)) for s in systems)
        lines.append(f"| {label} | {vals} |")

    # Per-Category aggregation
    lines.append("\n## Nach Kategorie\n")
    cats = sorted({c.category for c in query_cases})
    for cat in cats:
        cat_ids = {c.id for c in query_cases if c.category == cat}
        cat_runs = [r for qr_id, qr in runs_by_query.items() if qr_id in cat_ids
                    for r in qr.values()]
        lines.append(f"\n### {cat}\n")
        lines.append("| Metrik | " + " | ".join(systems) + " |")
        lines.append("|--------|" + "|".join("--------" for _ in systems) + "|")
        for label, key, fmt in [
            ("nDCG@10",      "ndcg@k",       "{:.3f}"),
            ("Relevance@10", "relevance@10", "{:.1%}"),
            ("Relevance@3",  "relevance@3",  "{:.1%}"),
        ]:
            row_vals = []
            for s in systems:
                sys_cat_runs = [r for r in cat_runs if r.system == s]
                if not sys_cat_runs:
                    row_vals.append("-")
                    continue
                if key == "ndcg@k":
                    v = sum(r.ndcg_at_k(top_k) for r in sys_cat_runs) / len(sys_cat_runs)
                elif key == "relevance@10":
                    v = sum(r.relevance_at_k(10) for r in sys_cat_runs) / len(sys_cat_runs)
                elif key == "relevance@3":
                    v = sum(r.relevance_at_k(3) for r in sys_cat_runs) / len(sys_cat_runs)
                row_vals.append(fmt.format(v))
            lines.append(f"| {label} | " + " | ".join(row_vals) + " |")

    # Per-Query Detail
    lines.append("\n## Detail pro Query\n")
    for case in query_cases:
        qruns = runs_by_query.get(case.id, {})
        lines.append(f"\n### {case.id} — {case.category}\n")
        lines.append(f"**Query:** {case.query}\n")
        lines.append(f"**Kontext:** {case.context}\n")

        lines.append("| System | nDCG | Rel@10 | Rel@3 | Top-1 | Latenz |")
        lines.append("|--------|------|--------|-------|-------|--------|")
        for sys_name, run in qruns.items():
            lines.append(
                f"| {sys_name} | {run.ndcg_at_k(top_k):.2f} | "
                f"{run.relevance_at_k(10):.0%} | {run.relevance_at_k(3):.0%} | "
                f"{run.top_1_score()} | {run.latency_sec:.1f}s |"
            )

        # Top-3 Chunks pro System
        for sys_name, run in qruns.items():
            lines.append(f"\n#### {sys_name} — Top 3")
            for c in run.chunks[:3]:
                loc = c.metadata.get("breadcrumb") or c.metadata.get("document_name", "?")
                txt = strip_breadcrumb(c.text)[:200].replace("\n", " ")
                lines.append(f"- **[Judge={c.judge_score}]** `{loc[:60]}` — {c.judge_reason}")
                lines.append(f"  > {txt}...")

    path.write_text("\n".join(lines), encoding="utf-8")


def write_json_dump(path: Path, runs_by_query: dict):
    """Rohdaten aller Runs fuer spaetere Analyse."""
    dump = {}
    for qid, sys_runs in runs_by_query.items():
        dump[qid] = {
            sys_name: {
                "latency_sec": run.latency_sec,
                "chunks": [
                    {
                        "rank": c.rank,
                        "score": c.score,
                        "judge_score": c.judge_score,
                        "judge_reason": c.judge_reason,
                        "text_preview": strip_breadcrumb(c.text)[:300],
                        "metadata": {k: v for k, v in c.metadata.items()
                                     if k in ("breadcrumb", "paragraph", "gesetz",
                                              "randnummer", "document_name")},
                    }
                    for c in run.chunks
                ],
            }
            for sys_name, run in sys_runs.items()
        }
    path.write_text(json.dumps(dump, indent=2, ensure_ascii=False), encoding="utf-8")


# ---------------------------------------------------------------------------
# Main benchmark loop
# ---------------------------------------------------------------------------

def run_benchmark(query_file: str, top_k: int, systems: list[str],
                  output_dir: str, skip_judge: bool):
    # Load queries
    with open(query_file) as f:
        doc = yaml.safe_load(f)
    query_cases = [QueryCase(**q) for q in doc["queries"]]
    print(f"▶ Geladen: {len(query_cases)} Queries aus {query_file}")

    # Init retrievers
    retrievers = {}
    if "ours" in systems:
        print("▶ Lade unser Retrieval-System ...")
        retrievers["ours"] = JuristischerRetriever()
    if "ragie" in systems:
        print("▶ Lade RAGIE-Client ...")
        retrievers["ragie"] = RagieRetriever(partition="strafrecht", rerank=True)
    if "openai" in systems:
        print("▶ Lade OpenAI Vector Store Client ...")
        retrievers["openai"] = OpenAIRetriever(rewrite_query=False)
    if "gemini" in systems:
        print("▶ Lade Gemini File Search Client ...")
        retrievers["gemini"] = GeminiRetriever()
    if "vectara" in systems:
        print("▶ Lade Vectara Client ...")
        retrievers["vectara"] = VectaraRetriever()
    if "ours-cohere" in systems:
        print("▶ Lade Ours-Cohere Client ...")
        retrievers["ours-cohere"] = OursCohereRetriever()
    if "ours-mxbai" in systems:
        print("▶ Lade Ours-Mxbai-DE Client ...")
        retrievers["ours-mxbai"] = OursMxbaiRetriever()
    if "ours-mxbai-voyage" in systems:
        print("▶ Lade Ours-Mxbai + Voyage-Rerank Client ...")
        retrievers["ours-mxbai-voyage"] = OursMxbaiVoyageRetriever()
    if "ours-api" in systems:
        print("▶ Lade Ours-API Client (mxbai-API + Voyage-Rerank) ...")
        retrievers["ours-api"] = OursApiRetriever()

    judge = None
    if not skip_judge:
        print("▶ Initialisiere LLM-Judge (Claude) ...")
        judge = LLMJudge()

    # Run retrievals (sequentially per query, parallel across systems)
    runs_by_query: dict[str, dict[str, SystemRun]] = {}

    print(f"\n▶ Starte Benchmark: {len(systems)} Systeme × {len(query_cases)} Queries\n")

    for case in tqdm(query_cases, desc="Queries"):
        qruns: dict[str, SystemRun] = {}

        # Parallel retrieval across systems
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(systems)) as ex:
            futures = {}
            if "ours" in systems:
                futures["ours"] = ex.submit(run_our_rag, retrievers["ours"],
                                             case.query, top_k)
            if "ragie" in systems:
                futures["ragie"] = ex.submit(run_ragie, retrievers["ragie"],
                                              case.query, top_k)
            if "openai" in systems:
                futures["openai"] = ex.submit(run_openai, retrievers["openai"],
                                               case.query, top_k)
            if "vectara" in systems:
                futures["vectara"] = ex.submit(run_vectara, retrievers["vectara"],
                                                case.query, top_k)
            if "ours-cohere" in systems:
                futures["ours-cohere"] = ex.submit(
                    run_ours_cohere, retrievers["ours-cohere"], case.query, top_k)
            if "ours-mxbai" in systems:
                futures["ours-mxbai"] = ex.submit(
                    run_ours_mxbai, retrievers["ours-mxbai"], case.query, top_k)
            if "ours-mxbai-voyage" in systems:
                futures["ours-mxbai-voyage"] = ex.submit(
                    run_ours_mxbai_voyage, retrievers["ours-mxbai-voyage"],
                    case.query, top_k)
            if "ours-api" in systems:
                futures["ours-api"] = ex.submit(
                    run_ours_api, retrievers["ours-api"], case.query, top_k)
            if "gemini" in systems:
                futures["gemini"] = ex.submit(run_gemini, retrievers["gemini"],
                                               case.query, top_k)

            for sys_name, fut in futures.items():
                try:
                    results, latency = fut.result()
                except Exception as e:
                    log.error(f"{sys_name} fehlgeschlagen fuer {case.id}: {e}")
                    results, latency = [], 0.0

                qruns[sys_name] = SystemRun(
                    system=sys_name,
                    query_id=case.id,
                    latency_sec=latency,
                    chunks=[
                        JudgedChunk(
                            rank=i + 1,
                            text=r.text,
                            score=r.score,
                            judge_score=0,   # wird unten gesetzt
                            judge_reason="",
                            metadata=r.metadata,
                        )
                        for i, r in enumerate(results)
                    ],
                )

        # LLM-Judge — pro Chunk (parallelisiert pro Query)
        if judge is not None:
            all_chunks = [(sys_name, c)
                          for sys_name, run in qruns.items()
                          for c in run.chunks]

            def judge_one(item):
                sys_name, c = item
                s, r = judge.judge(case.query, case.context,
                                    strip_breadcrumb(c.text))
                c.judge_score = s
                c.judge_reason = r
                return None

            with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
                list(ex.map(judge_one, all_chunks))

        runs_by_query[case.id] = qruns

    # Reports
    print_cli_report(query_cases, runs_by_query, top_k)

    if output_dir:
        outdir = Path(output_dir)
        outdir.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        md_path = outdir / f"benchmark_report_{stamp}.md"
        json_path = outdir / f"benchmark_results_{stamp}.json"
        write_markdown_report(md_path, query_cases, runs_by_query, top_k)
        write_json_dump(json_path, runs_by_query)
        print(f"✔ Report geschrieben:\n  {md_path}\n  {json_path}\n")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="RAG-Benchmark (unser Qdrant-RAG vs. RAGIE)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--queries", default="eval_queries.yaml",
                        help="YAML mit Test-Queries (default: eval_queries.yaml)")
    parser.add_argument("--top-k", type=int, default=DEFAULT_TOP_K,
                        help=f"Chunks pro System (default: {DEFAULT_TOP_K})")
    parser.add_argument("--systems",
                        default="ours,ragie,openai,gemini,vectara,ours-cohere,ours-mxbai,ours-mxbai-voyage,ours-api",
                        help="Komma-Liste verschiedener Retrieval-Systeme")
    parser.add_argument("--output", default="./benchmark_results",
                        help="Output-Verzeichnis fuer Reports")
    parser.add_argument("--skip-judge", action="store_true",
                        help="Ohne LLM-Scoring (nur Latenz/Retrieval)")
    parser.add_argument("--env-file", default=".env.local")
    args = parser.parse_args()

    load_dotenv(args.env_file, override=True)
    systems = [s.strip() for s in args.systems.split(",") if s.strip()]
    if not systems:
        print("Keine Systeme angegeben.")
        sys.exit(1)

    run_benchmark(
        query_file=args.queries,
        top_k=args.top_k,
        systems=systems,
        output_dir=args.output,
        skip_judge=args.skip_judge,
    )


if __name__ == "__main__":
    main()
