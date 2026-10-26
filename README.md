# Personal Intelligence Platform

An evidence-driven research system for creating, executing, and delivering traceable research jobs. The architecture separates request planning from job execution and treats every factual output as a claim with source evidence and confidence.

## Components

- `apps/api` — FastAPI API, job lifecycle, policy checks, and research worker entry points.
- `apps/dashboard` — Next.js research-workspace shell.
- `engines` — pluggable web, product, B2B lead, and website analysis capabilities.
- `services` — normalization, deduplication, source validation, scoring, and report assembly.
- `config` — deployment-safe policy defaults.

## Start with Docker

```powershell
Copy-Item .env.example .env
docker compose up --build
```

The API exposes `/docs`, `/healthz`, and `/v1/research-jobs`. The dashboard runs on port 3000; API runs on port 8000.

## Engineering principles

1. A job cannot execute until it has an explicit plan and passed policy checks.
2. Evidence is normalized, deduplicated, and attributed before report generation.
3. Engines receive a narrow query contract; external-provider keys never enter a job record.
4. Jobs are idempotent at the API boundary and transition through a bounded lifecycle.

## Verify

```powershell
pip install -e ".[dev]"
ruff check .
pytest
```