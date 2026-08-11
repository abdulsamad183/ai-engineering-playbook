---
title: "7. Cross-Validation"
description: "Rotate validation folds — stabler estimates and safer tuning."
domain: machine-learning
tags: [evaluation, cross-validation]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 7. Cross-Validation

> Rotate validation folds — stabler estimates and safer tuning.

## Definition

**Cross-validation (CV)** splits data into K folds; each fold is validation once while the rest trains. Reports mean ± std of the metric.

## Code

```python
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

scores = cross_val_score(RandomForestClassifier(n_estimators=100), X, y, cv=5, scoring="f1")
print(scores.mean(), scores.std())
```

## Variants

| Variant | When |
|---------|------|
| K-fold | Default i.i.d. |
| Stratified | Classification imbalance |
| TimeSeriesSplit | Temporal data |
| GroupKFold | Group leakage risk |

## Common mistakes

- Preprocessing fit outside the CV loop (leakage)

---

## Continue

- **Section hub:** [Model Evaluation](README.md)
- **ML overview:** [Machine Learning](../README.md)
