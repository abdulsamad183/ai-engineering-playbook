---
title: "8. t-SNE"
description: "Nonlinear 2D/3D visualization that preserves local neighborhoods."
domain: machine-learning
tags: [unsupervised, tsne]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 8. t-SNE

> Nonlinear 2D/3D visualization that preserves local neighborhoods.

## Definition

**t-SNE** embeds points so nearby high-d neighbors stay close in 2D/3D. Great for visualization; not a general feature compressor for downstream models.

## Code

```python
from sklearn.manifold import TSNE

Z = TSNE(n_components=2, perplexity=30, random_state=42).fit_transform(X_scaled)
```

## Common mistakes

- Interpreting global distances / cluster sizes too literally  
- Using t-SNE features as model inputs without care  
- Re-running without fixed seed and comparing layouts

---

## Continue

- **Section hub:** [Unsupervised Learning](README.md)
- **ML overview:** [Machine Learning](../README.md)
