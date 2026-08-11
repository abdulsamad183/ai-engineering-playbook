---
title: "Pandas: Series & DataFrame"
description: "Core classes — labeled 1D and 2D data structures."
domain: python-frameworks-libraries
tags: [pandas, dataframe]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Pandas: Series & DataFrame

> Core classes — labeled 1D and 2D data structures.

## Definition

- **`Series`**: 1D labeled array (index + values)
- **`DataFrame`**: 2D table (rows index + named columns)

## Key classes

| Class | Role |
|-------|------|
| `pandas.Series` | Single column / vector |
| `pandas.DataFrame` | Table |
| `pandas.Index` | Label axis |

## Important attributes / properties

| Name | Meaning |
|------|---------|
| `shape`, `dtypes`, `columns`, `index` | Structure |
| `head`, `tail`, `info`, `describe` | Inspection |
| `values` / `to_numpy()` | NumPy backing |

## Code

```python
import pandas as pd

s = pd.Series([0.9, 0.2, 0.7], index=["a", "b", "c"], name="score")
print(s["b"], s.mean())

df = pd.DataFrame({
    "query": ["what is rag?", "define agent"],
    "score": [0.9, 0.6],
    "passed": [True, False],
})
print(df.shape, df.dtypes)
print(df.head())
print(df.describe(include="all"))
```

## Uses

- Hold eval rows
- Feature tables before sklearn
- Intermediate analytics on logs

---

## Continue

- **Hub:** [Pandas hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
