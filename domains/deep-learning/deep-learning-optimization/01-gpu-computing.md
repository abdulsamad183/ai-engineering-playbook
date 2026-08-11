---
title: "1. GPU Computing"
description: "Train on accelerators — device placement, batched kernels, and memory."
domain: deep-learning
tags: [optimization, gpu]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 1. GPU Computing

> Train on accelerators — device placement, batched kernels, and memory.

## Definition

**GPU computing** moves tensors and kernels to accelerators for throughput. Most DL training assumes CUDA/ROCm/Metal-class devices.

## Code

```python
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
x = x.to(device)
```

## Tips

- Batch to saturate the GPU  
- Watch VRAM (activations + optimizer states)

---

## Continue

- **Section hub:** [Deep Learning Optimization](README.md)
- **DL overview:** [Deep Learning](../README.md)
