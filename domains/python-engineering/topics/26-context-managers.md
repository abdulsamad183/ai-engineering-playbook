---
title: "Context Managers"
description: "The with statement — deterministic setup/teardown for files, locks, sessions, and temporary state."
domain: python-engineering
tags: [python, context-managers, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Context Managers

> The with statement — deterministic setup/teardown for files, locks, sessions, and temporary state.

## Definition

A **context manager** is an object that defines runtime contexts entered/exited via the `with` statement. It guarantees cleanup (`__exit__`) runs even if an exception occurs.

## Uses

- Files, DB connections, HTTP sessions
- Locks and temporary env vars
- Timing blocks, tracing spans

## Types

| Style | How |
|-------|-----|
| Class-based | `__enter__` / `__exit__` |
| Generator-based | `@contextmanager` |
| Async | `__aenter__` / `__aexit__` / `@asynccontextmanager` |

```mermaid
flowchart LR
  E[__enter__] --> B[with body]
  B --> X[__exit__]
  B -->|error| X
```

## Code examples

```python
from pathlib import Path
path = Path("cm.txt")
with path.open("w", encoding="utf-8") as f:
    f.write("hello\n")
# file closed here even if write failed
```

```python
from contextlib import contextmanager
import time

@contextmanager
def timed(label: str):
    start = time.perf_counter()
    try:
        yield
    finally:
        print(label, "ms:", (time.perf_counter() - start) * 1000)

with timed("sum"):
    sum(range(100000))
```

```python
class Acquire:
    def __init__(self, name: str) -> None:
        self.name = name

    def __enter__(self):
        print("acquire", self.name)
        return self

    def __exit__(self, exc_type, exc, tb):
        print("release", self.name)
        return False  # do not suppress exceptions

with Acquire("lock"):
    print("critical section")
```

```python
# Multiple context managers
from pathlib import Path
p1, p2 = Path("a.txt"), Path("b.txt")
p1.write_text("1", encoding="utf-8")
p2.write_text("2", encoding="utf-8")
with p1.open(encoding="utf-8") as f1, p2.open(encoding="utf-8") as f2:
    print(f1.read(), f2.read())
```

## Common mistakes

- Opening files without `with`
- Doing heavy work in `__enter__` without matching cleanup
- Suppressing all exceptions in `__exit__`

---

## Continue

- **Previous:** [Decorators](25-decorators.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [Type Hints](27-type-hints.md)
- **AI production guide:** [Python for AI Engineering](../python-for-ai-engineering.md)
