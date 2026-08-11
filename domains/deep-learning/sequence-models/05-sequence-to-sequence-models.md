---
title: "5. Sequence-to-Sequence Models"
description: "Encoder–decoder for transduction — translation, summarization, ASR roots."
domain: deep-learning
tags: [sequence, seq2seq]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 5. Sequence-to-Sequence Models

> Encoder–decoder for transduction — translation, summarization, ASR roots.

## Definition

**Seq2seq** maps an input sequence to an output sequence via an encoder (reads source) and decoder (writes target), historically with RNNs + attention.

## Pattern

```mermaid
flowchart LR
  Src[Source] --> Enc[Encoder]
  Enc --> Ctx[Context / memory]
  Ctx --> Dec[Decoder]
  Dec --> Tgt[Target tokens]
```

## See also

- [Attention Mechanism](../advanced-deep-learning/04-attention-mechanism.md) · [Transformers](../../transformers/README.md)

---

## Continue

- **Section hub:** [Sequence Models](README.md)
- **DL overview:** [Deep Learning](../README.md)
