---
title: "FastAPI: Status Codes & Errors"
description: "HTTPException, status codes, and consistent error payloads."
domain: python-frameworks-libraries
tags: [fastapi, errors]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# FastAPI: Status Codes & Errors

> HTTPException, status codes, and consistent error payloads.

## Definition

Use **`HTTPException`** for expected API errors. Set **`status_code`** on success routes. Clients should rely on stable error shapes.

## Important APIs

| API | Use |
|-----|-----|
| `HTTPException` | Raise API error |
| `status` (fastapi) | Constants like `HTTP_201_CREATED` |
| `RequestValidationError` | Auto 422 on bad input |

## Code

```python
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/docs/{doc_id}", status_code=status.HTTP_200_OK)
def get_doc(doc_id: str):
    if doc_id == "missing":
        raise HTTPException(status_code=404, detail="doc not found")
    return {"id": doc_id}
```

## Practices

- 4xx for client problems, 5xx for server/provider failures
- Don’t leak stack traces to clients

---

## Continue

- **Hub:** [FastAPI hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
