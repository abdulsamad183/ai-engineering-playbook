---
title: "6. Elastic Net Regression"
description: "Mix of L1 and L2 — sparsity with group-friendly shrinkage."
domain: machine-learning
tags: [regression, elastic-net]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 6. Elastic Net Regression

> Mix of L1 and L2 — sparsity with group-friendly shrinkage.

## Definition

**Elastic Net** combines L1 and L2 penalties. Often more stable than Lasso when features are correlated.

## Code

```python
from sklearn.linear_model import ElasticNet

model = ElasticNet(alpha=0.01, l1_ratio=0.5, max_iter=5000)
model.fit(X_train, y_train)
```

## Hyperparameters

| Param | Role |
|-------|------|
| `alpha` | Overall strength |
| `l1_ratio` | 1 → Lasso-like, 0 → Ridge-like |

---

## Continue

- **Section hub:** [Regression](README.md)
- **ML overview:** [Machine Learning](../README.md)
