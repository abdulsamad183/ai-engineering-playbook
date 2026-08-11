---
title: "Pandas: Apply & Transforms"
description: "Column assignment, map/apply, assign, and vectorized string ops."
domain: python-frameworks-libraries
tags: [pandas, transforms]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Pandas: Apply & Transforms

> Column assignment, map/apply, assign, and vectorized string ops.

## Definition

**Transforms** create or modify columns. Prefer vectorized ops; use `apply` when logic is custom.

## Important APIs

| API | Use |
|-----|-----|
| `df["c"] = ...` | Assign column |
| `assign` | Fluent new columns |
| `map` | Series value map |
| `apply` | Row/column function |
| `astype` | Cast dtype |
| `.str` | String accessor |
| `.dt` | Datetime accessor |

## Code

```python
import pandas as pd

df = pd.DataFrame({"text": ["  Hello ", "RAG"], "score": ["0.9", "0.2"]})
df = df.assign(
    text=lambda d: d["text"].str.strip().str.lower(),
    score=lambda d: d["score"].astype(float),
    passed=lambda d: d["score"] >= 0.5,
)
print(df)

# apply (row-wise) — slower; use sparingly
df["len"] = df["text"].apply(len)
print(df)
```

## Uses

- Normalize text fields
- Parse score columns
- Derive pass/fail flags for eval

---

## Continue

- **Hub:** [Pandas hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
