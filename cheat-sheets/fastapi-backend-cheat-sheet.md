# FastAPI Backend Cheat Sheet

> Quick reference for production FastAPI AI backends. See [FastAPI Complete Guide](../domains/fastapi/fastapi-complete-guide.md) for depth.

## Project Bootstrap

```bash
uv init my-ai-api && cd my-ai-api
uv add fastapi uvicorn pydantic pydantic-settings httpx
```

## Minimal App

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/health")
async def health():
    return {"status": "ok"}
```

## Dependency Injection

```python
from fastapi import Depends

def get_service() -> ChatService:
    return ChatService(...)

@router.post("/chat")
async def chat(svc: ChatService = Depends(get_service)):
    return await svc.handle(...)
```

## Streaming (SSE)

```python
from fastapi.responses import StreamingResponse

async def generate():
    async for token in llm_stream():
        yield f"data: {token}\n\n"
    yield "data: [DONE]\n\n"

return StreamingResponse(generate(), media_type="text/event-stream")
```

## Test Override

```python
app.dependency_overrides[get_llm] = lambda: MockLLM()
client = TestClient(app)
```

## Common Status Codes

| Code | When |
|------|------|
| 200 | Success |
| 201 | Created |
| 400 | Validation / bad input |
| 401 | Missing/invalid auth |
| 403 | Forbidden |
| 404 | Resource not found |
| 429 | Rate limited |
| 503 | Service degraded |

## Do / Don't

| Do | Don't |
|----|-------|
| `async def` for I/O | `time.sleep()` in async routes |
| `response_model` on routes | Return raw dicts without validation |
| Release DB before LLM calls | Hold connections during 30s LLM waits |
| `Depends()` for wiring | Instantiate services in route handlers |

## See Also

- [Backend Engineering](../domains/backend-engineering/README.md)
- [Backend Templates](../meta/templates/backend/)
