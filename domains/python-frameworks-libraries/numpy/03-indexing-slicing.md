---
title: "NumPy: Indexing & Slicing"
description: "Basic slices, fancy indexing, boolean masks, and views vs copies."
domain: python-frameworks-libraries
tags: [numpy, indexing]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# NumPy: Indexing & Slicing

> Basic slices, fancy indexing, boolean masks, and views vs copies.

## Definition

**Indexing** selects elements; **slicing** selects ranges. NumPy also supports **boolean masks** and **integer arrays** (fancy indexing).

## Patterns

| Pattern | Example | Result |
|---------|---------|--------|
| Scalar | `a[0]` | element |
| Slice | `a[1:4]` | view |
| 2D | `a[0, 2]` | element |
| Row/col | `a[0, :]` / `a[:, 1]` | 1D |
| Mask | `a[a > 0]` | copy |
| Fancy | `a[[0, 2]]` | copy |

## Code

```python
import numpy as np

a = np.arange(12).reshape(3, 4)
print(a)
print(a[1, 2])       # 6
print(a[0:2, 1:3])   # submatrix
print(a[:, -1])      # last column

# Boolean mask
scores = np.array([0.2, 0.9, 0.55, 0.1])
print(scores[scores >= 0.5])

# Fancy index
print(scores[[0, 2]])

# View caveat: slices share memory
b = a[0, :]
b[0] = 999
print(a[0, 0])       # 999 — modified original
```

## Uses

- Filter low-confidence scores
- Select top-k rows after `argsort`
- Take embedding rows by id list

---

## Continue

- **Hub:** [NumPy hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
