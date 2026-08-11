---
title: "FastAPI: App, Router & Routes"
description: "Create applications and map HTTP methods to Python callables."
domain: python-frameworks-libraries
tags: [fastapi, routing]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# FastAPI: App, Router & Routes

> Create applications and map HTTP methods to Python callables.

## Definition

A **`FastAPI`** app is an ASGI application. **Routes** bind HTTP method + path to a function. **`APIRouter`** splits large apps into modules.

## Key classes / functions

| API | Role |
|-----|------|
| `FastAPI` | Application |
| `APIRouter` | Sub-router |
| `@app.get/post/put/patch/delete` | Route decorators |
| `app.include_router` | Mount router |

## Code

```python
from fastapi import FastAPI, APIRouter

app = FastAPI(title="AI API", version="1.0.0")
router = APIRouter(prefix="/v1", tags=["chat"])

@app.get("/health")
def health():
    return {"ok": True}

@router.post("/chat")
def chat():
    return {"message": "hello"}

app.include_router(router)

# Run: uvicorn main:app --reload
```

## Uses

- Service entrypoint
- Modular routers per domain (`/rag`, `/agents`)

---

## Continue

- **Hub:** [FastAPI hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
