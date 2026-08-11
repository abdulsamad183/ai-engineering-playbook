---
title: "4. Attention Mechanism"
description: "Weighted focus over memory — the core idea behind transformers."
domain: deep-learning
tags: [advanced, attention]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 4. Attention Mechanism

> Weighted focus over memory — the core idea behind transformers.

## Definition

**Attention** computes weights over a set of values given a query (often via softmax of scores). Enables dynamic routing of information.

## Sketch

```text
Attention(Q, K, V) = softmax(QK^T / √d) V
```

## See also

- [Transformers](../../transformers/README.md)

---

## Continue

- **Section hub:** [Advanced Deep Learning](README.md)
- **DL overview:** [Deep Learning](../README.md)
