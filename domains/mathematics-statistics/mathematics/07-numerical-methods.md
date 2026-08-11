---
title: "7. Numerical Methods"
description: "Approximating math on computers — stability, discretization, and floating point care."
domain: mathematics-statistics
tags: [mathematics, numerical-methods]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 7. Numerical Methods

> Approximating math on computers — stability, discretization, and floating point care.

## Definition

**Numerical methods** compute approximate solutions when closed forms are unavailable or expensive: integration, root finding, linear solves, and differential equations.

## Core themes

| Theme | Meaning |
|-------|---------|
| Discretization | Continuous → finite steps |
| Stability | Errors don't explode |
| Conditioning | Sensitivity to input noise |
| Floating point | Finite precision IEEE floats |
| Iterative solvers | Approximate linear/nonlinear systems |

## Floating point caution

```python
print(0.1 + 0.2)          # not exactly 0.3
print(1e16 + 1 - 1e16)    # precision loss
```

## Useful techniques

| Method | Use |
|--------|-----|
| Finite differences | Check gradients |
| Newton / quasi-Newton | Root / optimization |
| SVD / QR | Stable linear algebra |
| Monte Carlo | Expectation estimates |

## Code (log-sum-exp stability)

```python
import numpy as np

def logsumexp(x):
    m = np.max(x)
    return m + np.log(np.sum(np.exp(x - m)))

logits = np.array([1000.0, 1001.0, 999.0])
# np.exp(logits) overflows; logsumexp is safe
print(logsumexp(logits))
```

## Uses in AI

- Stable softmax / log-softmax  
- Mixed precision training awareness  
- Numerical gradient checks  

## Common mistakes

- Subtracting nearly equal floats  
- Exponentiating large logits without stabilization  

## See also

- [2. Calculus](02-calculus.md) · [6. Optimization](06-optimization.md)

---

## Continue

- **Section hub:** [Mathematics](README.md)
- **Math & Stats overview:** [Mathematics & Statistics](../README.md)
- Next topic: use the numbered list on the hub
