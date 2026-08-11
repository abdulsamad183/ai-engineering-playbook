---
title: "14. Correlation & Covariance"
description: "How variables move together — covariance, Pearson/Spearman correlation, and pitfalls."
domain: mathematics-statistics
tags: [statistics, correlation]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 14. Correlation & Covariance

> How variables move together — covariance, Pearson/Spearman correlation, and pitfalls.

## Definition

**Covariance** measures joint variability of two variables. **Correlation** normalizes that relationship (Pearson to [-1, 1] for linear association).

## Measures

| Measure | Meaning |
|---------|---------|
| Covariance | Scale-dependent co-movement |
| Pearson r | Linear correlation |
| Spearman ρ | Rank correlation (monotonic) |

## Code

```python
import numpy as np

rng = np.random.default_rng(0)
x = rng.normal(0, 1, 200)
y = 0.8 * x + rng.normal(0, 0.5, 200)
print("cov", np.cov(x, y, ddof=1)[0, 1])
print("pearson", np.corrcoef(x, y)[0, 1])
```

## Uses

- Feature redundancy checks  
- Relating latency vs size  
- Eval metric relationships  

## Common mistakes

- Correlation ≠ causation  
- Pearson misses nonlinear dependence  
- Spurious correlation from confounders

---

## Continue

- **Section hub:** [Statistics](README.md)
- **Math & Stats overview:** [Mathematics & Statistics](../README.md)
