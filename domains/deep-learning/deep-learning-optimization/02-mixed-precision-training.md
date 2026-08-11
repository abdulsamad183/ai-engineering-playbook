---
title: "2. Mixed Precision Training"
description: "FP16/BF16 compute with FP32 master weights — faster, less memory."
domain: deep-learning
tags: [optimization, amp]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 2. Mixed Precision Training

> FP16/BF16 compute with FP32 master weights — faster, less memory.

## Definition

**Mixed precision** runs many ops in lower precision while keeping stable master weights/loss scaling (AMP).

## Code

```python
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()
opt.zero_grad()
with autocast():
    loss = model(x).loss
scaler.scale(loss).backward()
scaler.step(opt)
scaler.update()
```

---

## Continue

- **Section hub:** [Deep Learning Optimization](README.md)
- **DL overview:** [Deep Learning](../README.md)
