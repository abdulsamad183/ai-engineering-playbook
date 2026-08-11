---
title: "NumPy: Shape, Reshape & Axes"
description: "reshape, ravel, transpose, expand_dims, and thinking in axes."
domain: python-frameworks-libraries
tags: [numpy, shape]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# NumPy: Shape, Reshape & Axes

> reshape, ravel, transpose, expand_dims, and thinking in axes.

## Definition

An array’s **shape** is the length of each **axis** (dimension). Many reductions take an `axis=` argument meaning “collapse this dimension.”

## Important functions

| Function | Use |
|----------|-----|
| `reshape` | New shape (must match size) |
| `ravel` / `flatten` | 1D (ravel may be view) |
| `transpose` / `.T` | Swap axes |
| `np.expand_dims` | Add axis |
| `np.squeeze` | Remove size-1 axes |
| `np.concatenate` | Join along axis |
| `np.stack` | Stack along new axis |
| `np.split` | Split into chunks |

## Code

```python
import numpy as np

a = np.arange(6)
print(a.reshape(2, 3))
print(a.reshape(3, -1))      # -1 infers

batch = np.arange(24).reshape(2, 3, 4)  # (batch, seq, feat)
print(batch.shape)
print(batch.mean(axis=1).shape)         # mean over seq → (2, 4)

x = np.array([1, 2, 3])
print(np.expand_dims(x, 0).shape)       # (1, 3) row
print(np.stack([x, x], axis=0).shape)   # (2, 3)
```

## Mental model

- `axis=0` → rows (first dimension)
- For embeddings `(n, d)`, reduce over `axis=0` for feature stats, `axis=1` for per-vector norms

---

## Continue

- **Hub:** [NumPy hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
