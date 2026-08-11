---
title: "Pandas: Important APIs Cheat Sheet"
description: "High-frequency Pandas classes and methods for AI workflows."
domain: python-frameworks-libraries
tags: [pandas, cheatsheet]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Pandas: Important APIs Cheat Sheet

> High-frequency Pandas classes and methods for AI workflows.

## Classes

`Series`, `DataFrame`, `Index`

## Everyday methods

`head`, `info`, `describe`, `loc`, `iloc`, `isna`, `fillna`, `dropna`, `groupby`, `agg`, `merge`, `concat`, `sort_values`, `drop_duplicates`, `value_counts`, `assign`, `astype`

## Eval workflow sketch

```python
import pandas as pd

df = pd.DataFrame({
    "id": [1, 2, 3],
    "score": [0.9, 0.2, 0.7],
    "label": [1, 0, 1],
})
df["pred"] = (df["score"] >= 0.5).astype(int)
acc = (df["pred"] == df["label"]).mean()
print("accuracy", acc)
print(df.groupby("label")["score"].mean())
```

---

## Continue

- **Hub:** [Pandas hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
