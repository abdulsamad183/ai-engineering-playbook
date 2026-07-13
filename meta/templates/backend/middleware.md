---
title: "Middleware Template"
description: "Custom FastAPI middleware template for AI backends."
type: backend-template
---

# Middleware Template

## Request ID Middleware

```python
import uuid
from contextvars import ContextVar

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

request_id_ctx: ContextVar[str] = ContextVar("request_id", default="")


class RequestIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        request_id_ctx.set(request_id)
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        return response
```

## Registration

```python
from fastapi import FastAPI

app = FastAPI()
app.add_middleware(RequestIDMiddleware)
```

## Ordering

Middleware executes in **reverse** order of registration. Register outermost first:

```python
app.add_middleware(CORSMiddleware, ...)      # outermost
app.add_middleware(RequestIDMiddleware)
app.add_middleware(SecurityHeadersMiddleware)  # innermost
```

## See Also

- [FastAPI Complete Guide](../../../domains/fastapi/fastapi-complete-guide.md)
- [Backend Logging for AI](../../../domains/logging/backend-logging-for-ai.md)
