---
title: "6. Handling Missing Values"
description: "Drop, impute, or model — and when missingness itself is a signal."
domain: machine-learning
tags: [feature-engineering, missing]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 6. Handling Missing Values

> Drop, impute, or model — and when missingness itself is a signal.

## Definition

Missing data can be dropped, imputed (mean/median/mode/model), or handled natively (trees/XGBoost). Often add a missing indicator.

## Code

```python
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

imp = SimpleImputer(strategy="median")
X_num = imp.fit_transform(X_train_num)
```

## Common mistakes

- Imputing with statistics computed on train+test  
- Ignoring MNAR patterns that carry information

---

## Continue

- **Section hub:** [Feature Engineering](README.md)
- **ML overview:** [Machine Learning](../README.md)
