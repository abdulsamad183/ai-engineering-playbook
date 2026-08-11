---
title: "7. Optimization"
description: "How models learn — gradient steps, closed form, and tree greediness."
domain: machine-learning
tags: [ml-basics, optimization]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 7. Optimization

> How models learn — gradient steps, closed form, and tree greediness.

## Definition

**Optimization** finds parameters that minimize loss. Classical ML uses closed-form solutions, convex solvers, coordinate descent, or greedy tree splitting — not only SGD.

## Approaches

| Approach | Used by |
|----------|---------|
| Closed form / normal equations | OLS linear regression |
| Gradient / Newton | Logistic, GLM |
| Coordinate descent | Lasso / Elastic Net |
| Quadratic programming | SVM |
| Greedy impurity decrease | Decision trees |
| SGD / Adam | Large / neural models |

## Code (gradient step)

```python
import numpy as np

w = np.zeros(3)
lr = 0.1
# toy: minimize ||Xw - y||^2
grad = X.T @ (X @ w - y) / len(y)
w = w - lr * grad
```

## See also

- [Optimization for ML](../../mathematics-statistics/ml-oriented/22-optimization-for-ml.md)

---

## Continue

- **Section hub:** [ML Basics](README.md)
- **ML overview:** [Machine Learning](../README.md)
