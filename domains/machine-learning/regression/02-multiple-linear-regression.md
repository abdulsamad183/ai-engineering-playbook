---
title: "2. Multiple Linear Regression"
description: "Same linear model with many features — interpretation and multicollinearity."
domain: machine-learning
tags: [regression, multiple-linear]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 2. Multiple Linear Regression

> Same linear model with many features — interpretation and multicollinearity.

## Definition

**Multiple linear regression** is linear regression with \(p > 1\) predictors. Same math; harder interpretation when features correlate.

## Practical checklist

1. Scale features if comparing coefficient magnitudes  
2. Check VIF / correlations for multicollinearity  
3. Prefer regularization when p is large  

## Code

```python
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

pipe = make_pipeline(StandardScaler(), LinearRegression())
pipe.fit(X_train, y_train)
```

## See also

- [Ridge](04-ridge-regression.md) · [Feature Scaling](../feature-engineering/01-feature-scaling.md)

---

## Continue

- **Section hub:** [Regression](README.md)
- **ML overview:** [Machine Learning](../README.md)
