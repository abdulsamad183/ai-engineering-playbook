---
title: "3. GRU"
description: "Simpler gated RNN — fewer parameters than LSTM, often similar quality."
domain: deep-learning
tags: [sequence, gru]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 3. GRU

> Simpler gated RNN — fewer parameters than LSTM, often similar quality.

## Definition

A **GRU** merges gating into update/reset gates — a lighter recurrent alternative to LSTM.

## Code

```python
import torch.nn as nn

gru = nn.GRU(input_size=32, hidden_size=64, batch_first=True)
```

## Tip

- Try GRU when you want recurrent inductive bias with less overhead

---

## Continue

- **Section hub:** [Sequence Models](README.md)
- **DL overview:** [Deep Learning](../README.md)
