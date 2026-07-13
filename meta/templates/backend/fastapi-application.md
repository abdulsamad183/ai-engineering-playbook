---
title: "FastAPI Application Template"
description: "Scaffold template for a production FastAPI AI backend application."
type: backend-template
---

# FastAPI Application Scaffold

> Copy and adapt when starting a new AI backend service.

## Directory Layout

```
my_ai_api/
├── src/my_ai_api/
│   ├── __init__.py
│   ├── main.py                 # create_app() factory
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py         # Pydantic BaseSettings
│   ├── api/
│   │   ├── __init__.py
│   │   ├── dependencies.py     # DI wiring
│   │   ├── middleware.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── router.py       # Aggregates v1 routes
│   │       └── endpoints/
│   │           ├── health.py
│   │           └── chat.py
│   ├── schemas/                # Pydantic request/response models
│   ├── services/               # Business logic
│   ├── repositories/           # Data access (ports)
│   ├── models/                 # SQLAlchemy ORM models
│   ├── database/
│   │   ├── session.py
│   │   └── base.py
│   ├── clients/                # External HTTP (LLM, etc.)
│   └── core/
│       ├── exceptions.py
│       └── logging.py
├── tests/
│   ├── conftest.py
│   ├── unit/
│   └── integration/
├── alembic/
├── pyproject.toml
├── Dockerfile
└── .env.example
```

## main.py Template

```python
from contextlib import asynccontextmanager

from fastapi import FastAPI

from my_ai_api.api.v1.router import api_router
from my_ai_api.config.settings import get_settings
from my_ai_api.core.logging import setup_logging
from my_ai_api.database.session import init_db, close_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    await init_db()
    yield
    await close_db()


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        lifespan=lifespan,
    )
    app.include_router(api_router, prefix="/api/v1")
    return app


app = create_app()
```

## Checklist

- [ ] Settings from environment (no hardcoded secrets)
- [ ] Health and readiness endpoints
- [ ] Structured JSON logging with request IDs
- [ ] Global exception handlers
- [ ] CORS configured for known origins
- [ ] OpenAPI docs disabled in production (optional)

## See Also

- [Production Project Structure](../../../domains/backend-engineering/production-project-structure-for-ai.md)
- [FastAPI Complete Guide](../../../domains/fastapi/fastapi-complete-guide.md)
