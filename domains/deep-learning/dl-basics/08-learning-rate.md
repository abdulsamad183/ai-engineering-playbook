---
title: "8. Learning Rate"
description: "The step-size knob — too large diverges, too small crawls."
domain: deep-learning
tags: [dl-basics, learning-rate]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 8. Learning Rate

> The step-size knob — too large diverges, too small crawls.

## Definition

The **learning rate** \(\eta\) scales each optimizer update. It is often the most important hyperparameter.

## Practical ranges

| Setting | Effect |
|---------|--------|
| Too high | Loss spikes / NaNs |
| Too low | Slow progress |
| Schedule | Warmup + decay often helps |

## Code

```python
import torch.optim as optim

opt = optim.AdamW(model.parameters(), lr=3e-4)
```

## See also

- [Learning Rate Scheduling](../deep-learning-training/04-learning-rate-scheduling.md)

---

## Continue

- **Section hub:** [Deep Learning Basics](README.md)
- **DL overview:** [Deep Learning](../README.md)
