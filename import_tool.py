#!/usr/bin/env python3
"""
RAG Import-Tool fuer juristische Analysen
==========================================
Spezialisiert auf:
  1. Fachliteratur (Kommentare) - Paragraph-aware Chunking mit Randnummer-Erkennung
  2. Ermittlungsakten - Dokumenttyp-basiertes Chunking

Embedding:  intfloat/multilingual-e5-large (1024 dim) mit Instruction Prefix
Sparse:     TF-basiert mit Qdrant-seitigem IDF (BM25-aehnlich)
Collections: 'fachliteratur' + 'ermittlungsakten' (Hybrid Search faehig)

Nutzung:
  python import_tool.py --all                 # Alles importieren
  python import_tool.py --fachliteratur       # Nur Kommentare
  python import_tool.py --ermittlungsakten    # Nur Akten
  python import_tool.py --all --recreate      # Collections neu aufbauen
  python import_tool.py --all --dry-run       # Nur Chunking-Statistiken
"""

import os
import re
import sys
import uuid
import hashlib
import argparse
import logging
from pathlib import Path
from dataclasses import dataclass, field
from collections import Counter
from typing import Optional

from dotenv import load_dotenv
from tqdm import tqdm
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

DENSE_MODEL_NAME = "intfloat/multilingual-e5-large"
DENSE_DIM = 1024
EMBED_BATCH_SIZE = 64
UPLOAD_BATCH_SIZE = 100

FACHLITERATUR_COLLECTION = "fachliteratur"
ERMITTLUNGSAKTEN_COLLECTION = "ermittlungsakten"

# Approximate chars-per-token for German legal text
CHARS_PER_TOKEN = 3.5

# Chunking limits (in characters)
KOMMENTAR_MAX_CHARS = int(768 * CHARS_PER_TOKEN)   # ~2688
KOMMENTAR_MIN_CHARS = int(80 * CHARS_PER_TOKEN)    # ~280
AKTE_MAX_CHARS = int(1536 * CHARS_PER_TOKEN)       # ~5376
AKTE_MIN_CHARS = int(150 * CHARS_PER_TOKEN)        # ~525

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# German stop words for sparse vector computation
# ---------------------------------------------------------------------------

GERMAN_STOP_WORDS = frozenset({
    "der", "die", "das", "ein", "eine", "einen", "einem", "einer", "eines",
    "und", "oder", "aber", "doch", "jedoch", "sondern", "weder", "noch",
    "in", "von", "zu", "mit", "auf", "fuer", "an", "bei", "aus", "nach",
    "ueber", "unter", "vor", "hinter", "neben", "zwischen", "durch", "für",
    "über",
    "ist", "sind", "war", "waren", "wird", "werden", "wurde", "wurden",
    "hat", "haben", "hatte", "hatten", "sein", "seine", "seinen", "seinem",
    "seiner",
    "nicht", "kein", "keine", "keinen", "keinem", "keiner",
    "dem", "den", "des", "sich", "sich", "es", "er", "sie", "wir", "ihr",
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
    "jedoch", "hingegen", "vielmehr", "gleichwohl", "indes", "dass",
})


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class Chunk:
    """A single text chunk with metadata."""
    text: str
    metadata: dict = field(default_factory=dict)

    @property
    def point_id(self) -> str:
        """Deterministic UUID based on content hash (idempotent re-imports)."""
        return str(uuid.uuid5(uuid.NAMESPACE_URL, self.text))


# ---------------------------------------------------------------------------
# Sparse vector computation
# ---------------------------------------------------------------------------

def compute_sparse_vector(text: str) -> tuple[list[int], list[float]]:
    """
    Compute term-frequency sparse vector for BM25-like hybrid search.
    Token → index mapping via MD5 hash (collision-free in practice).
    Qdrant applies IDF weighting server-side (Modifier.IDF).
    """
    tokens = re.findall(r"\b\w+\b", text.lower())
    tokens = [t for t in tokens if t not in GERMAN_STOP_WORDS and len(t) > 2]
    counts = Counter(tokens)

    indices: list[int] = []
    values: list[float] = []
    for token, count in counts.items():
        idx = int(hashlib.md5(token.encode()).hexdigest()[:8], 16)
        indices.append(idx)
        values.append(float(count))

    return indices, values


# ---------------------------------------------------------------------------
# Fachliteratur Chunker  (Paragraph-aware, Randnummer-Erkennung)
# ---------------------------------------------------------------------------

class FachliteraturChunker:
    """
    Chunking-Strategie fuer Beck'sche Kurz-Kommentare (Fischer StGB, Schmitt/Koehler StPO).

    Erkennt:
      - ## Seite N          → Seitenzahl-Tracking
      - § N (standalone)    → Paragraph-Kontext
      - Zahl am Zeilenanfang → Randnummer
      - A./B./I./II.        → Gliederungsebene

    Jeder Chunk bekommt einen Breadcrumb-Prefix:
      [§ 263 StGB – B. Obj. Tatbestand – Rn. 78]
    """

    # Lines to skip
    SKIP_PATTERNS = re.compile(
        r"^(#{1,3}\s*Inhaltsverzeichnis|#{1,3}\s*Vorwort|#{1,3}\s*Abkürzungsverzeichnis)"
    )

    def __init__(self, max_chars: int = KOMMENTAR_MAX_CHARS,
                 min_chars: int = KOMMENTAR_MIN_CHARS):
        self.max_chars = max_chars
        self.min_chars = min_chars

    def chunk_file(self, filepath: str) -> list[Chunk]:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Determine Gesetz / Kommentar
        if "StGB" in filepath:
            gesetz, kommentar = "StGB", "Fischer/Anstötz/Lutz StGB"
        elif "StPO" in filepath or "Strafprozess" in filepath:
            gesetz, kommentar = "StPO", "Schmitt/Köhler StPO"
        else:
            gesetz = Path(filepath).stem
            kommentar = gesetz

        lines = content.split("\n")
        chunks: list[Chunk] = []

        # State
        page = 0
        para: Optional[str] = None       # current § (e.g. "§ 263")
        section: Optional[str] = None     # current section header
        rn: Optional[int] = None          # current Randnummer
        buf: list[str] = []               # line buffer for current chunk
        buf_rn: Optional[int] = None
        buf_page: int = 0
        skip_until_next_page = False

        for line in lines:
            # --- Page marker ---
            m = re.match(r"^## Seite (\d+)", line)
            if m:
                page = int(m.group(1))
                skip_until_next_page = False
                continue

            # Skip front matter (title, copyright, TOC)
            if page < 5:
                continue

            # Skip known non-content sections
            if self.SKIP_PATTERNS.match(line.strip()):
                skip_until_next_page = True
                continue
            if skip_until_next_page:
                continue

            # --- Separator ---
            if line.strip() == "---":
                continue

            # --- Standalone § marker (page header) ---
            # Matches:  "§ 1"  /  "§ 1 StPO"  /  "§ 263a"  /  "StPO § 2"
            m = (re.match(r"^\s*§\s*(\d+\w?)\s*(?:StGB|StPO)?\s*$", line.strip())
                 or re.match(r"^\s*(?:StGB|StPO)\s*§\s*(\d+\w?)\s*$", line.strip()))
            if m:
                new_para = f"§ {m.group(1)}"
                if new_para != para:
                    # New paragraph – flush
                    self._flush(buf, chunks, filepath, gesetz, kommentar,
                                para, section, buf_rn, buf_page)
                    buf = []
                    para = new_para
                    section = None
                    rn = None
                    buf_rn = None
                continue

            # --- Empty line ---
            if not line.strip():
                if buf:
                    buf.append("")
                continue

            # --- Bare page number (e.g. "132") ---
            if re.match(r"^\d{1,4}$", line.strip()):
                continue

            # --- Section header (A., B., C. / I., II.) ---
            m = re.match(r"^([A-Z]{1,3})\.?\s+(.+?)(?:\.|$)", line.strip())
            if m and len(line.strip()) < 200:
                section = f"{m.group(1)}. {m.group(2).rstrip('.')}"

            # --- Randnummer detection ---
            m = re.match(r"^(\d{1,3})\s+\S", line)
            if m:
                rn_candidate = int(m.group(1))
                if rn_candidate < 500:
                    # Flush previous buffer
                    if buf:
                        self._flush(buf, chunks, filepath, gesetz, kommentar,
                                    para, section, buf_rn, buf_page)
                        buf = []
                    rn = rn_candidate
                    buf_rn = rn
                    buf_page = page

            # --- Accumulate line ---
            if not buf:
                buf_page = page
                if buf_rn is None:
                    buf_rn = rn
            buf.append(line)

            # --- Overflow check ---
            if len("\n".join(buf)) > self.max_chars:
                self._flush(buf, chunks, filepath, gesetz, kommentar,
                            para, section, buf_rn, buf_page)
                buf = []
                buf_rn = rn
                buf_page = page

        # Final flush
        self._flush(buf, chunks, filepath, gesetz, kommentar,
                    para, section, buf_rn, buf_page)

        return chunks

    # ---- internal helpers ----

    def _flush(self, buf: list[str], chunks: list[Chunk],
               filepath: str, gesetz: str, kommentar: str,
               para: Optional[str], section: Optional[str],
               rn: Optional[int], page: int):
        if not buf:
            return
        text = "\n".join(buf).strip()
        if len(text) < 60:
            return

        breadcrumb = self._breadcrumb(gesetz, para, section, rn)
        enriched = f"[{breadcrumb}]\n{text}"

        # If still too large, split at sentence boundaries
        if len(enriched) > self.max_chars * 1.5:
            parts = self._split_text(text, self.max_chars)
            for i, part in enumerate(parts):
                bc = breadcrumb + (f" (Teil {i+1})" if len(parts) > 1 else "")
                chunks.append(Chunk(
                    text=f"[{bc}]\n{part}",
                    metadata=self._meta(filepath, gesetz, kommentar,
                                        para, section, rn, bc, page),
                ))
        else:
            chunks.append(Chunk(
                text=enriched,
                metadata=self._meta(filepath, gesetz, kommentar,
                                    para, section, rn, breadcrumb, page),
            ))

    @staticmethod
    def _breadcrumb(gesetz: str, para: Optional[str],
                    section: Optional[str], rn: Optional[int]) -> str:
        parts = [f"{para} {gesetz}" if para else gesetz]
        if section:
            parts.append(section)
        if rn is not None:
            parts.append(f"Rn. {rn}")
        return " – ".join(parts)

    @staticmethod
    def _meta(filepath, gesetz, kommentar, para, section, rn, breadcrumb, page):
        return {
            "source_type": "fachliteratur",
            "source_file": str(filepath),
            "gesetz": gesetz,
            "kommentar": kommentar,
            "paragraph": para or "",
            "section": section or "",
            "randnummer": rn,
            "breadcrumb": breadcrumb,
            "page": page,
        }

    @staticmethod
    def _split_text(text: str, max_chars: int) -> list[str]:
        """Split at sentence boundaries (period/semicolon followed by space)."""
        sentences = re.split(r"(?<=[.;])\s+", text)
        parts: list[str] = []
        current: list[str] = []
        length = 0
        for sent in sentences:
            if length + len(sent) > max_chars and current:
                parts.append(" ".join(current))
                current = [sent]
                length = len(sent)
            else:
                current.append(sent)
                length += len(sent)
        if current:
            parts.append(" ".join(current))
        return parts


# ---------------------------------------------------------------------------
# Ermittlungsakten Chunker  (Dokumenttyp-basiert, grosse Chunks)
# ---------------------------------------------------------------------------

class ErmittlungsaktenChunker:
    """
    Chunking-Strategie fuer Ermittlungsakten.

    - Splittet an ## Headings (Vermerk, Anklageschrift, Zeugenaussage, …)
    - Klassifiziert Dokumenttyp automatisch
    - Behält Aktenzeichen und Blatt-Referenzen als Metadata
    - Groessere Chunks (1024-1536 Tokens) um Kontext zu bewahren
    """

    DOC_TYPE_PATTERNS = {
        "Anklageschrift": r"Anklageschrift|Anklage\b",
        "Vermerk": r"Vermerk|Vfa\.\s*Vermerk|Verfügung",
        "Zeugenaussage": r"Zeug(?:in|e)|Vernehmung|Aussage|Befragung",
        "Beschluss": r"Beschluss|Beschluß|Gerichtsbeschluss",
        "Urteil": r"Urteil\b|Urteilsbegründung|Strafbefehl",
        "Gutachten": r"Gutachten|Sachverständig",
        "Schreiben": r"Schreiben\b|Brief\b|Mitteilung|Mandatsniederlegung",
        "Protokoll": r"Protokoll|Hauptverhandlung|Sitzung",
        "Durchsuchung": r"Durchsuchung|Beschlagnahme",
        "Haftbefehl": r"Haftbefehl|Untersuchungshaft",
        "Bewertung": r"Bewertung|Analyse|Einschätzung",
        "Abrechnung": r"Abrechnung|Rechnung|Zahlung|Konto",
    }

    AZ_PATTERN = re.compile(r"(\d+\s*(?:Js|KLs|Ds|Ls)\s*\d+[/_]\d+)")

    def __init__(self, max_chars: int = AKTE_MAX_CHARS,
                 min_chars: int = AKTE_MIN_CHARS):
        self.max_chars = max_chars
        self.min_chars = min_chars

    def chunk_file(self, filepath: str) -> list[Chunk]:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        path = Path(filepath)
        fall = self._extract_fall(path)
        aktenzeichen = self._extract_aktenzeichen(path, content)

        sections = self._split_by_headings(content)
        chunks: list[Chunk] = []

        for heading, body in sections:
            doc_type = self._classify(heading, body[:500])
            blatt = self._extract_blatt(heading + " " + body[:300])
            full_text = f"{heading}\n{body}".strip() if heading else body.strip()

            if not full_text or len(full_text) < 60:
                continue

            prefix = self._build_prefix(fall, aktenzeichen, doc_type)
            meta = {
                "source_type": "ermittlungsakte",
                "source_file": str(filepath),
                "fall": fall,
                "aktenzeichen": aktenzeichen,
                "dokument_typ": doc_type,
                "blatt": blatt,
                "heading": (heading or "")[:200],
            }

            if len(full_text) <= self.max_chars:
                enriched = f"[{prefix}]\n{full_text}" if prefix else full_text
                chunks.append(Chunk(text=enriched, metadata=meta))
            else:
                parts = self._split_section(full_text, self.max_chars)
                for i, part in enumerate(parts):
                    m = {**meta, "teil": i + 1}
                    enriched = f"[{prefix}]\n{part}" if prefix else part
                    chunks.append(Chunk(text=enriched, metadata=m))

        return chunks

    # ---- helpers ----

    @staticmethod
    def _build_prefix(fall: str, az: str, doc_type: str) -> str:
        parts = []
        if fall:
            parts.append(f"Fall: {fall}")
        if az:
            parts.append(f"Az: {az}")
        if doc_type:
            parts.append(f"Typ: {doc_type}")
        return " | ".join(parts)

    def _extract_fall(self, path: Path) -> str:
        skip = {"Probenheld-MD", "data", "ermittlungsakten", ".", ".."}
        for part in reversed(path.parent.parts):
            if part in skip:
                continue
            return part
        return path.stem

    def _extract_aktenzeichen(self, path: Path, content: str) -> str:
        # From filename
        m = self.AZ_PATTERN.search(path.name)
        if m:
            return m.group(1).replace("_", "/")
        # From directory
        for part in path.parts:
            m = self.AZ_PATTERN.search(part)
            if m:
                return m.group(1).replace("_", "/")
        # From content header
        m = self.AZ_PATTERN.search(content[:1000])
        if m:
            return m.group(1).replace("_", "/")
        return ""

    def _classify(self, heading: str, text_start: str) -> str:
        combined = f"{heading} {text_start}"
        for doc_type, pattern in self.DOC_TYPE_PATTERNS.items():
            if re.search(pattern, combined, re.IGNORECASE):
                return doc_type
        return "Sonstiges"

    @staticmethod
    def _extract_blatt(text: str) -> str:
        m = re.search(r"(?:BL\.?|Blatt|Bl\.)\s*(\d+(?:\s*[-–]\s*\d+)?)",
                       text, re.IGNORECASE)
        return m.group(0) if m else ""

    def _split_by_headings(self, content: str) -> list[tuple[str, str]]:
        parts = re.split(r"^(#{1,3}\s+.+)$", content, flags=re.MULTILINE)
        sections: list[tuple[str, str]] = []

        if parts[0].strip():
            sections.append(("", parts[0]))

        for i in range(1, len(parts), 2):
            heading = parts[i].strip()
            body = parts[i + 1] if i + 1 < len(parts) else ""
            sections.append((heading, body))

        # Merge tiny sections into their predecessor
        merged: list[tuple[str, str]] = []
        for heading, body in sections:
            full = f"{heading}\n{body}".strip()
            if merged and len(full) < self.min_chars:
                prev_h, prev_b = merged[-1]
                merged[-1] = (prev_h, f"{prev_b}\n{heading}\n{body}")
            else:
                merged.append((heading, body))

        return merged

    @staticmethod
    def _split_section(text: str, max_chars: int) -> list[str]:
        paragraphs = text.split("\n\n")
        parts: list[str] = []
        current: list[str] = []
        length = 0
        for para in paragraphs:
            if length + len(para) > max_chars and current:
                parts.append("\n\n".join(current))
                current = [para]
                length = len(para)
            else:
                current.append(para)
                length += len(para) + 2
        if current:
            parts.append("\n\n".join(current))
        return parts


# ---------------------------------------------------------------------------
# Embedding Engine
# ---------------------------------------------------------------------------

class EmbeddingEngine:
    """sentence-transformers wrapper with E5 instruction prefix."""

    def __init__(self, model_name: str = DENSE_MODEL_NAME):
        log.info(f"Lade Embedding-Modell: {model_name} ...")
        self.model = SentenceTransformer(model_name)
        log.info("Modell geladen.")

    def embed_passages(self, texts: list[str],
                       batch_size: int = EMBED_BATCH_SIZE) -> list[list[float]]:
        """Embed with 'passage:' prefix (for indexing; use 'query:' at retrieval)."""
        prefixed = [f"passage: {t}" for t in texts]
        emb = self.model.encode(
            prefixed,
            batch_size=batch_size,
            show_progress_bar=False,
            normalize_embeddings=True,
        )
        return emb.tolist()


# ---------------------------------------------------------------------------
# Qdrant Manager
# ---------------------------------------------------------------------------

class QdrantManager:
    """Create collections, payload indexes, and upload points."""

    def __init__(self, url: str, api_key: str):
        self.client = QdrantClient(url=url, api_key=api_key, timeout=180)
        log.info(f"Qdrant verbunden: {url}")

    def setup_collection(self, name: str, recreate: bool = False):
        exists = self.client.collection_exists(name)

        if exists and recreate:
            log.info(f"Loesche Collection '{name}' ...")
            self.client.delete_collection(name)
            exists = False
        elif exists:
            log.info(f"Collection '{name}' existiert bereits (--recreate zum Neuaufbau).")
            return

        log.info(f"Erstelle Collection '{name}' ...")
        self.client.create_collection(
            collection_name=name,
            vectors_config={
                "dense": models.VectorParams(
                    size=DENSE_DIM,
                    distance=models.Distance.COSINE,
                    on_disk=True,
                ),
            },
            sparse_vectors_config={
                "bm25": models.SparseVectorParams(
                    modifier=models.Modifier.IDF,
                ),
            },
        )

        # Keyword indexes for metadata filtering
        keyword_fields = [
            "source_type", "gesetz", "paragraph", "kommentar",
            "aktenzeichen", "fall", "dokument_typ",
        ]
        for field_name in keyword_fields:
            try:
                self.client.create_payload_index(
                    collection_name=name,
                    field_name=field_name,
                    field_schema=models.PayloadSchemaType.KEYWORD,
                )
            except Exception:
                pass

        # Integer index for randnummer
        try:
            self.client.create_payload_index(
                collection_name=name,
                field_name="randnummer",
                field_schema=models.PayloadSchemaType.INTEGER,
            )
        except Exception:
            pass

        # Full-text index on text payload for keyword search fallback
        try:
            self.client.create_payload_index(
                collection_name=name,
                field_name="text",
                field_schema=models.TextIndexParams(
                    type=models.TextIndexType.TEXT,
                    tokenizer=models.TokenizerType.WORD,
                    min_token_len=3,
                    lowercase=True,
                ),
            )
        except Exception:
            pass

        log.info(f"Collection '{name}' mit Indexes erstellt.")

    def upload_chunks(self, collection_name: str, chunks: list[Chunk],
                      dense_embeddings: list[list[float]]):
        points: list[models.PointStruct] = []
        for chunk, dense_vec in zip(chunks, dense_embeddings):
            sp_idx, sp_val = compute_sparse_vector(chunk.text)
            points.append(models.PointStruct(
                id=chunk.point_id,
                vector={
                    "dense": dense_vec,
                    "bm25": models.SparseVector(indices=sp_idx, values=sp_val),
                },
                payload={"text": chunk.text, **chunk.metadata},
            ))

        total = len(points)
        for start in tqdm(range(0, total, UPLOAD_BATCH_SIZE),
                          desc=f"Upload → {collection_name}"):
            batch = points[start : start + UPLOAD_BATCH_SIZE]
            self.client.upsert(collection_name=collection_name, points=batch)

        log.info(f"{total} Punkte in '{collection_name}' hochgeladen.")


# ---------------------------------------------------------------------------
# Import pipelines
# ---------------------------------------------------------------------------

def import_fachliteratur(data_dir: str, qdrant: QdrantManager,
                         embedder: EmbeddingEngine, recreate: bool = False):
    fach_dir = Path(data_dir) / "fachliteratur"
    if not fach_dir.exists():
        log.error(f"Verzeichnis nicht gefunden: {fach_dir}")
        return

    md_files = sorted(fach_dir.rglob("*.md"))
    if not md_files:
        log.warning(f"Keine .md Dateien in {fach_dir}")
        return

    log.info(f"{len(md_files)} Fachliteratur-Datei(en) gefunden")
    qdrant.setup_collection(FACHLITERATUR_COLLECTION, recreate=recreate)

    chunker = FachliteraturChunker()
    all_chunks: list[Chunk] = []
    for fp in md_files:
        log.info(f"Chunking: {fp.name}")
        ch = chunker.chunk_file(str(fp))
        log.info(f"  → {len(ch)} Chunks")
        all_chunks.extend(ch)

    log.info(f"Fachliteratur gesamt: {len(all_chunks)} Chunks")
    if not all_chunks:
        return

    log.info("Berechne Dense Embeddings ...")
    texts = [c.text for c in all_chunks]
    all_emb: list[list[float]] = []
    for start in tqdm(range(0, len(texts), EMBED_BATCH_SIZE), desc="Embedding"):
        batch = texts[start : start + EMBED_BATCH_SIZE]
        all_emb.extend(embedder.embed_passages(batch))

    qdrant.upload_chunks(FACHLITERATUR_COLLECTION, all_chunks, all_emb)


def import_ermittlungsakten(data_dir: str, qdrant: QdrantManager,
                            embedder: EmbeddingEngine, recreate: bool = False):
    akten_dir = Path(data_dir) / "ermittlungsakten"
    if not akten_dir.exists():
        log.error(f"Verzeichnis nicht gefunden: {akten_dir}")
        return

    md_files = sorted(akten_dir.rglob("*.md"))
    if not md_files:
        log.warning(f"Keine .md Dateien in {akten_dir}")
        return

    log.info(f"{len(md_files)} Ermittlungsakten-Datei(en) gefunden")
    qdrant.setup_collection(ERMITTLUNGSAKTEN_COLLECTION, recreate=recreate)

    chunker = ErmittlungsaktenChunker()
    all_chunks: list[Chunk] = []
    for fp in tqdm(md_files, desc="Chunking Akten"):
        try:
            all_chunks.extend(chunker.chunk_file(str(fp)))
        except Exception as e:
            log.error(f"Fehler bei {fp.name}: {e}")

    log.info(f"Ermittlungsakten gesamt: {len(all_chunks)} Chunks")
    if not all_chunks:
        return

    log.info("Berechne Dense Embeddings ...")
    texts = [c.text for c in all_chunks]
    all_emb: list[list[float]] = []
    for start in tqdm(range(0, len(texts), EMBED_BATCH_SIZE), desc="Embedding"):
        batch = texts[start : start + EMBED_BATCH_SIZE]
        all_emb.extend(embedder.embed_passages(batch))

    qdrant.upload_chunks(ERMITTLUNGSAKTEN_COLLECTION, all_chunks, all_emb)


# ---------------------------------------------------------------------------
# Dry-run: show chunking statistics without embedding/uploading
# ---------------------------------------------------------------------------

def dry_run(data_dir: str, do_fach: bool, do_akten: bool):
    log.info("=== DRY RUN – nur Chunking-Statistiken ===\n")

    if do_fach:
        fach_dir = Path(data_dir) / "fachliteratur"
        chunker = FachliteraturChunker()
        total = 0
        for fp in sorted(fach_dir.rglob("*.md")):
            chunks = chunker.chunk_file(str(fp))
            total += len(chunks)
            log.info(f"  {fp.name}: {len(chunks)} Chunks")

            # Show some stats
            sizes = [len(c.text) for c in chunks]
            paras = set(c.metadata.get("paragraph", "") for c in chunks if c.metadata.get("paragraph"))
            log.info(f"    Zeichenlänge: min={min(sizes)}, max={max(sizes)}, "
                     f"avg={sum(sizes)//len(sizes)}")
            log.info(f"    Paragraphen: {len(paras)} verschiedene")

            # Show first 3 chunks as examples
            for c in chunks[:3]:
                preview = c.text[:150].replace("\n", " ")
                log.info(f"    Beispiel: {preview}...")
            print()

        log.info(f"  Fachliteratur gesamt: {total} Chunks\n")

    if do_akten:
        akten_dir = Path(data_dir) / "ermittlungsakten"
        chunker = ErmittlungsaktenChunker()
        total = 0
        type_counts: Counter = Counter()
        for fp in sorted(akten_dir.rglob("*.md")):
            try:
                chunks = chunker.chunk_file(str(fp))
            except Exception as e:
                log.error(f"  Fehler bei {fp.name}: {e}")
                continue
            total += len(chunks)
            for c in chunks:
                type_counts[c.metadata.get("dokument_typ", "?")] += 1

        log.info(f"  Ermittlungsakten gesamt: {total} Chunks")
        log.info(f"  Dokumenttypen:")
        for dt, cnt in type_counts.most_common():
            log.info(f"    {dt}: {cnt}")
        print()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="RAG Import-Tool fuer juristische Analysen",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--data-dir", default="./data",
                        help="Datenverzeichnis (default: ./data)")
    parser.add_argument("--env-file", default=".env.local",
                        help="Env-Datei mit QDRANT_ENDPOINT + QDRANT_API_KEY")
    parser.add_argument("--fachliteratur", action="store_true",
                        help="Nur Fachliteratur importieren")
    parser.add_argument("--ermittlungsakten", action="store_true",
                        help="Nur Ermittlungsakten importieren")
    parser.add_argument("--all", action="store_true",
                        help="Alles importieren")
    parser.add_argument("--recreate", action="store_true",
                        help="Collections neu erstellen (loescht bestehende Daten!)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Nur Chunking testen, kein Embedding/Upload")
    args = parser.parse_args()

    do_fach = args.fachliteratur or args.all
    do_akten = args.ermittlungsakten or args.all

    if not (do_fach or do_akten):
        parser.print_help()
        sys.exit(1)

    # --- Dry run (no Qdrant, no model needed) ---
    if args.dry_run:
        dry_run(args.data_dir, do_fach, do_akten)
        return

    # --- Full import ---
    load_dotenv(args.env_file)
    qdrant_url = os.getenv("QDRANT_ENDPOINT")
    qdrant_key = os.getenv("QDRANT_API_KEY")

    if not qdrant_url or not qdrant_key:
        log.error(f"QDRANT_ENDPOINT und QDRANT_API_KEY muessen in {args.env_file} gesetzt sein.")
        sys.exit(1)

    embedder = EmbeddingEngine()
    qdrant = QdrantManager(qdrant_url, qdrant_key)

    if do_fach:
        import_fachliteratur(args.data_dir, qdrant, embedder, recreate=args.recreate)

    if do_akten:
        import_ermittlungsakten(args.data_dir, qdrant, embedder, recreate=args.recreate)

    log.info("Import abgeschlossen.")


if __name__ == "__main__":
    main()
