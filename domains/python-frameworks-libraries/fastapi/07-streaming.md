---
title: "FastAPI: Streaming Responses"
description: "SSE/streaming for token-by-token chat UIs."
domain: python-frameworks-libraries
tags: [fastapi, streaming]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# FastAPI: Streaming Responses

> SSE/streaming for token-by-token chat UIs.

## Definition

**Streaming** sends data in chunks before the full response is ready — essential for LLM token streams.

## Important APIs

| API | Use |
|-----|-----|
| `StreamingResponse` | Generic stream |
| `EventSourceResponse` (sse-starlette) | SSE helper |
| media type `text/event-stream` | SSE |

## Code

```python
import asyncio
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

async def token_generator():
    for tok in ["Hello", " ", "world", "!"]:
        yield tok
        await asyncio.sleep(0.05)

@app.get("/stream")
async def stream():
    return StreamingResponse(token_generator(), media_type="text/plain")
```

## Practices

- Bound stream lifetime with timeouts/cancellation
- Don’t buffer the entire model output first

---

## Continue

- **Hub:** [FastAPI hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
