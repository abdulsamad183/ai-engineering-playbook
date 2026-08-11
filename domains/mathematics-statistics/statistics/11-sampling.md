---
title: "11. Sampling"
description: "How data is drawn — i.i.d., bias, stratified samples, and Monte Carlo."
domain: mathematics-statistics
tags: [statistics, sampling]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 11. Sampling

> How data is drawn — i.i.d., bias, stratified samples, and Monte Carlo.

## Definition

**Sampling** is selecting a subset of a population for measurement. Good sampling makes inference possible; bad sampling creates bias no model can fix.

## Types / methods

| Method | Meaning |
|--------|---------|
| Simple random | Equal chance |
| Stratified | Sample within strata |
| Systematic | Every k-th |
| Cluster | Sample groups |
| Bootstrap | Resample dataset with replacement |
| Monte Carlo | Sample from a distribution to estimate |

## Code

```python
import numpy as np

rng = np.random.default_rng(0)
pop = np.arange(1000)
sample = rng.choice(pop, size=50, replace=False)
print(sample[:10])

# Stratify toy example
labels = rng.choice(["a", "b"], size=200, p=[0.8, 0.2])
idx_a = np.where(labels == "a")[0]
idx_b = np.where(labels == "b")[0]
take = np.concatenate([
    rng.choice(idx_a, 40, replace=False),
    rng.choice(idx_b, 10, replace=False),
])
print(np.unique(labels[take], return_counts=True))
```

## Uses

- Build representative eval sets  
- Train/val/test splits  
- Bootstrap confidence intervals  

## Common mistakes

- Convenience samples that miss production segments  
- Leakage between train and test via near-duplicates

---

## Continue

- **Section hub:** [Statistics](README.md)
- **Math & Stats overview:** [Mathematics & Statistics](../README.md)
