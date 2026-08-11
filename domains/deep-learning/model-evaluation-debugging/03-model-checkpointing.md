---
title: "3. Model Checkpointing"
description: "Save the best weights — resume training and ship reliable artifacts."
domain: deep-learning
tags: [eval, checkpointing]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 3. Model Checkpointing

> Save the best weights — resume training and ship reliable artifacts.

## Definition

**Checkpointing** stores model (and often optimizer) state. Keep the best validation checkpoint, not only the last epoch.

## Code

```python
import torch

torch.save({"model": model.state_dict(), "opt": opt.state_dict(), "epoch": epoch}, "ckpt.pt")
ckpt = torch.load("ckpt.pt", map_location="cpu")
model.load_state_dict(ckpt["model"])
```

---

## Continue

- **Section hub:** [Model Evaluation & Debugging](README.md)
- **DL overview:** [Deep Learning](../README.md)
