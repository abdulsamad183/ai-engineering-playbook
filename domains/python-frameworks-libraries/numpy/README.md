# NumPy

> Numerical Python — fast N-dimensional arrays, vectorized math, and the foundation of the scientific Python stack.

**Prerequisites:** [Python](../../python-engineering/README.md)  
**Part of:** [Python Frameworks & Libraries](../README.md)

---

## Definition

**NumPy** provides the `ndarray` type: homogeneous, contiguous (or strided) multi-dimensional arrays with broadcasting and a huge library of fast C-backed operations. Pandas, scikit-learn, PyTorch (interop), and Matplotlib all build on NumPy concepts.

---

## When to use NumPy

| Use | Example |
|-----|---------|
| Numeric arrays | embeddings batch as `float32` matrix |
| Vectorized math | normalize, distances, masks |
| Linear algebra | dot products, norms |
| Random sampling | seeds for reproducible experiments |

---

## Learning path

```mermaid
flowchart LR
  A[ndarray basics] --> B[Create & index]
  B --> C[Shape & broadcast]
  C --> D[ufuncs & aggregate]
  D --> E[linalg & random]
```

---

## Topics

| # | Topic | Document |
|---|-------|----------|
| 1 | ndarray basics | [01-ndarray-basics.md](01-ndarray-basics.md) |
| 2 | Creating arrays | [02-creating-arrays.md](02-creating-arrays.md) |
| 3 | Indexing & slicing | [03-indexing-slicing.md](03-indexing-slicing.md) |
| 4 | Shape, reshape & axes | [04-shape-reshape-axes.md](04-shape-reshape-axes.md) |
| 5 | Universal functions (ufuncs) | [05-ufuncs-math.md](05-ufuncs-math.md) |
| 6 | Aggregations | [06-aggregations.md](06-aggregations.md) |
| 7 | Broadcasting | [07-broadcasting.md](07-broadcasting.md) |
| 8 | Linear algebra essentials | [08-linear-algebra.md](08-linear-algebra.md) |
| 9 | Random module | [09-random.md](09-random.md) |
| 10 | Important APIs cheat sheet | [10-important-apis.md](10-important-apis.md) |

---

## Related

- [Pandas](../pandas/README.md) · [Matplotlib](../matplotlib/README.md) · [Machine Learning](../../machine-learning/README.md)
