---
title: "Reranking for RAG"
description: "Cross-encoders, bi-encoders, Cohere/Jina/BGE rerankers, LLM reranking — latency, cost, quality tradeoffs."
domain: rag
tags: [rag, reranking, cross-encoder]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - retrieval-strategies.md
  - rag-evaluation.md
keywords: [reranking, cross-encoder, Cohere rerank]
author: hp
---

# Reranking for RAG

## Overview

Section **12**. Bi-encoder retrieval is fast but approximate; **cross-encoders** score (query, passage) jointly for higher precision.

```mermaid
flowchart LR
    RET[Top-50 candidates] --> RER[Cross-encoder]
    RER --> TOP[Top-8 for LLM]
```

## Approaches

| Type | Latency | Quality |
|------|---------|---------|
| **Bi-encoder** (retrieval) | Low | Good recall |
| **Cross-encoder** | Medium | High precision |
| **Cohere Rerank API** | Low ops | Strong |
| **Jina / BGE reranker** | Self-host | Cost control |
| **LLM reranking** | High | Flexible, expensive |

## Typical Gains

NDCG@10 improvements of 10–30% vs retrieval-only — standard in production.

## Python Example

```python
# sentence-transformers cross-encoder
from sentence_transformers import CrossEncoder

model = CrossEncoder("BAAI/bge-reranker-v2-m3")
pairs = [[query, c.text] for c in candidates]
scores = model.predict(pairs)
ranked = sorted(zip(candidates, scores), key=lambda x: -x[1])
```

## Navigation

- [RAG Context Compression](rag-context-compression.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
