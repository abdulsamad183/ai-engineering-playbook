---
title: "4. Bidirectional RNNs"
description: "Read left→right and right→left — full context for offline sequences."
domain: deep-learning
tags: [sequence, birnn]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 4. Bidirectional RNNs

> Read left→right and right→left — full context for offline sequences.

## Definition

A **bidirectional RNN** runs two recurrent passes and concatenates states so each position sees past and future context (when future is available).

## Code

```python
import torch.nn as nn

bi = nn.LSTM(32, 64, bidirectional=True, batch_first=True)
# output hidden size = 128
```

## Caution

- Not causal — avoid for true next-token generation

---

## Continue

- **Section hub:** [Sequence Models](README.md)
- **DL overview:** [Deep Learning](../README.md)
