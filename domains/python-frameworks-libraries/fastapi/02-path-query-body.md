---
title: "FastAPI: Path, Query & Body Parameters"
description: "Declare inputs — path params, query strings, and JSON bodies."
domain: python-frameworks-libraries
tags: [fastapi, parameters]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# FastAPI: Path, Query & Body Parameters

> Declare inputs — path params, query strings, and JSON bodies.

## Definition

FastAPI extracts parameters from the URL path, query string, headers, or body using type hints and defaults.

## Important APIs

| API | Use |
|-----|-----|
| Path params | ` deb(item_id: int)` in `/items/{item_id}` |
| Query params | function args with defaults / `Query()` |
| Body | Pydantic model parameter |
| `Path()`, `Query()`, `Body()`, `Header()` | Constraints & metadata |

## Code

```python
from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, Field

app = FastAPI()

class ChatIn(BaseModel):
    message: str = Field(min_length=1, max_length=8000)
    temperature: float = 0.2

@app.get("/users/{user_id}")
def get_user(user_id: int = Path(ge=1), verbose: bool = False):
    return {"user_id": user_id, "verbose": verbose}

@app.get("/search")
def search(q: str = Query(min_length=1), k: int = Query(5, ge=1, le=50)):
    return {"q": q, "k": k}

@app.post("/chat")
def chat(body: ChatIn):
    return {"echo": body.message, "temperature": body.temperature}
```

## Uses

- Validate `k` for RAG top-k
- Bound prompt length at the edge

---

## Continue

- **Hub:** [FastAPI hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
