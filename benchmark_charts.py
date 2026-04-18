#!/usr/bin/env python3
"""
Benchmark-Chart-Generator
=========================
Liest die neueste benchmark_results_*.json und erstellt Visualisierungen:

  1. overview.png       — Gesamt-Metriken (Balken-Vergleich)
  2. per_category.png   — Aufschluesselung nach Kategorie
  3. per_query.png      — nDCG pro Query, horizontale Balken
  4. latency.png        — Latenz-Boxplot je System

Usage:
    python benchmark_charts.py                          # letzten Run nutzen
    python benchmark_charts.py --input FILE             # bestimmte JSON
    python benchmark_charts.py --eval eval_queries.yaml # Kategorien aus YAML
"""

import argparse
import glob
import json
import math
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # headless
import matplotlib.pyplot as plt
import numpy as np
import yaml


# ---------------------------------------------------------------------------
# Farben & Style
# ---------------------------------------------------------------------------

COLORS = {
    "ours":    "#4c72b0",  # kraeftiges Blau
    "ragie":   "#dd8452",  # warmes Orange
    "openai":  "#55a868",  # gedaempftes Gruen
    "gemini":  "#c44e52",  # Gemini-Rot
    "vectara": "#8172b2",  # Vectara-Violett
}

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.titlesize": 12,
    "axes.titleweight": "bold",
    "figure.facecolor": "white",
    "axes.grid": True,
    "grid.alpha": 0.25,
    "axes.axisbelow": True,
})


# ---------------------------------------------------------------------------
# Metrik-Berechnung (identisch zu benchmark.py)
# ---------------------------------------------------------------------------

def ndcg(rels: list[int], k: int = 10) -> float:
    rels = rels[:k]
    if not rels:
        return 0.0
    dcg = sum(r / math.log2(i + 2) for i, r in enumerate(rels))
    ideal = sorted(rels, reverse=True)
    idcg = sum(r / math.log2(i + 2) for i, r in enumerate(ideal))
    return dcg / idcg if idcg > 0 else 0.0


def relevance_at_k(rels: list[int], k: int, threshold: int = 2) -> float:
    top = rels[:k]
    if not top:
        return 0.0
    return sum(1 for r in top if r >= threshold) / len(top)


def compute_metrics(chunks: list[dict]) -> dict:
    rels = [c["judge_score"] for c in chunks]
    return {
        "ndcg@10":      ndcg(rels, 10),
        "relevance@10": relevance_at_k(rels, 10),
        "relevance@3":  relevance_at_k(rels, 3),
        "top1":         rels[0] if rels else 0,
        "mean":         sum(rels) / len(rels) if rels else 0,
    }


# ---------------------------------------------------------------------------
# Datenladen
# ---------------------------------------------------------------------------

def load_benchmark(json_path: Path) -> dict:
    with open(json_path) as f:
        return json.load(f)


def load_categories(yaml_path: Path) -> dict[str, str]:
    """Gibt {query_id: category} zurueck."""
    with open(yaml_path) as f:
        doc = yaml.safe_load(f)
    return {q["id"]: q.get("category", "other") for q in doc["queries"]}


def load_queries(yaml_path: Path) -> dict[str, str]:
    """Gibt {query_id: query_text} zurueck."""
    with open(yaml_path) as f:
        doc = yaml.safe_load(f)
    return {q["id"]: q["query"] for q in doc["queries"]}


# ---------------------------------------------------------------------------
# Charts
# ---------------------------------------------------------------------------

def chart_overview(bench: dict, out_path: Path):
    """Balken-Vergleich der Gesamt-Metriken."""
    systems = sorted({sys for q in bench.values() for sys in q.keys()})

    # Aggregate: mean of metrics over all queries
    agg = {s: {"ndcg@10": [], "relevance@10": [], "relevance@3": [],
               "top1": [], "mean": []} for s in systems}
    for qid, sys_runs in bench.items():
        for s, run in sys_runs.items():
            m = compute_metrics(run["chunks"])
            for k, v in m.items():
                agg[s][k].append(v)

    metrics = ["ndcg@10", "relevance@10", "relevance@3", "top1", "mean"]
    labels = ["nDCG@10", "Relevance@10", "Relevance@3", "Top-1-Score", "Mean-Score"]

    fig, (ax_bars, ax_lat) = plt.subplots(1, 2, figsize=(13, 5.5),
                                           gridspec_kw={"width_ratios": [3, 1]})

    x = np.arange(len(metrics))
    width = 0.36

    for i, s in enumerate(systems):
        vals = [np.mean(agg[s][m]) for m in metrics]
        # Normalise top1 and mean to 0-1 range for comparable bars
        vals_norm = [v if m not in ("top1", "mean") else v / 3.0
                     for v, m in zip(vals, metrics)]
        offset = (i - (len(systems) - 1) / 2) * width
        bars = ax_bars.bar(x + offset, vals_norm, width,
                           label=s, color=COLORS.get(s, "#888"),
                           edgecolor="white", linewidth=1.5)
        # Labels above bars
        for bar, v, m in zip(bars, vals, metrics):
            if m in ("top1", "mean"):
                text = f"{v:.2f}"
            elif m.startswith("relevance"):
                text = f"{v:.0%}"
            else:
                text = f"{v:.3f}"
            ax_bars.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.015,
                         text, ha="center", va="bottom", fontsize=9, fontweight="bold")

    ax_bars.set_xticks(x)
    ax_bars.set_xticklabels(labels)
    ax_bars.set_ylabel("Wert (Top-1/Mean normiert auf 0-1)")
    ax_bars.set_title("Gesamt-Qualitaet")
    ax_bars.set_ylim(0, 1.15)
    ax_bars.legend(loc="upper right", frameon=True, facecolor="white")
    ax_bars.spines["top"].set_visible(False)
    ax_bars.spines["right"].set_visible(False)

    # Latency bars (right subplot)
    lat_means = []
    for s in systems:
        lats = [run["latency_sec"] for run in (sr[s] for sr in bench.values() if s in sr)]
        lat_means.append(np.mean(lats))

    bars = ax_lat.bar(systems, lat_means,
                      color=[COLORS.get(s, "#888") for s in systems],
                      edgecolor="white", linewidth=1.5, width=0.55)
    for bar, v in zip(bars, lat_means):
        ax_lat.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1,
                    f"{v:.2f}s", ha="center", va="bottom",
                    fontsize=10, fontweight="bold")

    ax_lat.set_ylabel("Latenz (Sekunden)")
    ax_lat.set_title("Durchschnittliche Latenz")
    ax_lat.spines["top"].set_visible(False)
    ax_lat.spines["right"].set_visible(False)
    ax_lat.set_ylim(0, max(lat_means) * 1.25)

    fig.suptitle(f"RAG Benchmark — {len(bench)} Queries",
                 fontsize=14, fontweight="bold", y=1.0)
    plt.tight_layout()
    plt.savefig(out_path, dpi=140, bbox_inches="tight")
    plt.close()
    print(f"  ✓ {out_path}")


def chart_per_category(bench: dict, categories: dict, out_path: Path):
    """nDCG@10 aufgeschluesselt nach Kategorie."""
    systems = sorted({sys for q in bench.values() for sys in q.keys()})
    cats = sorted(set(categories.values()))

    # {system: {cat: [ndcg values]}}
    data = {s: {c: [] for c in cats} for s in systems}
    for qid, sys_runs in bench.items():
        cat = categories.get(qid, "other")
        for s, run in sys_runs.items():
            rels = [c["judge_score"] for c in run["chunks"]]
            data[s][cat].append(ndcg(rels, 10))

    # Pretty category labels
    label_map = {
        "exakte-paragraphen": "Exakte §-Fragen",
        "konzept":            "Konzept",
        "alltagssprache":     "Alltagssprache",
        "stpo-prozess":       "StPO-Prozess",
        "cross-reference":    "Cross-Reference",
    }
    cat_labels = [label_map.get(c, c) for c in cats]

    fig, ax = plt.subplots(figsize=(11, 5.5))
    x = np.arange(len(cats))
    width = 0.36

    for i, s in enumerate(systems):
        vals = [np.mean(data[s][c]) if data[s][c] else 0 for c in cats]
        offset = (i - (len(systems) - 1) / 2) * width
        bars = ax.bar(x + offset, vals, width,
                      label=s, color=COLORS.get(s, "#888"),
                      edgecolor="white", linewidth=1.5)
        for bar, v in zip(bars, vals):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.01,
                    f"{v:.2f}", ha="center", va="bottom",
                    fontsize=9, fontweight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels(cat_labels)
    ax.set_ylabel("nDCG@10")
    ax.set_title("Qualitaet nach Frage-Kategorie (nDCG@10)")
    ax.set_ylim(0, 1.1)
    ax.legend(loc="lower right", frameon=True, facecolor="white")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    plt.savefig(out_path, dpi=140, bbox_inches="tight")
    plt.close()
    print(f"  ✓ {out_path}")


def chart_per_query(bench: dict, queries: dict, categories: dict, out_path: Path):
    """Horizontal stacked bars: nDCG@10 pro Query, nach Kategorie gruppiert."""
    systems = sorted({sys for q in bench.values() for sys in q.keys()})

    # Sort queries by category, then by id
    qids = sorted(bench.keys(),
                  key=lambda q: (categories.get(q, "z"), q))

    # Compute ndcg per query per system
    per_query = {}
    for qid in qids:
        per_query[qid] = {}
        for s in systems:
            if s in bench[qid]:
                rels = [c["judge_score"] for c in bench[qid][s]["chunks"]]
                per_query[qid][s] = ndcg(rels, 10)
            else:
                per_query[qid][s] = 0

    # Generous sizing so labels and bars are readable
    fig, ax = plt.subplots(figsize=(14, max(8, len(qids) * 0.55)))

    y = np.arange(len(qids))
    height = 0.38

    for i, s in enumerate(systems):
        vals = [per_query[q][s] for q in qids]
        offset = (i - (len(systems) - 1) / 2) * height
        bars = ax.barh(y + offset, vals, height,
                       label=s, color=COLORS.get(s, "#888"),
                       edgecolor="white", linewidth=1.2)
        # Label values at the end of each bar
        for bar, v in zip(bars, vals):
            ax.text(bar.get_width() + 0.008, bar.get_y() + bar.get_height() / 2,
                    f"{v:.2f}", va="center", ha="left",
                    fontsize=8.5, fontweight="bold",
                    color=COLORS.get(s, "#444"))

    # Truncate query strings
    def trunc(q_text: str, n: int = 70) -> str:
        if len(q_text) <= n:
            return q_text
        return q_text[:n - 1] + "…"

    yticklabels = []
    for qid in qids:
        cat = categories.get(qid, "")
        cat_short = cat.replace("exakte-paragraphen", "§").replace("alltagssprache", "alltag") \
                       .replace("cross-reference", "xref").replace("stpo-prozess", "stpo") \
                       .replace("konzept", "konz")
        qtext = trunc(queries.get(qid, qid))
        yticklabels.append(f"{qid} [{cat_short}]  {qtext}")

    ax.set_yticks(y)
    ax.set_yticklabels(yticklabels, fontsize=10)
    ax.invert_yaxis()
    ax.set_xlabel("nDCG@10", fontsize=11)
    ax.set_xlim(0, 1.15)
    ax.set_title("Qualitaet pro Einzel-Query (nDCG@10)", fontsize=13, pad=12)
    ax.legend(loc="lower right", frameon=True, facecolor="white", fontsize=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Light zebra shading per-row
    for i in range(len(qids)):
        if i % 2 == 0:
            ax.axhspan(i - 0.5, i + 0.5, color="#f4f4f4", zorder=0)

    # Reference line at 1.0
    ax.axvline(1.0, color="black", linewidth=0.7, linestyle=":", alpha=0.5)

    plt.tight_layout()
    plt.savefig(out_path, dpi=140, bbox_inches="tight")
    plt.close()
    print(f"  ✓ {out_path}")


def chart_latency_distribution(bench: dict, out_path: Path):
    """Latenz-Verteilung pro System (Box + Scatter)."""
    systems = sorted({sys for q in bench.values() for sys in q.keys()})

    data = []
    for s in systems:
        lats = [run["latency_sec"] for run in (sr[s] for sr in bench.values() if s in sr)]
        data.append(lats)

    fig, ax = plt.subplots(figsize=(8, 5))
    box = ax.boxplot(data, tick_labels=systems, patch_artist=True,
                     widths=0.5, showfliers=False)
    for patch, s in zip(box["boxes"], systems):
        patch.set_facecolor(COLORS.get(s, "#888"))
        patch.set_alpha(0.55)
    for median in box["medians"]:
        median.set_color("black")
        median.set_linewidth(2)

    # Scatter individual points
    rng = np.random.default_rng(42)
    for i, (s, lats) in enumerate(zip(systems, data)):
        xs = rng.normal(i + 1, 0.05, size=len(lats))
        ax.scatter(xs, lats, alpha=0.7, s=35,
                   color=COLORS.get(s, "#888"),
                   edgecolor="white", linewidth=0.8, zorder=3)

    ax.set_ylabel("Latenz pro Query (Sekunden)")
    ax.set_title("Latenz-Verteilung je System")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    plt.savefig(out_path, dpi=140, bbox_inches="tight")
    plt.close()
    print(f"  ✓ {out_path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Benchmark-Visualisierungen")
    parser.add_argument("--input", help="Pfad zu benchmark_results_*.json (default: neueste)")
    parser.add_argument("--eval", default="eval_queries.yaml",
                        help="YAML mit Query-Kategorien")
    parser.add_argument("--output-dir", default="benchmark_results",
                        help="Zielverzeichnis fuer PNGs")
    args = parser.parse_args()

    # Find latest JSON if not specified
    if args.input:
        json_path = Path(args.input)
    else:
        candidates = sorted(glob.glob(f"{args.output_dir}/benchmark_results_*.json"))
        if not candidates:
            print("Keine benchmark_results_*.json gefunden.")
            sys.exit(1)
        json_path = Path(candidates[-1])
    print(f"▶ Input: {json_path}")

    bench = load_benchmark(json_path)
    categories = load_categories(Path(args.eval))
    queries = load_queries(Path(args.eval))

    outdir = Path(args.output_dir)
    outdir.mkdir(parents=True, exist_ok=True)

    # Match naming to the source JSON timestamp
    stamp = json_path.stem.replace("benchmark_results_", "")

    print("▶ Generiere Charts:")
    chart_overview(bench, outdir / f"overview_{stamp}.png")
    chart_per_category(bench, categories,
                        outdir / f"per_category_{stamp}.png")
    chart_per_query(bench, queries, categories,
                     outdir / f"per_query_{stamp}.png")
    chart_latency_distribution(bench, outdir / f"latency_{stamp}.png")

    # Also save latest/ copies without timestamp for stable README links
    import shutil
    for name in ["overview", "per_category", "per_query", "latency"]:
        src = outdir / f"{name}_{stamp}.png"
        dst = outdir / f"{name}_latest.png"
        shutil.copy(src, dst)
    print(f"\n✔ Stabile Kopien als *_latest.png gespeichert.\n")


if __name__ == "__main__":
    main()
