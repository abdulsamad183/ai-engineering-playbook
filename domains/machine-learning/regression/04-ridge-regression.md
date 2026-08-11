---
title: "4. Ridge Regression"
description: "L2 regularization — shrink coefficients, keep all features."
domain: machine-learning
tags: [regression, ridge]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 4. Ridge Regression

> L2 regularization — shrink coefficients, keep all features.

## Definition

**Ridge** minimizes MSE + \(\alpha \|w\|_2^2\). Shrinks weights; handles multicollinearity better than OLS.

## Code

```python
from sklearn.linear_model import Ridge

model = Ridge(alpha=1.0)
model.fit(X_train, y_train)
```

## When to use

- Many correlated features  
- You want all features kept (vs Lasso sparsity)  

## See also

- [Regularization](../model-optimization/05-regularization.md)

---

## Continue

- **Section hub:** [Regression](README.md)
- **ML overview:** [Machine Learning](../README.md)
