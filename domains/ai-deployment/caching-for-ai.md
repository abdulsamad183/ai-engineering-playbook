---
title: "Caching for AI Applications"
description: "Redis, prompt, embedding, response, retrieval, context caching."
domain: ai-deployment
tags: [caching, redis, performance, phase-12]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../../examples/production-ai/example-redis-cache.py
  - ../databases/redis/README.md
keywords: [prompt cache, embedding cache, Redis AI]
author: hp
---

# Caching for AI Applications

## Overview

Section **11** of Phase 12.

```mermaid
flowchart LR
    REQ[Request] --> CACHE{Redis hit?}
    CACHE -->|yes| OUT[Response]
    CACHE -->|no| LLM[LLM + store]
```

## Cache Types

| Cache | Key | TTL |
|-------|-----|-----|
| **Prompt prefix** | Provider-managed | Session |
| **Embedding** | hash(text) | Days |
| **Retrieval** | hash(query+index_ver) | Minutes |
| **Full response** | hash(query+prompt_ver) | Short |
| **Session context** | session_id | Hours |

## Invalidation

Bump `prompt_version` or `index_version` in cache key.

## Navigation

- [Security](security-production-ai.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 12 Section 11 |
