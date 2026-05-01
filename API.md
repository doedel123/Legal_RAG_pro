# Legalwinner RAG API

HTTP-API für semantische Suche in deutscher juristischer Fachliteratur.
Eine POST-Anfrage mit einer natürlichsprachigen Frage liefert relevante
Textpassagen aus Kommentaren und Sachbüchern zurück — mit strukturierten
Metadaten (Paragraph, Randnummer, Buch, Kapitel …).

**Basis-URL:** `https://api.legalwinner.de`

---

## Inhaltsverzeichnis

- [Auth](#auth)
- [Datenbestand](#datenbestand)
- [Retrieval-Pipeline](#retrieval-pipeline)
- [Chunking](#chunking)
- [Endpoints](#endpoints)
  - [GET /health](#get-health)
  - [POST /search](#post-search)
  - [GET /openai/tool_schema](#get-openaitool_schema)
- [Response-Schema](#response-schema)
- [Integration](#integration)
- [Caveats](#caveats)

---

## Auth

Alle Endpoints außer `/health` verlangen den Header `X-API-Key`.

```bash
curl -H "X-API-Key: $LW_API_KEY" https://api.legalwinner.de/...
```

Fehlt oder stimmt der Key nicht: `401 Unauthorized` mit
`{"detail": "Ungueltiger oder fehlender X-API-Key"}`.

Den Key bekommst du vom Admin (in Railway unter Environment Variables,
Key `API_KEY`).

---

## Datenbestand

**50 058 Chunks** aus **11 Quellen** über **6 Rechtsgebiete**.

| Domain-Key | Chunks | Quellen |
|---|---:|---|
| `strafrecht` | 13 779 | Fischer StGB, Schmitt/Köhler StPO |
| `arbeitsrecht` | 9 584 | Erfurter Kommentar |
| `mietrecht` | 9 212 | Mietrecht-Kommentar (Beck), *Mietrecht für Mieter 2026* (Ratgeber), *Nebenkostenabrechnung für Vermieter* (Ratgeber) |
| `verkehrsrecht` | 7 625 | Straßenverkehrsrecht-Kommentar (Beck), *Fehlerquellen polizeiliche Messverfahren* 11. + 13. Auflage (Ratgeber) |
| `ao` | 6 393 | Abgabenordnung-Kommentar (Beck) |
| `owigrecht` | 3 465 | OWiG-Kommentar (Beck) |

Zwei Quellen-Typen (`source_type` im Response):
- **`fachliteratur`** — klassische Kommentare mit Randnummern-Struktur
- **`ratgeber`** — Sachbücher / Anwendungshandbücher ohne §/Randnummer

---

## Retrieval-Pipeline

```
Frage (natürliche Sprache)
   │
   ▼
[1] Query Expansion (Anthropic Claude)
   │   reformuliert in juristische Fachterminologie,
   │   extrahiert ggf. § / Gesetz als Filter-Hints
   ▼
[2] Encoding
   │   Dense:  mxbai-embed-de-large-v1 (1024-dim, über Mixedbread API)
   │           Prompt: "Represent this sentence for searching relevant passages: <query>"
   │   Sparse: BM25-artiger TF-Vektor, IDF server-seitig in Qdrant
   ▼
[3] Hybrid Search (Qdrant Cloud)
   │   Dense-Kandidaten  ──┐
   │                       ├─► Reciprocal Rank Fusion (gewichtet)
   │   BM25-Kandidaten  ───┘   ~40 Kandidaten
   │   Storage: Vektoren on-disk + INT8 Scalar Quantization always_ram,
   │            Rescoring mit Volltext-Vektoren (~0% Recall-Verlust)
   │   Optional: Pre-Filter auf `domain` (Keyword-Index)
   ▼
[4] Reranking (Voyage rerank-2.5)
   │   Cross-Encoder, sortiert die 40 Kandidaten neu
   ▼
Top-K Chunks (default 5, max 20)
```

**Typische Gesamtlatenz:** 3–5 Sekunden (dominiert von Query Expansion
+ Reranking, nicht vom Qdrant-Lookup).

---

## Chunking

Zwei verschiedene Chunker, je nach Quellen-Typ — siehe
[import_tool.py](import_tool.py) für die Implementierung.

### FachliteraturChunker (Kommentare)

- Target-Größe: **~2,7 KB** pro Chunk (~768 Tokens)
- Erkennt `§ N`, Randnummern, Gliederungsebenen (A./B./I./II.)
- Paragraph-aware: neuer § → flush, neuer Chunk
- Jeder Chunk bekommt einen **Breadcrumb-Prefix** im Text:
  ```
  [§ 263 StGB – B. Objektiver Tatbestand – Rn. 78]
  ```
  Dieser Prefix dient als Kontext-Anker für das Reranking und ist auch
  im Response-Feld `breadcrumb` separat enthalten.

### RatgeberChunker (Sachbücher)

- Target-Größe: **~4,9 KB** pro Chunk (~1400 Tokens, größer wegen
  narrativer Struktur)
- Splittet an `##` / `###` Headings
- Breadcrumb: `Buch > Kapitel > Abschnitt > Heading`
- Kleine Sektionen werden in den Vorgänger-Chunk gemerged

### Deterministische IDs

Jeder Chunk bekommt eine `point_id = uuid5(NAMESPACE_URL, text)`.
Das macht Re-Imports idempotent: bei identischem Text-Inhalt wird der
bestehende Chunk überschrieben, nicht dupliziert.

---

## Endpoints

### GET /health

Ungesichert. Gibt den Zustand des Retrievers zurück.

```json
{"status": "ok", "retriever_ready": true}
```

`retriever_ready: false` bedeutet Cold-Start läuft noch (max. ~10 s nach
Container-Restart).

### POST /search

Haupt-Endpoint. Nimmt eine Frage, gibt relevante Chunks zurück.

**Request-Body:**

| Feld | Typ | Default | Beschreibung |
|---|---|---|---|
| `query` | string | *required* | Juristische Fragestellung in natürlicher Sprache |
| `top_k` | int (1–20) | `5` | Anzahl zurückgegebener Chunks |
| `domain` | string \| null | `null` | Fachgebiet-Filter. Einer von `strafrecht`, `arbeitsrecht`, `mietrecht`, `ao`, `owigrecht`, `verkehrsrecht`. `null` = cross-domain über alle 6 Gebiete. |

**Fehler-Cases:**
- `400 Bad Request` — unbekannter `domain`-Wert (Antwort listet die erlaubten)
- `401 Unauthorized` — Auth-Fehler
- `500 Internal Server Error` — Retrieval-Pipeline hat versagt (siehe Railway-Logs)
- `503 Service Unavailable` — Retriever noch nicht initialisiert (Cold-Start)

**Beispiel:**

```bash
curl -X POST https://api.legalwinner.de/search \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $LW_API_KEY" \
  -d '{
    "query": "Kuendigung wegen Eigenbedarfs",
    "top_k": 3,
    "domain": "mietrecht"
  }'
```

### GET /openai/tool_schema

Liefert eine fertige OpenAI-Function-Calling-Tool-Definition für
`search_fachliteratur` — inkl. aller Parameter und `domain`-Enum.
Kann direkt in OpenAI / Claude / Gemini Tool-Use-Requests übernommen werden.

```bash
curl -H "X-API-Key: $LW_API_KEY" \
  https://api.legalwinner.de/openai/tool_schema
```

---

## Response-Schema

`POST /search` liefert:

```json
{
  "query": "...",
  "count": 3,
  "results": [ Chunk, ... ]
}
```

Jeder `Chunk` hat folgende Felder. Welche gefüllt sind, hängt vom
`source_type` ab.

| Feld | Typ | Immer | Für Kommentar | Für Ratgeber | Beschreibung |
|---|---|---|---|---|---|
| `text` | string | ✓ | | | Volltext des Chunks, mit Breadcrumb-Prefix in eckigen Klammern |
| `score` | float | ✓ | | | Rerank-Score (höher = relevanter). Nicht normalisiert, nur intra-query vergleichbar. |
| `breadcrumb` | string | ✓ | | | Kurze Quellen-Angabe, für UI/Fußnoten |
| `domain` | string | ✓ | | | Rechtsgebiet des Treffers |
| `source_type` | string | ✓ | | | `"fachliteratur"` oder `"ratgeber"` |
| `source_file` | string | ✓ | | | Quelldatei, nur zu Debug-Zwecken |
| `paragraph` | string | | ✓ | (leer) | `"§ 263"` o.ä. |
| `gesetz` | string | | ✓ | (leer) | `"StGB"`, `"BGB/Miet"`, `"StVG/StVO"` … |
| `kommentar` | string | | ✓ | (leer) | Kommentar-Langtitel, z.B. `"Fischer StGB"` |
| `randnummer` | int \| null | | ✓ | `null` | Randnummer falls erkannt |
| `buch` | string | | (leer) | ✓ | Buchtitel, z.B. `"Fehlerquelle polizeiliche Messverfahren 11. Auflage"` |
| `kapitel` | string | | (leer) | (meist ✓) | Oberkapitel, z.B. `"Teil 2 Fehlerquellen bei ..."` |
| `abschnitt` | string | | (leer) | (ggf.) | Zweite Gliederungsebene, kann leer sein bei flachen Büchern |
| `heading` | string | | (leer) | ✓ | Konkrete Abschnittsüberschrift |

### Beispiel-Response (Ratgeber-Treffer)

```json
{
  "text": "[Fehlerquelle polizeiliche Messverfahren 11. Auflage > Teil 2 ...] ...",
  "score": 0.824,
  "breadcrumb": "Fehlerquelle polizeiliche Messverfahren 11. Auflage > Teil 2 Fehlerquellen bei Geschwindigkeits- und Abstandsmessungen > b) Messfehler durch horizontales Schwenken des Laserstrahls",
  "domain": "verkehrsrecht",
  "source_type": "ratgeber",
  "paragraph": "",
  "gesetz": "",
  "kommentar": "",
  "randnummer": null,
  "buch": "Fehlerquelle polizeiliche Messverfahren 11. Auflage",
  "kapitel": "Teil 2 Fehlerquellen bei Geschwindigkeits- und Abstandsmessungen sowie Rotlichtverstößen, Wägungen und Atemalkoholmessungen",
  "abschnitt": "",
  "heading": "b) Messfehler durch unbewusstes oder bewusstes horizontales Schwenken des Laserstrahls an parallel oder teilweise parallel zur Fahrtrichtung ausgerichteten Bauteilen eines Fahrzeugs",
  "source_file": "data/fachliteratur/Verkehrsrecht/..."
}
```

### Beispiel-Response (Kommentar-Treffer)

```json
{
  "text": "[§ 263 StGB – B. Objektiver Tatbestand – Rn. 78] ...",
  "score": 0.912,
  "breadcrumb": "§ 263 StGB – B. Objektiver Tatbestand – Rn. 78",
  "domain": "strafrecht",
  "source_type": "fachliteratur",
  "paragraph": "§ 263",
  "gesetz": "StGB",
  "kommentar": "Fischer/Anstötz/Lutz StGB",
  "randnummer": 78,
  "buch": "",
  "kapitel": "",
  "abschnitt": "",
  "heading": "",
  "source_file": "data/fachliteratur/Strafrecht/StGB_Kommentar/StGB_Kommentar.md"
}
```

---

## Integration

### Python (requests)

```python
import os, requests

API = "https://api.legalwinner.de"
HEADERS = {"X-API-Key": os.environ["LW_API_KEY"]}

def search(query: str, top_k: int = 5, domain: str | None = None):
    r = requests.post(
        f"{API}/search",
        headers=HEADERS,
        json={"query": query, "top_k": top_k, "domain": domain},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()["results"]

hits = search("Untersuchungshaft bei Fluchtgefahr", domain="strafrecht")
for h in hits:
    print(f"[{h['breadcrumb']}]  score={h['score']:.2f}")
    print(h["text"][:300])
```

### OpenAI / Claude Function Calling

```python
import requests, os

schema = requests.get(
    "https://api.legalwinner.de/openai/tool_schema",
    headers={"X-API-Key": os.environ["LW_API_KEY"]},
).json()

# Dann schema direkt in deine Anthropic/OpenAI Tool-Liste einhängen.
# Der LLM entscheidet selbst, ob/wann er search_fachliteratur aufruft,
# und mit welchen Argumenten (query, top_k, domain).
```

Der Tool-Name ist `search_fachliteratur`. Wenn der LLM den Tool-Call
auslöst, musst du ihn auf deiner Seite gegen `POST /search` auflösen.

### Format-Empfehlung für RAG-Prompts

Wenn du die Chunks in einen Antwort-Prompt einfügst, nutze den
`breadcrumb` als Quellen-Marker und erlaube dem LLM, diesen zu zitieren:

```
Du bist ein juristischer Assistent. Nutze ausschliesslich die folgenden
Quellen und zitiere sie im Format [Quelle: <breadcrumb>].

QUELLEN:
---
[Quelle: § 573 BGB/Miet – C. Die Kuendigungstatbestaende – Rn. 102]
<chunk.text>
---
[Quelle: Mietrecht fuer Mieter 2026 > Kapitel 3 > ...]
<chunk.text>
---

FRAGE: <user query>
```

---

## Caveats

- **Query-Qualität:** Die Query-Expansion via Claude funktioniert am
  besten, wenn die Frage fachlich verankert ist. Bei sehr vagen Fragen
  („was ist mit Mietrecht?") streuen die Treffer stärker. Lieber gezielt
  fragen oder `domain` setzen.
- **Cross-Domain vs Filter:** Die Semantik der Anfrage routet in der
  Regel automatisch ins richtige Fachgebiet. `domain` brauchst du nur
  dann, wenn derselbe Begriff in mehreren Gebieten vorkommt
  (z.B. "Kündigung" existiert in Miet- und Arbeitsrecht).
- **Ratgeber-Felder:** `kapitel` ist meist gefüllt, `abschnitt` nur bei
  Büchern mit zweistufiger Gliederung. Für eine saubere Quellen-Anzeige
  ist `breadcrumb` die robusteste Option.
- **Kein Akten-Retrieval:** Diese API liefert nur Fachliteratur.
  Mandatsakten werden separat an den LLM-Kontext gegeben
  (bis ca. 500 k Tokens direkt, darüber eigenes Retrieval).
- **Latenz:** 3–5 s sind normal, gelegentlich 8 s+ bei Cold-Start
  Anthropic/Voyage. Setze Client-Timeouts auf ≥ 30 s.
- **Rate-Limits:** Aktuell keine harten Limits im API-Server selbst;
  upstream begrenzt Anthropic (Query Expansion) und Voyage (Rerank)
  die Durchsatzrate. Bei Lastspitzen ggf. clientseitig batchen.
- **Versionierung:** Die API hat derzeit keine explizite
  `/v1/`-Version. Breaking Changes werden in `CHANGELOG.md` angekündigt.

---

## Code-Referenzen

| Zweck | Datei |
|---|---|
| FastAPI-Server | [server.py](server.py) |
| Retriever + Hybrid-Suche + Reranking | [retrieve.py](retrieve.py) |
| Mixedbread-API-Embedder | [ours_mxbai_api_client.py](ours_mxbai_api_client.py) |
| Voyage-Reranker | [voyage_reranker.py](voyage_reranker.py) |
| Chunker + Qdrant-Setup | [import_tool.py](import_tool.py) |
| Fachliteratur-Import (Dispatcher) | [import_fachliteratur_mxbai.py](import_fachliteratur_mxbai.py) |
| Dockerfile / Railway | [Dockerfile](Dockerfile), [railway.json](railway.json) |
