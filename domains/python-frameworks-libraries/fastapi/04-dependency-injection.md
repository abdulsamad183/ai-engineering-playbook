---
title: "FastAPI: Dependency Injection"
description: "Depends() — share DB sessions, auth, settings, and clients."
domain: python-frameworks-libraries
tags: [fastapi, dependencies]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# FastAPI: Dependency Injection

> Depends() — share DB sessions, auth, settings, and clients.

## Definition

**Dependencies** are callables FastAPI runs before your endpoint, injecting their return values. They compose cleanly for auth, settings, and resource clients.

## Important APIs

| API | Use |
|-----|-----|
| `Depends(fn)` | Inject dependency |
| `Annotated[T, Depends(fn)]` | Modern typing style |
| `app.dependency_overrides` | Testing doubles |

## Code

```python
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Header

app = FastAPI()

def get_settings():
    return {"model": "gpt-4.1-mini"}

def require_api_key(x_api_key: str | None = Header(default=None)):
    if x_api_key != "secret":
        raise HTTPException(status_code=401, detail="unauthorized")
    return x_api_key

@app.get("/config")
def config(
    settings: Annotated[dict, Depends(get_settings)],
    _: Annotated[str, Depends(require_api_key)],
):
    return settings
```

## Uses

- Inject LLM client singleton
- Authn/z per request
- Swap fakes in pytest

---

## Continue

- **Hub:** [FastAPI hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
