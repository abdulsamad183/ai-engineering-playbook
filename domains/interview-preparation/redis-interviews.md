---
title: "Redis Interviews for AI Engineers"
description: "Redis interviews — caching, pub/sub, streams, locks, rate limiting, sessions."
domain: interview-preparation
tags: [interview, redis, caching, phase-13]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../databases/redis/README.md
  - production-ai-interviews.md
keywords: [Redis interview, rate limiting, session cache]
author: hp
---

# Redis Interviews for AI Engineers

## Overview

Section **6**. Redis powers **caching**, **rate limits**, and **session state** in AI APIs.

## Core Concepts

| Pattern | AI use |
|---------|--------|
| **Cache** | Embed query hash → retrieval results |
| **Rate limit** | Token bucket per user/API key |
| **Session** | Hot conversation context |
| **Pub/Sub** | Notify index refresh |
| **Streams** | Job queue for embed workers |
| **Distributed lock** | Single indexer leader |

## FAQ

**Q: Implement rate limiting with Redis.**

> `INCR` key with TTL window; or sliding window with sorted sets; or token bucket in Lua.

**Q: Cache invalidation when prompt version changes?**

> Include `prompt_version` in cache key; bump version on deploy.

**Q: Redis vs in-memory cache?**

> Redis: shared across API replicas. In-process: faster but per-pod only.

## Coding Exercise

Implement `SET key value EX 300 NX` for distributed lock with expiry.

## Trick Question

**Q: What happens when Redis is full?**

> Depends on `maxmemory-policy` — `allkeys-lru` evicts keys; can cause cache stampede.

## Further Reading

- [Caching for AI](../ai-deployment/caching-for-ai.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Section 6 |
