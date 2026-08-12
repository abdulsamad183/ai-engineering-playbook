---
title: "Lists"
description: "Ordered, mutable sequences — creating, indexing, slicing, methods, copying, and list algorithms."
domain: python-engineering
tags: [python, lists, collections, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-12
version: "1.1"
---

# Lists

> Ordered, mutable sequences — creating, indexing, slicing, methods, copying, and list algorithms.

## Definition

A **list** is an **ordered, mutable sequence** that can hold heterogeneous objects. Lists are the workhorse collection for dynamic ordered data.

## Uses

- Batches of records, messages, chunks
- Stacks/queues (with care)
- Accumulating results during processing

## Characteristics

| Property | List |
|----------|------|
| Ordered | Yes |
| Mutable | Yes |
| Indexed | Yes (`O(1)` access) |
| Allow duplicates | Yes |
| Allow mixed types | Yes (prefer homogeneity in practice) |

## Code examples

```python
xs = [10, 20, 30]
xs.append(40)             # add at end
xs.insert(1, 15)          # insert at index
xs.extend([50, 60])       # add many
print(xs.pop())           # remove & return last
xs.remove(15)             # remove first matching value
print(xs)
print(xs[0], xs[-1], xs[1:3])
```

```python
# Sorting
scores = [0.2, 0.9, 0.5]
print(sorted(scores))           # new list
scores.sort(reverse=True)       # in-place
print(scores)

rows = [{"id": 2, "s": 0.1}, {"id": 1, "s": 0.8}]
rows.sort(key=lambda r: r["s"], reverse=True)
print(rows)
```

```python
# Copying
a = [[1], [2]]
b = a                 # alias
c = a.copy()          # shallow copy
import copy
d = copy.deepcopy(a)  # deep copy
a[0].append(99)
print(b, c, d)        # b&c see inner change; d does not
```

```python
# As stack / queue
stack = []
stack.append("a"); stack.append("b")
print(stack.pop())                # LIFO → b

from collections import deque
q = deque(["a", "b"])
q.append("c")
print(q.popleft())                # FIFO → a
```

```python
# Idiomatic building
chunks = []
for i in range(3):
    chunks.append(f"chunk-{i}")
# Prefer comprehension when mapping/filtering simply (topic 13)
```

## Complexity (amortized)

| Op | Cost |
|----|------|
| Index / append | O(1) |
| Insert/pop front | O(n) |
| Membership `x in list` | O(n) — use set if frequent |

## Common mistakes

- `list = ...` shadowing built-in
- Shallow copy when nested mutables need isolation
- Using lists for heavy membership tests

---


## Worked example: top-k hits

```python
hits = [
    {"id": "a", "score": 0.4},
    {"id": "b", "score": 0.9},
    {"id": "c", "score": 0.7},
]

def top_k(rows: list[dict], k: int) -> list[dict]:
    ranked = sorted(rows, key=lambda r: r["score"], reverse=True)
    return ranked[:k]

print(top_k(hits, 2))
```

## Exercises

1. Implement stack push/pop with a list.
2. Deduplicate a list while preserving order.
3. Flatten a list of lists without comprehensions, then with them.


## Continue

- **Previous:** [Strings](08-strings.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [Tuples](10-tuples.md)
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

