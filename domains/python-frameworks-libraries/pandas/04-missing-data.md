---
title: "Pandas: Missing Data"
description: "Detect, drop, and fill NaNs — critical for clean eval pipelines."
domain: python-frameworks-libraries
tags: [pandas, missing-data]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Pandas: Missing Data

> Detect, drop, and fill NaNs — critical for clean eval pipelines.

## Definition

Missing values appear as `NaN` / `NaT` / `None`. Pandas provides detection and remediation helpers.

## Important functions

| Function | Use |
|----------|-----|
| `isna` / `notna` | Detect |
| `dropna` | Remove rows/cols |
| `fillna` | Impute |
| `replace` | Value mapping |

## Code

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({"q": ["a", "b", None], "score": [0.9, np.nan, 0.5]})
print(df.isna().sum())
print(df.dropna(subset=["q"]))
print(df.fillna({"score": 0.0, "q": ""}))
```

## Practices

- Decide missing policy explicitly (drop vs fill vs flag)
- Don’t silently fill labels for supervised eval

---

## Continue

- **Hub:** [Pandas hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
