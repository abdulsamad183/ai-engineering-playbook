---
title: "Asynchronous Programming"
description: "asyncio event loops, async/await, tasks, and non-blocking I/O for high-concurrency AI services."
domain: python-engineering
tags: [python, asyncio, async, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-12
version: "1.1"
---

# Asynchronous Programming

> asyncio event loops, async/await, tasks, and non-blocking I/O for high-concurrency AI services.

## Definition

**Asynchronous programming** in Python uses `async` / `await` and an **event loop** (`asyncio`) to interleave many I/O-bound tasks in one thread without blocking on each wait.

## Uses

- FastAPI request handlers
- Concurrent LLM/provider calls
- Fan-out retrieval + tools
- Websockets / streaming responses

## Core concepts

| Concept | Meaning |
|---------|---------|
| Coroutine | `async def` function |
| await | Pause until awaitable completes |
| Task | Scheduled coroutine |
| Event loop | Schedules ready tasks |
| async with / for | Async CM / iteration |

```mermaid
flowchart LR
  T1[Task A wait IO] --> Loop[Event loop]
  T2[Task B run] --> Loop
  Loop --> T1
```

## Code examples

```python
import asyncio

async def fetch(n: int) -> str:
    await asyncio.sleep(0.2)          # non-blocking sleep
    return f"result-{n}"

async def main():
    results = await asyncio.gather(*(fetch(i) for i in range(5)))
    print(results)

asyncio.run(main())
```

```python
async def bounded_gather(coros, limit: int = 10):
    sem = asyncio.Semaphore(limit)

    async def run(c):
        async with sem:
            return await c

    return await asyncio.gather(*(run(c) for c in coros))
```

```python
async def call():
    async with asyncio.timeout(1.0):   # 3.11+
        await asyncio.sleep(0.1)
        return "ok"
```

```python
import time
import asyncio

async def bad():
    time.sleep(1)                      # blocks everything

async def good():
    await asyncio.sleep(1)

async def read_blocking():
    return await asyncio.to_thread(time.sleep, 0.2)
```

## Rules for AI services

1. Use async HTTP clients (`httpx.AsyncClient`)
2. Bound concurrency (semaphores) to protect providers
3. Cancel/timeouts on every external call
4. Don’t mix blocking SDK calls into async handlers without `to_thread`

## Common mistakes

- Forgetting `await`
- Calling `asyncio.run` inside running loop
- CPU-heavy work on the loop thread

---

## Continue

- **Previous:** [Multiprocessing](35-multiprocessing.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [Memory Management](37-memory-management.md)
- **AI production guide:** [Python for AI Engineering](../python-for-ai-engineering.md)

---

## AI engineering angle

This topic shows up constantly in AI codebases: training scripts, eval runners, FastAPI services, agent tools, and data cleanup jobs. Prefer clear `main()` entrypoints, typed interfaces, and small testable functions over notebook-only workflows.

## Production checklist

- [ ] Errors are explicit (no bare `except:`)
- [ ] Logging instead of leftover `print` in services
- [ ] Deterministic seeds where experiments need reproduction
- [ ] Resource cleanup via `with` / context managers
- [ ] Unit tests for pure helpers

## Practice exercises

1. Rewrite one snippet from this page as a function with type hints and a docstring.
2. Add a failing unit test, then make it pass.
3. Note one way this concept appears in RAG, agents, or LLM API clients.

## Interview prompts

**Q: When would you choose a different approach than the default shown here?**

A: Tie the answer to performance, readability, concurrency, or API boundaries — and give a concrete AI-engineering example (streaming responses, batch embedding, tool sandboxing).

## See also

- [Python hub](../README.md)
- [Python Frameworks](../../python-frameworks-libraries/README.md)
- [LLM Application Development](../../llm-application-development/README.md)

