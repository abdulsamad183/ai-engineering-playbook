---
title: "Reliability for AI Systems"
description: "Retries, circuit breakers, failover, degradation, timeouts, idempotency."
domain: ai-deployment
tags: [reliability, circuit-breaker, retry]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../../examples/production-ai/example-retry-middleware.py
keywords: [circuit breaker, exponential backoff, graceful degradation]
author: hp
---

# Reliability for AI Systems

## Overview

Section **10**.

## Patterns

| Pattern | AI use |
|---------|--------|
| **Retry** | Transient 429/503 from LLM |
| **Exponential backoff** | Rate limit respect |
| **Circuit breaker** | Flaky tool API |
| **Failover** | Secondary LLM provider |
| **Graceful degradation** | Shorter answer, no RAG |
| **Timeouts** | Every external call |
| **Idempotency** | `Idempotency-Key` on writes |

```python
async def with_retry(fn, max_attempts=3):
    for i in range(max_attempts):
        try:
            return await fn()
        except TransientError:
            await asyncio.sleep(2 ** i)
    raise
```

## Health Probes

Liveness vs readiness — don't route to pod failing LLM connectivity.

## Navigation

- [Caching](caching-for-ai.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
