---
title: "9. UMAP"
description: "Fast manifold embedding — visualization and optional downstream features."
domain: machine-learning
tags: [unsupervised, umap]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 9. UMAP

> Fast manifold embedding — visualization and optional downstream features.

## Definition

**UMAP** builds a fuzzy topological graph and embeds it in low dimensions. Often faster than t-SNE and sometimes usable as a feature transform.

## Code

```python
# pip install umap-learn
import umap

Z = umap.UMAP(n_components=2, n_neighbors=15, min_dist=0.1, random_state=42).fit_transform(X_scaled)
```

## Tips

- `n_neighbors` trades local vs global structure  
- Still primarily a visualization / exploration tool

---

## Continue

- **Section hub:** [Unsupervised Learning](README.md)
- **ML overview:** [Machine Learning](../README.md)
