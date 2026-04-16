# Juristisches RAG-System fuer Strafrecht

Retrieval-Augmented Generation fuer **deutsche Strafrechtsliteratur** und **Ermittlungsakten**.

Verwandelt Alltagsfragen in praezise juristische Recherche — durchsucht Fischer StGB-Kommentar,
Schmitt/Koehler StPO-Kommentar und Ermittlungsakten mit einer dreistufigen Pipeline:

```
Nutzerfrage
  "Hat der Angeklagte die Kunden ueber das Internet betrogen?"

    |  Query Expansion (Claude)
    v
  "Internetbetrug, Taeuschung ueber Tatsachen mittels digitaler
   Kommunikation, Vermoegensverfuegung, § 263 Abs. 1 StGB"

    |  Hybrid Search (Dense + BM25)
    v
  40 Kandidaten aus Kommentaren + Ermittlungsakten

    |  Cross-Encoder Reranking (Cohere)
    v
  Top 5 Treffer, nach juristischer Relevanz sortiert
```

---

## Features

- **Paragraph-aware Chunking** — erkennt §§, Randnummern und Gliederungsebenen in
  Kommentarliteratur; Breadcrumb-Kontext in jedem Chunk (`[§ 263 StGB – B. Obj. Tatbestand – Rn. 78]`)
- **Dokumenttyp-Klassifikation** — ordnet Ermittlungsakten automatisch zu
  (Anklageschrift, Vermerk, Zeugenaussage, Beschluss, ...)
- **Gewichtete Hybrid-Suche** — Dense Embeddings (`multilingual-e5-large`) + BM25 Sparse Vectors
  mit quellenabhaengiger Gewichtung (Kommentare: BM25 staerker / Akten: Dense staerker)
- **Query Expansion** — Claude reformuliert Alltagssprache in juristische Fachterminologie
  und extrahiert automatisch relevante §§ als Metadata-Filter
- **Cross-Encoder Reranking** — Cohere `rerank-v3.5` (oder lokaler Fallback mit
  `BAAI/bge-reranker-v2-m3`) sortiert Kandidaten nach inhaltlicher Relevanz
- **Getrennte Collections** — `fachliteratur` (persistente Kommentare) und
  `ermittlungsakten` (fallbezogen), einzeln oder kombiniert durchsuchbar
- **Metadata-Filter** — `--paragraph`, `--gesetz`, `--fall`, `--aktenzeichen`, `--dokument-typ`
- **Interaktiver Modus** — REPL mit Live-Filtern, Toggle fuer Expansion/Reranking
- **Benchmark-Suite** — vergleicht Retrieval-Qualitaet mit anderen RAG-Systemen per
  LLM-as-Judge (Claude), inkl. automatischer Chart-Generierung

---

## Benchmark: Unser RAG vs. RAGIE vs. OpenAI

Der Benchmark vergleicht die Retrieval-Qualitaet unseres Systems gegen zwei externe RAG-Dienste
auf **18 juristischen Test-Queries** aus 5 Kategorien (exakte §-Fragen, Konzepte, Alltagssprache,
StPO-Prozessrecht, Cross-Reference). Alle drei Systeme werden mit **identischen Fachliteratur-Daten**
(Fischer StGB + Schmitt/Koehler StPO) befuellt, die Relevanz jedes Top-10 Chunks bewertet
**Claude** auf einer Skala 0-3.

| System | Technologie |
|---|---|
| **ours** | Qdrant + E5-Large + BM25 + Claude-Expansion + Cohere-Reranking |
| **ragie** | Managed RAG Service (hybrid + integriertes Reranking) |
| **openai** | OpenAI Vector Stores API (Dense-only) |

### Gesamtergebnis

![Benchmark Overview](benchmark_results/overview_latest.png)

**Unser RAG liegt bei Qualitaet klar vorne** — nDCG@10 von **0,975** (RAGIE 0,945, OpenAI 0,718),
und bei **Relevance@3** sind **96 %** der Top-3-Treffer tatsaechlich relevant (RAGIE 87 %, OpenAI 48 %).
OpenAI ist mit **1,7 s** zwar am schnellsten, zeigt aber deutlich schlechtere Qualitaet —
bei deutschsprachigen Fachtexten reicht reines Dense-Retrieval ohne BM25 und ohne Query-Expansion
nicht aus.

### Nach Kategorie

![Benchmark per Category](benchmark_results/per_category_latest.png)

| Kategorie | ours | ragie | openai | Gewinner |
|---|---|---|---|---|
| Exakte §-Fragen (z.B. "§ 112 StPO Haftgruende") | **0.99** | 0.92 | 0.89 | ours |
| Konzept ("Vermoegensverfuegung") | **0.99** | 0.98 | 0.44 | ours |
| Alltagssprache ("Wann darf die Polizei suchen?") | **0.98** | 0.95 | 0.54 | ours |
| Cross-Reference ("Betrug vs. Computerbetrug") | **0.96** | 0.92 | 0.85 | ours |
| StPO-Prozess | 0.94 | 0.95 | **0.97** | openai (knapp) |

**Staerken:**
- **ours** durch Query Expansion + Hybrid Search bei allen Frage-Typen robust
- **ragie** gleichmaessig gut, kein echter Schwachpunkt
- **openai** bei klaren juristischen Fragen (StPO-Prozess) okay

**Schwaechen:**
- **openai** bricht bei **Alltagssprache und Konzept-Fragen** dramatisch ein
  (z.B. q06 "Vermoegensverfuegung" → OpenAI liefert Chunks ueber Schuldunfaehigkeit
  und Sexualstraftaten). Ursache: **OpenAI Vector Stores sind Dense-only**,
  ohne BM25 versagt die Suche bei praeziser juristischer Terminologie.
- **ours** ist am langsamsten (~6 s) wegen Query-Expansion + Reranking-Overhead.

### Pro Einzel-Query

![Benchmark per Query](benchmark_results/per_query_latest.png)

Bei 4 Queries (q06, q07, q10, q12) hat OpenAI **nDCG = 0** — keine einzige der 10 zurueckgegebenen
Chunks wurde vom Judge als relevant bewertet. Unsere Pipeline hat bei allen 18 Queries mindestens
einen relevanten Treffer geliefert.

### Latenz-Verteilung

![Benchmark Latency](benchmark_results/latency_latest.png)

| System | Median | Range |
|---|---|---|
| ours | ~6 s | 4,8 – 11,6 s |
| ragie | ~2 s | 1,7 – 3,7 s |
| openai | ~1,7 s | 1,4 – 2,4 s |

Hauptkostenfaktor unserer Pipeline: **Query Expansion** (~3 s Claude-Call). Ohne Expansion
waere die Pipeline bei ~3 s und damit vergleichbar mit RAGIE.

### Kosten-Einschaetzung

| System | Kosten pro Query (ca.) | Kommentar |
|---|---|---|
| **ours** | ~0,005 $ | Claude-Expansion (~0,003) + Cohere-Rerank (~0,002); Qdrant Cloud extra |
| **ragie** | ~0,01 $ | Je nach Plan, Retrieval + Rerank im Paket |
| **openai** | ~0,003 $ | Vector Store Search günstig, aber schlechtere Qualitaet |

### Benchmark selber laufen lassen

```bash
python benchmark.py                                     # alle drei Systeme
python benchmark.py --systems ours,ragie                # nur 2 Systeme
python benchmark.py --systems ours --skip-judge         # nur Latenz messen
python benchmark_charts.py                              # Charts aus letztem Run erzeugen
```

Reports landen in `benchmark_results/`:
- `benchmark_report_TIMESTAMP.md` — ausfuehrlicher Markdown-Report
- `benchmark_results_TIMESTAMP.json` — Rohdaten (alle Chunks + Judge-Begruendungen)
- `overview_TIMESTAMP.png`, `per_category_*.png`, `per_query_*.png`, `latency_*.png` — Charts

Queries in `eval_queries.yaml` anpassen. Kosten-Schaetzung:
~**0,30 – 0,50 €** an Claude-API pro vollem Benchmark-Lauf (540 Judge-Calls bei 3 Systemen × 18 Queries × 10 Chunks).

---

## Architektur

```
data/
  fachliteratur/         Kommentare (Markdown)
    Strafrecht/
      StGB_Kommentar/      Fischer/Anstoetz/Lutz, 73. Aufl. 2026
      StPO_Kommentar/      Schmitt/Koehler, 68. Aufl. 2025
  ermittlungsakten/      Akten pro Fall (Markdown)
    Probenheld-MD/
      Probenheld (107 Js 1148_21)/
      Nuvigra/
      BEVIGRA/
      ...

import_tool.py           Chunking + Embedding + Upload nach Qdrant
retrieve.py              Query Expansion + Hybrid Search + Reranking
```

### Datenfluss Import

```
Markdown-Dateien
  |
  |-- Fachliteratur-Chunker ---- §-aware, Randnummer-Erkennung
  |                               512-768 Tokens, Breadcrumb-Prefix
  |
  |-- Ermittlungsakten-Chunker - Dokumenttyp-basiert
  |                               1024-1536 Tokens, Aktenzeichen/Blatt
  v
Dense Embedding (E5-large, passage: Prefix)
  +
Sparse Vector (TF, Qdrant-seitiges IDF)
  |
  v
Qdrant Cloud
  |-- Collection: fachliteratur     (~14.000 Chunks)
  |-- Collection: ermittlungsakten  (~11.000 Chunks)
       jeweils mit Keyword- + Fulltext-Indexes
```

### Datenfluss Retrieval

```
Nutzerfrage
  |
  v
[Query Expansion]     Claude Sonnet → juristische Praezisionsquery
  |                    + automatische §/Gesetz-Erkennung
  v
[Embedding]           E5-large (query: Prefix) + Sparse Vector
  |
  v
[Hybrid Search]       Dense + BM25 pro Collection
  |                    Gewichtete RRF-Fusion (k=60)
  |                    Fachliteratur:  45% Dense / 55% BM25
  |                    Akten:          65% Dense / 35% BM25
  v
[Reranking]           Cohere rerank-v3.5 (oder lokaler Cross-Encoder)
  |                    Top 40 → Top K
  v
Ergebnisse mit Score, Breadcrumb, Metadata
```

---

## Installation

```bash
git clone <repo-url>
cd RAG_LW

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Konfiguration

API-Keys in `.env.local` eintragen:

```env
# Pflicht
QDRANT_ENDPOINT=https://...cloud.qdrant.io:6333
QDRANT_API_KEY=...

# Fuer Query Expansion
ANTHROPIC_API_KEY=sk-ant-...

# Fuer Reranking (Production Key empfohlen)
COHERE_API_KEY=...

# Nur fuer Benchmark (optional)
RAGIE_API_KEY=...
OPENAI_API_KEY=sk-...
OPENAI_VECTOR_STORE_ID=vs_...
```

> Ohne `ANTHROPIC_API_KEY` laeuft das System ohne Query Expansion.
> Ohne `COHERE_API_KEY` wird automatisch ein lokaler Cross-Encoder verwendet.
> Ohne `RAGIE_API_KEY` / `OPENAI_API_KEY` werden diese Systeme im Benchmark uebersprungen.

---

## Nutzung

### 1. Daten importieren

```bash
# Alles importieren (Fachliteratur + Ermittlungsakten)
python import_tool.py --all --recreate

# Nur Fachliteratur
python import_tool.py --fachliteratur --recreate

# Nur Ermittlungsakten
python import_tool.py --ermittlungsakten --recreate

# Chunking-Statistiken ohne Upload
python import_tool.py --all --dry-run
```

Der Import laeuft lokal auf der CPU (Embedding mit `multilingual-e5-large`).
Dauer: ca. 15-30 Minuten fuer ~25.000 Chunks auf einem Apple Silicon Mac.

### 2. Suchen

**Einzelabfrage:**

```bash
# Volle Pipeline (Expansion + Reranking)
python retrieve.py "Hat der Angeklagte die Kunden betrogen?"

# Mit Query-Expansion-Anzeige
python retrieve.py --show-expansion "Wann ist U-Haft zulaessig?"

# Mit Filtern
python retrieve.py --paragraph "§ 263" --gesetz StGB "Taeuschungshandlung"
python retrieve.py --collection ermittlungsakten --fall Probenheld "Bestellbetrug"
python retrieve.py --typ Anklageschrift "Tatvorwurf"

# Ohne Expansion / Reranking
python retrieve.py --no-expand "§ 112 StPO Haftgruende Fluchtgefahr"
python retrieve.py --no-rerank "Vermoegensverfuegung"
```

**Interaktiver Modus:**

```bash
python retrieve.py --interactive
```

```
> Wann darf die Polizei eine Wohnung durchsuchen?
> /filter §=102 gesetz=StPO
> Durchsuchungsvoraussetzungen
> /coll akten
> /filter fall=Probenheld
> Bestellbetrug Kunden
> /reset
> /expand          (toggle Query Expansion an/aus)
> /rerank          (toggle Reranking an/aus)
> /verbose         (toggle ausfuehrliche Textanzeige)
> /quit
```

### 3. Als Python-Modul

```python
from retrieve import JuristischerRetriever

r = JuristischerRetriever()

# Volle Pipeline
results, expansion = r.search("Hat er die Kunden betrogen?")

# Nur Kommentare, ohne Expansion
results, _ = r.search_fachliteratur(
    "Taeuschungshandlung",
    paragraph="§ 263",
    expand=False,
)

# Nur Akten
results, _ = r.search_ermittlungsakten(
    "Bestellbetrug",
    fall="Probenheld",
)

for res in results:
    print(res.score, res.breadcrumb, res.short_text(200))
```

---

## CLI-Referenz

### import_tool.py

| Flag | Beschreibung |
|---|---|
| `--all` | Fachliteratur + Ermittlungsakten importieren |
| `--fachliteratur` | Nur Kommentare importieren |
| `--ermittlungsakten` | Nur Akten importieren |
| `--recreate` | Collections loeschen und neu aufbauen |
| `--dry-run` | Nur Chunking-Statistiken, kein Upload |
| `--data-dir DIR` | Datenverzeichnis (default: `./data`) |
| `--env-file FILE` | Env-Datei (default: `.env.local`) |

### retrieve.py

| Flag | Beschreibung |
|---|---|
| `-i`, `--interactive` | Interaktiver REPL-Modus |
| `-c`, `--collection` | `fachliteratur`, `ermittlungsakten` oder `all` |
| `-k`, `--top-k N` | Anzahl Ergebnisse (default: 10) |
| `-p`, `--paragraph` | Filter auf § (z.B. `"§ 263"` oder `"263"`) |
| `-g`, `--gesetz` | Filter auf Gesetz (`StGB` / `StPO`) |
| `-f`, `--fall` | Filter auf Fallname |
| `--az` | Filter auf Aktenzeichen |
| `--typ` | Filter auf Dokumenttyp |
| `--no-expand` | Query Expansion deaktivieren |
| `--no-rerank` | Reranking deaktivieren |
| `--show-expansion` | Expandierte Query anzeigen |
| `-v`, `--verbose` | Ausfuehrlichere Textanzeige |

---

## Technische Details

### Chunking-Strategie

| | Fachliteratur | Ermittlungsakten |
|---|---|---|
| **Methode** | §-aware, Randnummer-Erkennung | Dokumenttyp-basiert |
| **Chunk-Groesse** | 512-768 Tokens (~1.800-2.700 Zeichen) | 1.024-1.536 Tokens (~3.600-5.400 Zeichen) |
| **Kontext** | Breadcrumb-Prefix mit §, Abschnitt, Rn. | Fall, Aktenzeichen, Dokumenttyp |
| **Splitting** | An Randnummer-Grenzen, Satzgrenzen | An Heading-Grenzen, Absatzgrenzen |
| **Metadata** | Gesetz, §, Rn., Seite, Bearbeiter | Fall, Az., Dokumenttyp, Blatt |

### Embedding & Vektoren

| Komponente | Technologie | Details |
|---|---|---|
| Dense Embedding | `intfloat/multilingual-e5-large` | 1024 Dimensionen, Cosine Distance |
| Sparse Vector | TF-basiert (Token-Hashing) | Qdrant-seitiges IDF (Modifier.IDF) |
| E5 Prefix | `passage:` beim Import, `query:` beim Retrieval | Instruction-Tuned Embeddings |

### Hybrid-Gewichtung (RRF-Fusion)

| Quelle | Dense | BM25 | Begruendung |
|---|---|---|---|
| Fachliteratur | 45% | 55% | Exakte §-Matches und Fachbegriffe entscheidend |
| Ermittlungsakten | 65% | 35% | Variable Alltagssprache, semantische Naehe wichtiger |
| Gemischt | 55% | 45% | Ausgewogener Default |

### Pipeline-Latenzen (typisch)

| Stufe | Technologie | Latenz |
|---|---|---|
| Query Expansion | Claude Sonnet | ~3s |
| Embedding | E5-large (lokal, MPS) | <1s |
| Hybrid Search | Qdrant Cloud | ~1s |
| Reranking | Cohere rerank-v3.5 | ~1s |
| **Gesamt** | | **~5s** |

---

## Datenquellen

### Fachliteratur

| Kommentar | Autoren | Auflage | Chunks |
|---|---|---|---|
| StGB (Beck'sche Kurz-Kommentare Bd. 10) | Fischer / Anstoetz / Lutz | 73. Aufl. 2026 | ~7.200 |
| StPO (Beck'sche Kurz-Kommentare Bd. 6) | Schmitt / Koehler | 68. Aufl. 2025 | ~6.700 |

### Ermittlungsakten

560 Markdown-Dateien aus mehreren Verfahrenskomplexen, automatisch klassifiziert in:

| Dokumenttyp | Anzahl Chunks |
|---|---|
| Abrechnungen | ~3.100 |
| Schreiben | ~1.900 |
| Vermerke | ~1.100 |
| Zeugenaussagen | ~900 |
| Anklageschriften | ~180 |
| Protokolle, Beschluesse, Gutachten, ... | ~200 |
| Sonstiges | ~4.000 |

---

## Projektstruktur

```
RAG_LW/
  .env.local              API-Keys (Qdrant, Anthropic, Cohere, Ragie)
  requirements.txt        Python-Abhaengigkeiten
  import_tool.py          Import-Pipeline (Chunking → Embedding → Qdrant)
  retrieve.py             Retrieval-Pipeline (Expansion → Search → Reranking)
  benchmark.py            Benchmark-Runner (unser RAG vs. RAGIE vs. OpenAI)
  benchmark_charts.py     Chart-Generator (matplotlib)
  ragie_client.py         RAGIE-Adapter (gleiche API wie retrieve.py)
  openai_client.py        OpenAI Vector Store Adapter
  eval_queries.yaml       Benchmark-Test-Queries (18 Queries, 5 Kategorien)
  data/
    fachliteratur/        Kommentar-Markdown-Dateien
      Strafrecht/
        StGB_Kommentar/
        StPO_Kommentar/
    ermittlungsakten/     Akten-Markdown-Dateien
      Probenheld-MD/
        ...
  benchmark_results/      Benchmark-Reports, JSON-Dumps, PNG-Charts
```

---

## Abhaengigkeiten

| Paket | Zweck |
|---|---|
| `qdrant-client` | Vektor-Datenbank (Cloud) |
| `sentence-transformers` | Dense Embeddings + lokaler Cross-Encoder |
| `anthropic` | Query Expansion via Claude API |
| `cohere` | Cross-Encoder Reranking via API |
| `python-dotenv` | Env-Variablen |
| `tqdm` | Fortschrittsanzeige |
| `ragie` | RAGIE Python SDK (nur fuer Benchmark) |
| `openai` | OpenAI Vector Stores API (nur fuer Benchmark) |
| `pyyaml` | YAML-Parser fuer Test-Queries |
| `matplotlib` | Chart-Generator fuer Benchmark-Reports |

---

## Erweiterungsmoeglichkeiten

- **Weitere Kommentare** — Neue Markdown-Dateien in `data/fachliteratur/` ablegen und
  `python import_tool.py --fachliteratur --recreate` ausfuehren
- **Neue Faelle** — Akten in `data/ermittlungsakten/` ablegen und
  `python import_tool.py --ermittlungsakten --recreate` ausfuehren
- **RAG-Agent** — `retrieve.py` als Modul in einen Claude-Agent einbinden,
  der Retrieval-Ergebnisse zu vollstaendigen juristischen Analysen verarbeitet
- **Domain-Finetuning** — Synthetische Query-Passage-Paare aus den Kommentaren
  generieren und das Embedding-Modell feintunen
- **Cohere Production** — Mit Production-Key wird automatisch `rerank-v3.5`
  statt des lokalen Cross-Encoders verwendet
