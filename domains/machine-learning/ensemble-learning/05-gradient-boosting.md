---
title: "5. Gradient Boosting"
description: "Fit trees to loss gradients — the workhorse behind modern tabular ML."
domain: machine-learning
tags: [ensemble, gradient-boosting]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 5. Gradient Boosting

> Fit trees to loss gradients — the workhorse behind modern tabular ML.

## Definition

**Gradient boosting** adds models that approximate the negative gradient of the loss w.r.t. current predictions (functional gradient descent).

## Code

```python
from sklearn.ensemble import GradientBoostingClassifier

clf = GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42,
)
clf.fit(X_train, y_train)
```

## Key knobs

| Param | Effect |
|-------|--------|
| `n_estimators` | More trees |
| `learning_rate` | Shrink each step |
| `max_depth` | Tree complexity |

## See also

- [XGBoost](06-xgboost.md) · [Early Stopping](../model-optimization/06-early-stopping.md)

---

## Continue

- **Section hub:** [Ensemble Learning](README.md)
- **ML overview:** [Machine Learning](../README.md)
