---
title: "1. Regression Metrics"
description: "MSE, RMSE, MAE, R² — pick metrics that match the cost of error."
domain: machine-learning
tags: [evaluation, regression-metrics]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 1. Regression Metrics

> MSE, RMSE, MAE, R² — pick metrics that match the cost of error.

## Definition

**Regression metrics** score continuous predictions against true values.

## Common metrics

| Metric | Notes |
|--------|-------|
| MAE | Average absolute error; robust-ish |
| MSE / RMSE | Penalizes large errors |
| R² | Variance explained (can be misleading) |
| MAPE | % error; careful near zero targets |

## Code

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred) ** 0.5
r2 = r2_score(y_test, y_pred)
```

---

## Continue

- **Section hub:** [Model Evaluation](README.md)
- **ML overview:** [Machine Learning](../README.md)
