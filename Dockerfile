FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Nur die Server-Deps installieren (kein torch/sentence-transformers)
COPY requirements-server.txt .
RUN pip install -r requirements-server.txt

# Nur die tatsaechlich benoetigten Module kopieren — kein data/, keine Notebooks.
COPY retrieve.py \
     ours_mxbai_api_client.py \
     ours_mxbai_voyage_client.py \
     server.py \
     ./

EXPOSE 8080

# Railway setzt $PORT; fallback auf 8080.
CMD ["sh", "-c", "uvicorn server:app --host 0.0.0.0 --port ${PORT:-8080}"]
