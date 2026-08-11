---
title: "NumPy: Universal Functions (ufuncs)"
description: "Element-wise math — add, sqrt, exp, clip, where, and vectorized logic."
domain: python-frameworks-libraries
tags: [numpy, ufuncs, math]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# NumPy: Universal Functions (ufuncs)

> Element-wise math — add, sqrt, exp, clip, where, and vectorized logic.

## Definition

A **ufunc** (universal function) applies an operation **element-wise** across arrays, usually in compiled code — far faster than Python loops.

## Important ufuncs / functions

| Function | Use |
|----------|-----|
| `np.add`, `np.multiply`, … | Arithmetic |
| `np.sqrt`, `np.exp`, `np.log` | Elementary |
| `np.abs`, `np.sign` | Sign/abs |
| `np.clip(a, lo, hi)` | Clamp values |
| `np.maximum` / `np.minimum` | Pairwise |
| `np.where(cond, x, y)` | Vectorized if |
| `np.isnan` / `np.isfinite` | Float checks |
| `np.round` | Rounding |

## Code

```python
import numpy as np

x = np.array([0.0, 0.5, 1.0, 1.5])
print(np.sqrt(x))
print(np.clip(x, 0.0, 1.0))
print(np.where(x >= 1.0, 1.0, x))

logits = np.array([-1.0, 2.0, 0.5])
# stable-ish softmax sketch
z = logits - logits.max()
p = np.exp(z) / np.exp(z).sum()
print(p, p.sum())
```

## Uses

- Normalize scores
- Apply temperature / clip probabilities
- Clean NaNs before metrics

---

## Continue

- **Hub:** [NumPy hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
