---
title: "22. Optimization for ML"
description: "SGD, Adam, learning rates, and non-convex loss landscapes."
domain: mathematics-statistics
tags: [ml-math, optimization]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 22. Optimization for ML

> SGD, Adam, learning rates, and non-convex loss landscapes.

## Definition

**Optimization for ML** finds parameters that minimize a loss, usually with **stochastic gradient methods** on non-convex objectives.

## Methods

| Method | Idea |
|--------|------|
| SGD | Gradient on mini-batches |
| Momentum / Adam | Adaptive / smoothed steps |
| LR schedules | Warmup, decay, cosine |
| Regularization | Weight decay, early stop |
| Second-order | Rare at scale (approx Hessian) |

## Code (SGD sketch)

```python
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 3))
true_w = np.array([1.0, -2.0, 0.5])
y = X @ true_w + rng.normal(scale=0.1, size=200)

w = np.zeros(3)
lr, batch = 0.05, 32
for step in range(300):
    idx = rng.choice(len(X), batch, replace=False)
    xb, yb = X[idx], y[idx]
    grad = (2 / batch) * xb.T @ (xb @ w - yb)
    w -= lr * grad
print(w)
```

## Uses

- Training deep models  
- Choosing LR / batch size  
- Diagnosing divergence and plateaus  

## See also

- [6. Optimization](../mathematics/06-optimization.md) · [20. Calculus for ML](20-calculus-for-ml.md)

---

## Continue

- **Section hub:** [ML-Oriented Mathematics](README.md)
- **Math & Stats overview:** [Mathematics & Statistics](../README.md)
