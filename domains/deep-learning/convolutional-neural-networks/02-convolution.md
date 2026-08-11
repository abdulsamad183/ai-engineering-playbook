---
title: "2. Convolution"
description: "Filters produce feature maps — channels, kernels, and cross-correlation in practice."
domain: deep-learning
tags: [cnn, convolution]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 2. Convolution

> Filters produce feature maps — channels, kernels, and cross-correlation in practice.

## Definition

A **convolution layer** applies learnable kernels across spatial locations to produce feature maps (frameworks often implement cross-correlation).

## Code

```python
import torch.nn as nn

conv = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=1)
# input: (N, 3, H, W) -> (N, 16, H, W) with padding=1
```

## Key knobs

- `kernel_size`, `stride`, `padding`, `dilation`, `groups`

---

## Continue

- **Section hub:** [Convolutional Neural Networks](README.md)
- **DL overview:** [Deep Learning](../README.md)
