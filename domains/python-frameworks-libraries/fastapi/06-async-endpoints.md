---
title: "FastAPI: Async Endpoints"
description: "async def routes for non-blocking I/O to LLMs and databases."
domain: python-frameworks-libraries
tags: [fastapi, async]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# FastAPI: Async Endpoints

> async def routes for non-blocking I/O to LLMs and databases.

## Definition

Declare endpoints with **`async def`** when you `await` I/O (HTTPX, async DB). FastAPI runs sync `def` in a threadpool — fine for light work, not for heavy CPU.

## Important ideas

| Idea | Practice |
|------|----------|
| `async def` + `await` | Non-blocking I/O |
| sync `def` | Threadpool (don’t block event loop with CPU) |
| `httpx.AsyncClient` | Async HTTP to providers |
| `asyncio.to_thread` | Offload blocking SDK calls |

## Code

```python
import httpx
from fastapi import FastAPI

app = FastAPI()

@app.get("/ip")
async def ip():
    async with httpx.AsyncClient(timeout=10.0) as client:
        r = await client.get("https://httpbin.org/ip")
        r.raise_for_status()
        return r.json()
```

## Uses

- Concurrent provider calls
- Overlap retrieval + generation setup

---

## Continue

- **Hub:** [FastAPI hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
