# Codex Enterprise

A framework for building enterprise applications. Trying to make it easier to add AI capabilities to existing business systems.

## What's the goal

Most enterprise apps are built the same way — auth, CRUD, workflows, reporting. Codex is my attempt to create a reusable foundation so I don't have to start from scratch every time.

Current focus:
- FastAPI backend with auth
- PostgreSQL for data
- Redis for caching
- AI integration (OpenAI)

## Getting started

```bash
git clone https://github.com/Samar-Khalid/Codex-Enterprise.git
cd Codex-Enterprise
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Run with Docker:

```bash
docker-compose up -d
```

Or without:

```bash
uvicorn backend.api.main:app --reload
```

API docs at http://localhost:8000/docs

## Structure

```
backend/
├── core/       # Config, database
├── api/        # FastAPI endpoints
├── services/   # Business logic
└── workers/    # Background tasks
```

## Status

Early stage. Auth works, basic CRUD works. Still building out the AI features and ERP connectors.

## License

MIT
