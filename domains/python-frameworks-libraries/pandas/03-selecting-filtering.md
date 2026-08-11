---
title: "Pandas: Selecting & Filtering"
description: "loc, iloc, boolean masks, and column projection."
domain: python-frameworks-libraries
tags: [pandas, filtering]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Pandas: Selecting & Filtering

> loc, iloc, boolean masks, and column projection.

## Definition

**Selection** picks columns/rows; **filtering** keeps rows matching a condition. Prefer `.loc` (labels) and `.iloc` (positions).

## Important APIs

| API | Use |
|-----|-----|
| `df["col"]` / `df[["a","b"]]` | Columns |
| `df.loc[rows, cols]` | Label-based |
| `df.iloc[r, c]` | Position-based |
| Boolean mask | `df[df.score >= 0.5]` |
| `query` | String expressions |
| `isin` | Membership filter |

## Code

```python
import pandas as pd

df = pd.DataFrame({
    "model": ["a", "b", "a", "c"],
    "score": [0.9, 0.4, 0.7, 0.2],
})
print(df[["model", "score"]])
print(df.loc[df["score"] >= 0.5, ["model", "score"]])
print(df.query("score >= 0.5 and model == 'a'"))
print(df[df["model"].isin(["a", "c"])])
```

## Uses

- Slice failed eval cases
- Select feature columns for training
- Filter by model version

---

## Continue

- **Hub:** [Pandas hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
