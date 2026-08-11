---
title: "4. Residual Networks"
description: "Skip connections — learn residuals so very deep nets can train."
domain: deep-learning
tags: [architectures, resnet]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 4. Residual Networks

> Skip connections — learn residuals so very deep nets can train.

## Definition

**ResNets** add skip connections: \(y = F(x) + x\). Gradients flow through the identity path, enabling much deeper models.

```mermaid
flowchart LR
  X --> F[F(x)]
  X --> Add
  F --> Add
  Add --> Y
```

## Code

```python
import torch.nn as nn
import torch.nn.functional as F

class ResidualBlock(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.fc1 = nn.Linear(dim, dim)
        self.fc2 = nn.Linear(dim, dim)
    def forward(self, x):
        return x + self.fc2(F.relu(self.fc1(x)))
```

---

## Continue

- **Section hub:** [Neural Network Architectures](README.md)
- **DL overview:** [Deep Learning](../README.md)
