---
title: "1. Feature Scaling"
description: "Standardize or normalize numerics so distance and gradient methods behave."
domain: machine-learning
tags: [feature-engineering, scaling]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 1. Feature Scaling

> Standardize or normalize numerics so distance and gradient methods behave.

## Definition

**Feature scaling** puts numeric features on comparable scales (standardize, min-max, robust).

## Methods

| Method | Transform |
|--------|-----------|
| StandardScaler | (x − mean) / std |
| MinMaxScaler | to [0, 1] |
| RobustScaler | median / IQR |

## Code

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)  # fit on train only
```

## Needed for

- k-NN, SVM, logistic/linear with regularization, PCA, k-means  
- Trees/GBDT usually less sensitive

---

## Continue

- **Section hub:** [Feature Engineering](README.md)
- **ML overview:** [Machine Learning](../README.md)
