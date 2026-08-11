---
title: "9. Epochs & Batches"
description: "How data is consumed — batch size, steps, and epochs."
domain: deep-learning
tags: [dl-basics, batches]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 9. Epochs & Batches

> How data is consumed — batch size, steps, and epochs.

## Definition

- **Batch** — examples processed together in one forward/backward  
- **Step / iteration** — one optimizer update  
- **Epoch** — one full pass over the training set  

## Tradeoffs

| Larger batch | Smaller batch |
|--------------|---------------|
| Stable grads, needs more memory | Noisier, often better generalization |
| May need larger LR | More steps per epoch |

## Code

```python
from torch.utils.data import DataLoader

loader = DataLoader(dataset, batch_size=32, shuffle=True)
for epoch in range(10):
    for batch in loader:
        ...
```

---

## Continue

- **Section hub:** [Deep Learning Basics](README.md)
- **DL overview:** [Deep Learning](../README.md)
