---
title: "19. Linear Algebra for ML"
description: "Matrices as data and models — embeddings, attention, and SVD for ML systems."
domain: mathematics-statistics
tags: [ml-math, linear-algebra]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 19. Linear Algebra for ML

> Matrices as data and models — embeddings, attention, and SVD for ML systems.

## Definition

**Linear algebra for ML** focuses on the operations that show up in real models: matrix multiplies, norms, projections, eigendecompositions, and low-rank structure.

## Where it appears

| Concept | ML use |
|---------|--------|
| Matrix multiply | Dense layers, attention scores |
| Norms | Weight decay, cosine similarity |
| Rank / SVD | Compression, PCA, LoRA intuition |
| Orthogonal matrices | Stable transforms |
| Kronecker / broadcasting | Batched tensor ops |

## Code

```python
import numpy as np

# mini "attention" scores: QK^T / sqrt(d)
rng = np.random.default_rng(0)
Q = rng.normal(size=(4, 8))  # tokens x d
K = rng.normal(size=(4, 8))
d = Q.shape[1]
scores = (Q @ K.T) / np.sqrt(d)
weights = np.exp(scores - scores.max(axis=1, keepdims=True))
weights = weights / weights.sum(axis=1, keepdims=True)
print(weights.round(3))
```

## Uses

- Understand embeddings and projections  
- Debug shape errors in tensor pipelines  
- Reason about low-rank adapters  

## See also

- [1. Linear Algebra](../mathematics/01-linear-algebra.md)

---

## Continue

- **Section hub:** [ML-Oriented Mathematics](README.md)
- **Math & Stats overview:** [Mathematics & Statistics](../README.md)
