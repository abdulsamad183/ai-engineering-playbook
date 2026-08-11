---
title: "1. Bagging"
description: "Bootstrap aggregating — average many models to cut variance."
domain: machine-learning
tags: [ensemble, bagging]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 1. Bagging

> Bootstrap aggregating — average many models to cut variance.

## Definition

**Bagging** trains models on bootstrap samples of the data and aggregates predictions (vote / average). Reduces variance of unstable base learners (e.g. deep trees).

## Code

```python
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

clf = BaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators=50,
    random_state=42,
)
clf.fit(X_train, y_train)
```

## Intuition

```mermaid
flowchart LR
  D[Data] --> B1[Bootstrap 1]
  D --> B2[Bootstrap 2]
  D --> Bn[Bootstrap n]
  B1 --> M1[Model]
  B2 --> M2[Model]
  Bn --> Mn[Model]
  M1 --> A[Aggregate]
  M2 --> A
  Mn --> A
```

---

## Continue

- **Section hub:** [Ensemble Learning](README.md)
- **ML overview:** [Machine Learning](../README.md)
