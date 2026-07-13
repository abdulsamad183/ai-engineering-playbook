---
title: "Backend Engineering Mistakes"
description: "Phase 3 troubleshooting guide for AI backend failures — blocking async, session leaks, missing indexes, poor API design, large payloads, memory leaks, circular imports, bad folder structure, hardcoded config, missing validation, weak auth, and improper error handling — with symptoms, root cause, diagnosis, fix, and prevention."
domain: backend-engineering
tags: [backend, debugging, production, troubleshooting, mistakes, advanced]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - backend-fundamentals-for-ai.md
  - backend-architecture-for-ai.md
  - production-project-structure-for-ai.md
  - ai-backend-reference-architecture.md
  - async-programming-for-ai-backends.md
  - ../common-mistakes/common-engineering-mistakes.md
keywords: [troubleshooting, blocking async, session leaks, database indexes, API design, memory leaks, circular imports, validation, auth, error handling]
author: hp
---

# Backend Engineering Mistakes

> Phase 3 troubleshooting guide for the backend failures that take down AI services in production — structured as symptoms, root cause, diagnosis, fix, and prevention for each mistake.

## Table of Contents

- [How to Use This Guide](#how-to-use-this-guide)
- [Severity and Triage Matrix](#severity-and-triage-matrix)
- [1. Blocking Async](#1-blocking-async)
- [2. Session Leaks](#2-session-leaks)
- [3. Missing Indexes](#3-missing-indexes)
- [4. Poor API Design](#4-poor-api-design)
- [5. Large Payloads](#5-large-payloads)
- [6. Memory Leaks](#6-memory-leaks)
- [7. Circular Imports](#7-circular-imports)
- [8. Bad Folder Structure](#8-bad-folder-structure)
- [9. Hardcoded Config](#9-hardcoded-config)
- [10. Missing Validation](#10-missing-validation)
- [11. Weak Auth](#11-weak-auth)
- [12. Improper Error Handling](#12-improper-error-handling)
- [Diagnostic Toolkit](#diagnostic-toolkit)
- [Pre-Production Checklist](#pre-production-checklist)
- [Interview Preparation](#interview-preparation)
- [Navigation](#navigation)

---

## How to Use This Guide

Each mistake follows the same troubleshooting structure:

| Section | Purpose |
|---------|---------|
| **Symptoms** | What you observe in production, logs, or monitoring |
| **Root Cause** | Why the failure happens at a mechanical level |
| **Diagnose** | Concrete steps and commands to confirm the hypothesis |
| **Fix** | Code and configuration changes that resolve the issue |
| **Prevention** | Practices and review checks that stop recurrence |

This document is a **Phase 3 backend-specific** companion to [Common Engineering Mistakes](../common-mistakes/common-engineering-mistakes.md). It assumes you have read:

| Prerequisite | Covers |
|--------------|--------|
| [Backend Fundamentals for AI](backend-fundamentals-for-ai.md) | Request lifecycle, async endpoints, middleware |
| [Async Programming for AI Backends](async-programming-for-ai-backends.md) | Event loop, non-blocking I/O |
| [Production Project Structure for AI](production-project-structure-for-ai.md) | Folder layout and import rules |
| [AI Backend Reference Architecture](ai-backend-reference-architecture.md) | Component interactions at runtime |

> **Production Standard:** When an AI API degrades under load, the root cause is almost always engineering — not the model. Start with async discipline, connection pools, and indexes before tuning prompts.

---

## Severity and Triage Matrix

Use this matrix to prioritize during incidents or code review.

| Mistake | User Impact | Data Risk | Cost Risk | Fix Urgency |
|---------|-------------|-----------|-----------|-------------|
| Blocking async | **Critical** — all requests stall | Low | Medium | Immediate |
| Session leaks | High — DB exhaustion | Medium | Low | Immediate |
| Missing indexes | High — timeouts | Low | Medium | High |
| Weak auth | High — breach | **Critical** | High | Immediate |
| Memory leaks | High — OOM kills | Medium | Medium | High |
| Large payloads | Medium — timeouts | Low | High (LLM tokens) | Medium |
| Hardcoded config | Low until breach | **Critical** | Medium | High |
| Missing validation | Medium — bad data | Medium | Medium | Medium |
| Poor API design | Medium — client bugs | Low | Low | Planned |
| Circular imports | Dev blocked | Low | Low | Before merge |
| Bad folder structure | Slow velocity | Low | Low | Planned |
| Improper error handling | Medium — opaque failures | Medium | Low | Medium |

---

## 1. Blocking Async

### Symptoms

- Latency spikes affect **all** concurrent requests, not just the slow one
- p95 jumps from 200ms to 30s+ under moderate load (20–50 users)
- CPU usage stays low while requests queue — event loop is blocked
- Uvicorn workers appear healthy but clients time out
- Streaming chat stalls mid-response for every connected client
- `asyncio` debug mode logs: `Executing <Task...> took X seconds`

### Root Cause

A **synchronous blocking call** runs on the asyncio event loop thread. While blocked, no other coroutine can progress — including health checks, WebSocket pings, and unrelated API requests.

Common blockers in AI backends:

| Blocking Call | Where It Appears |
|---------------|------------------|
| Sync OpenAI SDK (`openai.OpenAI()`) | Route handlers, services |
| `requests.get()` | Tool adapters, web fetch |
| `time.sleep()` | Retry logic |
| PDF parsing (`PyPDF2`, `pdfplumber`) | Ingestion in async handler |
| `pandas.read_csv()` | Data export endpoints |
| Sync SQLAlchemy (`session.query()`) | Legacy repository code |

Cross-reference: [Async Programming for AI Backends](async-programming-for-ai-backends.md#blocking-the-event-loop).

### Diagnose

```bash
# Enable asyncio debug mode locally
PYTHONASYNCIODEBUG=1 uvicorn app.main:app --reload

# Profile a slow request
py-spy record -o profile.svg --pid $(pgrep -f uvicorn)

# Check if sync SDK is imported
rg "from openai import OpenAI[^A]" app/
rg "import requests" app/
rg "time\.sleep" app/

# Load test — if throughput flatlines regardless of workers, suspect blocking
hey -n 200 -c 50 http://localhost:8000/v1/chat
```

In production, look for:

- Request duration variance: one slow endpoint drags global p99
- Worker count increased but throughput unchanged
- Gap between request start log and first DB/LLM span in traces

### Fix

```python
# BAD — sync OpenAI client blocks the event loop
from openai import OpenAI

client = OpenAI()

@router.post("/chat")
async def chat(body: ChatRequest):
    response = client.chat.completions.create(  # BLOCKS
        model="gpt-4o",
        messages=[{"role": "user", "content": body.message}],
    )
    return {"reply": response.choices[0].message.content}


# GOOD — async client
from openai import AsyncOpenAI

@router.post("/chat")
async def chat(
    body: ChatRequest,
    llm: AsyncOpenAI = Depends(get_async_openai),
):
    response = await llm.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": body.message}],
    )
    return {"reply": response.choices[0].message.content}


# GOOD — CPU-bound work offloaded
@router.post("/ingest")
async def ingest(file: UploadFile):
    content = await file.read()
    text = await asyncio.to_thread(parse_pdf, content)
    return {"chars": len(text)}
```

| Blocker Type | Fix |
|--------------|-----|
| Sync HTTP SDK | Switch to async client (`httpx.AsyncClient`, `AsyncOpenAI`) |
| CPU-bound parsing | `asyncio.to_thread()` or worker queue |
| Sync DB driver | `asyncpg` + SQLAlchemy async session |
| `time.sleep` in retry | `await asyncio.sleep()` |

For ingestion and embedding batches, move work to [Background Processing for AI](background-processing-for-ai.md) workers entirely.

### Prevention

- [ ] Code review rule: no sync I/O in `async def` functions
- [ ] Lint against `import requests` and sync `OpenAI` in `app/`
- [ ] Load test with 50+ concurrent requests before launch
- [ ] Use `httpx.AsyncClient` and `AsyncOpenAI` from project start
- [ ] CI job running `pytest` with `asyncio` mode and integration tests under concurrency

---

## 2. Session Leaks

### Symptoms

- `TooManyConnectionsError` or `FATAL: remaining connection slots are reserved`
- PostgreSQL `pg_stat_activity` shows hundreds of `idle in transaction` connections
- API works initially, degrades over hours without traffic spike
- Connection pool exhaustion after deploy or traffic burst
- Memory grows on database server
- Intermittent `TimeoutError` acquiring a session from the pool

### Root Cause

SQLAlchemy `AsyncSession` objects are opened but **never closed** — typically because:

1. Session created outside `async with` or `yield` dependency without guaranteed cleanup
2. Exception raised before `session.close()` in manual session management
3. Session stored on `request.state` or global variable and reused across requests
4. Background task holds session reference after request completes
5. `autoflush` + long-running LLM call inside an open transaction locks rows

Cross-reference: [SQLAlchemy for AI Applications](../databases/postgresql/sqlalchemy-for-ai-applications.md), [Production Project Structure for AI](production-project-structure-for-ai.md#database--connection-lifecycle).

### Diagnose

```sql
-- PostgreSQL: count connections by state
SELECT state, count(*)
FROM pg_stat_activity
WHERE datname = 'ai_backend'
GROUP BY state;

-- Find long-running idle transactions
SELECT pid, state, query_start, query
FROM pg_stat_activity
WHERE state = 'idle in transaction'
  AND query_start < now() - interval '5 minutes';
```

```python
# Add pool logging temporarily
engine = create_async_engine(url, echo_pool=True)
```

```bash
# Search for manual session creation without context manager
rg "AsyncSession\(" app/ --glob '!tests/*'
rg "session\.close" app/
```

Check application logs for exceptions mid-request that skip the `finally` block.

### Fix

```python
# BAD — session leak on exception
@router.get("/documents/{doc_id}")
async def get_document(doc_id: str, factory=Depends(get_session_factory)):
    session = factory()
    doc = await session.get(DocumentORM, doc_id)
    # if LLM call raises here, session never closes
    result = await expensive_llm_call(doc)
    await session.close()
    return result


# GOOD — dependency with yield guarantees cleanup
async def get_session(
    factory: async_sessionmaker[AsyncSession] = Depends(get_session_factory),
) -> AsyncIterator[AsyncSession]:
    async with factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise


# GOOD — keep transactions short; LLM calls outside transaction
async def get_document(doc_id: str, repo: DocumentRepository = Depends(...)):
    doc = await repo.get_by_id(doc_id)  # short transaction
    summary = await llm.summarize(doc.content)  # no open session during LLM
    return {"doc": doc, "summary": summary}
```

| Fix | Detail |
|-----|--------|
| Use `yield` dependency | FastAPI calls cleanup after response |
| Short transactions | Never hold session open during LLM calls |
| Pool sizing | `pool_size=10`, `max_overflow=20` — tune to PostgreSQL `max_connections` |
| Lifespan shutdown | `await engine.dispose()` on app shutdown |

### Prevention

- [ ] All DB access through `get_session` yield dependency — no manual `AsyncSession()`
- [ ] Code review: flag any `session =` assignment outside dependency injection
- [ ] Monitor `pg_stat_activity` count as a metric
- [ ] Set `pool_pre_ping=True` and reasonable `pool_recycle=3600`
- [ ] Integration tests that run 100+ sequential requests and assert stable pool count

---

## 3. Missing Indexes

### Symptoms

- Endpoints fast with 100 rows, timeout with 100,000 rows
- PostgreSQL CPU at 100% with simple `SELECT` queries
- `EXPLAIN ANALYZE` shows `Seq Scan` on large tables
- Chat history load slows as conversation count grows
- Document listing by `tenant_id` degrades per customer
- RAG metadata queries slow despite small vector store

### Root Cause

Queries filter or join on columns **without indexes**. AI backends accumulate data fast — messages, chunks, usage events, ingestion logs — and sequential scans that were fine in development become production incidents.

High-risk unindexed columns in AI apps:

| Table | Column | Query Pattern |
|-------|--------|---------------|
| `messages` | `session_id` | Load chat history |
| `messages` | `(tenant_id, created_at)` | Tenant message listing |
| `documents` | `(tenant_id, status)` | Ingestion dashboard |
| `documents` | `created_at` | Pagination sort |
| `usage_events` | `(tenant_id, created_at)` | Billing aggregation |
| `agent_runs` | `(tenant_id, status)` | Active run listing |

Cross-reference: [PostgreSQL for AI](../databases/postgresql/postgresql-for-ai.md), [Alembic Migrations for AI](../databases/postgresql/alembic-migrations-for-ai.md).

### Diagnose

```sql
-- Find sequential scans on large tables
SELECT schemaname, relname, seq_scan, seq_tup_read, idx_scan
FROM pg_stat_user_tables
WHERE seq_scan > 1000
ORDER BY seq_tup_read DESC;

-- Explain a slow query
EXPLAIN (ANALYZE, BUFFERS)
SELECT * FROM messages
WHERE session_id = 'abc123'
ORDER BY created_at DESC
LIMIT 20;
```

```bash
# Enable slow query log in development
# postgresql.conf: log_min_duration_statement = 200
```

Use APM trace spans — DB queries over 100ms on indexed lookups indicate missing indexes.

### Fix

```python
# alembic/versions/003_add_message_indexes.py
def upgrade() -> None:
    op.create_index("ix_messages_session_id", "messages", ["session_id"])
    op.create_index(
        "ix_messages_tenant_created",
        "messages",
        ["tenant_id", "created_at"],
    )
    op.create_index(
        "ix_documents_tenant_status",
        "documents",
        ["tenant_id", "status"],
    )
```

```python
# models/orm/message.py — declare indexes in ORM
class MessageORM(Base):
    __tablename__ = "messages"
    __table_args__ = (
        Index("ix_messages_session_created", "session_id", "created_at"),
    )
```

| Scenario | Index Type |
|----------|------------|
| Equality filter | B-tree on column |
| Tenant + sort | Composite `(tenant_id, created_at DESC)` |
| JSONB metadata search | GIN index on JSONB path |
| Vector similarity | IVFFlat or HNSW on embedding column (pgvector) |

### Prevention

- [ ] `EXPLAIN ANALYZE` for every new query in code review
- [ ] Seed load test with 100k+ rows before launch
- [ ] Monitor `seq_scan` vs `idx_scan` ratio in PostgreSQL metrics
- [ ] Add indexes in Alembic migrations, not ad hoc in production
- [ ] Composite indexes match `WHERE` + `ORDER BY` column order

---

## 4. Poor API Design

### Symptoms

- Frontend team requests API changes every sprint — contract unstable
- Breaking changes shipped without version bump
- Clients parse error bodies inconsistently; no standard error shape
- Pagination missing — endpoints return unbounded lists
- Chat endpoint returns full history instead of cursor-based pages
- No idempotency — duplicate document uploads on retry
- Inconsistent naming: `/getUserChats`, `/chat/create`, `/v1/message`

### Root Cause

APIs designed for the **first client** (usually the developer's own frontend) without contract discipline. AI products exacerbate this — streaming, job status polling, and tool schemas each need explicit design.

Cross-reference: [API Design for AI](../apis/api-design-for-ai.md), [HTTP Fundamentals for AI](../apis/http-fundamentals-for-ai.md).

### Diagnose

- Review OpenAPI spec at `/docs` — are response models complete?
- Check for endpoints returning raw dicts without `response_model`
- Search for breaking changes without `/v2/` prefix
- Client bug reports mentioning "unexpected response shape"
- Load test listing endpoints — do they return megabytes?

```bash
# Find routes without response_model
rg "@router\.(get|post|put|delete)" app/api/ -A2 | rg -v "response_model"
```

### Fix

```python
# BAD — ambiguous, unversioned, unbounded
@router.get("/chats")
async def get_chats(user_id: str):
    return await db.execute("SELECT * FROM messages WHERE user_id = :id", {"id": user_id})


# GOOD — versioned, typed, paginated
@router.get("/v1/sessions", response_model=SessionListResponse)
async def list_sessions(
    user: User = Depends(get_current_user),
    cursor: str | None = None,
    limit: int = Query(20, le=100),
    service: ChatService = Depends(get_chat_service),
) -> SessionListResponse:
    return await service.list_sessions(user.id, cursor=cursor, limit=limit)
```

| Principle | Implementation |
|-----------|----------------|
| Versioning | `/v1/` prefix; breaking changes → `/v2/` |
| Consistent errors | `{"error": {"code": "...", "message": "...", "request_id": "..."}}` |
| Pagination | Cursor-based for chat history and document lists |
| Long operations | `202 Accepted` + `job_id` + `GET /jobs/{id}` |
| Idempotency | `Idempotency-Key` header on uploads and billing |
| Streaming | `Accept: text/event-stream` documented in OpenAPI |

### Prevention

- [ ] OpenAPI spec reviewed before every release
- [ ] Standard error schema in `schemas/errors.py`
- [ ] API design doc or ADR for new resource types
- [ ] Contract tests that validate response shapes
- [ ] Follow [API Design for AI](../apis/api-design-for-ai.md) naming conventions

---

## 5. Large Payloads

### Symptoms

- `413 Payload Too Large` from reverse proxy (nginx default 1MB)
- Request timeouts on document upload or chat with long context
- LLM API errors: context length exceeded
- Memory spikes when deserializing large JSON bodies
- PostgreSQL `JSONB` columns bloating table size
- High LLM costs from sending entire documents instead of chunks

### Root Cause

No limits on **inbound** request size, **outbound** response size, or **LLM context** assembly. AI backends naturally handle large data — without explicit bounds, a single request can exhaust memory or token budgets.

Cross-reference: [File Handling for AI](file-handling-for-ai.md), [AI Backend Reference Architecture](ai-backend-reference-architecture.md#architecture-2-rag-backend).

### Diagnose

```bash
# Check nginx/client_max_body_size
rg "client_max_body_size" deploy/

# Find endpoints without size limits
rg "UploadFile" app/api/ -B5 | rg -v "max.*size|File\(.*max"

# Monitor request body size in middleware logs
```

```python
# Log payload sizes temporarily
@app.middleware("http")
async def log_body_size(request: Request, call_next):
    body = await request.body()
    if len(body) > 100_000:
        logger.warning("large_request", size=len(body), path=request.url.path)
    ...
```

Check LLM token counts in monitoring — sudden spikes indicate context bloat.

### Fix

```python
# Request validation — limit message length
class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=8_000)


# File upload — explicit size check
MAX_UPLOAD_BYTES = 50 * 1024 * 1024  # 50 MB

@router.post("/v1/documents")
async def upload(file: UploadFile):
    content = await file.read(MAX_UPLOAD_BYTES + 1)
    if len(content) > MAX_UPLOAD_BYTES:
        raise PayloadTooLargeError(max_bytes=MAX_UPLOAD_BYTES)
    ...


# Context assembly — token budget
class ContextBuilder:
    def build(self, chunks: list[Chunk], max_tokens: int = 4000) -> str:
        selected, total = [], 0
        for chunk in chunks:
            tokens = count_tokens(chunk.text)
            if total + tokens > max_tokens:
                break
            selected.append(chunk)
            total += tokens
        return "\n\n".join(c.text for c in selected)
```

| Layer | Limit |
|-------|-------|
| Reverse proxy | `client_max_body_size 50m` |
| Pydantic schema | `max_length` on strings, `max_items` on lists |
| File upload | Stream to S3; never load 500MB into memory |
| LLM context | Hard cap with trimming — [RAGService](ai-backend-reference-architecture.md#architecture-2-rag-backend) |
| Response | Paginate; never return 10k messages in one response |

### Prevention

- [ ] Pydantic `Field` limits on every string and list input
- [ ] Streaming upload to object storage for files > 1MB
- [ ] Token counting before LLM calls
- [ ] Middleware warning on requests > 100KB
- [ ] Integration test asserting 413 on oversized upload

---

## 6. Memory Leaks

### Symptoms

- Pod memory grows linearly over hours/days — never released
- OOMKilled containers in Kubernetes after sustained traffic
- `htop` shows Python process RSS climbing without traffic increase
- Global caches without TTL or max size grow unbounded
- Worker processes not recycling after N tasks (Celery `max_tasks_per_child`)
- Client disconnects during streaming but server memory not freed

### Root Cause

Objects accumulate because nothing releases them:

| Leak Source | Mechanism |
|-------------|-----------|
| Global dict cache | Grows with every unique query/key |
| Unclosed `httpx.AsyncClient` | Connection objects retained |
| Streaming generator not consumed | Client disconnect leaves generator suspended |
| `lru_cache` on unbounded inputs | Cache grows with every unique argument |
| Event listener not removed | Handlers accumulate on repeated startup |
| Large objects on `app.state` | Never cleared between requests |

### Diagnose

```bash
# Memory profiling
mprof run uvicorn app.main:app
mprof plot

# tracemalloc snapshot comparison
python -c "
import tracemalloc
tracemalloc.start()
# ... run load test ...
snapshot = tracemalloc.take_snapshot()
for stat in snapshot.statistics('lineno')[:10]:
    print(stat)
"

# Check for global mutable state
rg "^[A-Z_]+ = \{\}|^[a-z_]+_cache = " app/
```

In Kubernetes: graph container memory over 24h — sawtooth (healthy) vs ramp (leak).

### Fix

```python
# BAD — unbounded global cache
_response_cache: dict[str, str] = {}

async def get_cached_response(key: str) -> str | None:
    if key not in _response_cache:
        _response_cache[key] = await call_llm(key)
    return _response_cache[key]


# GOOD — Redis with TTL or LRU with max size
from cachetools import TTLCache
_cache: TTLCache = TTLCache(maxsize=1000, ttl=3600)


# GOOD — httpx client in lifespan, closed on shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.http_client = httpx.AsyncClient(timeout=30.0)
    yield
    await app.state.http_client.aclose()


# GOOD — handle streaming client disconnect
@router.post("/v1/chat/stream")
async def stream_chat(body: ChatRequest):
    async def generate():
        try:
            async for token in service.stream_reply(body.message):
                yield token
        except asyncio.CancelledError:
            logger.info("client_disconnected")
            raise

    return StreamingResponse(generate(), media_type="text/event-stream")
```

### Prevention

- [ ] No module-level mutable caches — use Redis with TTL
- [ ] HTTP clients created in lifespan, closed on shutdown
- [ ] Celery `worker_max_tasks_per_child = 100`
- [ ] Memory limit on containers with restart policy
- [ ] 24h soak test monitoring RSS before production launch

---

## 7. Circular Imports

### Symptoms

- `ImportError: cannot import name 'X' from partially initialized module`
- Import works in REPL but fails when running the app
- Adding a new file breaks unrelated modules
- `mypy` or IDE shows import cycles in dependency graph
- Tests fail with different import order than production
- Startup crash only in certain entry points (`workers/` vs `api/`)

### Root Cause

Module A imports B, B imports C, C imports A — Python cannot resolve the cycle. In AI backends, cycles often form when:

- `services/` imports from `api/deps.py`
- `models/` imports from `services/`
- `repositories/` imports from `schemas/`
- Type hints import concrete classes instead of `TYPE_CHECKING` forward refs

Cross-reference: [Production Project Structure for AI](production-project-structure-for-ai.md#import-rules-and-layer-boundaries).

### Diagnose

```bash
# Find import cycles
pip install grimp
grimp app --print-cycles

# Or manually trace
python -c "import app.main"
```

IDE tools (PyCharm, VS Code Pylance) highlight cyclic imports in the problems panel.

### Fix

```python
# BAD — service imports from api layer
# services/chat_service.py
from app.api.deps import get_settings  # CYCLE


# GOOD — service receives settings via constructor
# services/chat_service.py
class ChatService:
    def __init__(self, settings: Settings, ...) -> None:
        self._settings = settings


# BAD — runtime import for type hint
from app.services.rag_service import RAGService

def get_rag_service() -> RAGService: ...


# GOOD — TYPE_CHECKING forward reference
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.services.rag_service import RAGService

def get_rag_service() -> "RAGService": ...
```

| Strategy | When to Use |
|----------|-------------|
| Enforce layer boundaries | Always — see import rules table |
| `TYPE_CHECKING` imports | Type hints only |
| Move shared types to `models/domain/` | Both service and repo need same entity |
| Composition root in `dependencies.py` | Wiring without services importing api |
| Lazy import inside function | Last resort for optional dependencies |

### Prevention

- [ ] `grimp` or `import-linter` in CI enforcing layer contracts
- [ ] Code review: services never import from `api/`
- [ ] Shared entities in `models/domain/` — not in services or schemas
- [ ] Document import direction in [Production Project Structure for AI](production-project-structure-for-ai.md)

---

## 8. Bad Folder Structure

### Symptoms

- New engineers ask "where does this go?" every day
- `utils.py` at project root grows to 2000 lines
- Same logic duplicated in `main.py`, `helpers.py`, and `rag.py`
- Tests import production code through hacky `sys.path` manipulation
- Features cannot be owned by team — everything touches everything
- Import cycles proliferate
- LLM calls found in route handlers, workers, and scripts with no shared abstraction

### Root Cause

No agreed layout — files accumulate by convenience. Notebooks export code to random paths. "Just this once" shortcuts become permanent.

Cross-reference: [Production Project Structure for AI](production-project-structure-for-ai.md), [Software Engineering for AI](../foundations/software-engineering-for-ai.md#project-organization).

### Diagnose

```bash
# Flat structure indicators
ls -la app/ | wc -l  # too many files at one level
find app -name "utils.py" | wc -l  # multiple utils files
find app -maxdepth 1 -name "*.py" ! -name "__init__.py" | wc -l

# LLM calls outside services
rg "openai|anthropic|chat\.completions" app/ --glob '!services/*' --glob '!repositories/*'
```

Review onboarding time — if new engineers take a week to make a first PR, structure is likely the bottleneck.

### Fix

Migrate incrementally to the canonical layout:

```
app/
├── api/v1/          # Move all routes here
├── services/        # Extract logic from main.py
├── repositories/  # Extract SQL from services
├── schemas/         # Extract Pydantic models from routes
├── config/          # Extract hardcoded settings
└── workers/         # Extract background logic
```

```python
# Migration strategy — strangler fig
# 1. Create service with logic extracted from route
# 2. Route becomes thin wrapper
# 3. Delete old function from main.py
# 4. Repeat per endpoint — do not big-bang rewrite
```

### Prevention

- [ ] Adopt [Production Project Structure for AI](production-project-structure-for-ai.md) at project start
- [ ] PR template: "Which folder does new code belong in?"
- [ ] Reject PRs adding files to project root
- [ ] `CODEOWNERS` per folder for team boundaries
- [ ] Architecture review at 10th endpoint — before structure debt compounds

---

## 9. Hardcoded Config

### Symptoms

- API keys in git history — security scanner alerts
- "Works on my machine" — different behavior per developer
- Deploy to staging accidentally hits production LLM account
- Cannot change model name without code deploy
- Tests hit real OpenAI API and incur charges
- Feature flags require code change and redeploy

### Root Cause

Configuration values embedded in source code instead of environment variables loaded through a typed settings module.

```python
# The anti-pattern everyone starts with
client = OpenAI(api_key="sk-proj-...")
DATABASE_URL = "postgresql://user:pass@localhost/ai"
MODEL = "gpt-4o"  # changed 47 times in git blame
```

Cross-reference: [Configuration and Secrets](../foundations/configuration-and-secrets.md), [Production Project Structure for AI](production-project-structure-for-ai.md#config--configuration-management).

### Diagnose

```bash
# Secret scanning
rg "sk-[a-zA-Z0-9]{20,}" .
rg "postgresql://.*:.*@" app/
rg "api_key\s*=\s*['\"]" app/

# Pre-commit hook
pip install detect-secrets
detect-secrets scan
```

Check git history if keys were ever committed — rotate immediately.

### Fix

```python
# config/settings.py
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    openai_api_key: str
    database_url: str
    default_model: str = "gpt-4o"
    environment: str = "development"


# dependencies.py
@lru_cache
def get_settings() -> Settings:
    return Settings()


def get_llm(settings: Settings = Depends(get_settings)) -> AsyncOpenAI:
    return AsyncOpenAI(api_key=settings.openai_api_key)
```

```bash
# .env.example — committed, no real values
OPENAI_API_KEY=sk-your-key-here
DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/ai_backend
DEFAULT_MODEL=gpt-4o
ENVIRONMENT=development
```

| Config Type | Source |
|-------------|--------|
| Secrets | Environment variables / secret manager |
| Feature flags | Settings or external flag service |
| Model names | Settings with per-tenant override in DB |
| Connection strings | Environment only |

### Prevention

- [ ] `detect-secrets` in pre-commit hooks
- [ ] No string literals matching `sk-`, `postgresql://`, `redis://` in `app/`
- [ ] `.env` in `.gitignore`; `.env.example` committed
- [ ] Tests use `Settings` override with fake keys
- [ ] Secret rotation runbook documented

---

## 10. Missing Validation

### Symptoms

- LLM receives empty strings, null context, or malformed tool JSON
- Database constraint violations return 500 instead of 422
- `ValidationError` stack traces in production logs
- Prompt injection via unvalidated user input in system prompts
- Integer overflow on `top_k` or `max_tokens` parameters
- Unexpected types in API responses break frontend clients

### Root Cause

Input validation skipped at the HTTP boundary — raw dicts, unbounded query parameters, or manual parsing without Pydantic. Inner layers trust that input was validated.

Cross-reference: [FastAPI Complete Guide](../fastapi/fastapi-complete-guide.md), [API Design for AI](../apis/api-design-for-ai.md).

### Diagnose

```bash
# Routes accepting raw dicts
rg "dict\[str" app/api/
rg "@router\.(post|put)" app/api/ -A3 | rg -v "BaseModel|response_model"

# Fuzz testing
curl -X POST /v1/chat -d '{"message": ""}' -H "Content-Type: application/json"
curl -X POST /v1/chat -d '{"message": "'$(python -c 'print("x"*100000)')'"}' 
```

Check logs for `IntegrityError`, `ValidationError`, or LLM 400 errors with malformed input.

### Fix

```python
# BAD — no validation
@router.post("/v1/rag/query")
async def query(body: dict):
    return await rag_service.answer(body["query"], body.get("top_k", 5))


# GOOD — Pydantic validation at boundary
class RAGQueryRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=2000)
    top_k: int = Field(5, ge=1, le=20)
    include_sources: bool = True


class RAGQueryResponse(BaseModel):
    answer: str
    citations: list[Citation]
    model: str


@router.post("/v1/rag/query", response_model=RAGQueryResponse)
async def query(
    body: RAGQueryRequest,
    user: User = Depends(get_current_user),
    service: RAGService = Depends(get_rag_service),
) -> RAGQueryResponse:
    result = await service.answer(user.tenant_id, body.query, body.top_k)
    return RAGQueryResponse.from_domain(result)
```

| Validation Layer | Responsibility |
|------------------|----------------|
| Pydantic schemas | Type, length, range, format at HTTP boundary |
| Service layer | Business rules (quota, ownership, state transitions) |
| Database | Constraints as last resort — not primary validation |

### Prevention

- [ ] Every endpoint has request and response Pydantic models
- [ ] `Field()` constraints on all user-controlled strings and integers
- [ ] Fuzz tests for boundary values (empty, max length, negative numbers)
- [ ] Custom validators for domain-specific rules (slug format, enum values)
- [ ] Never use `dict` or `Any` as request body type in production routes

---

## 11. Weak Auth

### Symptoms

- User A accesses user B's chat sessions by changing `session_id`
- Tenant A retrieves tenant B's documents by guessing UUIDs
- API endpoints work without `Authorization` header
- JWT never expires — stolen tokens valid forever
- Admin endpoints accessible to regular users
- API keys logged in plaintext
- RAG vector search returns cross-tenant results

### Root Cause

Authentication (who are you) and authorization (what can you do) are missing, optional, or not enforced at the data layer. AI backends expose powerful operations — document access, agent tool execution, LLM quota — that amplify auth failures.

Cross-reference: [Authentication and Authorization for AI](../security/authentication-authorization-for-ai.md), [AI Backend Reference Architecture](ai-backend-reference-architecture.md#architecture-4-ai-saas-backend).

### Diagnose

```bash
# Endpoints without auth dependency
rg "@router\.(get|post|put|delete)" app/api/ -A5 | rg -v "Depends|get_current"

# Queries without tenant filter
rg "select\(" app/repositories/ -i | rg -v "tenant_id"

# JWT config
rg "expire|ACCESS_TOKEN" app/auth/
```

Penetration test: obtain user A token, request user B resources. Attempt unauthenticated access to every endpoint.

### Fix

```python
# BAD — user-controlled ID with no ownership check
@router.get("/v1/sessions/{session_id}")
async def get_session(session_id: str):
    return await repo.get_messages(session_id)


# GOOD — auth + ownership enforced in service
@router.get("/v1/sessions/{session_id}", response_model=SessionResponse)
async def get_session(
    session_id: str,
    user: User = Depends(get_current_user),
    service: ChatService = Depends(get_chat_service),
) -> SessionResponse:
    return await service.get_session(user.id, session_id)


# Service enforces ownership
class ChatService:
    async def get_session(self, user_id: str, session_id: str) -> Session:
        session = await self._repo.get_session(session_id)
        if session is None or session.user_id != user_id:
            raise NotFoundError("session", session_id)
        return session
```

| Layer | Auth Responsibility |
|-------|---------------------|
| `auth/dependencies.py` | Token validation, user resolution |
| Service layer | Resource ownership checks |
| Repository layer | `tenant_id` filter on every query |
| Vector store | Metadata filter `tenant_id` on every search |

### Prevention

- [ ] Every endpoint except `/health` requires authentication
- [ ] Integration tests for cross-tenant access (must return 404, not 403 with data leak)
- [ ] JWT with short expiry + refresh token rotation
- [ ] API keys hashed in database — never stored plaintext
- [ ] Security review before multi-tenant launch

---

## 12. Improper Error Handling

### Symptoms

- Clients receive raw Python tracebacks in JSON responses
- All errors return HTTP 500 — clients cannot distinguish retryable failures
- LLM timeout crashes the request with unhandled exception
- Logs contain no `request_id` — impossible to correlate user report to trace
- Sensitive data (SQL, API keys) in error messages
- Silent failures — ingestion marked complete but vectors not indexed
- Frontend shows "Internal Server Error" with no actionable code

### Root Cause

No structured exception hierarchy, no global exception handlers, and bare `except Exception` blocks that swallow errors or re-raise as generic 500.

Cross-reference: [Logging and Error Handling](../logging/logging-and-error-handling.md), [Backend Architecture for AI](backend-architecture-for-ai.md).

### Diagnose

```bash
# Bare except blocks
rg "except:" app/ --glob '!tests/*'
rg "except Exception" app/ -A2 | rg "pass$"

# Missing exception handlers
rg "exception_handler|@app\.exception_handler" app/

# Test error responses
curl -X POST /v1/chat -H "Authorization: Bearer invalid" -w "%{http_code}"
curl -X GET /v1/documents/nonexistent-id -w "%{http_code}"
```

Review production error logs — if stack traces appear in client-facing JSON, handlers are missing.

### Fix

```python
# core/exceptions.py
class AppError(Exception):
    def __init__(self, message: str, code: str = "internal_error") -> None:
        self.message = message
        self.code = code
        super().__init__(message)

class NotFoundError(AppError):
    def __init__(self, resource: str, id: str) -> None:
        super().__init__(f"{resource} not found", code="not_found")

class LLMTimeoutError(AppError):
    def __init__(self) -> None:
        super().__init__("LLM request timed out", code="llm_timeout")


# core/error_handlers.py
@app.exception_handler(AppError)
async def app_error_handler(request: Request, exc: AppError) -> JSONResponse:
    status = 404 if exc.code == "not_found" else 400
    if exc.code == "llm_timeout":
        status = 504
    return JSONResponse(
        status_code=status,
        content={
            "error": {
                "code": exc.code,
                "message": exc.message,
                "request_id": request.state.request_id,
            }
        },
    )


@app.exception_handler(Exception)
async def unhandled_handler(request: Request, exc: Exception) -> JSONResponse:
    logger.exception("unhandled_error", request_id=request.state.request_id)
    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "code": "internal_error",
                "message": "An unexpected error occurred",
                "request_id": request.state.request_id,
            }
        },
    )
```

| Error Type | HTTP Status | Client Action |
|------------|-------------|---------------|
| Validation failure | 422 | Fix request body |
| Not found | 404 | Stop retrying |
| Auth failure | 401 | Refresh token |
| Rate limit | 429 | Backoff and retry |
| LLM timeout | 504 | Retry with backoff |
| Quota exceeded | 402/403 | Upgrade plan |

### Prevention

- [ ] Typed exception hierarchy in `core/exceptions.py`
- [ ] Global handlers registered in `create_app()` — never expose tracebacks in production
- [ ] `request_id` in every error response and log line
- [ ] LLM calls wrapped with timeout and mapped to `LLMTimeoutError`
- [ ] Test suite asserting status codes and error body shape for each failure mode

---

## Diagnostic Toolkit

Quick reference for production investigations:

| Symptom Domain | Tool / Query |
|----------------|--------------|
| Event loop blocking | `PYTHONASYNCIODEBUG=1`, `py-spy` |
| DB connections | `pg_stat_activity`, pool `echo_pool=True` |
| Slow queries | `EXPLAIN ANALYZE`, slow query log |
| Memory growth | `mprof`, `tracemalloc`, container RSS graph |
| Import cycles | `grimp`, `import-linter` |
| Secret leakage | `detect-secrets`, `rg "sk-"` |
| Auth gaps | Unauthenticated `curl` against all endpoints |
| API contract | OpenAPI diff between releases |

```mermaid
flowchart TD
    SLOW[High Latency] --> Q1{All endpoints<br/>or one?}
    Q1 -->|All| BLOCK[Check blocking async]
    Q1 -->|One| Q2{DB or LLM?}
    Q2 -->|DB| INDEX[Check indexes + EXPLAIN]
    Q2 -->|LLM| TIMEOUT[Check timeout + payload size]
    SLOW --> POOL[Check connection pool]

    OOM[Memory Growth] --> CACHE[Check global caches]
    OOM --> CLIENT[Check httpx client lifecycle]
    OOM --> STREAM[Check streaming disconnect handling]

    ERR[500 Errors] --> TRACE[Check logs for request_id]
    ERR --> VALID[Check validation errors]
    ERR --> HANDLER[Check exception handlers]
```

---

## Pre-Production Checklist

Before launching an AI backend to production:

- [ ] No blocking I/O in async handlers — [§1](#1-blocking-async)
- [ ] All DB sessions use yield dependency — [§2](#2-session-leaks)
- [ ] `EXPLAIN ANALYZE` on all production queries — [§3](#3-missing-indexes)
- [ ] Versioned API with typed request/response models — [§4](#4-poor-api-design), [§10](#10-missing-validation)
- [ ] Payload size limits at proxy, schema, and LLM context layers — [§5](#5-large-payloads)
- [ ] No unbounded in-memory caches — [§6](#6-memory-leaks)
- [ ] Import layer contracts enforced — [§7](#7-circular-imports)
- [ ] Canonical folder structure adopted — [§8](#8-bad-folder-structure)
- [ ] All config via `Settings` — no secrets in code — [§9](#9-hardcoded-config)
- [ ] Auth on every endpoint; tenant scoping in repositories — [§11](#11-weak-auth)
- [ ] Structured error responses with `request_id` — [§12](#12-improper-error-handling)
- [ ] Load test: 50 concurrent users, 24h soak test
- [ ] Cross-tenant access integration tests pass

---

## Interview Preparation

**Q1: Your chat API works locally but times out at 50 concurrent users. Walk through diagnosis.**

> **Strong answer:** Check for blocking calls in async handlers first (sync OpenAI SDK, `requests`, PDF parsing). Then connection pool exhaustion (session leaks). Then reverse proxy timeouts. Mention `PYTHONASYNCIODEBUG`, load testing, and `pg_stat_activity`. Reference [§1](#1-blocking-async) and [§2](#2-session-leaks).

**Q2: How do you prevent cross-tenant data leaks in a RAG system?**

> **Strong answer:** `tenant_id` on every PostgreSQL query in repositories. Metadata filter on every vector search. Auth dependency resolves tenant. Integration tests attempt cross-tenant access. Reference [§11](#11-weak-auth) and [AI SaaS Architecture](ai-backend-reference-architecture.md#architecture-4-ai-saas-backend).

**Q3: What belongs in Pydantic schemas vs the service layer for validation?**

> **Strong answer:** Schemas validate type, length, range at HTTP boundary (422). Services validate business rules — ownership, quota, state transitions. Database constraints are last resort. Reference [§10](#10-missing-validation).

---

## Navigation

### Prerequisites

- [Backend Fundamentals for AI](backend-fundamentals-for-ai.md) — foundational patterns these mistakes violate
- [Async Programming for AI Backends](async-programming-for-ai-backends.md) — event loop depth for §1
- [Production Project Structure for AI](production-project-structure-for-ai.md) — structural fixes for §7, §8

### Related Topics

- [Common Engineering Mistakes](../common-mistakes/common-engineering-mistakes.md) — broader engineering anti-patterns
- [AI Backend Reference Architecture](ai-backend-reference-architecture.md) — where components fail at runtime
- [Backend Architecture for AI](backend-architecture-for-ai.md) — architectural patterns that prevent these mistakes
- [Logging and Error Handling](../logging/logging-and-error-handling.md) — §12 depth

### Next Topics

- [Background Processing for AI](background-processing-for-ai.md) — offload work that causes §1, §5, §6
- [PostgreSQL for AI](../databases/postgresql/postgresql-for-ai.md) — §2, §3 database depth
- [Authentication and Authorization for AI](../security/authentication-authorization-for-ai.md) — §11 depth

### Future Reading

- [Production Incidents](../production-incidents/README.md) — real incident postmortems
- [Debugging](../debugging/README.md) — general debugging methodology
- [Performance Optimization](../performance-optimization/README.md) — after structural fixes

---

## See Also

- [Production Project Structure for AI](production-project-structure-for-ai.md)
- [AI Backend Reference Architecture](ai-backend-reference-architecture.md)
- [Backend Architecture for AI](backend-architecture-for-ai.md)
- [Common Engineering Mistakes](../common-mistakes/common-engineering-mistakes.md)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial Phase 3 release — 12 mistake categories with full troubleshooting structure |
