---
title: "Tuples"
description: "Immutable ordered sequences — records, multiple returns, dictionary keys, and tuple unpacking."
domain: python-engineering
tags: [python, tuples, collections, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Tuples

> Immutable ordered sequences — records, multiple returns, dictionary keys, and tuple unpacking.

## Definition

A **tuple** is an **ordered, immutable sequence**. After creation, you cannot add/remove/change elements (but mutable objects *inside* a tuple can still mutate).

## Uses

- Fixed records `(x, y)`
- Multiple return values
- Dict keys / set elements (if contents are hashable)
- Safer public APIs (“don’t mutate this”)

## Tuple vs list

| | Tuple | List |
|---|-------|------|
| Mutable | No | Yes |
| Syntax | `(1, 2)` | `[1, 2]` |
| Hashable | If elements are | No |
| Intent | Fixed structure | Grow/shrink |

## Code examples

```python
point = (3, 4)
# parentheses optional in many assignments:
point2 = 3, 4
singleton = (42,)         # trailing comma required for 1-tuple
empty = ()

print(point[0], len(point))
x, y = point              # unpacking
print(x, y)
```

```python
def min_max(xs: list[int]) -> tuple[int, int]:
    return min(xs), max(xs)

lo, hi = min_max([3, 1, 7])
print(lo, hi)
```

```python
# Tuple as dict key
locations = {
    (0, 0): "origin",
    (1, 2): "A",
}
print(locations[(1, 2)])
```

```python
# Immutable container, mutable content
t = ([1, 2], [3, 4])
t[0].append(99)           # allowed — list inside changes
print(t)
# t[0] = [0]              # TypeError — cannot rebind slot
```

```python
# namedtuple / typing.NamedTuple for clarity
from typing import NamedTuple

class Chunk(NamedTuple):
    doc_id: str
    text: str
    score: float

c = Chunk("d1", "hello", 0.9)
print(c.text, c.score)
```

## Common mistakes

- Forgetting comma in singleton `(42)` is just `42`
- Expecting tuples to deep-freeze contents

---

## Continue

- **Previous:** [Lists](09-lists.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [Sets](11-sets.md)
- **AI production guide:** [Python for AI Engineering](../python-for-ai-engineering.md)
