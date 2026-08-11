---
title: "FastAPI: Important APIs Cheat Sheet"
description: "High-frequency FastAPI classes and functions."
domain: python-frameworks-libraries
tags: [fastapi, cheatsheet]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# FastAPI: Important APIs Cheat Sheet

> High-frequency FastAPI classes and functions.

## App & routing

`FastAPI`, `APIRouter`, `include_router`, `@app.get/post/...`

## Parameters

`Path`, `Query`, `Body`, `Header`, `Depends`, `Annotated`

## Responses / errors

`response_model`, `HTTPException`, `status`, `StreamingResponse`

## Middleware

`CORSMiddleware`, `@app.middleware("http")`

## Minimal AI endpoint sketch

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class ChatIn(BaseModel):
    message: str = Field(min_length=1)

@app.post("/v1/chat")
async def chat(body: ChatIn):
    # await llm_client.complete(body.message)
    return {"reply": body.message[::-1]}
```

See also: [FastAPI Complete Guide](../../fastapi/fastapi-complete-guide.md)

---

## Continue

- **Hub:** [FastAPI hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
