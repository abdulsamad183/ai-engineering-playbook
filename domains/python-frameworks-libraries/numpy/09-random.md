---
title: "NumPy: Random Module"
description: "Seeded RNGs — rand, randn, choice, shuffle for reproducible experiments."
domain: python-frameworks-libraries
tags: [numpy, random]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# NumPy: Random Module

> Seeded RNGs — rand, randn, choice, shuffle for reproducible experiments.

## Definition

`numpy.random` generates random numbers. Prefer the modern **Generator** API (`default_rng`) for better seeding and statistical quality.

## Important APIs

| API | Use |
|-----|-----|
| `np.random.default_rng(seed)` | Create Generator |
| `rng.random(shape)` | Uniform [0, 1) |
| `rng.normal(loc, scale, size)` | Gaussian |
| `rng.integers(low, high, size)` | Ints |
| `rng.choice(a, size, replace)` | Sample items |
| `rng.shuffle(x)` | In-place shuffle |
| `rng.permutation(x)` | Shuffled copy |

## Code

```python
import numpy as np

rng = np.random.default_rng(42)
print(rng.normal(0, 1, size=(2, 3)))
print(rng.choice(["a", "b", "c"], size=5, replace=True))

idx = np.arange(10)
rng.shuffle(idx)
print(idx)
```

## Uses

- Train/val splits
- Dropout-like masks (toy)
- Bootstrap sampling for metrics

---

## Continue

- **Hub:** [NumPy hub](README.md)
- **Frameworks overview:** [Python Frameworks & Libraries](../README.md)
