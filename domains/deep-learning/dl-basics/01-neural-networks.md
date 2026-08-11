---
title: "1. Neural Networks"
description: "Stacked layers of parameterized transforms that learn representations from data."
domain: deep-learning
tags: [dl-basics, neural-networks]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 1. Neural Networks

> Stacked layers of parameterized transforms that learn representations from data.

## Definition

A **neural network** composes layers of linear maps and nonlinear activations to approximate functions. Depth lets the model build hierarchical features.

## Core pieces

| Piece | Role |
|-------|------|
| Layer | Affine transform + nonlinearity |
| Weights / biases | Learnable parameters |
| Forward pass | Input → prediction |
| Loss | How wrong the prediction is |
| Backward pass | Gradients for each parameter |

```mermaid
flowchart LR
  X[Input] --> H1[Hidden]
  H1 --> H2[Hidden]
  H2 --> Y[Output]
```

## Code (PyTorch sketch)

```python
import torch.nn as nn

model = nn.Sequential(
    nn.Linear(20, 64),
    nn.ReLU(),
    nn.Linear(64, 10),
)
```

## See also

- [Perceptron](02-perceptron.md) · [Forward Propagation](03-forward-propagation.md)

---

## Continue

- **Section hub:** [Deep Learning Basics](README.md)
- **DL overview:** [Deep Learning](../README.md)
