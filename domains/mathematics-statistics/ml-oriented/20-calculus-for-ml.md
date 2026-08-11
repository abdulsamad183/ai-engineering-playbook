---
title: "20. Calculus for ML"
description: "Gradients, chain rule, and backpropagation — calculus that trains neural nets."
domain: mathematics-statistics
tags: [ml-math, calculus]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 20. Calculus for ML

> Gradients, chain rule, and backpropagation — calculus that trains neural nets.

## Definition

**Calculus for ML** is about derivatives of loss functions with respect to parameters, computed via the chain rule (automatic differentiation / backprop).

## Key ideas

| Idea | Meaning |
|------|---------|
| Gradient ∇θ L | Direction of steepest ascent of loss |
| Jacobian / Hessian | Higher-order local structure |
| Chain rule | Composition of layers |
| Autograd | Automatic reverse-mode AD |
| Learning rate | Step size along −∇θ L |

## Code (manual gradient of MSE)

```python
import numpy as np

x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
w, b = 0.0, 0.0
lr = 0.05
for _ in range(200):
    pred = w * x + b
    err = pred - y
    # dL/dw, dL/db for L = mean(err^2)
    dw = (2 / len(x)) * np.dot(err, x)
    db = (2 / len(x)) * err.sum()
    w -= lr * dw
    b -= lr * db
print(w, b)
```

## Uses

- Train / fine-tune models  
- Understand vanishing/exploding gradients  
- Design custom losses  

## See also

- [2. Calculus](../mathematics/02-calculus.md) · [22. Optimization for ML](22-optimization-for-ml.md)

---

## Continue

- **Section hub:** [ML-Oriented Mathematics](README.md)
- **Math & Stats overview:** [Mathematics & Statistics](../README.md)
