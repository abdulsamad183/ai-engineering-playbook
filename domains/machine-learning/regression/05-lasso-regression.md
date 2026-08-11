---
title: "5. Lasso Regression"
description: "L1 regularization — sparse models that zero out weak features."
domain: machine-learning
tags: [regression, lasso]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 5. Lasso Regression

> L1 regularization — sparse models that zero out weak features.

## Definition

**Lasso** minimizes MSE + \(\alpha \|w\|_1\). Drives some coefficients exactly to zero → built-in feature selection.

## Code

```python
from sklearn.linear_model import Lasso

model = Lasso(alpha=0.01, max_iter=5000)
model.fit(X_train, y_train)
print((model.coef_ != 0).sum(), "nonzero coeffs")
```

## When to use

- Want sparse, interpretable subset of features  
- p large relative to n  

## Common mistakes

- Unstable feature selection with correlated groups (prefer Elastic Net)

---

## Continue

- **Section hub:** [Regression](README.md)
- **ML overview:** [Machine Learning](../README.md)
