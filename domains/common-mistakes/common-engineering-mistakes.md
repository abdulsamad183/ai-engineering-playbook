---
title: "Common Engineering Mistakes in AI Applications"
description: "Production reference guide to the engineering mistakes that sink AI demos — overengineering, coupling, API design, testing gaps, secrets, and AI-specific pitfalls — with bad vs good code examples and cross-links to Phase 2 foundations."
domain: common-mistakes
tags: [foundations, debugging, production, intermediate]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../foundations/ai-engineering-overview.md
  - ../foundations/software-engineering-for-ai.md
  - ../python-engineering/python-for-ai-engineering.md
  - ../apis/http-fundamentals-for-ai.md
  - ../backend-engineering/backend-fundamentals-for-ai.md
  - ../fastapi/fastapi-foundation.md
  - ../databases/databases-for-ai-applications.md
keywords: [overengineering, tight coupling, API design, DRY, logging, testing, performance, secrets, project structure, AI engineering mistakes, production]
author: hp
---

# Common Engineering Mistakes in AI Applications

> A production reference guide to the engineering mistakes that turn AI prototypes into unmaintainable, fragile, and expensive systems — with root causes, impact, fixes, and code examples.

## Table of Contents

- [How to Use This Guide](#how-to-use-this-guide)
- [Mistake Severity Matrix](#mistake-severity-matrix)
- [1. Overengineering](#1-overengineering)
- [2. Tight Coupling](#2-tight-coupling)
- [3. Poor API Design](#3-poor-api-design)
- [4. Duplicated Code](#4-duplicated-code)
- [5. Missing Logging](#5-missing-logging)
- [6. Missing Tests](#6-missing-tests)
- [7. Ignoring Performance](#7-ignoring-performance)
- [8. Poor Folder Organization](#8-poor-folder-organization)
- [9. Hardcoded Secrets](#9-hardcoded-secrets)
- [10. LLM Logic in Route Handlers](#10-llm-logic-in-route-handlers)
- [11. No Provider Abstraction](#11-no-provider-abstraction)
- [12. Blocking I/O in Async Handlers](#12-blocking-io-in-async-handlers)
- [13. Untyped Boundaries](#13-untyped-boundaries)
- [14. No Configuration Management](#14-no-configuration-management)
- [15. Ignoring LLM Failure Modes](#15-ignoring-llm-failure-modes)
- [16. No Cost or Rate Controls](#16-no-cost-or-rate-controls)
- [17. PII and Secrets in Logs](#17-pii-and-secrets-in-logs)
- [18. Notebook Patterns in Production](#18-notebook-patterns-in-production)
- [19. No Evaluation for AI Outputs](#19-no-evaluation-for-ai-outputs)
- [20. Prompts as Inline Strings](#20-prompts-as-inline-strings)
- [Pre-Production Mistake Checklist](#pre-production-mistake-checklist)
- [Interview Preparation](#interview-preparation)
- [Navigation](#navigation)

---

## How to Use This Guide

This document is a **production reference**, not a style opinion piece. Each mistake follows the same structure:

| Section | Purpose |
|---------|---------|
| **Why it happens** | The cognitive or organizational pressure that causes the mistake |
| **Impact** | What breaks in development, operations, or interviews |
| **How to avoid** | Concrete engineering practices with links to foundation docs |
| **Bad vs good** | Minimal code examples showing the fix |

Cross-references point to Phase 2 foundation material:

| Foundation Doc | What It Covers |
|----------------|----------------|
| [AI Engineering Overview](../foundations/ai-engineering-overview.md) | Role scope, lifecycle, production principles |
| [Software Engineering for AI](../foundations/software-engineering-for-ai.md) | Clean architecture, SOLID, layered design |
| [Python for AI Engineering](../python-engineering/python-for-ai-engineering.md) | Typing, async, logging, project layout |
| [HTTP Fundamentals for AI](../apis/http-fundamentals-for-ai.md) | REST, auth, status codes, streaming |
| [Backend Fundamentals for AI](../backend-engineering/backend-fundamentals-for-ai.md) | Middleware, DI, async patterns |
| [FastAPI Foundation](../fastapi/fastapi-foundation.md) | Routers, lifespan, testing, deployment |
| [Databases for AI Applications](../databases/databases-for-ai-applications.md) | Store selection, pooling, migrations |

> **Production Standard:** Most AI production incidents trace to engineering discipline failures, not model quality. Fix the system around the model first.

---

## Mistake Severity Matrix

Use this matrix to prioritize remediation during code review or incident postmortems.

| Mistake | Dev Velocity | Production Risk | Security Risk | Cost Risk |
|---------|-------------|-----------------|---------------|-----------|
| Hardcoded secrets | Low | High | **Critical** | Medium |
| PII in logs | Low | High | **Critical** | Low |
| Missing tests | High | High | Medium | Medium |
| LLM logic in routes | Medium | High | Medium | Medium |
| No provider abstraction | Medium | High | Low | High |
| Blocking I/O in async | Low | **Critical** | Low | Medium |
| No cost controls | Low | Medium | Low | **Critical** |
| Overengineering | **Critical** | Medium | Low | Low |
| Poor API design | Medium | High | Medium | Low |
| Missing logging | Medium | **Critical** | Medium | Medium |

---

## 1. Overengineering

### Why it happens

Engineers anticipate scale that does not exist yet, copy enterprise patterns from blog posts, or build abstraction layers before a second use case appears. In AI projects, framework churn amplifies this — teams scaffold multi-agent orchestration before a single RAG query works reliably.

### Impact

- Weeks spent on infrastructure instead of product validation
- New contributors cannot navigate the codebase
- Simple changes require touching five layers
- Interview red flag: "We built a plugin system for two prompts"

### How to avoid

- **YAGNI** — build for today's requirements; extract abstractions when duplication appears twice
- Start with [layered architecture](../foundations/software-engineering-for-ai.md#layered-architecture), not microservices
- Ship a vertical slice (one endpoint, one flow) before generalizing
- Revisit architecture at defined milestones, not on day one

See [Software Engineering for AI — Modular Design](../foundations/software-engineering-for-ai.md#modular-design).

### Bad vs good

```python
# BAD — abstraction before need
class AbstractEmbeddingStrategyFactory(ABC):
    @abstractmethod
    def create_strategy(self, config: EmbeddingConfig) -> EmbeddingStrategy: ...

class OpenAIEmbeddingStrategyFactory(AbstractEmbeddingStrategyFactory):
    def create_strategy(self, config: EmbeddingConfig) -> EmbeddingStrategy:
        return OpenAIEmbeddingStrategy(config)

# GOOD — direct implementation until a second provider is required
async def embed_texts(client: AsyncOpenAI, texts: list[str]) -> list[list[float]]:
    response = await client.embeddings.create(
        model="text-embedding-3-small",
        input=texts,
    )
    return [item.embedding for item in response.data]
```

---

## 2. Tight Coupling

### Why it happens

Fast prototypes inline dependencies — OpenAI SDK calls inside route handlers, raw SQL in services, Redis keys scattered across modules. Speed feels justified; coupling compounds silently.

### Impact

- Cannot swap LLM providers without rewriting routes
- Unit tests require live APIs or databases
- One team's schema change breaks another's feature
- Refactoring cost grows superlinearly with codebase size

### How to avoid

- Apply [dependency inversion](../foundations/software-engineering-for-ai.md#dependency-injection) — services depend on interfaces, not SDKs
- Use [FastAPI dependency injection](../fastapi/fastapi-foundation.md#dependency-injection-patterns) at the composition root
- Keep domain logic free of framework imports
- One direction of dependency: outer layers → inner layers only

### Bad vs good

```python
# BAD — route handler coupled to OpenAI SDK and vector DB client
@router.post("/chat")
async def chat(query: str):
    client = AsyncOpenAI(api_key="sk-...")
    embedding = await client.embeddings.create(model="text-embedding-3-small", input=query)
    results = pinecone_index.query(vector=embedding.data[0].embedding, top_k=5)
    completion = await client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": f"Context: {results}\n\n{query}"}],
    )
    return {"answer": completion.choices[0].message.content}


# GOOD — route delegates to injected service; service depends on ports
@router.post("/chat", response_model=ChatResponse)
async def chat(
    body: ChatRequest,
    rag_service: RAGService = Depends(get_rag_service),
) -> ChatResponse:
    return await rag_service.answer(body.query)
```

---

## 3. Poor API Design

### Why it happens

APIs are treated as internal glue, designed around the current frontend screen rather than resources. AI endpoints often expose raw prompt strings, model names, and internal retrieval scores to clients.

### Impact

- Breaking changes on every UI iteration
- Clients must understand LLM internals
- No versioning path when models change
- Security exposure of implementation details

### How to avoid

- Follow [REST principles](../apis/http-fundamentals-for-ai.md#rest-principles) and [HTTP status codes](../apis/http-fundamentals-for-ai.md#http-status-codes)
- Design resource-oriented endpoints (`POST /v1/conversations/{id}/messages`)
- Use [API versioning](../apis/http-fundamentals-for-ai.md#api-versioning) from day one
- Return stable response schemas; hide model and retrieval internals
- Document via OpenAPI — see [FastAPI Foundation](../fastapi/fastapi-foundation.md#api-documentation)

### Bad vs good

```python
# BAD — leaky, unversioned, wrong status codes
@router.post("/ask")
async def ask(data: dict):
    try:
        result = do_rag(data["q"])
        return result
    except Exception as e:
        return {"error": str(e)}  # always 200


# GOOD — versioned, typed, correct errors
@router.post("/v1/conversations/{conversation_id}/messages", response_model=MessageResponse)
async def create_message(
    conversation_id: UUID,
    body: CreateMessageRequest,
    service: ConversationService = Depends(get_conversation_service),
) -> MessageResponse:
    try:
        return await service.send_message(conversation_id, body.content)
    except ConversationNotFoundError:
        raise HTTPException(status_code=404, detail="Conversation not found")
    except LLMProviderError as exc:
        raise HTTPException(status_code=502, detail="Upstream model unavailable") from exc
```

---

## 4. Duplicated Code

### Why it happens

Copy-paste is faster than extracting shared utilities, especially across notebooks, scripts, and API code. Prompt templates, retry logic, and embedding calls get duplicated per feature.

### Impact

- Bug fixes must be applied in multiple places (and one is always missed)
- Inconsistent behavior across endpoints
- Token counting, retry, and redaction logic diverges
- Test coverage gaps in duplicated paths

### How to avoid

- Extract shared logic into `domain/` services or `infrastructure/` clients
- Centralize prompts in `domain/prompts/` — see [Software Engineering for AI](../foundations/software-engineering-for-ai.md#production-considerations)
- Use [reusable utilities](../python-engineering/python-for-ai-engineering.md#reusable-utilities) for cross-cutting concerns
- Apply DRY at the **behavior** level, not just the syntax level

### Bad vs good

```python
# BAD — retry logic duplicated in every LLM call site
async def summarize(text: str) -> str:
    for attempt in range(3):
        try:
            return await openai_client.chat.completions.create(...)
        except RateLimitError:
            await asyncio.sleep(2 ** attempt)

async def classify(text: str) -> str:
    for attempt in range(3):
        try:
            return await openai_client.chat.completions.create(...)
        except RateLimitError:
            await asyncio.sleep(2 ** attempt)


# GOOD — single retry wrapper, reused everywhere
async def with_retry(coro_factory: Callable[[], Awaitable[T]], max_attempts: int = 3) -> T:
    for attempt in range(max_attempts):
        try:
            return await coro_factory()
        except RateLimitError:
            if attempt == max_attempts - 1:
                raise
            await asyncio.sleep(2 ** attempt)
    raise RuntimeError("unreachable")
```

---

## 5. Missing Logging

### Why it happens

`print()` works in development. Structured logging feels like overhead until the first 3 a.m. page. AI systems add complexity — token usage, retrieval latency, model version — that is invisible without intentional instrumentation.

### Impact

- Incidents take hours instead of minutes to diagnose
- Cannot correlate user reports with request traces
- No data for cost attribution or quality regression
- Compliance failures when audit trails are absent

### How to avoid

- Use Python `logging` with structured JSON in production — see [Python for AI Engineering — Logging](../python-engineering/python-for-ai-engineering.md#logging)
- Log at service boundaries: request ID, user ID (hashed), latency, token counts, model ID
- Never log raw prompts containing PII — see [§17](#17-pii-and-secrets-in-logs)
- Correlate logs with [observability](../observability/README.md) traces

### Bad vs good

```python
# BAD — silent failures, no correlation
async def answer(query: str) -> str:
    chunks = await retriever.search(query)
    response = await llm.complete(build_prompt(chunks, query))
    return response.content


# GOOD — structured, correlatable, production-safe
logger = logging.getLogger(__name__)

async def answer(query: str, request_id: str) -> str:
    start = time.perf_counter()
    logger.info(
        "rag_query_started",
        extra={"request_id": request_id, "query_length": len(query)},
    )
    chunks = await retriever.search(query)
    logger.info(
        "rag_retrieval_complete",
        extra={
            "request_id": request_id,
            "chunk_count": len(chunks),
            "retrieval_ms": (time.perf_counter() - start) * 1000,
        },
    )
    response = await llm.complete(build_prompt(chunks, query))
    logger.info(
        "rag_query_complete",
        extra={
            "request_id": request_id,
            "model": response.model,
            "input_tokens": response.input_tokens,
            "output_tokens": response.output_tokens,
            "total_ms": (time.perf_counter() - start) * 1000,
        },
    )
    return response.content
```

---

## 6. Missing Tests

### Why it happens

LLM outputs are non-deterministic, so teams conclude "you cannot test AI." They skip unit tests for orchestration logic and ship without contract tests for APIs.

### Impact

- Refactoring breaks production silently
- Provider SDK upgrades cause undetected regressions
- No safety net for prompt or retrieval changes
- Interview failure: cannot explain test strategy for AI systems

### How to avoid

- Test **orchestration**, not exact LLM strings — see [Testing Philosophy](../foundations/software-engineering-for-ai.md#testing-philosophy)
- Mock LLM ports in unit tests; use [FastAPI TestClient](../fastapi/fastapi-foundation.md#testing-fastapi-ai-services) for API contracts
- Add evaluation harnesses for quality (separate from unit tests) — Phase 4+
- Run tests in CI on every PR

### Bad vs good

```python
# BAD — no tests; manual curl verification only
# (entire service untested)


# GOOD — unit test with mocked LLM port
@pytest.fixture
def mock_llm() -> LLMClient:
    client = AsyncMock(spec=LLMClient)
    client.complete.return_value = LLMResponse(
        content="Paris is the capital of France.",
        model="gpt-4o",
        input_tokens=50,
        output_tokens=10,
    )
    return client


@pytest.mark.asyncio
async def test_rag_service_calls_retriever_and_llm(mock_llm: LLMClient):
    retriever = AsyncMock()
    retriever.search.return_value = [DocumentChunk(text="France info", score=0.9)]
    service = RAGService(retriever=retriever, llm=mock_llm)

    result = await service.answer("What is the capital of France?")

    retriever.search.assert_called_once_with("What is the capital of France?")
    mock_llm.complete.assert_called_once()
    assert "Paris" in result.content
```

---

## 7. Ignoring Performance

### Why it happens

Demos run on a laptop with one user. Production brings concurrent requests, cold starts, N+1 database queries, and synchronous embedding calls inside async handlers.

### Impact

- p95 latency exceeds user tolerance (especially for streaming chat)
- Event loop blocking stalls all concurrent requests
- Database connection exhaustion under load
- LLM costs spike from redundant calls with no caching

### How to avoid

- Keep I/O async at the framework layer — see [Async Programming](../python-engineering/python-for-ai-engineering.md#async-programming)
- Cache LLM responses and embeddings where safe — see [Redis for AI](../databases/redis/redis-for-ai.md)
- Use [connection pooling](../databases/databases-for-ai-applications.md#connection-pooling) for PostgreSQL
- Profile before optimizing; measure p50/p95/p99 latency
- Offload CPU-bound work (PDF parsing, large embedding batches) to workers

### Bad vs good

```python
# BAD — blocking call inside async handler freezes the event loop
@router.post("/embed")
async def embed_documents(files: list[UploadFile]):
    texts = []
    for f in files:
        texts.append(parse_pdf(f.file.read()))  # CPU-bound, blocking
    embeddings = openai_client.embeddings.create(input=texts, model="...")  # sync SDK
    return embeddings


# GOOD — async I/O, CPU work offloaded
@router.post("/embed")
async def embed_documents(
    files: list[UploadFile],
    embedding_service: EmbeddingService = Depends(get_embedding_service),
):
  texts = await asyncio.gather(*[
      asyncio.to_thread(parse_pdf, (await f.read()))
      for f in files
  ])
  return await embedding_service.embed_batch(texts)
```

---

## 8. Poor Folder Organization

### Why it happens

Files accumulate at the repository root (`main.py`, `utils.py`, `helpers.py`, `rag.py`, `prompts.py`). Notebooks export code into random paths. No one agrees on where new code belongs.

### Impact

- Import cycles and circular dependencies
- Onboarding takes days instead of hours
- Features cannot be owned by team boundaries
- Tests mirror production chaos

### How to avoid

- Adopt [project organization](../foundations/software-engineering-for-ai.md#project-organization) from [Software Engineering for AI](../foundations/software-engineering-for-ai.md)
- Follow [FastAPI project structure](../fastapi/fastapi-foundation.md#project-structure)
- Use [Python project layouts](../python-engineering/python-for-ai-engineering.md#project-layouts-for-ai-applications) with `src/` layout
- Enforce boundaries: `api/` → `services/` → `domain/` → `infrastructure/`

### Bad vs good

```text
# BAD — flat, ambiguous
my-ai-app/
├── main.py
├── utils.py
├── rag.py
├── openai_stuff.py
├── test.py
└── prompts.txt


# GOOD — layered, navigable
my-ai-app/
├── src/
│   └── my_ai_app/
│       ├── api/
│       │   ├── routes/
│       │   └── dependencies.py
│       ├── domain/
│       │   ├── models/
│       │   ├── ports/
│       │   └── prompts/
│       ├── services/
│       └── infrastructure/
│           ├── llm/
│           ├── db/
│           └── cache/
├── tests/
│   ├── unit/
│   └── integration/
└── pyproject.toml
```

---

## 9. Hardcoded Secrets

### Why it happens

API keys in source code ship the fastest. `.env` files get committed. Keys appear in notebooks, example scripts, and CI logs.

### Impact

- **Critical security incident** — key rotation, billing fraud, data breach
- Keys in git history persist after deletion
- Different environments share the same credentials
- Compliance violations (SOC 2, GDPR processor requirements)

### How to avoid

- Load secrets from environment variables or a secrets manager at startup
- Never commit `.env` — use `.env.example` with placeholder values
- Use [HTTP authentication patterns](../apis/http-fundamentals-for-ai.md#authentication) for inbound API security
- Scan repositories with secret detection in CI
- Rotate keys immediately if exposed

### Bad vs good

```python
# BAD — secret in source code
client = AsyncOpenAI(api_key="sk-proj-abc123realkeyhere")


# GOOD — config from environment, validated at startup
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    database_url: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()  # fails fast if OPENAI_API_KEY missing
client = AsyncOpenAI(api_key=settings.openai_api_key)
```

---

## 10. LLM Logic in Route Handlers

### Why it happens

FastAPI makes it easy to write an endpoint in ten lines. RAG pipelines grow inside that endpoint because "it's just one file."

### Impact

- Routes become untestable god functions
- Cannot reuse logic from CLI, workers, or agents
- OpenAPI docs describe implementation, not contracts
- Violates [separation of concerns](../foundations/software-engineering-for-ai.md#separation-of-concerns)

### How to avoid

- Routes validate input, call services, map exceptions to HTTP errors
- AI orchestration lives in `services/` or `domain/`
- See [Backend Fundamentals](../backend-engineering/backend-fundamentals-for-ai.md) and [FastAPI Foundation](../fastapi/fastapi-foundation.md)

### Bad vs good

```python
# BAD — 80 lines of RAG in a route (truncated)
@router.post("/query")
async def query(body: dict):
    # chunking, embedding, retrieval, prompting, LLM call, parsing...
    ...


# GOOD — thin route
@router.post("/v1/query", response_model=QueryResponse)
async def query(
    body: QueryRequest,
    service: QueryService = Depends(get_query_service),
) -> QueryResponse:
    return await service.execute(body)
```

---

## 11. No Provider Abstraction

### Why it happens

The team standardizes on one LLM vendor. Abstraction feels premature until the vendor has an outage, raises prices, or deprecates a model.

### Impact

- Provider outage = full application outage
- Cannot A/B test models without code changes
- Vendor pricing changes are forced migrations under fire
- Testing requires live API calls

### How to avoid

- Define an `LLMClient` port in the domain layer — see [Software Engineering for AI](../foundations/software-engineering-for-ai.md#clean-architecture)
- Implement adapters per provider in `infrastructure/llm/`
- Inject the client via [dependency injection](../fastapi/fastapi-foundation.md#dependency-injection-patterns)
- Configure default and fallback models via environment

### Bad vs good

```python
# BAD — OpenAI types leak into domain
from openai import AsyncOpenAI

async def generate_summary(text: str) -> str:
    client = AsyncOpenAI()
    resp = await client.chat.completions.create(model="gpt-4o", messages=[...])
    return resp.choices[0].message.content


# GOOD — domain port, infrastructure adapter
# domain/ports/llm.py
class LLMClient(ABC):
    @abstractmethod
    async def complete(self, prompt: str, system: str = "") -> LLMResponse: ...

# infrastructure/llm/openai_adapter.py
class OpenAILLMClient(LLMClient):
    def __init__(self, client: AsyncOpenAI, model: str) -> None:
        self._client = client
        self._model = model

    async def complete(self, prompt: str, system: str = "") -> LLMResponse:
        ...
```

---

## 12. Blocking I/O in Async Handlers

### Why it happens

Many SDKs are synchronous. Developers call them directly inside `async def` endpoints, not realizing they block the entire event loop.

### Impact

- Throughput collapses under concurrent load
- Health checks fail while one request parses a PDF
- Latency spikes are misattributed to the LLM provider
- Production incidents that do not reproduce locally

### How to avoid

- Use async-native clients (`AsyncOpenAI`, `asyncpg`, `redis.asyncio`)
- Wrap unavoidable sync calls with `asyncio.to_thread()` or a process pool
- See [Async Endpoints](../backend-engineering/backend-fundamentals-for-ai.md#async-endpoints) and [Concurrency](../python-engineering/python-for-ai-engineering.md#concurrency-and-multiprocessing)

### Bad vs good

```python
# BAD
@router.get("/health")
async def health():
    result = sync_redis_client.ping()  # blocks event loop
    return {"redis": result}


# GOOD
@router.get("/health")
async def health(redis: Redis = Depends(get_redis)):
    result = await redis.ping()
    return {"redis": result}
```

---

## 13. Untyped Boundaries

### Why it happens

Python allows `dict` and `Any` everywhere. JSON from LLMs is parsed loosely. Type errors surface at runtime in production.

### Impact

- `KeyError` and `AttributeError` in production paths
- IDE and mypy cannot catch integration mistakes
- API contract drift between frontend and backend
- Refactoring is guesswork

### How to avoid

- Use [Pydantic models](../python-engineering/python-for-ai-engineering.md#pydantic) at API and LLM output boundaries
- Enable mypy or pyright on `src/`
- Parse LLM JSON into typed models, not raw dicts
- See [Pydantic Models for AI APIs](../fastapi/fastapi-foundation.md#pydantic-models-for-ai-apis)

### Bad vs good

```python
# BAD
async def extract_entities(text: str) -> dict:
    raw = await llm.complete(f"Extract entities as JSON: {text}")
    return json.loads(raw.content)  # hope the shape is right


# GOOD
class Entity(BaseModel):
    name: str
    type: str

class EntityExtractionResult(BaseModel):
    entities: list[Entity]

async def extract_entities(text: str) -> EntityExtractionResult:
    raw = await llm.complete(
        f"Extract entities as JSON matching schema: {EntityExtractionResult.model_json_schema()}"
    )
    return EntityExtractionResult.model_validate_json(raw.content)
```

---

## 14. No Configuration Management

### Why it happens

Magic numbers and model names are scattered across files. Environment-specific behavior is managed with `if os.getenv("ENV") == "prod"` inline.

### Impact

- Staging does not mirror production configuration
- Model or temperature changes require code deploys
- Cannot tune retrieval `top_k` or timeouts without a release
- Rollback does not restore configuration state

### How to avoid

- Centralize settings in a `Settings` class (Pydantic Settings)
- Separate config from code — see [Configuration Management](../foundations/software-engineering-for-ai.md#configuration-management)
- Document all environment variables in deployment guides
- Use feature flags for gradual rollout, not hardcoded booleans

### Bad vs good

```python
# BAD
TOP_K = 5
MODEL = "gpt-4o"
TEMPERATURE = 0.7  # duplicated in three files


# GOOD
class RAGSettings(BaseSettings):
    retrieval_top_k: int = 5
    llm_model: str = "gpt-4o"
    llm_temperature: float = 0.7
    llm_timeout_seconds: float = 30.0

    model_config = SettingsConfigDict(env_prefix="RAG_")
```

---

## 15. Ignoring LLM Failure Modes

### Why it happens

Happy-path development assumes the LLM provider always returns 200 in under two seconds. Timeouts, rate limits, and malformed JSON are discovered in production.

### Impact

- Unhandled exceptions become 500 errors with stack traces
- Retry storms amplify outages
- Users see hung requests with no feedback
- No fallback when primary model is unavailable

### How to avoid

- Implement retries with exponential backoff for transient errors
- Set explicit timeouts on every external call
- Map provider errors to stable API errors — see [Error Handling](../fastapi/fastapi-foundation.md#error-handling)
- Configure fallback models and degraded responses
- See [HTTP status codes for upstream failures](../apis/http-fundamentals-for-ai.md#http-status-codes) (502, 503, 429)

### Bad vs good

```python
# BAD
async def complete(prompt: str) -> str:
    response = await client.chat.completions.create(model="gpt-4o", messages=[...])
    return response.choices[0].message.content


# GOOD
async def complete(prompt: str) -> str:
    try:
        response = await asyncio.wait_for(
            client.chat.completions.create(model=settings.primary_model, messages=[...]),
            timeout=settings.llm_timeout_seconds,
        )
        return response.choices[0].message.content
    except asyncio.TimeoutError:
        logger.warning("primary_model_timeout, falling back")
        response = await client.chat.completions.create(model=settings.fallback_model, messages=[...])
        return response.choices[0].message.content
    except RateLimitError as exc:
        raise LLMProviderError("Rate limited") from exc
```

---

## 16. No Cost or Rate Controls

### Why it happens

Demos have no billing alarm. Token usage is unbounded. A single user or bug loop can exhaust monthly budget in hours.

### Impact

- Surprise invoices from LLM providers
- Abuse vectors (prompt bombing, embedding spam)
- No fairness across tenants in multi-user systems
- Cannot forecast unit economics

### How to avoid

- Implement [rate limiting](../apis/http-fundamentals-for-ai.md#rate-limiting) per user and API key
- Track token usage per request and aggregate in metrics
- Set per-request and per-user token budgets
- Cache identical queries — see [Redis](../databases/redis/redis-for-ai.md)
- Alert on anomalous usage patterns

### Bad vs good

```python
# BAD — unbounded tokens, no rate limit
@router.post("/chat")
async def chat(body: ChatRequest):
    return await llm.complete(body.message)  # could be 100k tokens


# GOOD — budget enforcement
@router.post("/chat")
async def chat(
    body: ChatRequest,
    user: User = Depends(get_current_user),
    rate_limiter: RateLimiter = Depends(get_rate_limiter),
):
    await rate_limiter.check(user.id, limit=60, window_seconds=60)
    if body.max_tokens > settings.max_tokens_per_request:
        raise HTTPException(status_code=400, detail="max_tokens exceeded")
    return await llm.complete(body.message, max_tokens=body.max_tokens)
```

---

## 17. PII and Secrets in Logs

### Why it happens

Developers log full request bodies and LLM prompts for debugging. Structured logging copies everything into Elasticsearch.

### Impact

- GDPR/CCPA violations; mandatory breach notification
- API keys in log aggregators
- Customer data exposed to support staff without need
- Logs become toxic assets — expensive to store, dangerous to query

### How to avoid

- Redact PII before logging (emails, names, account numbers)
- Never log authorization headers or API keys
- Log metadata (length, hash, category) instead of content
- See [API Security](../apis/http-fundamentals-for-ai.md#api-security)

### Bad vs good

```python
# BAD
logger.info(f"User prompt: {prompt}")
logger.debug(f"Authorization: {request.headers['authorization']}")


# GOOD
logger.info(
    "chat_request_received",
    extra={
        "user_id_hash": hash_user_id(user.id),
        "prompt_length": len(prompt),
        "conversation_id": str(conversation_id),
    },
)
```

---

## 18. Notebook Patterns in Production

### Why it happens

AI work starts in Jupyter. Cells become scripts; scripts become `main.py` with global state, unordered execution, and `!pip install` commands.

### Impact

- Non-reproducible environments
- No tests, no linting, no type checking
- State leaks between requests in shared processes
- Cannot deploy to containers reliably

### How to avoid

- Prototype in notebooks; **productize** in the layered project structure
- Pin dependencies with lockfiles — see [Dependency Locking](../python-engineering/python-for-ai-engineering.md#dependency-locking)
- Extract notebook logic into importable modules with tests
- Follow [development workflow](../foundations/ai-engineering-overview.md) — requirements before code

### Bad vs good

```python
# BAD — notebook-isms in production
%pip install openai langchain  # cell magic
documents = []  # global mutable state

def ask(q):
    global documents
    ...


# GOOD — importable module, explicit dependencies
# services/query_service.py
class QueryService:
    def __init__(self, retriever: Retriever, llm: LLMClient) -> None:
        self._retriever = retriever
        self._llm = llm

    async def ask(self, query: str) -> str:
        ...
```

---

## 19. No Evaluation for AI Outputs

### Why it happens

Teams ship when outputs "look good" on five manual examples. Retrieval quality and answer faithfulness are not measured.

### Impact

- Silent quality regression after model or prompt changes
- Cannot justify model upgrades with data
- User trust erodes before engineering notices
- No baseline for incident response ("was it always this bad?")

### How to avoid

- Build a golden dataset of representative queries
- Measure retrieval recall and answer relevance separately
- Run evals in CI when prompts, models, or chunking change
- See [AI Engineering Overview — Production AI Principles](../foundations/ai-engineering-overview.md#production-ai-principles)
- Deeper coverage in [ai-evaluation](../ai-evaluation/README.md) (Phase 8+)

### Bad vs good

```python
# BAD — manual eyeballing only
# "Looks fine to me" — ship it


# GOOD — automated regression check (simplified)
GOLDEN_SET = [
    {"query": "What is our refund policy?", "expected_doc_id": "policy-42"},
]

async def eval_retrieval(retriever: Retriever) -> float:
    hits = 0
    for case in GOLDEN_SET:
        results = await retriever.search(case["query"], top_k=3)
        if any(r.doc_id == case["expected_doc_id"] for r in results):
            hits += 1
    return hits / len(GOLDEN_SET)
```

---

## 20. Prompts as Inline Strings

### Why it happens

Prompts are copied into f-strings inside functions. Versioning, review, and A/B testing are impossible.

### Impact

- Prompt changes require code deploys
- No audit trail of what prompt produced a given output
- Teams overwrite each other's prompts in merge conflicts
- Cannot roll back a bad prompt without reverting code

### How to avoid

- Store prompts as versioned files in `domain/prompts/`
- Load and compose prompts in a dedicated `PromptBuilder`
- Include prompt version in logs and traces
- See [Software Engineering for AI — Production Considerations](../foundations/software-engineering-for-ai.md#production-considerations)

### Bad vs good

```python
# BAD
async def summarize(text: str) -> str:
    prompt = f"You are a helpful assistant. Summarize this in 3 bullets:\n\n{text}"
    return await llm.complete(prompt)


# GOOD
# domain/prompts/summarize_v2.txt
# domain/prompts/prompt_loader.py
class PromptBuilder:
    def __init__(self, prompts_dir: Path) -> None:
        self._dir = prompts_dir

    def render(self, name: str, version: str, **kwargs: str) -> str:
        template = (self._dir / f"{name}_{version}.txt").read_text()
        return template.format(**kwargs)

async def summarize(text: str, prompts: PromptBuilder, llm: LLMClient) -> str:
    prompt = prompts.render("summarize", version="v2", text=text)
    return (await llm.complete(prompt)).content
```

---

## Pre-Production Mistake Checklist

Run this checklist before any AI feature reaches production. It consolidates the mistakes above into actionable gates.

### Architecture and Code

- [ ] No LLM or database logic in route handlers
- [ ] External dependencies behind interfaces (LLM, DB, cache)
- [ ] Layered folder structure with clear import direction
- [ ] No duplicated retry, embedding, or prompt logic
- [ ] Prompts versioned outside inline strings

### API and Security

- [ ] Versioned API paths (`/v1/...`)
- [ ] Correct HTTP status codes for all error paths
- [ ] No secrets in source code or git history
- [ ] Authentication on all non-public endpoints
- [ ] Rate limiting and token budgets configured

### Operations

- [ ] Structured logging with request correlation IDs
- [ ] No PII or auth headers in logs
- [ ] Timeouts and retries on all external calls
- [ ] Fallback model or degraded mode documented
- [ ] Health check endpoint covers critical dependencies

### Quality and Performance

- [ ] Unit tests for services with mocked ports
- [ ] API contract tests via TestClient
- [ ] Async handlers use async clients (no blocking I/O)
- [ ] Connection pooling configured for databases
- [ ] Baseline eval dataset for retrieval or generation quality

---

## Interview Preparation

### Frequently Asked Questions

**Q1: What are the most common reasons AI demos fail in production?**

> **Strong answer:** Engineering failures dominate: no observability, LLM logic coupled to routes, missing error handling for provider outages, unbounded token costs, no tests for orchestration, and secrets in code. Model quality matters, but the system around the model determines reliability. Reference layered architecture, provider abstraction, and eval harnesses.

**Q2: How do you test code that calls an LLM?**

> **Strong answer:** Do not assert exact LLM strings in unit tests. Mock the `LLMClient` port and verify the service passes correct inputs, handles errors, and maps responses to typed models. Use separate evaluation pipelines with golden datasets for quality regression. API contract tests use FastAPI dependency overrides.

**Q3: How would you refactor a 500-line FastAPI route that does RAG end-to-end?**

> **Strong answer:** Identify responsibilities: retrieval, prompt building, LLM completion, response mapping. Extract each into injectable components. Route becomes a thin delegate. Introduce ports for LLM and vector store. Add unit tests per component. Move prompts to versioned files. Discuss migration strategy: strangle the monolith endpoint behind a feature flag.

**Q4: How do you prevent runaway LLM costs?**

> **Strong answer:** Rate limiting per user, per-request token caps, response caching for identical queries, cheaper fallback models for simple tasks, monitoring with budget alerts, and pre-request cost estimation for large contexts. Mention Redis for caching and metrics for token attribution.

### Real-World Scenarios

**Scenario A:** A teammate committed an OpenAI API key to the repository three months ago. The key is still active.

> **Discussion points:** Rotate the key immediately. Scan git history. Add secret detection to CI. Move to environment-based config. Assess billing for anomalous usage. Document in a postmortem.

**Scenario B:** p95 latency jumped from 2s to 30s after a "small" PDF upload feature shipped.

> **Discussion points:** Check for blocking I/O in async handlers. Profile PDF parsing. Move CPU work to thread pool or worker queue. Check database N+1 queries. Verify connection pool sizing.

**Scenario C:** RAG answers were good in staging but users report hallucinations after a prompt tweak.

> **Discussion points:** No eval pipeline caught the regression. Propose golden dataset, retrieval metrics separate from generation metrics, CI eval gate on prompt changes, prompt versioning in logs.

### Mistake → Fix Quick Reference

| Symptom in Interview | Likely Mistake | Fix to Mention |
|---------------------|----------------|----------------|
| "We couldn't switch models" | No provider abstraction | Port/adapter + DI |
| "Debugging took all night" | Missing logging | Structured logs + trace IDs |
| "One PDF upload slowed everything" | Blocking I/O in async | Async clients + thread pool |
| "AWS bill tripled" | No cost controls | Rate limits + caching + budgets |
| "Couldn't test anything" | LLM logic in routes | Service layer + mocked ports |

---

## Navigation

### Prerequisites

- [AI Engineering Overview](../foundations/ai-engineering-overview.md) — understand what production AI engineering requires
- [Software Engineering for AI](../foundations/software-engineering-for-ai.md) — architecture patterns that prevent most mistakes

### Related Topics

| Topic | Document |
|-------|----------|
| Python patterns | [Python for AI Engineering](../python-engineering/python-for-ai-engineering.md) |
| HTTP and REST | [HTTP Fundamentals for AI](../apis/http-fundamentals-for-ai.md) |
| Backend patterns | [Backend Fundamentals for AI](../backend-engineering/backend-fundamentals-for-ai.md) |
| FastAPI depth | [FastAPI Foundation](../fastapi/fastapi-foundation.md) |
| Data layer | [Databases for AI Applications](../databases/databases-for-ai-applications.md) |
| PostgreSQL | [PostgreSQL for AI](../databases/postgresql/postgresql-for-ai.md) |
| Redis caching | [Redis for AI](../databases/redis/redis-for-ai.md) |

### Phase 2 Foundation Path

Follow this sequence after reading this guide:

1. [AI Engineering Overview](../foundations/ai-engineering-overview.md)
2. [Software Engineering for AI](../foundations/software-engineering-for-ai.md)
3. [Python for AI Engineering](../python-engineering/python-for-ai-engineering.md)
4. [HTTP Fundamentals for AI](../apis/http-fundamentals-for-ai.md)
5. [Backend Fundamentals for AI](../backend-engineering/backend-fundamentals-for-ai.md)
6. [FastAPI Foundation](../fastapi/fastapi-foundation.md)
7. [Databases for AI Applications](../databases/databases-for-ai-applications.md)

### Next Topics

- [Debugging](../debugging/README.md) — systematic troubleshooting when mistakes surface in production
- [Observability](../observability/README.md) — metrics, traces, and alerts
- [Security](../security/README.md) — auth, secrets, prompt injection

### Future Reading

- [AI Evaluation](../ai-evaluation/README.md) — quality measurement beyond unit tests
- [Performance Optimization](../performance-optimization/README.md) — latency and cost tuning
- [Production Incidents](../production-incidents/README.md) — postmortems and patterns

---

## See Also

- [Common Mistakes Domain Index](README.md)
- [Knowledge: Mistakes](../../knowledge/mistakes/README.md)
- [Learning Roadmap — Phase 2](../../meta/roadmap.md#phase-2-backend-engineering)
- [Style Guide](../../meta/style-guide.md)
- [Glossary](../../meta/glossary.md)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial version — 20 mistakes with bad/good examples, severity matrix, checklist, interview prep, Phase 2 cross-references |
