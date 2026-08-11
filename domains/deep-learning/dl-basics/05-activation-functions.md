---
title: "5. Activation Functions"
description: "Nonlinearities that make deep stacks expressive — ReLU, sigmoid, GELU, and friends."
domain: deep-learning
tags: [dl-basics, activations]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 5. Activation Functions

> Nonlinearities that make deep stacks expressive — ReLU, sigmoid, GELU, and friends.

## Definition

**Activations** introduce nonlinearity between layers. Without them, a deep net collapses to one linear map.

## Common choices

| Activation | Notes |
|------------|-------|
| ReLU | Fast default for many nets |
| GELU / SiLU | Common in transformers |
| Sigmoid / Tanh | Bounded; can saturate |
| Softmax | Output distribution over classes |

## Code

```python
import torch
import torch.nn.functional as F

z = torch.randn(4, 8)
print(F.relu(z).min())
print(F.gelu(z).shape)
print(F.softmax(z, dim=-1).sum(dim=-1))
```

---

## Continue

- **Section hub:** [Deep Learning Basics](README.md)
- **DL overview:** [Deep Learning](../README.md)
