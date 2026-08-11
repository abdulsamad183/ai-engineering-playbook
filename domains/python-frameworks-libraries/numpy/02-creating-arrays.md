---
title: "NumPy: Creating Arrays"
description: "Constructors — array, zeros, ones, arange, linspace, eye, from buffers."
domain: python-frameworks-libraries
tags: [numpy, arrays]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# NumPy: Creating Arrays

> Constructors — array, zeros, ones, arange, linspace, eye, from buffers.

## Definition

Array **creation functions** build new `ndarray`s from Python sequences, ranges, or filled constants.

## Important functions

| Function | Use |
|----------|-----|
| `np.array(obj)` | From list/tuple |
| `np.asarray(obj)` | Convert; avoid copy if already array |
| `np.zeros(shape)` | All zeros |
| `np.ones(shape)` | All ones |
| `np.full(shape, v)` | Constant fill |
| `np.empty(shape)` | Uninitialized (fast; garbage values) |
| `np.arange(start, stop, step)` | Integer/float range |
| `np.linspace(a, b, n)` | `n` evenly spaced |
| `np.eye(n)` | Identity matrix |
| `np.zeros_like(a)` | Same shape/dtype, zeros |

## Code

```python
import numpy as np

print(np.array([1, 2, 3]))
print(np.zeros((2, 3)))
print(np.ones((2, 2), dtype=np.int32))
print(np.arange(0, 10, 2))
print(np.linspace(0, 1, 5))
print(np.eye(3))

# From nested lists → 2D
X = np.array([[0.1, 0.2], [0.3, 0.4]], dtype=np.float32)
print(X.shape)
```

## Tips

- Pick `dtype` early (`float32` often enough for ML features)
- Use `zeros_like` / `ones_like` to match an existing array

---

## Continue

- **Hub:** [NumPy hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
