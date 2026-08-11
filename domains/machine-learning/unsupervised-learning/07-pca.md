---
title: "7. PCA"
description: "Principal components — orthogonal directions of maximum variance."
domain: machine-learning
tags: [unsupervised, pca]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 7. PCA

> Principal components — orthogonal directions of maximum variance.

## Definition

**PCA** finds orthogonal axes (principal components) that capture the most variance. Projection = low-rank approximation via SVD.

## Code

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

pca = make_pipeline(StandardScaler(), PCA(n_components=0.95))  # keep 95% variance
Z = pca.fit_transform(X)
```

## Tips

- Standardize before PCA on mixed-scale features  
- Components are linear mixes — not always interpretable

---

## Continue

- **Section hub:** [Unsupervised Learning](README.md)
- **ML overview:** [Machine Learning](../README.md)
