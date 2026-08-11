---
title: "3. Differential Equations"
description: "Equations involving derivatives — dynamics, continuous-time models, and intuition for change."
domain: mathematics-statistics
tags: [mathematics, differential-equations]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 3. Differential Equations

> Equations involving derivatives — dynamics, continuous-time models, and intuition for change.

## Definition

A **differential equation (DE)** relates a function to its derivatives. **ODEs** involve one independent variable (often time); **PDEs** involve several.

## Types

| Type | Meaning |
|------|---------|
| ODE | Ordinary — one independent variable |
| PDE | Partial — multiple independents |
| Linear vs nonlinear | Superposition holds or not |
| Initial value problem | State at t0 given |

## Why AI engineers care

- Continuous-time views of optimization / residual nets  
- Diffusion models connect to SDEs/PDEs conceptually  
- Physics-informed ML and dynamical systems  

## Simple ODE intuition

```text
dx/dt = -k x   →  exponential decay toward 0
```

## Code (Euler method sketch)

```python
import numpy as np

def euler(f, x0, t0, t1, n):
    t = np.linspace(t0, t1, n)
    x = np.zeros(n)
    x[0] = x0
    dt = t[1] - t[0]
    for i in range(n - 1):
        x[i + 1] = x[i] + dt * f(t[i], x[i])
    return t, x

# dx/dt = -x
t, x = euler(lambda t, x: -x, x0=1.0, t0=0.0, t1=5.0, n=50)
print(t[:3], x[:3])
```

## Uses

- Modeling growth/decay of quantities  
- Background for score-based generative models  
- Control / RL continuous dynamics  

## Common mistakes

- Numerical instability with too-large step sizes  
- Overfitting DE jargon when discrete SGD view is enough  

## See also

- [6. Optimization](06-optimization.md) · [22. Optimization for ML](../ml-oriented/22-optimization-for-ml.md)

---

## Continue

- **Section hub:** [Mathematics](README.md)
- **Math & Stats overview:** [Mathematics & Statistics](../README.md)
- Next topic: use the numbered list on the hub
