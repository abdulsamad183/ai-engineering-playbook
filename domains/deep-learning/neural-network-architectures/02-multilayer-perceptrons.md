---
title: "2. Multilayer Perceptrons"
description: "Classic MLP — stacked fully connected layers with nonlinearities."
domain: deep-learning
tags: [architectures, mlp]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 2. Multilayer Perceptrons

> Classic MLP — stacked fully connected layers with nonlinearities.

## Definition

An **MLP** is a feedforward net of fully connected (dense) layers. Still a strong baseline for tabular data and small problems.

## Code

```python
import torch.nn as nn

mlp = nn.Sequential(
    nn.Linear(20, 128), nn.ReLU(),
    nn.Linear(128, 128), nn.ReLU(),
    nn.Linear(128, 2),
)
```

## Tips

- Scale inputs  
- Prefer AdamW + modest width before going huge

---

## Continue

- **Section hub:** [Neural Network Architectures](README.md)
- **DL overview:** [Deep Learning](../README.md)
