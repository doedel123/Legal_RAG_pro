#!/usr/bin/env python3
"""
Juristisches Retrieval-Modul
============================
Vollstaendige RAG-Pipeline fuer juristische Texte:

  Nutzer-Query
    → [Query Expansion]   Claude reformuliert → praezise juristische Query
    → [Hybrid Search]     Dense + BM25, Top 40 Kandidaten
    → [Reranking]         Cohere Cross-Encoder, Top 40 → Top K
    → Ergebnisse

Features:
  - Query Expansion via Claude API (juristische Praezisionsquery)
  - Gewichtbare Hybrid-Suche (Dense vs. BM25 pro Source-Type)
  - Cross-Encoder Reranking via Cohere rerank-v3.5
  - Metadata-Filter (§, Gesetz, Fall, Dokumenttyp, …)
  - Multi-Collection-Suche

Nutzung als Modul:
    from retrieve import JuristischerRetriever
    r = JuristischerRetriever()
    results = r.search("Hat der Angeklagte die Kunden betrogen?")

Nutzung als CLI:
    python retrieve.py "Voraussetzungen Betrug § 263"
    python retrieve.py --no-expand --no-rerank "§ 263 Täuschung"
    python retrieve.py --show-expansion "Hat der betrogen?"
    python retrieve.py --interactive
"""

import os
import re
import sys
import json
import hashlib
import argparse
import logging
from dataclasses import dataclass, field
from collections import Counter
from typing import Optional

from dotenv import load_dotenv
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer

# Optional imports — graceful fallback if API keys missing
try:
    import anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False

try:
    import cohere
    HAS_COHERE = True
except ImportError:
    HAS_COHERE = False

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

DENSE_MODEL_NAME = "intfloat/multilingual-e5-large"

FACHLITERATUR_COLLECTION = "fachliteratur"
ERMITTLUNGSAKTEN_COLLECTION = "ermittlungsakten"

# Hybrid-Gewichtung: Anteil Dense vs. BM25
# Fuer Kommentare: BM25 staerker (exakte §-Matches, Fachbegriffe)
# Fuer Akten: Dense staerker (Alltagssprache, semantische Naehe)
WEIGHT_PROFILES = {
    "fachliteratur": {"dense": 0.45, "bm25": 0.55},
    "ermittlungsakten": {"dense": 0.65, "bm25": 0.35},
    "mixed": {"dense": 0.55, "bm25": 0.45},
}

DEFAULT_TOP_K = 10
PREFETCH_MULTIPLIER = 4  # prefetch N * top_k candidates per method
RERANK_CANDIDATES = 40   # how many candidates to send to reranker

# Query Expansion
EXPANSION_MODEL = "claude-sonnet-4-20250514"
EXPANSION_MAX_TOKENS = 400

# Reranking — local cross-encoder (Cohere API als opt-in Alternative)
LOCAL_RERANK_MODEL = "BAAI/bge-reranker-v2-m3"
COHERE_RERANK_MODEL = "rerank-v3.5"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# German stop words (same as import_tool.py)
# ---------------------------------------------------------------------------

GERMAN_STOP_WORDS = frozenset({
    "der", "die", "das", "ein", "eine", "einen", "einem", "einer", "eines",
    "und", "oder", "aber", "doch", "jedoch", "sondern", "weder", "noch",
    "in", "von", "zu", "mit", "auf", "für", "an", "bei", "aus", "nach",
    "über", "unter", "vor", "hinter", "neben", "zwischen", "durch",
    "ist", "sind", "war", "waren", "wird", "werden", "wurde", "wurden",
    "hat", "haben", "hatte", "hatten", "sein", "seine", "seinen", "seinem",
    "seiner",
    "nicht", "kein", "keine", "keinen", "keinem", "keiner",
    "dem", "den", "des", "sich", "es", "er", "sie", "wir", "ihr",
    "auch", "als", "wie", "so", "nur", "wenn", "dass", "da", "ob", "weil",
    "diese", "dieser", "dieses", "diesem", "diesen",
    "kann", "können", "soll", "sollen", "muss", "müssen", "will", "wollen",
    "darf", "dürfen",
    "zum", "zur", "im", "vom", "am", "um", "bis",
    "mehr", "schon", "noch", "sehr", "hier", "dort",
    "alle", "aller", "allem", "allen", "alles",
    "andere", "anderer", "anderem", "anderen", "anderes",
    "man", "mich", "mir", "dich", "dir", "uns", "euch", "ihnen",
    "was", "wer", "wen", "wem", "wessen",
    "dann", "denn", "also", "damit", "dabei", "dazu", "davon", "dafür",
    "selbst", "bereits", "wieder", "immer", "etwa", "eben",
    "gegen", "ohne", "während", "seit", "trotz", "wegen",
    "bzw", "vgl", "abs", "art", "gem", "ggf", "insb", "insbes",
    "sowie", "soweit", "sofern", "sowohl", "daher", "insoweit",
    "hingegen", "vielmehr", "gleichwohl", "indes",
})


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class SearchResult:
    """Ein einzelnes Suchergebnis."""
    text: str
    score: float
    collection: str
    metadata: dict = field(default_factory=dict)

    @property
    def breadcrumb(self) -> str:
        return self.metadata.get("breadcrumb", "")

    @property
    def paragraph(self) -> str:
        return self.metadata.get("paragraph", "")

    @property
    def gesetz(self) -> str:
        return self.metadata.get("gesetz", "")

    @property
    def source_type(self) -> str:
        return self.metadata.get("source_type", "")

    @property
    def dokument_typ(self) -> str:
        return self.metadata.get("dokument_typ", "")

    @property
    def fall(self) -> str:
        return self.metadata.get("fall", "")

    @property
    def aktenzeichen(self) -> str:
        return self.metadata.get("aktenzeichen", "")

    def short_text(self, max_len: int = 300) -> str:
        """Gekuerzter Text fuer Anzeige."""
        # Skip breadcrumb prefix in display
        t = self.text
        if t.startswith("["):
            idx = t.find("]\n")
            if idx > 0:
                t = t[idx + 2:]
        return t[:max_len].strip() + ("..." if len(t) > max_len else "")


# ---------------------------------------------------------------------------
# Sparse vector (identisch zu import_tool.py)
# ---------------------------------------------------------------------------

def _compute_sparse_vector(text: str) -> tuple[list[int], list[float]]:
    tokens = re.findall(r"\b\w+\b", text.lower())
    tokens = [t for t in tokens if t not in GERMAN_STOP_WORDS and len(t) > 2]
    counts = Counter(tokens)
    indices, values = [], []
    for token, count in counts.items():
        idx = int(hashlib.md5(token.encode()).hexdigest()[:8], 16)
        indices.append(idx)
        values.append(float(count))
    return indices, values


# ---------------------------------------------------------------------------
# Metadata-Filter Builder
# ---------------------------------------------------------------------------

def build_filter(
    paragraph: Optional[str] = None,
    gesetz: Optional[str] = None,
    fall: Optional[str] = None,
    aktenzeichen: Optional[str] = None,
    dokument_typ: Optional[str] = None,
) -> Optional[models.Filter]:
    """Baut einen Qdrant-Filter aus den uebergebenen Kriterien."""
    conditions = []

    if paragraph:
        # Normalize: "263" → "§ 263", "§263" → "§ 263"
        p = paragraph.strip()
        if not p.startswith("§"):
            p = f"§ {p}"
        p = re.sub(r"§\s*", "§ ", p)
        conditions.append(
            models.FieldCondition(
                key="paragraph",
                match=models.MatchValue(value=p),
            )
        )

    if gesetz:
        # Normalize: accept "stgb", "StGB", "STGB" etc.
        g = gesetz.strip()
        if g.lower() == "stgb":
            g = "StGB"
        elif g.lower() == "stpo":
            g = "StPO"
        conditions.append(
            models.FieldCondition(
                key="gesetz",
                match=models.MatchValue(value=g),
            )
        )

    if fall:
        conditions.append(
            models.FieldCondition(
                key="fall",
                match=models.MatchText(text=fall),
            )
        )

    if aktenzeichen:
        conditions.append(
            models.FieldCondition(
                key="aktenzeichen",
                match=models.MatchText(text=aktenzeichen),
            )
        )

    if dokument_typ:
        conditions.append(
            models.FieldCondition(
                key="dokument_typ",
                match=models.MatchValue(value=dokument_typ),
            )
        )

    if not conditions:
        return None
    return models.Filter(must=conditions)


# ---------------------------------------------------------------------------
# Query Expansion (Claude API)
# ---------------------------------------------------------------------------

EXPANSION_SYSTEM_PROMPT = """\
Du bist ein juristischer Query-Expansion-Assistent fuer ein deutsches Strafrechts-RAG-System.
Deine Aufgabe: Reformuliere die Nutzeranfrage in eine praezise juristische Suchanfrage.

Das RAG-System durchsucht:
1. StGB-Kommentar (Fischer) und StPO-Kommentar (Schmitt/Koehler) — mit §§ und Randnummern
2. Ermittlungsakten (Vermerke, Anklageschriften, Zeugenaussagen)

Antworte AUSSCHLIESSLICH mit einem JSON-Objekt (kein Markdown, kein Codeblock):
{
  "expanded_query": "Praezise juristische Suchanfrage mit Fachbegriffen",
  "keywords": ["Fachbegriff1", "Fachbegriff2"],
  "paragraph": "§ 263" oder null,
  "gesetz": "StGB" oder "StPO" oder null
}

Regeln:
- Verwende exakte juristische Terminologie (Tatbestandsmerkmale, Rechtsbegriffe)
- Wenn ein § erkennbar ist, extrahiere ihn
- Die expanded_query soll 1-3 Saetze lang sein
- Fuege relevante Synonyme und verwandte Rechtsbegriffe hinzu
- Bei Fragen zu Ermittlungsakten: behalte Sachverhaltsbezug bei
"""


@dataclass
class ExpandedQuery:
    """Ergebnis der Query Expansion."""
    original: str
    expanded: str
    keywords: list[str] = field(default_factory=list)
    paragraph: Optional[str] = None
    gesetz: Optional[str] = None


class QueryExpander:
    """Reformuliert Nutzeranfragen via Claude API in praezise juristische Queries."""

    def __init__(self):
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY nicht gesetzt")
        self.client = anthropic.Anthropic(api_key=api_key)
        log.info("QueryExpander (Claude) bereit.")

    def expand(self, query: str) -> ExpandedQuery:
        """Expandiert eine Nutzeranfrage."""
        try:
            response = self.client.messages.create(
                model=EXPANSION_MODEL,
                max_tokens=EXPANSION_MAX_TOKENS,
                system=EXPANSION_SYSTEM_PROMPT,
                messages=[{"role": "user", "content": query}],
            )
            text = response.content[0].text.strip()

            # Parse JSON — handle potential markdown wrapping
            if text.startswith("```"):
                text = re.sub(r"^```(?:json)?\s*", "", text)
                text = re.sub(r"\s*```$", "", text)

            data = json.loads(text)
            return ExpandedQuery(
                original=query,
                expanded=data.get("expanded_query", query),
                keywords=data.get("keywords", []),
                paragraph=data.get("paragraph"),
                gesetz=data.get("gesetz"),
            )
        except Exception as e:
            log.warning(f"Query Expansion fehlgeschlagen: {e} — verwende Original-Query")
            return ExpandedQuery(original=query, expanded=query)


# ---------------------------------------------------------------------------
# Reranking (Local Cross-Encoder / Cohere API fallback)
# ---------------------------------------------------------------------------

class LocalReranker:
    """Cross-Encoder Reranking mit BAAI/bge-reranker-v2-m3 (lokal, multilingual)."""

    def __init__(self):
        from sentence_transformers import CrossEncoder
        log.info(f"Lade Reranking-Modell: {LOCAL_RERANK_MODEL} ...")
        self.model = CrossEncoder(LOCAL_RERANK_MODEL)
        log.info("LocalReranker bereit.")

    def rerank(self, query: str, results: list["SearchResult"],
               top_k: int = DEFAULT_TOP_K) -> list["SearchResult"]:
        if not results:
            return results

        # Extract raw text (strip breadcrumb prefix)
        pairs = []
        for r in results:
            t = r.text
            if t.startswith("["):
                idx = t.find("]\n")
                if idx > 0:
                    t = t[idx + 2:]
            pairs.append((query, t))

        # Score all pairs
        scores = self.model.predict(pairs)

        # Sort by cross-encoder score
        scored = sorted(zip(scores, results), key=lambda x: x[0], reverse=True)

        reranked = []
        for score, original in scored[:top_k]:
            reranked.append(SearchResult(
                text=original.text,
                score=float(score),
                collection=original.collection,
                metadata=original.metadata,
            ))
        return reranked


class CohereReranker:
    """Cross-Encoder Reranking via Cohere API (Production Key erforderlich)."""

    def __init__(self):
        api_key = os.getenv("COHERE_API_KEY") or os.getenv("CO_API_KEY")
        if not api_key:
            raise ValueError("COHERE_API_KEY nicht gesetzt")
        self.client = cohere.ClientV2(api_key=api_key)
        # Test ob der Key Reranking unterstuetzt
        try:
            self.client.rerank(
                model=COHERE_RERANK_MODEL,
                query="test", documents=["test"], top_n=1,
            )
        except Exception:
            raise ValueError("Cohere Key unterstuetzt kein Reranking (Trial?)")
        log.info("CohereReranker (rerank-v3.5) bereit.")

    def rerank(self, query: str, results: list["SearchResult"],
               top_k: int = DEFAULT_TOP_K) -> list["SearchResult"]:
        if not results:
            return results

        documents = []
        for r in results:
            t = r.text
            if t.startswith("["):
                idx = t.find("]\n")
                if idx > 0:
                    t = t[idx + 2:]
            documents.append(t)

        try:
            response = self.client.rerank(
                model=COHERE_RERANK_MODEL,
                query=query,
                documents=documents,
                top_n=min(top_k, len(documents)),
            )
            reranked = []
            for item in response.results:
                original = results[item.index]
                reranked.append(SearchResult(
                    text=original.text,
                    score=item.relevance_score,
                    collection=original.collection,
                    metadata=original.metadata,
                ))
            return reranked
        except Exception as e:
            log.warning(f"Cohere Reranking fehlgeschlagen: {e}")
            return results[:top_k]


# ---------------------------------------------------------------------------
# Retriever
# ---------------------------------------------------------------------------

class JuristischerRetriever:
    """
    Hybrid-Retriever fuer juristische Texte.

    Sucht in einer oder beiden Qdrant-Collections mit konfigurierbarer
    Dense/BM25-Gewichtung und optionalen Metadata-Filtern.
    """

    def __init__(self, env_file: str = ".env.local",
                 enable_expansion: bool = True,
                 enable_reranking: bool = True):
        load_dotenv(env_file, override=True)
        url = os.getenv("QDRANT_ENDPOINT")
        key = os.getenv("QDRANT_API_KEY")
        if not url or not key:
            raise ValueError("QDRANT_ENDPOINT / QDRANT_API_KEY nicht gesetzt")

        self.client = QdrantClient(url=url, api_key=key, timeout=30)
        log.info("Lade Embedding-Modell ...")
        self.model = SentenceTransformer(DENSE_MODEL_NAME)

        # Query Expansion (optional)
        self.expander: Optional[QueryExpander] = None
        if enable_expansion and HAS_ANTHROPIC and os.getenv("ANTHROPIC_API_KEY"):
            try:
                self.expander = QueryExpander()
            except Exception as e:
                log.warning(f"Query Expansion nicht verfuegbar: {e}")

        # Reranking (optional) — try Cohere API first, fallback to local
        self.reranker = None
        if enable_reranking:
            if HAS_COHERE and (os.getenv("COHERE_API_KEY") or os.getenv("CO_API_KEY")):
                try:
                    self.reranker = CohereReranker()
                except Exception:
                    log.info("Cohere Reranking nicht verfuegbar, nutze lokalen Cross-Encoder")
            if self.reranker is None:
                try:
                    self.reranker = LocalReranker()
                except Exception as e:
                    log.warning(f"Reranking nicht verfuegbar: {e}")

        log.info("Retriever bereit.%s%s",
                 " [+Expansion]" if self.expander else "",
                 " [+Reranking]" if self.reranker else "")

    # --- public API ---

    def search(
        self,
        query: str,
        collections: Optional[list[str]] = None,
        top_k: int = DEFAULT_TOP_K,
        paragraph: Optional[str] = None,
        gesetz: Optional[str] = None,
        fall: Optional[str] = None,
        aktenzeichen: Optional[str] = None,
        dokument_typ: Optional[str] = None,
        weight_profile: Optional[str] = None,
        expand: bool = True,
        rerank: bool = True,
    ) -> tuple[list[SearchResult], Optional[ExpandedQuery]]:
        """
        Volle RAG-Pipeline: Query Expansion → Hybrid Search → Reranking.

        Args:
            query:           Suchanfrage (natuerliche Sprache oder juristisch)
            collections:     ["fachliteratur"], ["ermittlungsakten"], oder beide (None = beide)
            top_k:           Anzahl Ergebnisse
            paragraph:       Filter auf § (z.B. "§ 263" oder "263")
            gesetz:          Filter auf Gesetz ("StGB" / "StPO")
            fall:            Filter auf Fallname
            aktenzeichen:    Filter auf Aktenzeichen
            dokument_typ:    Filter auf Dokumenttyp (nur Ermittlungsakten)
            weight_profile:  "fachliteratur" / "ermittlungsakten" / "mixed" (auto wenn None)
            expand:          Query Expansion aktivieren (default: True)
            rerank:          Reranking aktivieren (default: True)

        Returns:
            (results, expanded_query) — expanded_query ist None wenn Expansion deaktiviert
        """
        if collections is None:
            collections = self._available_collections()

        # --- Step 1: Query Expansion ---
        expansion: Optional[ExpandedQuery] = None
        search_query = query

        if expand and self.expander:
            expansion = self.expander.expand(query)
            search_query = expansion.expanded
            log.info(f"Query expandiert: {search_query[:120]}...")

            # Use extracted metadata as filters (if not already set by user)
            if not paragraph and expansion.paragraph:
                paragraph = expansion.paragraph
            if not gesetz and expansion.gesetz:
                gesetz = expansion.gesetz

        # --- Step 2: Encode ---
        dense_vec = self.model.encode(
            f"query: {search_query}", normalize_embeddings=True
        ).tolist()
        sp_idx, sp_val = _compute_sparse_vector(search_query)

        # Build filter
        qfilter = build_filter(
            paragraph=paragraph, gesetz=gesetz, fall=fall,
            aktenzeichen=aktenzeichen, dokument_typ=dokument_typ,
        )

        # How many candidates to fetch (more if reranking, since reranker will filter)
        fetch_k = RERANK_CANDIDATES if (rerank and self.reranker) else top_k

        # --- Step 3: Hybrid Search ---
        all_results: list[SearchResult] = []

        for coll in collections:
            if not self.client.collection_exists(coll):
                log.warning(f"Collection '{coll}' nicht gefunden, ueberspringe.")
                continue

            if weight_profile:
                profile = WEIGHT_PROFILES.get(weight_profile, WEIGHT_PROFILES["mixed"])
            else:
                profile = WEIGHT_PROFILES.get(coll, WEIGHT_PROFILES["mixed"])

            results = self._hybrid_search(
                collection=coll,
                dense_vec=dense_vec,
                sparse_indices=sp_idx,
                sparse_values=sp_val,
                weights=profile,
                top_k=fetch_k,
                qfilter=qfilter,
            )
            all_results.extend(results)

        all_results.sort(key=lambda r: r.score, reverse=True)
        candidates = all_results[:fetch_k]

        # --- Step 4: Reranking ---
        if rerank and self.reranker and candidates:
            # Use the expanded query for reranking (more precise)
            rerank_query = search_query
            candidates = self.reranker.rerank(rerank_query, candidates, top_k=top_k)
            log.info(f"Reranked: {len(candidates)} Ergebnisse")
        else:
            candidates = candidates[:top_k]

        return candidates, expansion

    def search_fachliteratur(self, query: str, top_k: int = DEFAULT_TOP_K,
                             **kwargs) -> tuple[list[SearchResult], Optional[ExpandedQuery]]:
        """Shortcut: nur in Fachliteratur suchen."""
        return self.search(query, collections=[FACHLITERATUR_COLLECTION],
                           top_k=top_k, **kwargs)

    def search_ermittlungsakten(self, query: str, top_k: int = DEFAULT_TOP_K,
                                **kwargs) -> tuple[list[SearchResult], Optional[ExpandedQuery]]:
        """Shortcut: nur in Ermittlungsakten suchen."""
        return self.search(query, collections=[ERMITTLUNGSAKTEN_COLLECTION],
                           top_k=top_k, **kwargs)

    # --- internal ---

    def _available_collections(self) -> list[str]:
        available = []
        for name in [FACHLITERATUR_COLLECTION, ERMITTLUNGSAKTEN_COLLECTION]:
            if self.client.collection_exists(name):
                available.append(name)
        return available

    def _hybrid_search(
        self,
        collection: str,
        dense_vec: list[float],
        sparse_indices: list[int],
        sparse_values: list[float],
        weights: dict[str, float],
        top_k: int,
        qfilter: Optional[models.Filter],
    ) -> list[SearchResult]:
        """
        Gewichtete Hybrid-Suche: holt Dense- und BM25-Kandidaten separat,
        kombiniert per Reciprocal Rank Fusion mit Gewichtung.
        """
        prefetch_k = top_k * PREFETCH_MULTIPLIER

        # --- Dense search ---
        dense_results = self.client.query_points(
            collection_name=collection,
            query=dense_vec,
            using="dense",
            limit=prefetch_k,
            query_filter=qfilter,
            with_payload=True,
        ).points

        # --- BM25 search ---
        sparse_results = self.client.query_points(
            collection_name=collection,
            query=models.SparseVector(indices=sparse_indices, values=sparse_values),
            using="bm25",
            limit=prefetch_k,
            query_filter=qfilter,
            with_payload=True,
        ).points

        # --- Weighted RRF fusion ---
        # RRF score = weight / (rank + 60)  (k=60 is standard)
        RRF_K = 60
        scores: dict[str, float] = {}
        payloads: dict[str, dict] = {}

        for rank, point in enumerate(dense_results):
            pid = str(point.id)
            scores[pid] = scores.get(pid, 0.0) + weights["dense"] / (rank + RRF_K)
            if pid not in payloads:
                payloads[pid] = point.payload

        for rank, point in enumerate(sparse_results):
            pid = str(point.id)
            scores[pid] = scores.get(pid, 0.0) + weights["bm25"] / (rank + RRF_K)
            if pid not in payloads:
                payloads[pid] = point.payload

        # Build results sorted by fused score
        fused = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        results = []
        for pid, score in fused[:top_k]:
            payload = payloads[pid]
            text = payload.pop("text", "")
            results.append(SearchResult(
                text=text,
                score=score,
                collection=collection,
                metadata=payload,
            ))

        return results


# ---------------------------------------------------------------------------
# CLI: Pretty-Print
# ---------------------------------------------------------------------------

def print_expansion(expansion: Optional[ExpandedQuery]):
    """Zeigt die Query-Expansion an."""
    if not expansion:
        return
    print(f"\n🔄 Query Expansion:")
    print(f"   Original:  {expansion.original}")
    print(f"   Expandiert: {expansion.expanded}")
    if expansion.keywords:
        print(f"   Keywords:   {', '.join(expansion.keywords)}")
    if expansion.paragraph:
        print(f"   §: {expansion.paragraph}", end="")
        if expansion.gesetz:
            print(f" {expansion.gesetz}", end="")
        print()
    print()


def print_results(results: list[SearchResult], verbose: bool = False,
                  expansion: Optional[ExpandedQuery] = None,
                  show_expansion: bool = False):
    """Formatierte Ausgabe der Suchergebnisse."""
    if show_expansion and expansion:
        print_expansion(expansion)

    if not results:
        print("\n  Keine Treffer gefunden.\n")
        return

    for i, r in enumerate(results, 1):
        # Header
        src_icon = "📖" if r.source_type == "fachliteratur" else "📁"
        coll_label = r.collection.upper()

        if r.source_type == "fachliteratur":
            location = r.breadcrumb or f"{r.paragraph} {r.gesetz}"
        else:
            parts = []
            if r.fall:
                parts.append(r.fall)
            if r.aktenzeichen:
                parts.append(f"Az: {r.aktenzeichen}")
            if r.dokument_typ:
                parts.append(r.dokument_typ)
            location = " | ".join(parts) or r.collection

        print(f"\n{src_icon} Treffer {i}  [{coll_label}]  Score: {r.score:.4f}")
        print(f"   {location}")
        print(f"   {'─' * min(len(location), 70)}")

        # Text
        text_len = 500 if verbose else 250
        print(f"   {r.short_text(text_len)}")

    print(f"\n{'═' * 60}")
    print(f"  {len(results)} Treffer insgesamt")
    print()


# ---------------------------------------------------------------------------
# CLI: Interactive mode
# ---------------------------------------------------------------------------

def interactive_mode(retriever: JuristischerRetriever):
    """Interaktiver REPL-Modus fuer Abfragen."""
    print("\n╔═══════════════════════════════════════════════════════╗")
    print("║  Juristisches RAG – Interaktive Suche                ║")
    print("║  Befehle: /help /quit /filter /expand /rerank /verbose║")
    print("╚═══════════════════════════════════════════════════════╝\n")

    has_exp = retriever.expander is not None
    has_rr = retriever.reranker is not None
    print(f"  Pipeline: Hybrid Search"
          f"{' + Query Expansion' if has_exp else ''}"
          f"{' + Reranking' if has_rr else ''}\n")

    filters: dict = {}
    verbose = False
    show_expansion = True
    do_expand = True
    do_rerank = True
    collections = None

    while True:
        try:
            query = input("🔍 > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nAuf Wiedersehen!")
            break

        if not query:
            continue

        # --- Commands ---
        if query in ("/quit", "/exit"):
            print("Auf Wiedersehen!")
            break

        if query == "/help":
            print("""
  /filter §=263 gesetz=StGB    Metadata-Filter setzen
  /filter fall=Probenheld      Fall-Filter
  /filter typ=Anklageschrift   Dokumenttyp-Filter
  /reset                       Alle Filter loeschen
  /coll fachliteratur          Nur in einer Collection suchen
  /coll all                    In allen Collections suchen
  /expand                      Query Expansion an/aus toggle
  /rerank                      Reranking an/aus toggle
  /verbose                     Ausfuehrliche Textanzeige toggle
  /quit                        Beenden
""")
            continue

        if query == "/reset":
            filters = {}
            collections = None
            print("  Filter zurueckgesetzt.\n")
            continue

        if query == "/verbose":
            verbose = not verbose
            print(f"  Verbose: {'an' if verbose else 'aus'}\n")
            continue

        if query == "/expand":
            do_expand = not do_expand
            print(f"  Query Expansion: {'an' if do_expand else 'aus'}\n")
            continue

        if query == "/rerank":
            do_rerank = not do_rerank
            print(f"  Reranking: {'an' if do_rerank else 'aus'}\n")
            continue

        if query.startswith("/coll"):
            arg = query.split(maxsplit=1)[1].strip() if " " in query else ""
            if arg in ("all", "beide", ""):
                collections = None
                print("  Suche in allen Collections.\n")
            elif arg in ("fach", "fachliteratur", "kommentar"):
                collections = [FACHLITERATUR_COLLECTION]
                print(f"  Suche nur in: {FACHLITERATUR_COLLECTION}\n")
            elif arg in ("akten", "ermittlungsakten", "akte"):
                collections = [ERMITTLUNGSAKTEN_COLLECTION]
                print(f"  Suche nur in: {ERMITTLUNGSAKTEN_COLLECTION}\n")
            else:
                print(f"  Unbekannt: {arg}  (fach/akten/all)\n")
            continue

        if query.startswith("/filter"):
            parts = query.split()[1:]
            for part in parts:
                if "=" in part:
                    k, v = part.split("=", 1)
                    k = k.strip().lower()
                    mapping = {
                        "§": "paragraph", "para": "paragraph", "paragraph": "paragraph",
                        "gesetz": "gesetz", "g": "gesetz",
                        "fall": "fall", "f": "fall",
                        "az": "aktenzeichen", "aktenzeichen": "aktenzeichen",
                        "typ": "dokument_typ", "dokument_typ": "dokument_typ",
                    }
                    field_name = mapping.get(k)
                    if field_name:
                        filters[field_name] = v
                        print(f"  Filter: {field_name} = {v}")
                    else:
                        print(f"  Unbekannter Filter: {k}")
            print()
            continue

        # --- Search ---
        results, expansion = retriever.search(
            query=query,
            collections=collections,
            expand=do_expand,
            rerank=do_rerank,
            **filters,
        )
        print_results(results, verbose=verbose,
                      expansion=expansion, show_expansion=show_expansion)


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Juristisches RAG Retrieval-Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Beispiele:
  python retrieve.py "Hat der Angeklagte die Kunden betrogen?"
  python retrieve.py --show-expansion "Wann ist U-Haft zulässig?"
  python retrieve.py --no-expand --no-rerank "§ 263 Täuschung"
  python retrieve.py --collection ermittlungsakten --fall Probenheld "Bestellbetrug"
  python retrieve.py --interactive
        """,
    )
    parser.add_argument("query", nargs="?", help="Suchanfrage")
    parser.add_argument("--interactive", "-i", action="store_true",
                        help="Interaktiver Modus")
    parser.add_argument("--collection", "-c",
                        choices=["fachliteratur", "ermittlungsakten", "all"],
                        default="all", help="Collection (default: all)")
    parser.add_argument("--top-k", "-k", type=int, default=DEFAULT_TOP_K,
                        help=f"Anzahl Ergebnisse (default: {DEFAULT_TOP_K})")
    parser.add_argument("--paragraph", "-p", help="Filter: § (z.B. '263' oder '§ 263')")
    parser.add_argument("--gesetz", "-g", help="Filter: Gesetz (StGB/StPO)")
    parser.add_argument("--fall", "-f", help="Filter: Fallname")
    parser.add_argument("--aktenzeichen", "--az", help="Filter: Aktenzeichen")
    parser.add_argument("--dokument-typ", "--typ", help="Filter: Dokumenttyp")
    parser.add_argument("--no-expand", action="store_true",
                        help="Query Expansion deaktivieren")
    parser.add_argument("--no-rerank", action="store_true",
                        help="Reranking deaktivieren")
    parser.add_argument("--show-expansion", action="store_true",
                        help="Expandierte Query anzeigen")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Ausfuehrlichere Textanzeige")
    parser.add_argument("--env-file", default=".env.local",
                        help="Env-Datei (default: .env.local)")

    args = parser.parse_args()

    if not args.query and not args.interactive:
        parser.print_help()
        sys.exit(1)

    retriever = JuristischerRetriever(
        env_file=args.env_file,
        enable_expansion=not args.no_expand,
        enable_reranking=not args.no_rerank,
    )

    if args.interactive:
        interactive_mode(retriever)
        return

    # Single query
    collections = None
    if args.collection != "all":
        collections = [args.collection]

    results, expansion = retriever.search(
        query=args.query,
        collections=collections,
        top_k=args.top_k,
        paragraph=args.paragraph,
        gesetz=args.gesetz,
        fall=args.fall,
        aktenzeichen=args.aktenzeichen,
        dokument_typ=args.dokument_typ,
    )
    print_results(results, verbose=args.verbose,
                  expansion=expansion, show_expansion=args.show_expansion)


if __name__ == "__main__":
    main()
