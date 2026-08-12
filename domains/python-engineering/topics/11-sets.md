---
title: "Sets"
description: "Unordered collections of unique hashable items — membership, algebra, and deduplication."
domain: python-engineering
tags: [python, sets, collections, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-12
version: "1.1"
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

