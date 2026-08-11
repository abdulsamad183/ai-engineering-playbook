---
title: "Functional Programming"
description: "FP ideas in Python — purity, immutability, higher-order functions, and practical functional style."
domain: python-engineering
tags: [python, functional, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Functional Programming

> FP ideas in Python — purity, immutability, higher-order functions, and practical functional style.

## Definition

**Functional programming (FP)** emphasizes **pure functions** (no side effects), **immutable data**, and **functions as values**. Python is multi-paradigm: use FP ideas where they improve clarity, not as dogma.

## Uses

- Predictable transforms in data/RAG pipelines
- Easier testing (pure functions)
- Safer concurrency (less shared mutable state)

## Core ideas

| Idea | Meaning |
|------|---------|
| Pure function | Same inputs → same outputs; no side effects |
| Higher-order fn | Takes/returns functions |
| Immutability | Prefer new values over mutation |
| Composition | Build pipelines from small functions |
| Lazy eval | Generators / iterators |

## Code examples

```python
from collections.abc import Callable

def compose(f: Callable, g: Callable) -> Callable:
    return lambda x: f(g(x))

def normalize(s: str) -> str:
    return " ".join(s.strip().lower().split())

def exclaim(s: str) -> str:
    return s + "!"

pipeline = compose(exclaim, normalize)
print(pipeline("  Hello   RAG "))
```

```python
# Pure transform vs impure
def add_score_pure(row: dict, delta: float) -> dict:
    return {**row, "score": row["score"] + delta}  # new dict

def add_score_impure(row: dict, delta: float) -> dict:
    row["score"] += delta  # mutates caller data
    return row
```

```python
from collections.abc import Callable

def rank(items: list[str], key: Callable[[str], float]) -> list[str]:
    return sorted(items, key=key, reverse=True)

print(rank(["aa", "b", "cccc"], key=len))
```

```python
from functools import partial

def power(base: int, exp: int) -> int:
    return base ** exp

square = partial(power, exp=2)
print(square(5))
```

```python
from types import MappingProxyType
cfg = MappingProxyType({"temperature": 0.2})
# cfg["temperature"] = 0.0  # TypeError
```

## Balance

- FP for transforms; OOP/modules for boundaries; procedures for scripts
- Prefer readable comprehensions over clever FP chains

## Common mistakes

- Deep nested `reduce` nobody can read
- Pretending Python lists are immutable

---

## Continue

- **Previous:** [Regular Expressions](28-regular-expressions.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [Logging](30-logging.md)
- **AI production guide:** [Python for AI Engineering](../python-for-ai-engineering.md)
