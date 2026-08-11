---
title: "1. Feedforward Neural Networks"
description: "Information flows one way — input to output with no cycles."
domain: deep-learning
tags: [architectures, ffnn]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 1. Feedforward Neural Networks

> Information flows one way — input to output with no cycles.

## Definition

A **feedforward neural network (FFNN)** maps inputs to outputs through layered transforms without recurrent connections.

## Code

```python
import torch.nn as nn

class FFNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(32, 64), nn.ReLU(), nn.Linear(64, 4))
    def forward(self, x):
        return self.net(x)
```

---

## Continue

- **Section hub:** [Neural Network Architectures](README.md)
- **DL overview:** [Deep Learning](../README.md)
