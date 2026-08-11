---
title: "17. Multivariate Statistics"
description: "Multiple variables together — covariance matrices, PCA intuition, and joint distributions."
domain: mathematics-statistics
tags: [statistics, multivariate]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 17. Multivariate Statistics

> Multiple variables together — covariance matrices, PCA intuition, and joint distributions.

## Definition

**Multivariate statistics** analyzes more than one variable jointly: covariance matrices, multivariate normals, dimensionality reduction, and dependence structure.

## Key objects

| Object | Meaning |
|--------|---------|
| Mean vector | Center in R^d |
| Covariance matrix | Pairwise spreads |
| Multivariate Normal | Classic joint model |
| PCA | Principal directions of variance |
| Mahalanobis distance | Distance under covariance |

## Code

```python
import numpy as np

rng = np.random.default_rng(0)
X = rng.multivariate_normal(mean=[0, 0], cov=[[1, 0.8], [0.8, 1]], size=500)
print(X.shape)
print(np.cov(X, rowvar=False))

# PCA via SVD (center first)
Xc = X - X.mean(axis=0, keepdims=True)
_, s, vt = np.linalg.svd(Xc, full_matrices=False)
print("explained var ratio", (s**2) / (s**2).sum())
```

## Uses

- Embedding space analysis  
- Feature covariance / whitening  
- Anomaly detection distances  

## See also

- [1. Linear Algebra](../mathematics/01-linear-algebra.md) · [19. Linear Algebra for ML](../ml-oriented/19-linear-algebra-for-ml.md)

---

## Continue

- **Section hub:** [Statistics](README.md)
- **Math & Stats overview:** [Mathematics & Statistics](../README.md)
