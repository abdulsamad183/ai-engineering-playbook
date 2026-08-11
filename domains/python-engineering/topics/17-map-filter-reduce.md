---
title: "`map()`, `filter()`, `reduce()`"
description: "Functional helpers that transform and fold iterables — with idiomatic modern alternatives."
domain: python-engineering
tags: [python, functional, map, filter, reduce, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# `map()`, `filter()`, `reduce()`

> Functional helpers that transform and fold iterables — with idiomatic modern alternatives.

## Definition

- **`map(fn, iterable)`** — apply `fn` to each element (lazy iterator)
- **`filter(pred, iterable)`** — keep elements where `pred` is true (lazy)
- **`reduce(fn, iterable[, initializer])`** — repeatedly combine elements into one value (`functools.reduce`)

## Uses

- Functional pipelines over streams
- Folding counts/sums/products with custom logic
- Interop with codebases that prefer FP style

## Prefer comprehensions?

In modern Python, **list/dict comprehensions** and **generator expressions** are often clearer than `map`/`filter`. Know all three.

## Code examples

```python
nums = [1, 2, 3, 4]

# map
print(list(map(str, nums)))
print(list(map(lambda n: n * n, nums)))
print([n * n for n in nums])              # equivalent, often clearer
```

```python
# filter
print(list(filter(lambda n: n % 2 == 0, nums)))
print([n for n in nums if n % 2 == 0])
```

```python
from functools import reduce
import operator

print(reduce(lambda a, b: a + b, nums, 0))   # sum
print(reduce(operator.mul, nums, 1))         # product

# Usually prefer built-ins:
print(sum(nums), min(nums), max(nums))
```

```python
# Practical: normalize + filter scores
raw = ["0.9", "oops", "0.2", "1.1"]

def to_score(x: str) -> float | None:
    try:
        v = float(x)
    except ValueError:
        return None
    if 0 <= v <= 1:
        return v
    return None

scores = list(filter(lambda v: v is not None, map(to_score, raw)))
# clearer:
scores = [v for v in (to_score(x) for x in raw) if v is not None]
print(scores)
```

```python
# starmap for unpacking pairs
from itertools import starmap
pairs = [(2, 3), (4, 5)]
print(list(starmap(lambda a, b: a + b, pairs)))
```

## Comparison table

| Goal | Functional | Idiomatic alternative |
|------|------------|-----------------------|
| Transform | `map` | comprehension |
| Keep some | `filter` | comprehension + `if` |
| Fold | `reduce` | `sum`/`any`/`all`/loop |
| Side effects | avoid map | plain `for` |

## Common mistakes

- Forgetting `list(...)` when you need a concrete list (iterators are lazy)
- Using `reduce` for simple sums

---

## Continue

- **Previous:** [Lambda Functions](16-lambda-functions.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [Exception Handling](18-exception-handling.md)
- **AI production guide:** [Python for AI Engineering](../python-for-ai-engineering.md)
