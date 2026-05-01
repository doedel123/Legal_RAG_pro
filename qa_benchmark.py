#!/usr/bin/env python3
"""
Agentic QA-Benchmark: ours-mxbai vs PageIndex
==============================================
Vergleicht beide Systeme im natuerlichen Modus (finale Antwortqualitaet):

  ours-mxbai:  Hybrid-Retrieval Top-K → gpt-4o generiert Antwort
  pageindex:   openai-agents-SDK Agent mit Tree-Tools (iterative Tool-Calls)

Judge:        Claude Sonnet, pairwise blind mit Position-Swap gegen
              Ground-Truth aus eval_queries_akten.yaml.

Usage:
    python qa_benchmark.py
    python qa_benchmark.py --top-k 10 --queries eval_queries_akten.yaml
    python qa_benchmark.py --limit 3            # nur erste 3 Queries (smoke)
"""

from __future__ import annotations

import argparse
import asyncio
import concurrent.futures
import json
import logging
import os
import re
import sys
import time
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path

import yaml
from dotenv import load_dotenv
from tqdm import tqdm

import litellm
from agents import Agent, Runner, function_tool, set_tracing_disabled

# Projekt-Imports
sys.path.insert(0, str(Path(__file__).parent / "PageIndex"))
from pageindex import PageIndexClient  # noqa: E402
sys.path.pop(0)

from ours_mxbai_client import OursMxbaiRetriever  # noqa: E402
from pageindex_cloud_client import PageIndexCloudClient  # noqa: E402

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

GENERATOR_MODEL = "gpt-4o-2024-11-20"
JUDGE_MODEL = "claude-sonnet-4-20250514"
JUDGE_MAX_TOKENS = 400
PAGEINDEX_WORKSPACE = Path(__file__).parent / "PageIndex" / "qa_workspace"
DOC_ID_SELF = "donkredito"
DOC_ID_CLOUD = "pi-cmmyzwegr005l09pfofq73oe8"
AKTEN_COLLECTION = "ermittlungsakten_mxbai"
DEFAULT_TOP_K = 10

logging.basicConfig(level=logging.WARNING, format="%(asctime)s [%(levelname)s] %(message)s")
for noisy in ("httpx", "httpcore", "LiteLLM", "openai", "urllib3", "anthropic"):
    logging.getLogger(noisy).setLevel(logging.WARNING)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------

OURS_QA_SYSTEM = """\
Du bist ein juristischer Recherche-Assistent fuer Ermittlungsakten.
Beantworte die Anfrage kurz, praezise und ausschliesslich auf Basis der
angegebenen Auszuege aus der Akte. Wenn die Auszuege keine Antwort enthalten,
sage das klar. Nenne konkrete Namen, Daten und Aktenzeichen, wenn sie in den
Auszuegen stehen. Keine Ausschmueckung, keine Wiederholungen.
"""

PAGEINDEX_AGENT_SYSTEM = """\
Du bist ein Dokument-QA-Agent fuer eine deutsche Ermittlungsakte.
WERKZEUG-NUTZUNG:
- Rufe zuerst get_document() auf, um Status und Zeilenumfang zu pruefen.
- Dann get_document_structure(), um relevante Abschnitte / Zeilennummern zu finden.
- Rufe get_page_content(pages="...") mit engen Zeilenbereichen auf, niemals das ganze Dokument.
- Begruende jeden Tool-Call in einem kurzen Satz.
Beantworte die Frage kurz und praezise ausschliesslich auf Basis des
abgerufenen Inhalts. Nenne konkrete Namen, Daten und Aktenzeichen.
"""

JUDGE_SYSTEM = """\
Du bist ein unabhaengiger Juror, der zwei Antworten auf eine Frage zu einer
Ermittlungsakte vergleicht. Du kennst die Referenz-Antwort (Ground Truth).

Bewertungs-Kriterien (in dieser Reihenfolge):
  1. Korrektheit — stimmen die genannten Fakten mit der Ground Truth ueberein?
     Falsche Namen, Zahlen oder Paragraphen disqualifizieren stark.
  2. Vollstaendigkeit — sind die wesentlichen Punkte der Ground Truth abgedeckt?
  3. Spezifitaet — konkrete Namen/Daten/Werte statt vager Formulierungen?
  4. Kuerze — uebertriebene Laenge ohne Mehrwert ist ein Minuspunkt.

Antworte AUSSCHLIESSLICH mit einem JSON-Objekt ohne Markdown:
{"winner": "A"|"B"|"tie", "reason": "<max 25 Worte>"}
"""


def build_judge_user_prompt(query: str, ground_truth: str,
                            ans_a: str, ans_b: str) -> str:
    return (
        f"FRAGE:\n{query}\n\n"
        f"REFERENZ-ANTWORT (Ground Truth):\n{ground_truth.strip()}\n\n"
        f"ANTWORT A:\n{ans_a.strip()}\n\n"
        f"ANTWORT B:\n{ans_b.strip()}\n\n"
        "Welche Antwort ist besser? Reply JSON."
    )


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class QAQuery:
    id: str
    category: str
    query: str
    context: str
    ground_truth: str


@dataclass
class QAAnswer:
    system: str
    answer: str
    latency_sec: float
    tool_calls: int = 0


@dataclass
class JudgeVerdict:
    order: str              # "ours_first" | "pageindex_first"
    winner: str             # "ours-mxbai" | "pageindex" | "tie"
    reason: str


@dataclass
class QAResult:
    query_id: str
    ours: QAAnswer
    pageindex: QAAnswer
    verdicts: list[JudgeVerdict]


# ---------------------------------------------------------------------------
# ours-mxbai RAG-QA
# ---------------------------------------------------------------------------

def answer_ours_mxbai(retriever: OursMxbaiRetriever, query: str,
                      top_k: int) -> QAAnswer:
    t0 = time.time()
    hits = retriever.search(query, top_k=top_k)
    chunks_text = "\n\n---\n\n".join(
        f"[Quelle {i + 1}]\n{h.text.strip()}" for i, h in enumerate(hits)
    )
    user_msg = (
        f"QUELLEN AUS DER AKTE:\n{chunks_text}\n\n"
        f"FRAGE: {query}\n\n"
        "Kurze, praezise Antwort (max. 3 Saetze). Nenne konkrete Fakten aus "
        "den Quellen. Wenn die Quellen die Frage nicht beantworten, sage das."
    )
    resp = litellm.completion(
        model=GENERATOR_MODEL,
        messages=[
            {"role": "system", "content": OURS_QA_SYSTEM},
            {"role": "user", "content": user_msg},
        ],
        temperature=0,
    )
    answer = resp.choices[0].message.content or ""
    return QAAnswer(system="ours-mxbai", answer=answer.strip(),
                    latency_sec=time.time() - t0)


# ---------------------------------------------------------------------------
# PageIndex Agent-QA (via openai-agents SDK)
# ---------------------------------------------------------------------------

def build_pageindex_agent(client: PageIndexClient, doc_id: str) -> Agent:
    """Baut einen Agent mit den drei PageIndex-Tools, gebunden an doc_id."""

    @function_tool
    def get_document() -> str:
        """Liefert Metadaten zum Dokument (Name, Beschreibung, line_count)."""
        return client.get_document(doc_id)

    @function_tool
    def get_document_structure() -> str:
        """Liefert die Baumstruktur (Titel + Summaries) ohne Volltexte."""
        return client.get_document_structure(doc_id)

    @function_tool
    def get_page_content(pages: str) -> str:
        """Liefert den Rohtext fuer Zeilen-/Seitenbereiche wie '5-7' oder '3,8'."""
        return client.get_page_content(doc_id, pages)

    return Agent(
        name="PageIndexAgent",
        instructions=PAGEINDEX_AGENT_SYSTEM,
        tools=[get_document, get_document_structure, get_page_content],
        model=GENERATOR_MODEL,
    )


def answer_pageindex_cloud(client: PageIndexCloudClient, doc_id: str,
                           query: str) -> QAAnswer:
    """Fragt PageIndex Cloud Chat API — 1 Call, Antwort+Retrieval server-seitig."""
    ans = client.chat(doc_id, query)
    return QAAnswer(
        system="pageindex",
        answer=ans.answer,
        latency_sec=ans.latency_sec,
        tool_calls=0,  # server-seitig, nicht sichtbar
    )


def answer_pageindex(client: PageIndexClient, doc_id: str,
                     query: str) -> QAAnswer:
    agent = build_pageindex_agent(client, doc_id)
    t0 = time.time()

    async def _run():
        result = await Runner.run(agent, query)
        return result

    # Runner.run wants a running loop; use a dedicated thread pool
    try:
        asyncio.get_running_loop()
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
            result = pool.submit(asyncio.run, _run()).result()
    except RuntimeError:
        result = asyncio.run(_run())

    answer = str(result.final_output or "")
    # Rough tool-call count — look at RunItem list if available
    tc = sum(1 for item in getattr(result, "new_items", [])
             if getattr(item, "type", "") == "tool_call_item")
    return QAAnswer(system="pageindex", answer=answer.strip(),
                    latency_sec=time.time() - t0, tool_calls=tc)


# ---------------------------------------------------------------------------
# Judge
# ---------------------------------------------------------------------------

class PairwiseJudge:
    def __init__(self):
        import anthropic
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY fehlt")
        self.client = anthropic.Anthropic(api_key=api_key)

    def judge_once(self, query: str, ground_truth: str,
                   ans_a: str, ans_b: str) -> tuple[str, str]:
        try:
            resp = self.client.messages.create(
                model=JUDGE_MODEL,
                max_tokens=JUDGE_MAX_TOKENS,
                system=JUDGE_SYSTEM,
                messages=[{
                    "role": "user",
                    "content": build_judge_user_prompt(query, ground_truth,
                                                      ans_a, ans_b),
                }],
            )
            text = resp.content[0].text.strip()
            if text.startswith("```"):
                text = re.sub(r"^```(?:json)?\s*", "", text)
                text = re.sub(r"\s*```$", "", text)
            data = json.loads(text)
            winner = str(data.get("winner", "tie")).strip()
            reason = str(data.get("reason", ""))[:250]
            if winner not in ("A", "B", "tie"):
                winner = "tie"
            return winner, reason
        except Exception as e:
            log.warning("Judge-Fehler: %s", e)
            return "tie", f"judge-error: {e}"

    def judge_with_swap(self, query: str, ground_truth: str,
                        ans_ours: str, ans_pi: str) -> list[JudgeVerdict]:
        # Durchgang 1: A = ours, B = pageindex
        w1, r1 = self.judge_once(query, ground_truth, ans_ours, ans_pi)
        winner_sys1 = {"A": "ours-mxbai", "B": "pageindex", "tie": "tie"}[w1]

        # Durchgang 2: A = pageindex, B = ours (Positionen geswappt)
        w2, r2 = self.judge_once(query, ground_truth, ans_pi, ans_ours)
        winner_sys2 = {"A": "pageindex", "B": "ours-mxbai", "tie": "tie"}[w2]

        return [
            JudgeVerdict(order="ours_first", winner=winner_sys1, reason=r1),
            JudgeVerdict(order="pageindex_first", winner=winner_sys2, reason=r2),
        ]


# ---------------------------------------------------------------------------
# Aggregate helpers
# ---------------------------------------------------------------------------

def aggregate(results: list[QAResult]) -> dict:
    """Doppelte Stimmen (swap) zaehlen; Konsens + Flip-Rate ausweisen."""
    total_votes = 0
    ours_votes = pi_votes = ties = 0
    consistent = 0
    ours_lat = []
    pi_lat = []
    pi_tool_calls = []
    for r in results:
        ours_lat.append(r.ours.latency_sec)
        pi_lat.append(r.pageindex.latency_sec)
        pi_tool_calls.append(r.pageindex.tool_calls)
        winners = [v.winner for v in r.verdicts]
        for w in winners:
            total_votes += 1
            if w == "ours-mxbai":
                ours_votes += 1
            elif w == "pageindex":
                pi_votes += 1
            else:
                ties += 1
        if len(set(winners)) == 1:
            consistent += 1
    n = len(results)

    def _avg(xs):
        return sum(xs) / len(xs) if xs else 0.0

    return {
        "queries": n,
        "total_votes": total_votes,
        "ours_win_rate": ours_votes / total_votes if total_votes else 0.0,
        "pageindex_win_rate": pi_votes / total_votes if total_votes else 0.0,
        "tie_rate": ties / total_votes if total_votes else 0.0,
        "consistent_across_swap": consistent,
        "consistency_rate": consistent / n if n else 0.0,
        "ours_mean_latency": _avg(ours_lat),
        "pageindex_mean_latency": _avg(pi_lat),
        "pageindex_mean_tool_calls": _avg(pi_tool_calls),
    }


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def print_cli_report(queries: list[QAQuery], results: list[QAResult],
                     agg: dict):
    print()
    print("═" * 78)
    print(f"  AGENTIC QA BENCHMARK  ({agg['queries']} Queries, pairwise + swap)")
    print("═" * 78)

    for q, r in zip(queries, results):
        verdict_str = " / ".join(
            f"{v.order[:8]}:{v.winner}" for v in r.verdicts
        )
        print(f"\n[{q.id} / {q.category}]  {q.query}")
        print(f"  ours-mxbai ({r.ours.latency_sec:.1f}s):  "
              f"{r.ours.answer[:160].replace(chr(10), ' ')}")
        print(f"  pageindex  ({r.pageindex.latency_sec:.1f}s, "
              f"{r.pageindex.tool_calls} tools):  "
              f"{r.pageindex.answer[:160].replace(chr(10), ' ')}")
        print(f"  verdict:   {verdict_str}")
        if r.verdicts:
            print(f"    reason[1]: {r.verdicts[0].reason}")
            print(f"    reason[2]: {r.verdicts[1].reason}")

    print()
    print("─" * 78)
    print("  GESAMT (24 Stimmen = 12 Queries × 2 Swap-Orderings)")
    print("─" * 78)
    print(f"  ours-mxbai gewinnt:        {agg['ours_win_rate']:.1%}")
    print(f"  pageindex  gewinnt:        {agg['pageindex_win_rate']:.1%}")
    print(f"  Unentschieden:             {agg['tie_rate']:.1%}")
    print(f"  Konsens ueber Swap:        "
          f"{agg['consistent_across_swap']}/{agg['queries']} "
          f"({agg['consistency_rate']:.0%})")
    print(f"  Latenz ours-mxbai:         {agg['ours_mean_latency']:.2f}s")
    print(f"  Latenz pageindex:          {agg['pageindex_mean_latency']:.2f}s")
    print(f"  Pageindex avg tool-calls:  {agg['pageindex_mean_tool_calls']:.1f}")
    print()


def write_reports(outdir: Path, queries: list[QAQuery],
                  results: list[QAResult], agg: dict):
    outdir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    # JSON
    json_path = outdir / f"qa_benchmark_{stamp}.json"
    payload = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "aggregate": agg,
        "queries": [
            {
                "id": q.id,
                "category": q.category,
                "query": q.query,
                "ground_truth": q.ground_truth,
                "ours": asdict(r.ours),
                "pageindex": asdict(r.pageindex),
                "verdicts": [asdict(v) for v in r.verdicts],
            }
            for q, r in zip(queries, results)
        ],
    }
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2),
                         encoding="utf-8")

    # Markdown
    md_lines = [
        f"# Agentic QA Benchmark — ours-mxbai vs PageIndex",
        f"_Generiert: {datetime.now().isoformat(timespec='seconds')}_\n",
        "## Gesamtergebnis\n",
        f"- Queries: **{agg['queries']}** × 2 Swap-Orderings = {agg['total_votes']} Stimmen",
        f"- **ours-mxbai** gewinnt: **{agg['ours_win_rate']:.1%}**",
        f"- **pageindex** gewinnt: **{agg['pageindex_win_rate']:.1%}**",
        f"- Unentschieden: {agg['tie_rate']:.1%}",
        f"- Konsens ueber Swap: {agg['consistent_across_swap']}/{agg['queries']} "
        f"({agg['consistency_rate']:.0%})",
        f"- Latenz: ours {agg['ours_mean_latency']:.1f}s vs "
        f"pageindex {agg['pageindex_mean_latency']:.1f}s "
        f"({agg['pageindex_mean_tool_calls']:.1f} Tool-Calls ⌀)",
        "",
        "## Pro Query\n",
    ]
    for q, r in zip(queries, results):
        md_lines.append(f"### {q.id} · {q.category}  \n**{q.query}**\n")
        md_lines.append(f"**Ground Truth:** {q.ground_truth.strip()}\n")
        md_lines.append(f"**ours-mxbai** ({r.ours.latency_sec:.1f}s):\n")
        md_lines.append(f"> {r.ours.answer}\n")
        md_lines.append(f"**pageindex** ({r.pageindex.latency_sec:.1f}s, "
                        f"{r.pageindex.tool_calls} tool-calls):\n")
        md_lines.append(f"> {r.pageindex.answer}\n")
        for v in r.verdicts:
            md_lines.append(f"- Judge [{v.order}]: **{v.winner}** — {v.reason}")
        md_lines.append("")
    md_path = outdir / f"qa_benchmark_{stamp}.md"
    md_path.write_text("\n".join(md_lines), encoding="utf-8")

    print(f"✔ Reports:\n  {md_path}\n  {json_path}\n")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--queries", default="eval_queries_akten.yaml")
    parser.add_argument("--top-k", type=int, default=DEFAULT_TOP_K)
    parser.add_argument("--output", default="./benchmark_results")
    parser.add_argument("--env-file", default=".env.local")
    parser.add_argument("--pageindex-mode", choices=["self", "cloud"],
                        default="cloud",
                        help="self = openai-agents + lokaler Tree; "
                             "cloud = hosted API via /chat/completions (default)")
    parser.add_argument("--limit", type=int, default=0,
                        help="Nur die ersten N Queries ausfuehren (0 = alle)")
    args = parser.parse_args()

    load_dotenv(args.env_file, override=True)
    set_tracing_disabled(True)

    with open(args.queries) as f:
        doc = yaml.safe_load(f)
    queries = [
        QAQuery(
            id=q["id"],
            category=q["category"],
            query=q["query"],
            context=q.get("context", ""),
            ground_truth=q.get("ground_truth", "").strip(),
        )
        for q in doc["queries"]
    ]
    if args.limit:
        queries = queries[:args.limit]
    missing_gt = [q.id for q in queries if not q.ground_truth]
    if missing_gt:
        print(f"⚠ Fehlende ground_truth fuer: {missing_gt}")
        sys.exit(2)
    print(f"▶ {len(queries)} Queries mit Ground-Truth geladen")

    print("▶ Initialisiere ours-mxbai Retriever ...")
    ours = OursMxbaiRetriever(collection=AKTEN_COLLECTION, env_file=args.env_file)

    if args.pageindex_mode == "cloud":
        print("▶ Initialisiere PageIndex Cloud Client ...")
        pi_cloud = PageIndexCloudClient()
        meta = pi_cloud.metadata(DOC_ID_CLOUD)
        if meta.get("status") != "completed":
            print(f"Doc '{DOC_ID_CLOUD}' nicht fertig indiziert: status={meta.get('status')}")
            sys.exit(2)
        print(f"   Doc: {meta.get('name')} ({meta.get('pageNum')} Seiten)")
        pi_self = None
    else:
        print("▶ Initialisiere self-hosted PageIndex Agent ...")
        pi_self = PageIndexClient(workspace=str(PAGEINDEX_WORKSPACE))
        pi_self.model = GENERATOR_MODEL
        pi_self.retrieve_model = GENERATOR_MODEL
        if DOC_ID_SELF not in pi_self.documents:
            print(f"Doc '{DOC_ID_SELF}' nicht in Workspace gefunden. "
                  "Run PageIndex/build_workspace.py zuerst.")
            sys.exit(2)
        pi_cloud = None

    print("▶ Initialisiere Judge ...")
    judge = PairwiseJudge()

    results: list[QAResult] = []
    for q in tqdm(queries, desc="QA"):
        try:
            ours_ans = answer_ours_mxbai(ours, q.query, top_k=args.top_k)
        except Exception as e:
            log.error("ours-mxbai fehlgeschlagen fuer %s: %s", q.id, e)
            ours_ans = QAAnswer(system="ours-mxbai",
                                answer=f"[ERROR: {e}]", latency_sec=0.0)
        try:
            if args.pageindex_mode == "cloud":
                pi_ans = answer_pageindex_cloud(pi_cloud, DOC_ID_CLOUD, q.query)
            else:
                pi_ans = answer_pageindex(pi_self, DOC_ID_SELF, q.query)
        except Exception as e:
            log.error("pageindex fehlgeschlagen fuer %s: %s", q.id, e)
            pi_ans = QAAnswer(system="pageindex",
                              answer=f"[ERROR: {e}]", latency_sec=0.0)
        verdicts = judge.judge_with_swap(
            q.query, q.ground_truth, ours_ans.answer, pi_ans.answer)
        results.append(QAResult(
            query_id=q.id,
            ours=ours_ans,
            pageindex=pi_ans,
            verdicts=verdicts,
        ))

    agg = aggregate(results)
    print_cli_report(queries, results, agg)
    write_reports(Path(args.output), queries, results, agg)


if __name__ == "__main__":
    main()
