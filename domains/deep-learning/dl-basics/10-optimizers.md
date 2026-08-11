---
title: "10. Optimizers"
description: "SGD, Momentum, Adam, AdamW — algorithms that apply gradients."
domain: deep-learning
tags: [dl-basics, optimizers]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 10. Optimizers

> SGD, Momentum, Adam, AdamW — algorithms that apply gradients.

## Definition

An **optimizer** turns gradients into parameter updates (with momentum, adaptive rates, weight decay, etc.).

## Common choices

| Optimizer | When |
|-----------|------|
| SGD + momentum | Vision classics, careful tuning |
| Adam / AdamW | Strong default for many DL/NLP tasks |
| Adafactor / Lion | Alternatives in some LLM stacks |

## Code

```python
import torch.optim as optim

opt = optim.AdamW(model.parameters(), lr=1e-3, weight_decay=0.01)
opt.zero_grad()
loss.backward()
opt.step()
```

---

## Continue

- **Section hub:** [Deep Learning Basics](README.md)
- **DL overview:** [Deep Learning](../README.md)
