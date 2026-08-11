---
title: "NumPy: Linear Algebra Essentials"
description: "Dot products, norms, matmul, and cosine similarity for embeddings."
domain: python-frameworks-libraries
tags: [numpy, linalg]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# NumPy: Linear Algebra Essentials

> Dot products, norms, matmul, and cosine similarity for embeddings.

## Definition

NumPy’s **linear algebra** tools (`np.dot`, `@`, `np.linalg`) cover products, norms, inverses, and decompositions used constantly in ML/AI.

## Important functions

| Function | Use |
|----------|-----|
| `np.dot` / `@` / `np.matmul` | Products |
| `np.linalg.norm` | Vector/matrix norms |
| `np.linalg.inv` | Inverse (prefer solve) |
| `np.linalg.solve` | Solve linear systems |
| `np.linalg.eig` | Eigendecomposition |
| `np.linalg.svd` | SVD |

## Code

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([0.0, 1.0, 0.5])
print(np.dot(a, b))
print(a @ b)

# Cosine similarity
def cosine(u, v):
    return float(u @ v / (np.linalg.norm(u) * np.linalg.norm(v) + 1e-12))

print(cosine(a, b))

# Batch matmul: (n, d) @ (d, k)
X = np.random.randn(5, 8).astype(np.float32)
W = np.random.randn(8, 3).astype(np.float32)
print((X @ W).shape)  # (5, 3)
```

## Uses

- Embedding similarity search (brute force)
- Projection layers
- PCA via SVD (conceptual)

---

## Continue

- **Hub:** [NumPy hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
