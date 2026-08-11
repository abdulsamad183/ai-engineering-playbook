---
title: "13. Confidence Intervals"
description: "Range estimates that quantify uncertainty around a parameter."
domain: mathematics-statistics
tags: [statistics, confidence-intervals]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 13. Confidence Intervals

> Range estimates that quantify uncertainty around a parameter.

## Definition

A **confidence interval (CI)** is a range computed from a sample such that, under repeated sampling, a stated fraction (e.g. 95%) of such intervals would cover the true parameter.

## Key points

- A 95% CI is **not** "95% probability the parameter is inside" in the frequentist interpretation  
- Wider intervals → more uncertainty (often smaller n)  
- CI complements point estimates and p-values  

## Code (mean CI, normal approx)

```python
import numpy as np
from math import sqrt

rng = np.random.default_rng(0)
x = rng.normal(0.7, 0.1, size=80)
mean = x.mean()
se = x.std(ddof=1) / sqrt(len(x))
# ~95% CI using 1.96
lo, hi = mean - 1.96 * se, mean + 1.96 * se
print(mean, (lo, hi))
```

## Uses

- Report eval accuracy with uncertainty  
- Decide if you need more golden examples  
- Compare overlapping intervals cautiously  

## Common mistakes

- Interpreting CI as a prediction interval for one new point  
- Huge claims from intervals that include no effect

---

## Continue

- **Section hub:** [Statistics](README.md)
- **Math & Stats overview:** [Mathematics & Statistics](../README.md)
