---
title: "4. Learning Rate Scheduling"
description: "Change LR over training — warmup, step decay, cosine, plateau."
domain: deep-learning
tags: [training, lr-schedule]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 4. Learning Rate Scheduling

> Change LR over training — warmup, step decay, cosine, plateau.

## Definition

**LR schedules** vary \(\eta\) during training to improve convergence and final quality.

## Popular schedules

| Schedule | Idea |
|----------|------|
| Step / multistep | Drop LR at milestones |
| Cosine | Smooth decay to a floor |
| Warmup + cosine | Stabilize early training |
| Reduce-on-plateau | Decay when val stalls |

## Code

```python
from torch.optim.lr_scheduler import CosineAnnealingLR

sched = CosineAnnealingLR(optimizer, T_max=100)
scheduler.step()  # typically each epoch/step per API
```

---

## Continue

- **Section hub:** [Deep Learning Training](README.md)
- **DL overview:** [Deep Learning](../README.md)
