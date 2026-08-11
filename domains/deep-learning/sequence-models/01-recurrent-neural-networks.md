---
title: "1. Recurrent Neural Networks"
description: "Hidden state across time — sequential processing with shared weights."
domain: deep-learning
tags: [sequence, rnn]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 1. Recurrent Neural Networks

> Hidden state across time — sequential processing with shared weights.

## Definition

An **RNN** updates a hidden state \(h_t = f(h_{t-1}, x_t)\) to model sequences. Vanilla RNNs struggle with long-range dependencies (vanishing gradients).

```mermaid
flowchart LR
  X1 --> H1 --> H2 --> H3
  X2 --> H2
  X3 --> H3
```

## See also

- [LSTM](02-lstm.md) · [GRU](03-gru.md) · [Transformers](../../transformers/README.md)

---

## Continue

- **Section hub:** [Sequence Models](README.md)
- **DL overview:** [Deep Learning](../README.md)
