---
title: "Sets"
description: "Unordered collections of unique hashable items — membership, algebra, and deduplication."
domain: python-engineering
tags: [python, sets, collections, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Sets

> Unordered collections of unique hashable items — membership, algebra, and deduplication.

## Definition

A **set** is an **unordered collection of unique hashable elements**. Membership tests and deduplication are typically much faster than with lists (`O(1)` average).

`frozenset` is an immutable set (hashable; can be a dict key).

## Uses

- Deduplicate IDs/tokens
- Fast membership (`if user_id in allowed`)
- Set algebra: intersection/union for tags, permissions, vocabularies

## Types

| Type | Mutable | Hashable |
|------|---------|----------|
| `set` | Yes | No |
| `frozenset` | No | Yes |

## Code examples

```python
skills = {"python", "rag", "python"}
print(skills)                      # {"python", "rag"}

skills.add("agents")
skills.discard("missing")          # no error if absent
print("rag" in skills)             # True fast membership
```

```python
a = {1, 2, 3}
b = {3, 4}
print(a | b)                       # union
print(a & b)                       # intersection
print(a - b)                       # difference
print(a ^ b)                       # symmetric difference
print(a <= {1, 2, 3, 4})           # subset
```

```python
# Deduplicate while preserving order (dict trick 3.7+)
items = ["a", "b", "a", "c"]
unique_ordered = list(dict.fromkeys(items))
print(unique_ordered)
```

```python
# frozenset as dict key
groups = {
    frozenset(["admin", "user"]): "mixed",
    frozenset(["admin"]): "admins",
}
print(groups[frozenset(["user", "admin"])])
```

```python
# Only hashables allowed
# {{1, 2}}           # TypeError
ok = { (1, 2), (3, 4) }            # tuples of immutables OK
```

## Common mistakes

- Relying on set iteration order for logic (order is insertion-based but treat as unordered conceptually)
- Putting lists inside sets
- Using sets when you need counts → `collections.Counter`

---

## Continue

- **Previous:** [Tuples](10-tuples.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [Dictionaries](12-dictionaries.md)
- **AI production guide:** [Python for AI Engineering](../python-for-ai-engineering.md)
