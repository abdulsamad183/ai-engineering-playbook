---
title: "Type Hints"
description: "Optional static types for clarity and tooling — annotations, typing constructs, Protocols, and mypy/pyright."
domain: python-engineering
tags: [python, typing, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Type Hints

> Optional static types for clarity and tooling — annotations, typing constructs, Protocols, and mypy/pyright.

## Definition

**Type hints** (annotations) declare expected types for variables, parameters, and returns. They do **not** enforce types at runtime by default; tools like **Pyright** / **mypy** check them statically. Pydantic can validate at runtime on boundaries.

## Uses

- Document APIs for humans and IDEs
- Catch bugs before production
- Enable better autocomplete/refactors

## Common typing constructs

| Hint | Meaning |
|------|---------|
| `int`, `str` | Concrete types |
| `list[str]` | List of strings (3.9+) |
| `dict[str, int]` | Mapping |
| `X \| None` | Optional (3.10+) |
| `Iterable[X]` | Any iterable |
| `Callable[[A], R]` | Function types |
| `TypeVar` / generics | Parametric types |
| `Protocol` | Structural interface |
| `TypedDict` | Dict shape |
| `Literal["a","b"]` | Specific values |
| `Any` | Escape hatch (minimize) |

## Code examples

```python
def greet(name: str, times: int = 1) -> str:
    return " ".join([f"Hi {name}!"] * times)

print(greet("Samad"))
```

```python
from collections.abc import Iterable

def mean(xs: Iterable[float]) -> float:
    vals = list(xs)
    return sum(vals) / len(vals)

print(mean([1.0, 2.0, 3.0]))
```

```python
from typing import TypeVar

T = TypeVar("T")

def first(xs: list[T]) -> T | None:
    return xs[0] if xs else None

print(first([10, 20]))
```

```python
from typing import Protocol

class Embedder(Protocol):
    def embed(self, text: str) -> list[float]: ...

class LenEmbedder:
    def embed(self, text: str) -> list[float]:
        return [float(len(text))]

def run(e: Embedder, text: str) -> list[float]:
    return e.embed(text)

print(run(LenEmbedder(), "rag"))
```

```python
from typing import TypedDict

class Hit(TypedDict):
    doc_id: str
    score: float

hit: Hit = {"doc_id": "d1", "score": 0.9}
```

## Gradual typing strategy

1. Annotate public functions first
2. Keep `Any` rare
3. Validate at I/O boundaries (Pydantic)
4. Run Pyright/mypy in CI

## Common mistakes

- Thinking hints enforce runtime safety alone
- Overusing `Any`
- Annotating everything privately before APIs stabilize

---

## Continue

- **Previous:** [Context Managers](26-context-managers.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [Regular Expressions](28-regular-expressions.md)
- **AI production guide:** [Python for AI Engineering](../python-for-ai-engineering.md)
