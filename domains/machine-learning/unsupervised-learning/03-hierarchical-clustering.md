---
title: "3. Hierarchical Clustering"
description: "Build a tree of merges/splits — dendrograms and linkage choices."
domain: machine-learning
tags: [unsupervised, hierarchical]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 3. Hierarchical Clustering

> Build a tree of merges/splits — dendrograms and linkage choices.

## Definition

**Hierarchical clustering** builds a hierarchy: agglomerative (merge) or divisive (split). Linkage defines cluster distance (ward, average, complete).

## Code

```python
from sklearn.cluster import AgglomerativeClustering

clf = AgglomerativeClustering(n_clusters=4, linkage="ward")
labels = clf.fit_predict(X_scaled)
```

## When to use

- Want a dendrogram / multi-resolution view  
- Moderate n (naive methods scale poorly)

---

## Continue

- **Section hub:** [Unsupervised Learning](README.md)
- **ML overview:** [Machine Learning](../README.md)
