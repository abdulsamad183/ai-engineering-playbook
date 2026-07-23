# Logging Template

> Structured JSON logging with correlation IDs and log rotation.

---

## Purpose

Production logging module: JSON formatter, request ID context var, rotating file handler.

---

## Usage

```python
from structured_logger import setup_logging, bind_request_id, log_event
import logging

logger = setup_logging(level="INFO", log_file="app.log")
bind_request_id("req-123")
log_event(logger, "llm_call", model="gpt-4o", tokens=512)
```

---

## Related

- [FastAPI middleware](../fastapi-starter/src/app/api/middleware.py)
- [Production Observability](../../../domains/ai-deployment/observability-for-ai.md)
