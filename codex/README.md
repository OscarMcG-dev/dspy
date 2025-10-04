# Codex Experimentation Tool

Lightweight, pluggable LLM experimentation with observability.

## Quick start

1. Copy env

```bash
cp .env.example .env
```

2. Start infra (local)

```bash
docker compose -f infra/docker-compose.yml up -d
```

3. Run API locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r api/requirements.txt
uvicorn api.app:app --reload
```

4. Health check

```bash
curl localhost:8000/healthz
```

Grafana at http://localhost:3001
