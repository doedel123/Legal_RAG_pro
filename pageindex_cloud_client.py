#!/usr/bin/env python3
"""
PageIndex Cloud HTTP-Client
===========================
Duenner Wrapper um die hosted PageIndex-API (api.pageindex.ai). Nutzt den
``/chat/completions``-Endpoint, der die komplette reasoning-based Retrieval-
Pipeline auf ihrer Seite ausfuehrt und nur die finale Antwort liefert.

Doc muss via Web-Upload oder ``POST /doc/`` bereits indiziert sein; wir
uebergeben hier nur die ``doc_id``.
"""

from __future__ import annotations

import logging
import os
import time
from dataclasses import dataclass

import httpx

log = logging.getLogger(__name__)

BASE_URL = "https://api.pageindex.ai"


@dataclass
class CloudAnswer:
    answer: str
    latency_sec: float
    prompt_tokens: int = 0
    completion_tokens: int = 0


class PageIndexCloudClient:
    def __init__(self, api_key: str | None = None, timeout: float = 900.0,
                 max_retries: int = 3):
        key = api_key or os.getenv("PAGE_INDEX_API_KEY") or os.getenv("PAGEINDEX_API_KEY")
        if not key:
            raise ValueError("PAGE_INDEX_API_KEY fehlt in Umgebung")
        self.max_retries = max_retries
        self.client = httpx.Client(
            base_url=BASE_URL,
            headers={"api_key": key, "Content-Type": "application/json"},
            timeout=timeout,
        )

    def metadata(self, doc_id: str) -> dict:
        r = self.client.get(f"/doc/{doc_id}/metadata")
        r.raise_for_status()
        return r.json()

    def chat(self, doc_id: str, question: str,
             temperature: float = 0.0) -> CloudAnswer:
        t0 = time.time()
        last_err: Exception | None = None
        for attempt in range(self.max_retries):
            try:
                r = self.client.post(
                    "/chat/completions",
                    json={
                        "doc_id": doc_id,
                        "messages": [{"role": "user", "content": question}],
                        "stream": False,
                        "temperature": temperature,
                    },
                )
                r.raise_for_status()
                data = r.json()
                choice = data["choices"][0]
                msg = choice["message"]["content"]
                usage = data.get("usage", {})
                return CloudAnswer(
                    answer=msg.strip(),
                    latency_sec=time.time() - t0,
                    prompt_tokens=int(usage.get("prompt_tokens", 0)),
                    completion_tokens=int(usage.get("completion_tokens", 0)),
                )
            except (httpx.ReadError, httpx.ReadTimeout, httpx.ConnectError,
                    httpx.RemoteProtocolError) as e:
                last_err = e
                wait = 5 * (attempt + 1)
                log.warning("PageIndex Cloud retry %d/%d nach %s (%s): "
                            "wait %ds", attempt + 1, self.max_retries,
                            type(e).__name__, str(e)[:80], wait)
                time.sleep(wait)
        raise RuntimeError(f"PageIndex Cloud failed after {self.max_retries} "
                           f"retries: {last_err}") from last_err


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv(".env.local")
    c = PageIndexCloudClient()
    doc_id = "pi-cmmyzwegr005l09pfofq73oe8"
    print("Metadata:", c.metadata(doc_id).get("name"))
    ans = c.chat(doc_id, "Wer ist die Geschaedigte im Fall donkredito?")
    print(f"Answer ({ans.latency_sec:.1f}s):\n{ans.answer[:400]}")
