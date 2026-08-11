---
title: "2. K-Means"
description: "Partition into k spherical clusters by minimizing within-cluster variance."
domain: machine-learning
tags: [unsupervised, k-means]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 2. K-Means

> Partition into k spherical clusters by minimizing within-cluster variance.

## Definition

**K-means** assigns each point to the nearest centroid and updates centroids to means until convergence.

## Code

```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

pipe = make_pipeline(StandardScaler(), KMeans(n_clusters=5, n_init=10, random_state=42))
labels = pipe.fit_predict(X)
```

## Tips

- Always scale numeric features  
- Run multiple `n_init`  
- Bad fit for elongated / uneven density clusters → try GMM / DBSCAN

---

## Continue

- **Section hub:** [Unsupervised Learning](README.md)
- **ML overview:** [Machine Learning](../README.md)
