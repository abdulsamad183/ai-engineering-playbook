---
title: "3. Time Series"
description: "Ordered data — lags, leakage-safe splits, and forecasting basics."
domain: machine-learning
tags: [misc, time-series]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 3. Time Series

> Ordered data — lags, leakage-safe splits, and forecasting basics.

## Definition

**Time series** observations are ordered in time. Autocorrelation, seasonality, and leakage-safe validation dominate design.

## Essentials

| Idea | Practice |
|------|----------|
| Lags / rolling | Features from the past only |
| Split | Time-based / TimeSeriesSplit |
| Models | ARIMA, ETS, gradient boosting on lags, seq models |
| Metrics | MAE, MAPE, sMAPE, quantile loss |

## Code

```python
import pandas as pd

df = df.sort_values("ts")
df["lag_1"] = df["y"].shift(1)
df["roll_7"] = df["y"].shift(1).rolling(7).mean()
```

## Common mistakes

- Random K-fold across time (leakage)  
- Scaling using future statistics

---

## Continue

- **Section hub:** [Miscellaneous ML](README.md)
- **ML overview:** [Machine Learning](../README.md)
