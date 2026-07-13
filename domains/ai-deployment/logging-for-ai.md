---
title: "Logging for AI Applications"
description: "Structured JSON logs, correlation IDs, agent and tool logging."
domain: ai-deployment
tags: [logging, structured-logs, tracing, phase-12]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - observability-for-ai.md
  - ../logging/logging-and-error-handling.md
keywords: [structured logging, correlation ID, JSON logs]
author: hp
---

# Logging for AI Applications

## Overview

Section **7** of Phase 12.

## Structured Logging

```python
import json, logging
logger = logging.getLogger("ai.api")

def log_request(request_id: str, path: str, user_id: str, latency_ms: float):
    logger.info(json.dumps({
        "event": "http_request",
        "request_id": request_id,
        "path": path,
        "user_id": user_id,
        "latency_ms": latency_ms,
    }))
```

## Correlation IDs

- Generate at edge; propagate to LLM, RAG, tools
- `X-Request-ID` header

## What to Log

| Log | Don't log |
|-----|-----------|
| Tool names, latency | Full prompts with PII |
| Token counts | API keys |
| Model version | Raw user documents |

## Agent / Tool Logging

Log each tool call: name, args hash, duration, success.

## Navigation

- [Observability](observability-for-ai.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 12 Section 7 |
