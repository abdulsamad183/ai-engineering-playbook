---
title: "Decorators"
description: "Wrap functions and classes to add behavior — timing, retries, caching, auth checks — without rewriting call sites."
domain: python-engineering
tags: [python, decorators, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-12
version: "1.1"
---

# Decorators

> Wrap functions and classes to add behavior — timing, retries, caching, auth checks — without rewriting call sites.

## Definition

A **decorator** is a callable that takes a function/class and returns a new callable, usually wrapping it. Syntax sugar: `@decorator` above a `def` equals `f = decorator(f)`.

## Uses

- Logging / timing
- Retries and circuit breakers
- Caching (`functools.lru_cache`)
- Authz checks on FastAPI routes
- Registering tools/agents

## Types

| Kind | Example |
|------|---------|
| Function decorator | `@timer` |
| Decorator with args | `@retry(times=3)` |
| Class decorator | `@dataclass` |
| Method decorators | `@classmethod` `@staticmethod` `@property` |

```mermaid
flowchart LR
  Call[Caller] --> Wrap[Wrapper]
  Wrap --> Orig[Original function]
  Orig --> Wrap
  Wrap --> Call
```

## Code examples

```python
import time
from functools import wraps

def timer(fn):
    @wraps(fn)  # preserve name/docstring
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            ms = (time.perf_counter() - start) * 1000
            print(f"{fn.__name__} took {ms:.2f} ms")
    return wrapper

@timer
def work(n: int) -> int:
    return sum(range(n))

print(work(100000))
```

```python
# Decorator with arguments → nested factory
def retry(times: int = 3):
    def deco(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            last = None
            for attempt in range(1, times + 1):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    last = e
                    print(f"attempt {attempt} failed: {e}")
            raise last
        return wrapper
    return deco

@retry(times=2)
def flaky():
    raise RuntimeError("boom")
```

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(20))
```

```python
class Hot:
    count = 0

    @classmethod
    def bump(cls):
        cls.count += 1
        return cls.count

    @staticmethod
    def ping():
        return "pong"

print(Hot.bump(), Hot.ping())
```

## Common mistakes

- Forgetting `@wraps` (breaks debugging / FastAPI signatures)
- Decorators that swallow exceptions silently
- Heavy side effects at decoration import time

---

## Continue

- **Previous:** [Dataclasses](24-dataclasses.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [Context Managers](26-context-managers.md)
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

