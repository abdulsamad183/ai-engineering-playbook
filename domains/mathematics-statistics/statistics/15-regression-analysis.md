---
title: "15. Regression Analysis"
description: "Predict continuous targets — linear regression, residuals, and fit diagnostics."
domain: mathematics-statistics
tags: [statistics, regression]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 15. Regression Analysis

> Predict continuous targets — linear regression, residuals, and fit diagnostics.

## Definition

**Regression** models a target y as a function of inputs x. **Linear regression** uses y ≈ Xw + b and is the baseline every ML stack should beat.

## Key ideas

| Idea | Meaning |
|------|---------|
| Coefficients | Effect sizes |
| Residuals | y − ŷ |
| R² | Variance explained |
| OLS | Ordinary least squares |
| Regularization | Ridge/Lasso (bias–variance) |

## Code

```python
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(100, 1))
y = 3.0 * X[:, 0] + 2.0 + rng.normal(scale=0.3, size=100)

# closed-form with bias column
Xb = np.c_[np.ones(len(X)), X]
w, *_ = np.linalg.lstsq(Xb, y, rcond=None)
y_hat = Xb @ w
rmse = np.sqrt(np.mean((y - y_hat) ** 2))
print("weights", w, "rmse", rmse)
```

## Uses

- Baselines before complex models  
- Calibrating scores  
- Interpretable business drivers  

## See also

- [18. Statistical Modeling](18-statistical-modeling.md) · [Machine Learning](../../machine-learning/README.md)

---

## Continue

- **Section hub:** [Statistics](README.md)
- **Math & Stats overview:** [Mathematics & Statistics](../README.md)
