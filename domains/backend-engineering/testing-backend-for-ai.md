---
title: "Testing Backend for AI"
description: "Production backend testing for AI applications — pytest, unit tests, API testing, integration tests, mocking, fixtures, dependency overrides, test databases, and coverage with FastAPI patterns."
domain: backend-engineering
tags: [backend, testing, pytest, fastapi, mocking, integration, coverage, production, intermediate]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - backend-fundamentals-for-ai.md
  - backend-architecture-for-ai.md
  - async-programming-for-ai-backends.md
  - ../foundations/testing-fundamentals.md
  - ../fastapi/fastapi-foundation.md
  - ../logging/logging-and-error-handling.md
keywords: [pytest, fixtures, mocking, TestClient, dependency override, test database, coverage, integration tests, FastAPI, AI backend]
author: hp
---

# Testing Backend for AI

> Backend-specific testing depth for AI services — pytest suites that prove your FastAPI routes, services, and database wiring work without calling real LLMs or burning API credits in CI.

## Table of Contents

- [Foundation](#)
- [Backend Testing Strategy](#backend-testing-strategy)
- [pytest for AI Backends](#pytest-for-ai-backends)
- [Unit Testing Services](#unit-testing-services)
- [Mocking External Dependencies](#mocking-external-dependencies)
- [Fixtures and conftest Hierarchy](#fixtures-and-conftest-hierarchy)
- [API Testing with FastAPI](#api-testing-with-fastapi)
- [Dependency Overrides](#dependency-overrides)
- [Integration Testing](#integration-testing)
- [Test Database Patterns](#test-database-patterns)
- [Testing Async Backends](#testing-async-backends)
- [Coverage and Quality Gates](#coverage-and-quality-gates)
- [CI Pipeline for Backend Tests](#ci-pipeline-for-backend-tests)
- [Production Considerations](#production-considerations)
- [Common Mistakes](#common-mistakes)
- [Interview Preparation](#interview-preparation)
- [Navigation](#navigation)

---

## Foundation

This document is a **deep dive** backend depth. Before reading it, internalize the cross-cutting testing concepts in [Testing Fundamentals](../foundations/testing-fundamentals.md):

| Topic | Where It Lives | Extension Here |
|---------------|----------------|------------------------|
| Testing pyramid for AI apps | [Testing Pyramid](../foundations/testing-fundamentals.md#testing-pyramid-for-ai-apps) | Backend-specific layer split |
| pytest basics, markers, layout | [pytest Fundamentals](../foundations/testing-fundamentals.md#pytest-fundamentals) | `tests/api/`, `tests/integration/` layout |
| Fixtures and factory patterns | [Fixtures](../foundations/testing-fundamentals.md#fixtures) | Session-scoped DB, app factory |
| Mocking LLM ports | [Mocking and Fakes](../foundations/testing-fundamentals.md#mocking-and-fakes) | Repository and cache mocks |
| API testing intro | [API Testing with FastAPI](../foundations/testing-fundamentals.md#api-testing-with-fastapi) | Auth, streaming, dependency overrides |
| CI organization | [CI and Test Organization](../foundations/testing-fundamentals.md#ci-and-test-organization) | Backend pipeline stages |

> **Production Standard:** Foundations teach *what* to test and *why*. This handbook teaches *how* to wire FastAPI backends, test databases, and integration suites that survive refactors.

```mermaid
graph TB
    subgraph "Foundations"
        P2[Testing Fundamentals]
        P2 --> PYRAMID[Testing Pyramid]
        P2 --> MOCK[Mocking Philosophy]
        P2 --> EVAL[Eval vs Unit Boundary]
    end

    subgraph "Backend Depth"
        P3[Testing Backend for AI]
        P3 --> API[API Contract Tests]
        P3 --> DB[Test Database]
        P3 --> INT[Integration Wiring]
        P3 --> COV[Coverage Gates]
    end

    P2 --> P3
```

---

## Backend Testing Strategy

AI backends have three testable surfaces:

| Surface | What Breaks in Production | Test Type |
|---------|----------------------------|-----------|
| **HTTP API** | Wrong status codes, schema drift, auth bypass | API / contract tests |
| **Service layer** | Wrong `top_k`, missing retries, bad prompt assembly | Unit tests |
| **Infrastructure** | SQL bugs, migration failures, cache key collisions | Integration tests |

Separate **deterministic backend tests** from **non-deterministic model evaluation**. Backend pytest suites should never assert `response.content == "Paris"` from a real LLM.

```mermaid
graph LR
    subgraph "Fast — every commit"
        UNIT[Unit: services]
        API[API: TestClient]
    end

    subgraph "Medium — PR / merge"
        INT[Integration: real DB]
        CACHE[Integration: Redis]
    end

    subgraph "Slow — scheduled"
        EVAL[LLM Eval Harness]
        LOAD[Load Tests — k6]
    end

    UNIT --> CI[GitHub Actions]
    API --> CI
    INT --> CI
    CACHE --> CI
    EVAL --> NIGHTLY[Nightly Job]
```

Cross-reference [Backend Architecture for AI](backend-architecture-for-ai.md) for layer boundaries — tests should respect the same ports and adapters your production code uses.

---

## pytest for AI Backends

### Recommended Layout

```
tests/
  conftest.py                 # settings, app, shared mocks
  unit/
    conftest.py
    services/
      test_rag_service.py
      test_chat_service.py
    domain/
      test_prompt_builder.py
  api/
    conftest.py               # client, auth headers, overrides
    test_chat_routes.py
    test_document_routes.py
  integration/
    conftest.py               # test DB engine, migrations
    test_conversation_repo.py
    test_vector_index.py
  fakes/
    llm_fake.py
    retriever_fake.py
```

### `pyproject.toml`

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
asyncio_mode = "auto"
filterwarnings = ["ignore::DeprecationWarning"]
markers = [
    "integration: requires PostgreSQL or Redis",
    "slow: exceeds 5 seconds",
    "eval: LLM quality — excluded from default CI",
]

[tool.coverage.run]
source = ["app"]
omit = ["app/main.py", "*/migrations/*"]

[tool.coverage.report]
fail_under = 80
show_missing = true
exclude_lines = [
    "pragma: no cover",
    "if TYPE_CHECKING:",
    "raise NotImplementedError",
]
```

### Running Backend Tests

```bash
# Default CI — unit + API only
pytest -m "not integration and not eval" --cov=app --cov-report=term-missing

# Integration suite (requires docker-compose up)
pytest -m integration -v

# API tests only
pytest tests/api/ -v

# Fail fast during development
pytest tests/unit/test_rag_service.py -x --tb=short
```

---

## Unit Testing Services

Unit tests target the **service layer** — business orchestration with all ports mocked. They run in milliseconds and are your highest-ROI tests.

```python
# tests/unit/services/test_rag_service.py
import pytest
from unittest.mock import AsyncMock

from app.services.rag_service import RAGService
from app.domain.models import LLMResponse


@pytest.fixture
def mock_retriever():
    retriever = AsyncMock()
    retriever.search.return_value = [
        {"text": "RAG retrieves relevant documents.", "score": 0.95, "id": "c1"},
    ]
    return retriever


@pytest.fixture
def mock_llm():
    llm = AsyncMock()
    llm.complete.return_value = LLMResponse(
        content="RAG stands for Retrieval-Augmented Generation.",
        model="fake",
        input_tokens=50,
        output_tokens=20,
    )
    return llm


@pytest.fixture
def rag_service(mock_retriever, mock_llm) -> RAGService:
    return RAGService(retriever=mock_retriever, llm=mock_llm, top_k=5)


async def test_answer_searches_with_configured_top_k(rag_service, mock_retriever):
    await rag_service.answer("What is RAG?")
    mock_retriever.search.assert_awaited_once_with("What is RAG?", top_k=5)


async def test_answer_includes_retrieved_context_in_prompt(rag_service, mock_llm):
    await rag_service.answer("What is RAG?")
    prompt = mock_llm.complete.await_args.args[0]
    assert "RAG retrieves relevant documents." in prompt


async def test_answer_propagates_llm_rate_limit(rag_service, mock_llm):
    from app.domain.exceptions import RateLimitError
    mock_llm.complete.side_effect = RateLimitError("429 from provider")
    with pytest.raises(RateLimitError):
        await rag_service.answer("test")
```

### What to Unit Test in AI Backends

| Behavior | Example Assertion |
|----------|-------------------|
| Retrieval parameters | `top_k`, filters, tenant scoping |
| Prompt assembly | Context blocks, truncation, system prompt |
| Error mapping | Provider 429 → app `RateLimitError` |
| Retry logic | `side_effect` sequence, backoff calls |
| Token budget | Truncation when context exceeds limit |
| Idempotency | Duplicate request returns cached result |

See [Testing Fundamentals — Unit Testing Services](../foundations/testing-fundamentals.md#unit-testing-services) for additional patterns.

---

## Mocking External Dependencies

Mock at **port boundaries**, not deep inside vendor SDKs.

```python
# tests/unit/services/test_embedding_service.py
from unittest.mock import AsyncMock, patch
import pytest

from app.services.embedding_service import EmbeddingService


async def test_embed_batch_calls_provider_with_correct_model(mock_settings):
    mock_client = AsyncMock()
    mock_client.embed.return_value = [[0.1, 0.2, 0.3]]

    service = EmbeddingService(client=mock_client, model="text-embedding-3-small")
    result = await service.embed_batch(["hello", "world"])

    mock_client.embed.assert_awaited_once_with(
        texts=["hello", "world"],
        model="text-embedding-3-small",
    )
    assert len(result) == 2


async def test_embed_retries_on_transient_failure():
    mock_client = AsyncMock()
    mock_client.embed.side_effect = [
        ConnectionError("timeout"),
        [[0.1, 0.2]],
    ]
    service = EmbeddingService(client=mock_client, max_retries=2)
    result = await service.embed_batch(["hello"])
    assert mock_client.embed.await_count == 2
```

### Mock vs Fake Decision Matrix

| Dependency | Mock (`AsyncMock`) | Fake (in-memory impl) |
|------------|-------------------|----------------------|
| LLM client | Default choice | `FakeLLMClient` for multi-step flows |
| Vector retriever | Return canned chunks | `InMemoryRetriever` with scoring logic |
| Repository | Simple CRUD | `InMemoryConversationRepo` for stateful tests |
| Redis cache | `AsyncMock` with dict backing | `fakeredis` library |
| S3 storage | Mock `upload`/`download` | Local filesystem fake |

```python
# tests/fakes/llm_fake.py
from app.domain.models import LLMResponse


class FakeLLMClient:
    def __init__(self, responses: dict[str, str] | None = None):
        self._responses = responses or {}
        self.calls: list[dict] = []

    async def complete(self, prompt: str, *, system: str = "", **kwargs) -> LLMResponse:
        self.calls.append({"prompt": prompt, "system": system, **kwargs})
        content = self._responses.get(prompt, "default")
        return LLMResponse(content=content, model="fake", input_tokens=1, output_tokens=1)
```

---

## Fixtures and conftest Hierarchy

pytest discovers fixtures from nested `conftest.py` files upward. Organize by test layer.

```python
# tests/conftest.py
import pytest
from app.config.settings import Settings


@pytest.fixture
def settings() -> Settings:
    return Settings(
        app_env="test",
        database_url="postgresql+asyncpg://test:test@localhost:5433/ai_test",
        redis_url="redis://localhost:6380/15",
        openai_api_key="sk-test-fake-not-real",
        llm_model="gpt-4o-mini",
        log_level="warning",
        jwt_secret="test-secret-min-32-chars-long!!",
    )


@pytest.fixture
def make_message():
    def _factory(content: str = "Hello", role: str = "user", conversation_id: str = "conv-1"):
        from app.domain.models import Message
        return Message(content=content, role=role, conversation_id=conversation_id)
    return _factory
```

### Scoped Fixtures for Expensive Setup

| Scope | Backend Use Case |
|-------|------------------|
| `function` | Default — isolated DB transaction per test |
| `module` | Shared mock wiring for a test file |
| `session` | Test database engine, migrated schema |

```python
# tests/integration/conftest.py
import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker


@pytest.fixture(scope="session")
async def db_engine(settings):
    engine = create_async_engine(settings.database_url, echo=False)
    # run migrations once
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    await engine.dispose()


@pytest.fixture
async def db_session(db_engine) -> AsyncSession:
    async with async_sessionmaker(db_engine, expire_on_commit=False)() as session:
        yield session
        await session.rollback()  # isolate tests
```

> **Rule:** Use factory fixtures (`make_chunk`, `make_user`) instead of shared mutable objects. See [Testing Fundamentals — Factory Fixtures](../foundations/testing-fundamentals.md#factory-fixtures).

---

## API Testing with FastAPI

API tests verify HTTP contracts — status codes, response schemas, auth enforcement, and error envelopes. Use `TestClient` for sync tests or `httpx.AsyncClient` for async.

```python
# tests/api/test_chat_routes.py
import pytest
from httpx import AsyncClient, ASGITransport

from app.main import app


@pytest.fixture
async def client(override_deps):
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


async def test_create_message_returns_201(client, auth_headers):
    response = await client.post(
        "/v1/conversations/conv-1/messages",
        json={"content": "What is RAG?"},
        headers=auth_headers,
    )
    assert response.status_code == 201
    body = response.json()
    assert body["role"] == "assistant"
    assert "content" in body
    assert body["conversation_id"] == "conv-1"


async def test_create_message_rejects_empty_content(client, auth_headers):
    response = await client.post(
        "/v1/conversations/conv-1/messages",
        json={"content": ""},
        headers=auth_headers,
    )
    assert response.status_code == 422


async def test_create_message_requires_auth(client):
    response = await client.post(
        "/v1/conversations/conv-1/messages",
        json={"content": "hello"},
    )
    assert response.status_code == 401
```

### Testing Streaming Endpoints

```python
async def test_chat_stream_returns_sse_events(client, auth_headers):
    response = await client.post(
        "/v1/chat/stream",
        json={"message": "Hi"},
        headers=auth_headers,
    )
    assert response.status_code == 200
    assert "text/event-stream" in response.headers["content-type"]

    chunks = []
    async for line in response.aiter_lines():
        if line.startswith("data: "):
            chunks.append(line[6:])
    assert len(chunks) > 0
    assert chunks[-1] == "[DONE]"
```

Cross-reference [Backend Fundamentals — Streaming APIs](backend-fundamentals-for-ai.md#streaming-apis) and [Logging and Error Handling](../logging/logging-and-error-handling.md) for error response shapes to assert.

---

## Dependency Overrides

FastAPI's `app.dependency_overrides` is the primary mechanism for injecting test doubles without modifying production routes.

```python
# app/api/deps.py
from fastapi import Depends
from app.services.rag_service import RAGService
from app.infrastructure.llm.openai_client import get_llm_client
from app.infrastructure.retrieval.pg_retriever import get_retriever


def get_rag_service(
    llm=Depends(get_llm_client),
    retriever=Depends(get_retriever),
) -> RAGService:
    return RAGService(llm=llm, retriever=retriever)
```

```python
# tests/api/conftest.py
import pytest
from unittest.mock import AsyncMock

from app.main import app
from app.api.deps import get_rag_service, get_current_user
from app.domain.models import User, LLMResponse


@pytest.fixture
def fake_rag_service():
    service = AsyncMock()
    service.answer.return_value = LLMResponse(
        content="Test answer",
        model="fake",
        input_tokens=10,
        output_tokens=5,
    )
    return service


@pytest.fixture
def fake_user():
    return User(id="user-1", email="test@example.com", tenant_id="tenant-1")


@pytest.fixture
def override_deps(fake_rag_service, fake_user):
    app.dependency_overrides[get_rag_service] = lambda: fake_rag_service
    app.dependency_overrides[get_current_user] = lambda: fake_user
    yield
    app.dependency_overrides.clear()  # critical — prevents test pollution
```

### Override Patterns

| Pattern | When to Use |
|---------|-------------|
| Override service dependency | API tests for route logic only |
| Override repository | API tests with in-memory data |
| Override settings | Test-specific config without env files |
| Override auth dependency | Skip JWT validation in route tests |

```python
# Override settings via dependency
from app.config.settings import get_settings

@pytest.fixture
def override_settings(settings):
    app.dependency_overrides[get_settings] = lambda: settings
    yield
    app.dependency_overrides.clear()
```

> **Critical:** Always call `app.dependency_overrides.clear()` in fixture teardown. Missing cleanup causes order-dependent failures — documented in [Testing Fundamentals — Common Mistakes](../foundations/testing-fundamentals.md#common-mistakes).

---

## Integration Testing

Integration tests use **real infrastructure** (PostgreSQL, Redis) with **fake LLM** — proving SQL, migrations, indexes, and cache keys work.

```python
# tests/integration/test_conversation_repo.py
import pytest
from app.infrastructure.repositories.conversation_repo import ConversationRepository


@pytest.mark.integration
async def test_save_and_load_messages(db_session, make_message):
    repo = ConversationRepository(db_session)
    msg = make_message(content="Hello", conversation_id="conv-int-1")
    await repo.save_message(msg)

    loaded = await repo.get_messages("conv-int-1")
    assert len(loaded) == 1
    assert loaded[0].content == "Hello"


@pytest.mark.integration
async def test_tenant_isolation(db_session, make_message):
    repo = ConversationRepository(db_session)
    await repo.save_message(make_message(conversation_id="c1"), tenant_id="tenant-a")
    await repo.save_message(make_message(conversation_id="c2"), tenant_id="tenant-b")

    tenant_a_msgs = await repo.get_messages_for_tenant("tenant-a")
    assert all(m.conversation_id == "c1" for m in tenant_a_msgs)
```

### docker-compose for Integration Tests

```yaml
# docker-compose.test.yml
services:
  postgres-test:
    image: postgres:16
    environment:
      POSTGRES_USER: test
      POSTGRES_PASSWORD: test
      POSTGRES_DB: ai_test
    ports: ["5433:5432"]

  redis-test:
    image: redis:7
    ports: ["6380:6379"]
```

### testcontainers Alternative

```python
import pytest
from testcontainers.postgres import PostgresContainer


@pytest.fixture(scope="session")
def postgres_url():
    with PostgresContainer("postgres:16") as pg:
        yield pg.get_connection_url().replace("psycopg2", "asyncpg")
```

Mark integration tests with `@pytest.mark.integration` and exclude from default CI per [Testing Fundamentals](../foundations/testing-fundamentals.md#ci-and-test-organization).

---

## Test Database Patterns

| Pattern | Pros | Cons |
|---------|------|------|
| In-memory SQLite | Fast, no Docker | Diverges from PostgreSQL semantics |
| Dedicated test PostgreSQL | Production parity | Requires Docker/CI service |
| Transaction rollback per test | Fast isolation | Cannot test commit behavior |
| Truncate tables per test | Tests real commits | Slower cleanup |
| Alembic migrate once per session | Catches migration bugs | Slower startup |

### Transaction Rollback Pattern (Recommended)

```python
@pytest.fixture
async def db_session(db_engine):
    connection = await db_engine.connect()
    transaction = await connection.begin()
    session = AsyncSession(bind=connection, expire_on_commit=False)

    yield session

    await session.close()
    await transaction.rollback()
    await connection.close()
```

### Testing Migrations

```python
@pytest.mark.integration
async def test_migration_adds_prompt_version_column(alembic_runner, db_session):
    alembic_runner.upgrade("head")
    result = await db_session.execute(
        text("SELECT column_name FROM information_schema.columns "
             "WHERE table_name='messages' AND column_name='prompt_version'")
    )
    assert result.scalar() == "prompt_version"
```

See [Alembic Migrations for AI](../databases/postgresql/alembic-migrations-for-ai.md) for migration workflow.

---

## Testing Async Backends

AI backends are overwhelmingly async. Configure `asyncio_mode = "auto"` in `pyproject.toml` and use `pytest-asyncio`.

```python
# Async test with httpx
async def test_concurrent_requests_do_not_block(client, auth_headers):
    import asyncio
    tasks = [
        client.post("/v1/chat", json={"message": f"msg-{i}"}, headers=auth_headers)
        for i in range(10)
    ]
    responses = await asyncio.gather(*tasks)
    assert all(r.status_code == 200 for r in responses)
```

### Testing `asyncio` Utilities

```python
async def test_rate_limiter_delays_excess_calls():
    from app.infrastructure.rate_limit import AsyncRateLimiter
    import time

    limiter = AsyncRateLimiter(max_calls=2, period_seconds=1.0)
    start = time.monotonic()
    await limiter.acquire()
    await limiter.acquire()
    await limiter.acquire()  # should wait
    elapsed = time.monotonic() - start
    assert elapsed >= 0.9
```

Cross-reference [Async Programming for AI Backends](async-programming-for-ai-backends.md) for event loop pitfalls that tests should catch.

---

## Coverage and Quality Gates

Coverage measures **which lines ran**, not **whether behavior is correct**. Use it as a gap detector, not a target for its own sake.

| Layer | Target Coverage | Rationale |
|-------|----------------|-----------|
| Service layer | 85–95% | Highest business logic density |
| Domain models / validators | 90%+ | Cheap to test, high bug prevention |
| API routes | 70–80% | Focus on auth, errors, happy path |
| Infrastructure adapters | 60–70% | Integration tests supplement |
| Generated / boilerplate | Exclude | `omit` in coverage config |

```bash
# Generate HTML report for PR review
pytest --cov=app --cov-report=html
open htmlcov/index.html

# Fail CI below threshold
pytest --cov=app --cov-fail-under=80
```

### High-Value Coverage Gaps to Chase

- Error handlers and exception mappers
- Retry and circuit-breaker branches
- Tenant scoping in repositories
- Input validation edge cases (empty, max length, unicode)
- Background task enqueue paths

---

## CI Pipeline for Backend Tests

```yaml
# .github/workflows/backend-tests.yml
name: Backend Tests

on: [push, pull_request]

jobs:
  unit-and-api:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -e ".[test]"
      - run: pytest -m "not integration and not eval" --cov=app --cov-fail-under=80

  integration:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
          POSTGRES_DB: ai_test
        ports: ["5432:5432"]
      redis:
        image: redis:7
        ports: ["6379:6379"]
    steps:
      - uses: actions/checkout@v4
      - run: pip install -e ".[test]"
      - run: pytest -m integration -v
        env:
          DATABASE_URL: postgresql+asyncpg://test:test@localhost:5432/ai_test
          REDIS_URL: redis://localhost:6379/15
```

### Test Naming Convention

```
test_<unit>_<scenario>_<expected>

test_chat_route_missing_auth_returns_401()
test_rag_service_empty_retrieval_still_calls_llm()
test_conversation_repo_tenant_isolation_filters_correctly()
```

---

## Production Considerations

- **No real LLM keys in unit/API CI** — dependency overrides and fakes only; reserve API keys for nightly eval jobs.
- **Parallel workers** — use `pytest-xdist` for unit tests; give each integration worker its own database schema or use transaction isolation.
- **Test data hygiene** — never commit production PII; use factory-generated anonymized fixtures.
- **Contract tests as API documentation** — when frontend depends on response shape, API tests are the enforcement mechanism.
- **Flaky test policy** — quarantine flaky tests immediately; never merge "retry 3 times" as a permanent fix.
- **Snapshot review** — golden files for chunking/parsing require explicit PR review when updated.
- **Load testing is separate** — pytest is not a load tool; use k6 or Locust for throughput SLOs.

---

## Common Mistakes

| Mistake | Impact | Fix |
|---------|--------|-----|
| Real LLM calls in unit tests | Flaky, expensive CI | `dependency_overrides` + fakes |
| Forgetting `dependency_overrides.clear()` | Order-dependent failures | `yield` fixture with cleanup |
| SQLite for integration tests | Misses PostgreSQL-specific bugs | Test PostgreSQL in CI |
| Testing private methods | Brittle on refactor | Test public service interface |
| 100% coverage on adapters | Low-value assertions | Focus coverage on services |
| Shared mutable session fixtures | State leaks between tests | Transaction rollback per test |
| No `@pytest.mark.integration` | 30-minute CI runs | Mark and filter slow tests |
| Asserting exact LLM prose | Breaks on model change | Assert structure; eval for quality |
| Skipping auth tests | Production auth bypass | Test 401/403 on every protected route |
| No streaming tests | SSE bugs in production | `aiter_lines()` contract tests |

---

## Interview Preparation

### Frequently Asked Questions

**Q1: How do you test a FastAPI endpoint that calls an LLM without hitting the real API?**

> **Strong answer:** Use `app.dependency_overrides` to replace the service or LLM client dependency with an `AsyncMock` or `FakeLLMClient`. API tests assert HTTP status, response schema, and auth. Service unit tests assert the service called the port correctly. Never call OpenAI in default CI.

**Q2: What's the difference between unit, API, and integration tests for an AI backend?**

> **Strong answer:** Unit tests isolate service logic with all ports mocked — fast, deterministic. API tests hit routes via TestClient with dependency overrides — verify HTTP contracts and auth. Integration tests use real PostgreSQL/Redis with fake LLM — verify SQL, migrations, cache keys, and wiring. Model quality is a separate eval layer.

**Q3: How do you set up a test database for pytest?**

> **Strong answer:** Session-scoped engine with Alembic migrations run once. Function-scoped session with transaction rollback for isolation. docker-compose or testcontainers in CI. Never use production DB. Mention asyncpg + SQLAlchemy async session patterns.

**Q4: How do testing fundamentals relate to backend testing?**

> **Strong answer:** Foundations ([Testing Fundamentals](../foundations/testing-fundamentals.md)) covers the pyramid, mocking philosophy, and eval boundary. This handbook implements those principles for FastAPI — dependency overrides, test DB, integration markers, and coverage gates on the service layer.

### Real-World Scenario

**Scenario:** CI passes but staging breaks — new chat messages return 500 after a database migration. Unit tests still pass.

> **Discussion points:** Unit tests mocked the repository — integration test gap. Add migration integration test. Add API test with real DB session (marked integration). Verify Alembic downgrade/upgrade in CI. Check that `dependency_overrides` did not mask a schema mismatch.

---

## Navigation

### Prerequisites

- [Testing Fundamentals](../foundations/testing-fundamentals.md) — pyramid, mocking, eval boundary
- [Backend Fundamentals for AI](backend-fundamentals-for-ai.md) — DI, TestClient, request lifecycle
- [Software Engineering for AI](../foundations/software-engineering-for-ai.md) — ports and adapters

### Related Topics

- [Backend Architecture for AI](backend-architecture-for-ai.md) — layer boundaries under test
- [Async Programming for AI Backends](async-programming-for-ai-backends.md) — testing async handlers
- [FastAPI Foundation](../fastapi/fastapi-foundation.md) — advanced testing patterns
- [Logging and Error Handling](../logging/logging-and-error-handling.md) — asserting error envelopes

### Next Topics

- [Security for AI Backends](../security/security-for-ai-backends.md) — testing auth and input validation
- [Backend Performance for AI](../performance-optimization/backend-performance-for-ai.md) — load testing complement
- [CICD Domain](../cicd/README.md) — pipeline integration

### Future Reading

- [AI Evaluation Domain](../ai-evaluation/README.md) — model quality harnesses
- [Alembic Migrations for AI](../databases/postgresql/alembic-migrations-for-ai.md) — migration testing

---

## See Also

- [Backend Engineering Domain README](README.md)
- [Testing Fundamentals — Best Practices](../foundations/testing-fundamentals.md#best-practices)
- [Master Index](../../meta/indexes/MASTER-INDEX.md)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial release |
