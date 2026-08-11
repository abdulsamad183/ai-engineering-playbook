---
title: "8. Descriptive Statistics"
description: "Summarize data — center, spread, shape, and visualization of samples."
domain: mathematics-statistics
tags: [statistics, descriptive]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 8. Descriptive Statistics

> Summarize data — center, spread, shape, and visualization of samples.

## Definition

**Descriptive statistics** summarize a dataset without inferring about a larger population: center, spread, shape, and simple visuals.

## Key measures

| Measure | Meaning |
|---------|---------|
| Mean | Average |
| Median | 50th percentile |
| Mode | Most frequent |
| Variance / std | Spread |
| Range / IQR | Robust spread |
| Skewness / kurtosis | Shape |
| Percentiles | Distribution landmarks |

## Code

```python
import numpy as np

x = np.array([2, 4, 4, 4, 5, 5, 7, 9], dtype=float)
print("mean", x.mean())
print("median", np.median(x))
print("std", x.std(ddof=1))
print("q25/q75", np.percentile(x, [25, 75]))
```

## Uses

- Explore eval score distributions  
- Detect outliers before modeling  
- Report latency p50/p95/p99  

## Common mistakes

- Reporting only the mean on skewed data  
- Using population std (`ddof=0`) when sample std is intended

---

## Continue

- **Section hub:** [Statistics](README.md)
- **Math & Stats overview:** [Mathematics & Statistics](../README.md)
