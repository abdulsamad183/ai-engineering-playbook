---
title: "1. PyTorch"
description: "Eager-by-default tensors and autograd — the dominant research/production DL framework."
domain: deep-learning
tags: [frameworks, pytorch]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 1. PyTorch

> Eager-by-default tensors and autograd — the dominant research/production DL framework.

## Definition

**PyTorch** provides GPU tensors, autograd, `nn.Module`, and a rich ecosystem (Lightning, Hugging Face, TorchServe).

## Minimal loop

```python
import torch
import torch.nn as nn
import torch.optim as optim

model = nn.Linear(10, 1)
opt = optim.Adam(model.parameters(), lr=1e-3)
x, y = torch.randn(32, 10), torch.randn(32, 1)
pred = model(x)
loss = nn.functional.mse_loss(pred, y)
opt.zero_grad(); loss.backward(); opt.step()
```

## Docs

- https://pytorch.org/docs/

---

## Continue

- **Section hub:** [Deep Learning Frameworks](README.md)
- **DL overview:** [Deep Learning](../README.md)
