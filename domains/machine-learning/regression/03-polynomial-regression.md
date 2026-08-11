---
title: "3. Polynomial Regression"
description: "Linear in parameters, nonlinear in x — via polynomial feature expansion."
domain: machine-learning
tags: [regression, polynomial]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 3. Polynomial Regression

> Linear in parameters, nonlinear in x — via polynomial feature expansion.

## Definition

**Polynomial regression** adds powers/interactions of features, then fits a linear model in that expanded space.

## Code

```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

model = make_pipeline(PolynomialFeatures(degree=3, include_bias=False), LinearRegression())
model.fit(X_train, y_train)
```

## Tradeoffs

| Degree | Risk |
|--------|------|
| Too low | Underfit curves |
| Too high | Wild oscillation / overfit |

## Common mistakes

- High degree without regularization or enough data

---

## Continue

- **Section hub:** [Regression](README.md)
- **ML overview:** [Machine Learning](../README.md)
