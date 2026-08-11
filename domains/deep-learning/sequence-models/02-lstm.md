---
title: "2. LSTM"
description: "Gated memory cell — remember and forget across long sequences."
domain: deep-learning
tags: [sequence, lstm]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 2. LSTM

> Gated memory cell — remember and forget across long sequences.

## Definition

**LSTM** units add gates (input, forget, output) and a cell state to stabilize long-term credit assignment versus vanilla RNNs.

## Code

```python
import torch.nn as nn

lstm = nn.LSTM(input_size=32, hidden_size=64, num_layers=1, batch_first=True)
# x: (N, T, 32) -> out: (N, T, 64)
```

## Uses

- Classic NLP/speech before transformers  
- Still useful for some streaming / small-seq problems

---

## Continue

- **Section hub:** [Sequence Models](README.md)
- **DL overview:** [Deep Learning](../README.md)
