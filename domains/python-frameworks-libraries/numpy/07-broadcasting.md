---
title: "NumPy: Broadcasting"
description: "How NumPy stretches arrays of compatible shapes for element-wise ops."
domain: python-frameworks-libraries
tags: [numpy, broadcasting]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# NumPy: Broadcasting

> How NumPy stretches arrays of compatible shapes for element-wise ops.

## Definition

**Broadcasting** lets NumPy operate on arrays with different but **compatible** shapes by virtually expanding dimensions of size 1.

## Rules (simplified)

1. Align shapes on the **right**
2. Dimensions equal, or one is `1`, or missing
3. Otherwise → `ValueError`

## Code

```python
import numpy as np

# (3, 1) + (1, 4) → (3, 4)
a = np.arange(3).reshape(3, 1)
b = np.arange(4).reshape(1, 4)
print(a + b)

# Normalize rows of a matrix
X = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
mu = X.mean(axis=1, keepdims=True)   # (2, 1)
print(X - mu)

# Scale columns
scale = np.array([1.0, 0.5, 2.0])     # (3,)
print(X * scale)
```

## Uses

- Center/scale features
- Add bias vector to batch
- Apply per-class thresholds

---

## Continue

- **Hub:** [NumPy hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
