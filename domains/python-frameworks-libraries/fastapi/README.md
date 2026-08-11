# FastAPI

> Modern async Python web framework for high-performance AI APIs — routes, validation, DI, and OpenAPI.

**Prerequisites:** [Python](../../python-engineering/README.md) · [Pydantic](../pydantic/README.md)  
**Part of:** [Python Frameworks & Libraries](../README.md)  
**Deeper domain:** [domains/fastapi](../../fastapi/README.md)

---

## Definition

**FastAPI** is a web framework built on **Starlette** (ASGI) and **Pydantic** (validation). It gives you typed request/response models, automatic OpenAPI docs, dependency injection, and first-class `async` support — ideal for LLM/RAG/agent HTTP services.

---

## When to use FastAPI

| Use | Example |
|-----|---------|
| Chat/completions API | `POST /v1/chat` |
| RAG query endpoint | retrieve → generate |
| Streaming tokens | SSE responses |
| Tool webhooks | agent callbacks |

---

## Learning path

```mermaid
flowchart LR
  A[App & routes] --> B[Params & body]
  B --> C[Models & responses]
  C --> D[Dependencies]
  D --> E[Async & streaming]
```

---

## Topics

| # | Topic | Document |
|---|-------|----------|
| 1 | App, router & routes | [01-app-routes.md](01-app-routes.md) |
| 2 | Path, query & body parameters | [02-path-query-body.md](02-path-query-body.md) |
| 3 | Request/response models | [03-request-response-models.md](03-request-response-models.md) |
| 4 | Dependency injection | [04-dependency-injection.md](04-dependency-injection.md) |
| 5 | Status codes & errors | [05-status-errors.md](05-status-errors.md) |
| 6 | Async endpoints | [06-async-endpoints.md](06-async-endpoints.md) |
| 7 | Streaming responses | [07-streaming.md](07-streaming.md) |
| 8 | Middleware & CORS | [08-middleware-cors.md](08-middleware-cors.md) |
| 9 | Important APIs cheat sheet | [09-important-apis.md](09-important-apis.md) |

---

## Related

- [Pydantic](../pydantic/README.md) · [FastAPI domain](../../fastapi/README.md) · [LLM Application Development](../../llm-application-development/README.md)
