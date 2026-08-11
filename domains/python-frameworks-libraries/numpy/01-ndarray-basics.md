---
title: "NumPy: ndarray Basics"
description: "What an ndarray is — dtype, shape, strides, and why NumPy is fast."
domain: python-frameworks-libraries
tags: [numpy, arrays, fundamentals]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# NumPy: ndarray Basics

> What an ndarray is — dtype, shape, strides, and why NumPy is fast.

## Definition

An **`ndarray`** (N-dimensional array) is NumPy’s core class: a grid of values of the **same dtype**, with a **shape** (sizes per axis) and optional **strides**.

## Key class

| Class | Role |
|-------|------|
| `numpy.ndarray` | Core array object |
| `numpy.dtype` | Element type (`float32`, `int64`, …) |

## Important attributes

| Attribute | Meaning |
|-----------|---------|
| `ndim` | Number of dimensions |
| `shape` | Tuple of sizes |
| `size` | Total elements |
| `dtype` | Element type |
| `itemsize` | Bytes per element |
| `nbytes` | Total bytes |
| `T` | Transpose view |

## Code

```python
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)
print(type(a))          # <class 'numpy.ndarray'>
print(a.ndim, a.shape)  # 2 (2, 3)
print(a.dtype, a.nbytes)
print(a.T.shape)        # (3, 2)

# Prefer vectorized ops over Python loops
x = np.arange(5, dtype=np.float64)
print(x * 2 + 1)        # array([1., 3., 5., 7., 9.])
```

## Uses in AI

- Store embedding matrices `(n_docs, dim)`
- Batch features for classical ML
- Masks and score arrays for ranking

---

## Continue

- **Hub:** [NumPy hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
