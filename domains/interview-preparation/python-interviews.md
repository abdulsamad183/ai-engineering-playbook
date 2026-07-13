---
title: "Python Interviews for AI Engineers"
description: "Python interview guide — data structures, async, GIL, decorators, performance, coding exercises."
domain: interview-preparation
tags: [interview, python, coding, phase-13]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../python-engineering/README.md
  - fastapi-interviews.md
keywords: [Python interview, async, GIL, decorators]
author: hp
---

# Python Interviews for AI Engineers

## Overview

Section **2**. AI engineers spend most implementation time in **Python** — interviews test fluency, not trivia.

## Core Concepts

| Topic | Interview relevance |
|-------|---------------------|
| **Data structures** | dict/list for pipelines, heaps for top-k |
| **OOP** | Service classes, test doubles |
| **GIL** | CPU-bound → multiprocessing; I/O → async |
| **Async** | FastAPI + concurrent LLM calls |
| **Generators** | Stream tokens/chunks without loading all |
| **Decorators** | Retry, timing, auth wrappers |
| **Context managers** | DB sessions, file handles |
| **Typing** | Pydantic models, tool schemas |

## Frequently Asked Questions

**Q: What is the GIL? When does it matter for AI apps?**

> The Global Interpreter Lock allows one thread to execute Python bytecode at a time. It matters for CPU-heavy work (embedding batch on CPU, parsing huge JSON). It does **not** block I/O-bound LLM API calls — use `asyncio` for concurrent HTTP. Use `multiprocessing` or offload to C/Rust for CPU parallelism.

**Follow-up:** How would you parallelize embedding 1M documents?

> Chunk into batches; worker processes or a job queue (Celery/RQ); avoid threading for CPU embed.

**Q: `async def` vs `def` in FastAPI?**

> `async def` routes run on the event loop — good for I/O. CPU work in async routes blocks the loop — use `run_in_executor` or sync `def` route with thread pool.

**Q: Explain generators. Use case in AI?**

> `yield` produces lazy sequences — streaming LLM tokens to client without buffering full response in memory.

## Trick Questions

**Q: Is `list.append` thread-safe?**

> CPython's GIL makes single append atomic in practice, but compound read-modify-write is not — use locks or queues for shared state.

## Coding Exercises

| Exercise | Level | Outline |
|----------|-------|---------|
| Rate limiter (token bucket) | Mid | [example in production-ai](../../examples/production-ai/example-rate-limiting.py) |
| Async gather with timeout | Mid | `asyncio.wait_for` per task |
| LRU cache decorator | Mid | `functools.lru_cache` or OrderedDict |
| Parse streaming JSON lines | Senior | Buffer incomplete lines |

## Debugging Scenario

**Symptom:** FastAPI hangs under load.

> **Diagnosis:** Sync CPU work in `async def`; blocking DB driver; too few workers.

> **Fix:** Profile; move CPU out; use async driver; scale replicas.

## Common Mistakes

- Using threads for CPU embedding at scale
- Mutable default arguments in tool registries

## Seniority

- **Junior:** list/dict comprehensions, basic OOP
- **Mid:** async, decorators, typing
- **Senior:** GIL implications, performance profiling

## Further Reading

- [Python Engineering](../python-engineering/README.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Section 2 |
