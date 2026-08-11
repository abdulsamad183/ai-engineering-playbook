---
title: "2. Transformer Overview"
description: "Embeddings → N blocks of attention+FFN → output head."
domain: transformers
tags: [basics, overview]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# 2. Transformer Overview

> Embeddings → N blocks of attention+FFN → output head.

## Definition

A **Transformer** maps token embeddings through stacked blocks of multi-head attention and feed-forward layers with residuals and normalization.

```mermaid
flowchart TB
  Tok[Tokens] --> Emb[Embed + position]
  Emb --> B1[Block]
  B1 --> B2[Block x N]
  B2 --> Out[Logits / hidden states]
```

---

## Continue

- **Section hub:** [Transformer Basics](README.md)
- **Transformers overview:** [Transformers](../README.md)
