---
title: "1. Batch Normalization"
description: "Normalize layer activations using batch stats — stabilizes deep training."
domain: deep-learning
tags: [training, batchnorm]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 1. Batch Normalization

> Normalize layer activations using batch stats — stabilizes deep training.

## Definition

**BatchNorm** normalizes activations using mini-batch mean/variance, then applies learned scale/shift. Speeds training and can regularize mildly.

## Code

```python
import torch.nn as nn

nn.Sequential(
    nn.Linear(128, 128),
    nn.BatchNorm1d(128),
    nn.ReLU(),
)
```

## Notes

- Train vs eval mode matters (`model.train()` / `model.eval()`)  
- LayerNorm is often preferred in transformers

---

## Continue

- **Section hub:** [Deep Learning Training](README.md)
- **DL overview:** [Deep Learning](../README.md)
