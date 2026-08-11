---
title: "1. Linear Regression"
description: "Predict continuous y as a weighted sum of features — the classic baseline."
domain: machine-learning
tags: [regression, linear]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 1. Linear Regression

> Predict continuous y as a weighted sum of features — the classic baseline.

## Definition

**Linear regression** models \(y \approx w^\top x + b\). Fit by least squares (closed form or gradient methods).

## Key ideas

| Idea | Meaning |
|------|---------|
| Coefficients | Effect of each feature |
| Intercept | Baseline when x=0 |
| Residuals | y − ŷ |
| Assumptions | Linearity, noise roughly i.i.d. |

## Code

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
print(model.coef_, model.intercept_)
print(model.score(X_test, y_test))  # R²
```

## Uses

- Strong tabular baseline  
- Interpretable effect sizes  
- Residual analysis for feature gaps  

## Common mistakes

- Multicollinearity without care  
- Extrapolating far outside training range

---

## Continue

- **Section hub:** [Regression](README.md)
- **ML overview:** [Machine Learning](../README.md)
