---
title: "FastAPI: Middleware & CORS"
description: "Cross-cutting concerns — CORS, timing, request IDs."
domain: python-frameworks-libraries
tags: [fastapi, middleware]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# FastAPI: Middleware & CORS

> Cross-cutting concerns — CORS, timing, request IDs.

## Definition

**Middleware** wraps every request/response. **CORS** middleware allows browser frontends on other origins to call your API.

## Important APIs

| API | Use |
|-----|-----|
| `CORSMiddleware` | Browser CORS |
| `@app.middleware("http")` | Custom middleware |
| `BaseHTTPMiddleware` | Class-style middleware |

## Code

```python
import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_timing(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    response.headers["X-Process-Time-Ms"] = str((time.perf_counter() - start) * 1000)
    return response
```

---

## Continue

- **Hub:** [FastAPI hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
