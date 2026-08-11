---
title: "NumPy: Important APIs Cheat Sheet"
description: "High-frequency NumPy functions and classes for daily AI engineering."
domain: python-frameworks-libraries
tags: [numpy, cheatsheet]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# NumPy: Important APIs Cheat Sheet

> High-frequency NumPy functions and classes for daily AI engineering.

## Core class

| Class | Role |
|-------|------|
| `ndarray` | N-D array |

## Creation

`array`, `asarray`, `zeros`, `ones`, `full`, `arange`, `linspace`, `eye`, `zeros_like`

## Manipulation

`reshape`, `ravel`, `transpose`, `concatenate`, `stack`, `split`, `expand_dims`, `squeeze`

## Math / logic

`add`, `multiply`, `sqrt`, `exp`, `log`, `clip`, `where`, `isnan`, `isfinite`

## Reduce

`sum`, `mean`, `std`, `min`, `max`, `argmin`, `argmax`, `percentile`

## Linalg / random

`dot`, `matmul`, `@`, `linalg.norm`, `default_rng`

## Mini examples

```python
import numpy as np

# L2-normalize rows
X = np.random.randn(4, 16).astype(np.float32)
X = X / (np.linalg.norm(X, axis=1, keepdims=True) + 1e-12)

# Top-k indices
scores = np.array([0.1, 0.9, 0.4, 0.8])
topk = np.argsort(scores)[-2:][::-1]
print(topk, scores[topk])
```

---

## Continue

- **Hub:** [NumPy hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
