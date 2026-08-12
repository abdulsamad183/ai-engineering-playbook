---
title: "Lambda Functions"
description: "Small anonymous functions with lambda — where they shine and where a def is clearer."
domain: python-engineering
tags: [python, lambda, functional, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-12
version: "1.1"
---

# Lambda Functions

> Small anonymous functions with lambda — where they shine and where a def is clearer.

## Definition

A **lambda** is a small **anonymous function** expressed as a single expression:

`lambda parameters: expression`

It returns the expression’s value. Lambdas cannot contain statements (`if` blocks, assignments as statements, etc.).

## Uses

- Short `key=` functions for `sort` / `min` / `max`
- Tiny callbacks in `map` / `filter` (or prefer comprehensions)
- Inline adapters when defining a full `def` is noisier

## Types / forms

| Form | Example |
|------|---------|
| One arg | `lambda x: x*2` |
| Multi arg | `lambda a, b: a+b` |
| No arg | `lambda: 42` |
| With default | `lambda x, n=1: x+n` |

## Code examples

```python
double = lambda x: x * 2
print(double(5))

# Sorting
rows = [{"name": "b", "score": 0.2}, {"name": "a", "score": 0.9}]
rows.sort(key=lambda r: r["score"], reverse=True)
print(rows)

# Often clearer with operator.itemgetter
from operator import itemgetter
rows.sort(key=itemgetter("name"))
```

```python
# In map/filter — comprehension often clearer
nums = [1, 2, 3, 4]
print(list(map(lambda n: n * n, nums)))
print([n * n for n in nums])              # preferred by many style guides
```

```python
# Closure late-binding trap
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])               # [2, 2, 2]

funcs = [lambda i=i: i for i in range(3)] # bind default at creation
print([f() for f in funcs])               # [0, 1, 2]
```

```python
# When to use def instead
def normalize(score: float) -> float:
    """Clamp score into [0, 1]."""
    if score < 0:
        return 0.0
    if score > 1:
        return 1.0
    return score

# Multi-branch logic does not belong in lambda
```

## Limitations

- Single expression only
- No type-hint-friendly signature as nice as `def` (can annotate awkwardly)
- Harder to debug (anonymous in stack traces)

## Style rule

If you need a name, docstring, types, or more than one expression → use `def`.

---

## Continue

- **Previous:** [Generators](15-generators.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [`map()`, `filter()`, `reduce()`](17-map-filter-reduce.md)
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

