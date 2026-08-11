---
title: "2. Perceptron"
description: "The original linear classifier unit — building block intuition for deeper nets."
domain: deep-learning
tags: [dl-basics, perceptron]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 2. Perceptron

> The original linear classifier unit — building block intuition for deeper nets.

## Definition

A **perceptron** computes \(y = f(w^\top x + b)\) with a step (historically) or other activation. Single-layer perceptrons only separate linearly separable data.

## Update rule (classic)

For misclassified points, nudge weights toward correcting the sign.

## Code

```python
import numpy as np

def perceptron_step(w, b, x, y, lr=0.1):
    pred = 1 if (w @ x + b) >= 0 else 0
    w = w + lr * (y - pred) * x
    b = b + lr * (y - pred)
    return w, b
```

## Why it matters

- Shows limits of linear models  
- Motivates multilayer nets + nonlinear activations

---

## Continue

- **Section hub:** [Deep Learning Basics](README.md)
- **DL overview:** [Deep Learning](../README.md)
