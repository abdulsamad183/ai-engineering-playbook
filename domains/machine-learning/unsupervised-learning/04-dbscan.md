---
title: "4. DBSCAN"
description: "Density-based clusters of arbitrary shape — and automatic noise points."
domain: machine-learning
tags: [unsupervised, dbscan]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 4. DBSCAN

> Density-based clusters of arbitrary shape — and automatic noise points.

## Definition

**DBSCAN** grows clusters from dense neighborhoods (`eps`, `min_samples`). Points in sparse regions are labeled noise (−1).

## Code

```python
from sklearn.cluster import DBSCAN

clf = DBSCAN(eps=0.5, min_samples=5)
labels = clf.fit_predict(X_scaled)
```

## Tips

- Scale features; tune `eps` via k-distance plot  
- Struggles with varying densities → HDBSCAN (ecosystem)

---

## Continue

- **Section hub:** [Unsupervised Learning](README.md)
- **ML overview:** [Machine Learning](../README.md)
