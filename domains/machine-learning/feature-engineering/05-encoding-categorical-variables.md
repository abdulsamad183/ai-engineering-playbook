---
title: "5. Encoding Categorical Variables"
description: "One-hot, ordinal, target, and hashing — match cardinality and model."
domain: machine-learning
tags: [feature-engineering, encoding]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 5. Encoding Categorical Variables

> One-hot, ordinal, target, and hashing — match cardinality and model.

## Definition

**Encoding** maps categories to numbers models can consume.

## Options

| Encoder | When |
|---------|------|
| One-hot | Low cardinality, linear models |
| Ordinal | True order |
| Target / OOF | High cardinality (careful leakage) |
| Hashing | Huge cardinality |
| Native cat | CatBoost / LightGBM |

## Code

```python
from sklearn.preprocessing import OneHotEncoder

enc = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
X_cat = enc.fit_transform(df_train[["country"]])
```

---

## Continue

- **Section hub:** [Feature Engineering](README.md)
- **ML overview:** [Machine Learning](../README.md)
