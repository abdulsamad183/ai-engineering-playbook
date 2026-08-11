---
title: "FastAPI: Request & Response Models"
description: "Pydantic models for typed I/O and OpenAPI schemas."
domain: python-frameworks-libraries
tags: [fastapi, models]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# FastAPI: Request & Response Models

> Pydantic models for typed I/O and OpenAPI schemas.

## Definition

**Request models** validate inbound JSON. **Response models** declare outbound shape (`response_model=`), filtering fields and documenting schemas.

## Important APIs

| API | Use |
|-----|-----|
| Pydantic `BaseModel` | Schema |
| `response_model=` | Output model |
| `response_model_exclude_unset` | Omit defaults |
| `status_code=` | Default status |

## Code

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class ChatIn(BaseModel):
    message: str

class ChatOut(BaseModel):
    reply: str
    model: str = "demo"

@app.post("/chat", response_model=ChatOut)
def chat(body: ChatIn) -> ChatOut:
    return ChatOut(reply=f"you said: {body.message}")
```

## Uses

- Stable API contracts for clients
- Hide internal fields from responses

---

## Continue

- **Hub:** [FastAPI hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
