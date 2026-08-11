---
title: "Decorators"
description: "Wrap functions and classes to add behavior — timing, retries, caching, auth checks — without rewriting call sites."
domain: python-engineering
tags: [python, decorators, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
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
