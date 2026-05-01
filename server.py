#!/usr/bin/env python3
"""
FastAPI Server fuer das juristische RAG
========================================
Schlanker Produktions-Server mit API-only Retriever
(Mixedbread Embedding + Voyage Rerank + Anthropic Expansion + Qdrant).

Endpoints:
  GET  /health                 — Healthcheck fuer Railway/Cloud-Run
  POST /search                 — Haupt-Retrieval-Endpoint
  GET  /openai/tool_schema     — OpenAI Function-Calling Tool-Definition

Auth:
  Alle Endpoints ausser /health verlangen Header ``X-API-Key``.

Env-Variablen (.env.local / Railway Dashboard):
  API_KEY                Schuetzt die eigenen Endpoints
  QDRANT_ENDPOINT        Qdrant Cloud URL
  QDRANT_API_KEY         Qdrant Cloud Key
  ANTHROPIC_API_KEY      Fuer Query-Expansion (optional, empfohlen)
  MIXEDBREAD_API_KEY     Fuer Query-Embedding
  VOYAGE_API_KEY         Fuer Reranking
  PORT                   Port (von Railway gesetzt, default 8080)
"""

import os
import logging
from typing import Optional

from fastapi import FastAPI, HTTPException, Header, status
from pydantic import BaseModel, Field

from ours_mxbai_api_client import OursApiRetriever

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

app = FastAPI(
    title="Juristisches RAG",
    description="Retrieval-Augmented Generation fuer deutsche Strafrechtsliteratur",
    version="1.0.0",
)

# Retriever beim App-Start initialisieren (Cold-Start-Kosten einmalig)
RETRIEVER: Optional[OursApiRetriever] = None


@app.on_event("startup")
def _init_retriever():
    global RETRIEVER
    log.info("Initialisiere Retriever ...")
    RETRIEVER = OursApiRetriever()
    log.info("Retriever bereit.")


# --- Models ------------------------------------------------------------

SUPPORTED_DOMAINS = (
    "strafrecht", "arbeitsrecht", "mietrecht", "ao", "owigrecht", "verkehrsrecht",
)


class SearchRequest(BaseModel):
    query: str = Field(..., description="Juristische Fragestellung in natuerlicher Sprache")
    top_k: int = Field(5, ge=1, le=20, description="Anzahl Ergebnisse")
    domain: Optional[str] = Field(
        None,
        description=(
            "Optional: Rechtsgebiet-Filter. Einer von "
            "'strafrecht', 'arbeitsrecht', 'mietrecht', 'ao', "
            "'owigrecht', 'verkehrsrecht'. None = cross-domain (alle)."
        ),
    )


class Chunk(BaseModel):
    text: str
    score: float
    breadcrumb: str = ""
    domain: str = ""                        # strafrecht, mietrecht, …
    source_type: str = ""                   # "fachliteratur" | "ratgeber"
    # Felder fuer Kommentare:
    paragraph: str = ""
    gesetz: str = ""
    kommentar: str = ""
    randnummer: Optional[int] = None
    # Felder fuer Ratgeber / Sachbuecher:
    buch: str = ""
    kapitel: str = ""
    abschnitt: str = ""
    heading: str = ""
    source_file: str = ""


class SearchResponse(BaseModel):
    query: str
    results: list[Chunk]
    count: int


# --- Auth --------------------------------------------------------------

def require_api_key(x_api_key: Optional[str]) -> None:
    expected = os.getenv("API_KEY")
    if not expected:
        # In Dev ohne API_KEY laeuft's ungesichert.
        return
    if not x_api_key or x_api_key != expected:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Ungueltiger oder fehlender X-API-Key")


# --- Endpoints ---------------------------------------------------------

@app.get("/health")
def health():
    return {"status": "ok", "retriever_ready": RETRIEVER is not None}


@app.post("/search", response_model=SearchResponse)
def search(req: SearchRequest, x_api_key: Optional[str] = Header(None)):
    require_api_key(x_api_key)
    if RETRIEVER is None:
        raise HTTPException(status_code=503, detail="Retriever noch nicht initialisiert")

    domain = req.domain.strip().lower() if req.domain else None
    if domain and domain not in SUPPORTED_DOMAINS:
        raise HTTPException(
            status_code=400,
            detail=f"Unbekannte domain '{domain}'. Erlaubt: {list(SUPPORTED_DOMAINS)}",
        )

    try:
        hits = RETRIEVER.search(req.query, top_k=req.top_k, domain=domain)
    except Exception as e:
        log.exception("Search failed")
        raise HTTPException(status_code=500, detail=f"Retrieval-Fehler: {e}")

    results = []
    for h in hits:
        m = h.metadata or {}
        results.append(Chunk(
            text=h.text,
            score=float(h.score),
            breadcrumb=m.get("breadcrumb", "") or h.breadcrumb,
            domain=m.get("domain", ""),
            source_type=m.get("source_type", ""),
            paragraph=m.get("paragraph", "") or h.paragraph,
            gesetz=m.get("gesetz", ""),
            kommentar=m.get("kommentar", ""),
            randnummer=m.get("randnummer"),
            buch=m.get("buch", ""),
            kapitel=m.get("kapitel", ""),
            abschnitt=m.get("abschnitt", ""),
            heading=m.get("heading", ""),
            source_file=m.get("source_file", ""),
        ))
    return SearchResponse(query=req.query, results=results, count=len(results))


@app.get("/openai/tool_schema")
def openai_tool_schema(x_api_key: Optional[str] = Header(None)):
    """Liefert das Tool-Schema zum direkten Einsatz in OpenAI Function Calling."""
    require_api_key(x_api_key)
    return {
        "type": "function",
        "function": {
            "name": "search_fachliteratur",
            "description": (
                "Durchsucht juristische Fachliteratur aus den Rechtsgebieten "
                "Strafrecht (StGB/StPO), Arbeitsrecht (Erfurter Kommentar), "
                "Mietrecht (BGB), Abgabenordnung (AO), Ordnungswidrigkeitenrecht "
                "(OWiG) und Verkehrsrecht (StVG/StVO + Messverfahren) und "
                "liefert relevante Textpassagen. Die Bibliothek enthaelt zwei "
                "Quellen-Typen: 'fachliteratur' (Kommentare mit §, Randnummer, "
                "Kommentartitel) und 'ratgeber' (Sachbuecher mit Buch, Kapitel, "
                "Abschnitt, Heading). Jeder Treffer hat das Feld 'source_type', "
                "um zwischen beiden zu unterscheiden. Nutze den optionalen "
                "'domain'-Parameter, um gezielt ein Rechtsgebiet zu durchsuchen; "
                "ohne Filter wird in allen Gebieten gesucht. Nutze dieses Tool, "
                "wenn eine Frage juristische Fachkenntnisse erfordert."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Die juristische Fragestellung in natuerlicher Sprache.",
                    },
                    "top_k": {
                        "type": "integer",
                        "description": "Anzahl der zurueckzugebenden Top-Treffer (1-20, default 5).",
                        "default": 5,
                    },
                    "domain": {
                        "type": "string",
                        "enum": list(SUPPORTED_DOMAINS),
                        "description": (
                            "Optional: Rechtsgebiet-Filter. Weglassen fuer "
                            "cross-domain-Suche ueber alle Fachgebiete."
                        ),
                    },
                },
                "required": ["query"],
            },
        },
    }


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8080"))
    uvicorn.run(app, host="0.0.0.0", port=port)
