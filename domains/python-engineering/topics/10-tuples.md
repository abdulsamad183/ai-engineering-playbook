---
title: "Tuples"
description: "Immutable ordered sequences — records, multiple returns, dictionary keys, and tuple unpacking."
domain: python-engineering
tags: [python, tuples, collections, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-12
version: "1.1"
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

