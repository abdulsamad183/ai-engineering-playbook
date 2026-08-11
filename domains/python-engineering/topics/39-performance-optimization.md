---
title: "Performance Optimization"
description: "Make Python faster and leaner — measure first, then apply algorithmic, I/O, and runtime optimizations."
domain: python-engineering
tags: [python, performance, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Performance Optimization

> Make Python faster and leaner — measure first, then apply algorithmic, I/O, and runtime optimizations.

## Definition

**Performance optimization** improves latency, throughput, or memory. Rule zero: **measure before optimizing**. Premature optimization wastes time and harms clarity.

## Uses

- Speed up batch embedding / ETL
- Cut p95 API latency
- Reduce memory for large corpora

## Process

```mermaid
flowchart LR
  M[Measure] --> B[Bottleneck]
  B --> F[Fix biggest win]
  F --> V[Verify with benchmarks]
  V --> M
```

## Tooling

```python
import timeit
print(timeit.timeit("sum(range(1000))", number=1000))

import cProfile
cProfile.run("sum(i*i for i in range(100000))")
```

## High-ROI techniques

| Technique | Example |
|-----------|---------|
| Better algorithm | O(n) set membership vs O(n²) list scans |
| Generators | Stream instead of materializing |
| Vectorization | NumPy/Pandas over pure Python loops |
| Caching | `lru_cache` for pure expensive funcs |
| Avoid repeated work | Compile regex once |
| I/O concurrency | asyncio / batching |

## Code examples

```python
hay = list(range(10000))
needle = 9999
fast = set(hay)
print(needle in fast)
```

```python
parts = []
for i in range(1000):
    parts.append(str(i))
s = "".join(parts)                 # good
```

```python
import re
CRE = re.compile(r"\d+")
print(CRE.findall("a1b22"))
```

## AI-specific tips

1. Batch embedding requests
2. Bound concurrency to the sweet spot (not max)
3. Cache retrieval for identical queries when safe
4. Don’t micro-optimize prompts while retrieval is the bottleneck

## Common mistakes

- Optimizing without a profiler
- Trading clarity for tiny gains
- Caching without TTLs → stale/wrong answers

---

## Continue

- **Previous:** [Python Internals](38-python-internals.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [Clean Code & Python Best Practices](40-clean-code-best-practices.md)
- **AI production guide:** [Python for AI Engineering](../python-for-ai-engineering.md)
