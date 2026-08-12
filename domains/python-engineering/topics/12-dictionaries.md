---
title: "Dictionaries"
description: "Key–value maps — the central data structure for records, configs, JSON-like data, and fast lookups."
domain: python-engineering
tags: [python, dicts, collections, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-12
version: "1.1"
---

# Dictionaries

> Key–value maps — the central data structure for records, configs, JSON-like data, and fast lookups.

## Definition

A **dictionary** (`dict`) maps **hashable keys** to **values**. In modern CPython (3.7+), dicts preserve insertion order.

## Uses

- JSON-like objects and API payloads
- Indexes: `id → record`
- Configuration and feature flags
- Counting and grouping (`Counter`, `defaultdict`)

## Characteristics

| Property | Dict |
|----------|------|
| Keys unique | Yes |
| Keys hashable | Required |
| Values any object | Yes |
| Lookup by key | Average O(1) |
| Ordered (3.7+) | Insertion order |

## Code examples

```python
user = {"id": 1, "name": "Samad", "roles": ["admin"]}
print(user["name"])
print(user.get("email"))              # None if missing
print(user.get("email", "n/a"))

user["email"] = "a@b.com"             # insert/update
user.setdefault("plan", "free")      # set if absent
print(user.keys(), user.values())

for k, v in user.items():
    print(k, "=>", v)
```

```python
# Merging (3.9+| )
defaults = {"temperature": 0.2, "max_tokens": 512}
overrides = {"temperature": 0.0}
cfg = defaults | overrides
print(cfg)

# unpacking merge
cfg2 = {**defaults, **overrides}
```

```python
from collections import defaultdict, Counter

# Grouping
rows = [("a", 1), ("b", 2), ("a", 3)]
groups = defaultdict(list)
for k, v in rows:
    groups[k].append(v)
print(dict(groups))

# Counting
print(Counter(["rag", "rag", "agent"]))
```

```python
# Dict comprehension
scores = {"a": 0.9, "b": 0.2, "c": 0.7}
passed = {k: v for k, v in scores.items() if v >= 0.5}
print(passed)
```

```python
# JSON round-trip pattern
import json
payload = {"query": "what is rag?", "k": 5}
raw = json.dumps(payload)
back = json.loads(raw)
print(back["k"])
```

## Common mistakes

- `KeyError` — use `.get` or `in` checks
- Using unhashable keys (`list`)
- Mutating dict while iterating keys (iterate over `list(d)`)

---


## Worked example: inverted index sketch

```python
docs = {
    "d1": "rag retrieval generation",
    "d2": "agents tools planning",
}

inverted: dict[str, set[str]] = {}
for doc_id, text in docs.items():
    for token in text.split():
        inverted.setdefault(token, set()).add(doc_id)

print(sorted(inverted["rag"]))   # ['d1']
print(inverted.get("tools"))     # {'d2'}
```

## Exercises

1. Merge two config dicts with overrides winning.
2. Count word frequencies with `Counter`.
3. Invert a dict safely (detect collisions).


## Continue

- **Previous:** [Sets](11-sets.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [List/Set/Dictionary Comprehensions](13-comprehensions.md)
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

