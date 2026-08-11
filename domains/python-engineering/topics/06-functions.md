---
title: "Functions"
description: "Define reusable blocks of logic with parameters, returns, defaults, *args/**kwargs, and clean function design."
domain: python-engineering
tags: [python, functions, fundamentals, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Functions

> Define reusable blocks of logic with parameters, returns, defaults, *args/**kwargs, and clean function design.

## Definition

A **function** is a named, reusable block of code that can accept **parameters**, perform work, and optionally **return** a value. Functions are first-class objects in Python: you can pass them, store them, and return them.

## Uses

- Avoid copy-paste
- Isolate testable units
- Express clear inputs/outputs at module boundaries
- Build APIs of your application layer

## Types of parameters

| Kind | Syntax | Meaning |
|------|--------|---------|
| Positional | `def f(a, b)` | Order matters |
| Keyword | `f(a=1, b=2)` | Call by name |
| Default | `def f(a, b=0)` | Optional at call site |
| Var-positional | `*args` | Extra positional → tuple |
| Var-keyword | `**kwargs` | Extra keywords → dict |
| Keyword-only | `def f(a, *, b)` | `b` must be keyword |
| Positional-only | `def f(a, /, b)` | `a` must be positional (3.8+) |

```mermaid
flowchart LR
  Call[Caller] --> Args[Bind arguments]
  Args --> Body[Execute body]
  Body --> Ret[Return value or None]
```

## Code examples

```python
def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b

print(add(2, 3))
print(add(b=5, a=1))   # keyword call
```

```python
# Defaults — evaluated ONCE at definition time (mutable default pitfall!)
def append_item(item, bucket=None):
    if bucket is None:       # correct pattern
        bucket = []
    bucket.append(item)
    return bucket

print(append_item("a"))
print(append_item("b"))      # fresh list each time when using None
```

```python
# *args and **kwargs
def debug_log(message: str, *args, **kwargs):
    print("MSG:", message)
    print("ARGS:", args)
    print("KW:", kwargs)

debug_log("run", 1, 2, level="info", ok=True)
```

```python
# Keyword-only and return multiple values (tuple packing)
def split_name(full: str, *, lower: bool = False) -> tuple[str, str]:
    first, last = full.split(" ", 1)
    if lower:
        return first.lower(), last.lower()
    return first, last

f, l = split_name("Ada Lovelace", lower=True)
print(f, l)
```

```python
# Early return clarifies control flow
def normalize_score(score: float | None) -> float:
    if score is None:
        return 0.0
    if score < 0:
        return 0.0
    if score > 1:
        return 1.0
    return score
```

## Design guidelines

1. **One job per function** (or a clear facade)
2. **Pure when possible** — same inputs → same outputs, no hidden I/O
3. **Explicit returns** — don’t rely on accidental `None`
4. **Type hints on public functions** (topic 27)
5. **Docstrings** for non-obvious behavior

## Common mistakes

- Mutable default arguments (`def f(xs=[])`)
- Too many parameters → use a dataclass/TypedDict
- Side effects hidden behind innocent names like `get_*` that also write DB

---


## Worked example: prompt builder

```python
def build_prompt(
    question: str,
    contexts: list[str],
    *,
    max_contexts: int = 4,
    system: str = "Answer using only the context.",
) -> str:
    chosen = contexts[:max_contexts]
    context_block = "\n\n".join(
        f"[{i}] {c}" for i, c in enumerate(chosen, 1)
    )
    return (
        f"{system}\n\n"
        f"Context:\n{context_block}\n\n"
        f"Question: {question.strip()}\n"
        f"Answer:"
    )

print(build_prompt("What is RAG?", ["Retrieval...", "Generation..."]))
```

## Exercises

1. Write `clamp(x, lo, hi)` with type hints.
2. Demonstrate the mutable-default bug, then fix it.
3. Write a function returning `(mean, stdev)` via tuple unpacking.


## Continue

- **Previous:** [Loops](05-loops.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [Scope & Namespaces](07-scope-namespaces.md)
- **AI production guide:** [Python for AI Engineering](../python-for-ai-engineering.md)
