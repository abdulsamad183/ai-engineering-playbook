---
title: "Pandas: GroupBy & Aggregation"
description: "Split–apply–combine for metrics by segment."
domain: python-frameworks-libraries
tags: [pandas, groupby]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Pandas: GroupBy & Aggregation

> Split–apply–combine for metrics by segment.

## Definition

**GroupBy** splits a DataFrame by key(s), applies aggregations, and combines results — the workhorse of analytics.

## Important APIs

| API | Use |
|-----|-----|
| `groupby(key)` | Split |
| `.agg(...)` | Multiple aggregations |
| `.size()` / `.count()` | Counts |
| `.value_counts()` | Frequency table |
| `pivot_table` | Spreadsheet-style pivot |

## Code

```python
import pandas as pd

df = pd.DataFrame({
    "model": ["a", "a", "b", "b"],
    "score": [0.9, 0.8, 0.4, 0.5],
    "latency_ms": [120, 110, 300, 280],
})
print(df.groupby("model")["score"].mean())
print(df.groupby("model").agg(
    avg_score=("score", "mean"),
    p95_latency=("latency_ms", lambda s: s.quantile(0.95)),
    n=("score", "size"),
))
```

## Uses

- Metrics by model / prompt version
- Error rates by route
- Segment analysis for regressions

---

## Continue

- **Hub:** [Pandas hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
