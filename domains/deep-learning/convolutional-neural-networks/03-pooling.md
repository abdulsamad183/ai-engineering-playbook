---
title: "3. Pooling"
description: "Downsample feature maps — max/average pool for spatial compression."
domain: deep-learning
tags: [cnn, pooling]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 3. Pooling

> Downsample feature maps — max/average pool for spatial compression.

## Definition

**Pooling** reduces spatial resolution (and compute) while retaining salient signals — commonly max or average pooling.

## Code

```python
import torch.nn as nn

pool = nn.MaxPool2d(kernel_size=2, stride=2)  # H,W -> H/2,W/2
```

## Notes

- Modern nets sometimes prefer stride convolutions over pooling  
- Global average pool often replaces big flatten+dense heads

---

## Continue

- **Section hub:** [Convolutional Neural Networks](README.md)
- **DL overview:** [Deep Learning](../README.md)
