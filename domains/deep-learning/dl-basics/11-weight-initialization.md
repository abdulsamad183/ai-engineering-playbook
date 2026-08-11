---
title: "11. Weight Initialization"
description: "Start scales that keep signals and gradients healthy at depth."
domain: deep-learning
tags: [dl-basics, initialization]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 11. Weight Initialization

> Start scales that keep signals and gradients healthy at depth.

## Definition

**Initialization** sets starting weights so activations/gradients neither explode nor vanish early in training (Xavier/Glorot, Kaiming/He, etc.).

## Rules of thumb

| Activation | Init family |
|------------|-------------|
| tanh / sigmoid | Xavier |
| ReLU | Kaiming / He |
| Frameworks | Sensible defaults often built-in |

## Code

```python
import torch.nn as nn

layer = nn.Linear(128, 128)
nn.init.kaiming_uniform_(layer.weight, nonlinearity="relu")
nn.init.zeros_(layer.bias)
```

---

## Continue

- **Section hub:** [Deep Learning Basics](README.md)
- **DL overview:** [Deep Learning](../README.md)
