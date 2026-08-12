---
title: "Functional Programming"
description: "FP ideas in Python — purity, immutability, higher-order functions, and practical functional style."
domain: python-engineering
tags: [python, functional, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-12
version: "1.1"
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

