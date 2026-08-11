---
title: "Pandas: Merge, Join & Concat"
description: "Combine tables — SQL-style joins and stacking."
domain: python-frameworks-libraries
tags: [pandas, merge]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Pandas: Merge, Join & Concat

> Combine tables — SQL-style joins and stacking.

## Definition

- **`concat`**: stack DataFrames (rows/cols)
- **`merge`**: join on keys (SQL-like)
- **`join`**: index-based join helper

## Important functions

| Function | Use |
|----------|-----|
| `pd.concat` | Axis-wise stack |
| `pd.merge` | Key joins |
| `how=` | `inner`, `left`, `right`, `outer` |
| `on=` / `left_on` / `right_on` | Keys |

## Code

```python
import pandas as pd

preds = pd.DataFrame({"id": [1, 2, 3], "pred": [1, 0, 1]})
labels = pd.DataFrame({"id": [1, 2, 4], "label": [1, 1, 0]})
print(pd.merge(preds, labels, on="id", how="inner"))
print(pd.concat([preds.head(1), preds.tail(1)], ignore_index=True))
```

## Uses

- Join predictions to golden labels
- Append monthly log extracts
- Enrich traces with metadata tables

---

## Continue

- **Hub:** [Pandas hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
