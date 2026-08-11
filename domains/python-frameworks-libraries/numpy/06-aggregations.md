---
title: "NumPy: Aggregations"
description: "sum, mean, std, min/max, argmin/argmax, quantiles — whole array or per axis."
domain: python-frameworks-libraries
tags: [numpy, aggregations]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# NumPy: Aggregations

> sum, mean, std, min/max, argmin/argmax, quantiles — whole array or per axis.

## Definition

**Aggregations** reduce an array to a scalar or to a smaller array by collapsing one or more axes.

## Important functions

| Function | Use |
|----------|-----|
| `sum`, `mean`, `std`, `var` | Moments |
| `min`, `max` | Extrema |
| `argmin`, `argmax` | Index of extrema |
| `percentile` / `quantile` | Distribution |
| `any`, `all` | Boolean reduce |
| `cumsum`, `cumprod` | Prefix aggregates |

## Code

```python
import numpy as np

scores = np.array([[0.9, 0.1], [0.4, 0.6], [0.8, 0.2]])
print(scores.mean())              # global
print(scores.mean(axis=0))        # per column
print(scores.argmax(axis=1))      # best class per row

x = np.array([1.0, 2.0, 100.0])
print(np.median(x), np.percentile(x, 90))
```

## Uses

- Batch metrics
- Top-class prediction via `argmax`
- Outlier-aware stats with percentiles

---

## Continue

- **Hub:** [NumPy hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
