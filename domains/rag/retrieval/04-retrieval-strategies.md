---
title: "Retrieval Strategies for RAG"
description: "Dense, sparse, hybrid, hierarchical, multi-stage, multi-query, parent-child retrieval — comparison and production guidance."
domain: rag
tags: [rag, retrieval, hybrid, dense]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - bm25.md
  - query-engineering.md
  - reranking.md
  - embeddings-for-rag.md
keywords: [retrieval, dense retrieval, hybrid retrieval, multi-query]
author: hp
---

# Retrieval Strategies for RAG

> How production systems fetch candidate knowledge — strategy selection and tradeoffs.

## Overview

Section **9**.

| Strategy | Mechanism | Best for |
|----------|-----------|----------|
| **Dense** | Embedding similarity | Paraphrase, semantic |
| **Sparse** | BM25 / SPLADE | Keywords, SKUs, legal cites |
| **Lexical** | Inverted index | Exact terms |
| **Hybrid** | Fuse dense + sparse | Enterprise default |
| **Metadata filter** | SQL/JSON predicates | Tenant, ACL, date |
| **Hierarchical** | Tree walk + leaf search | Long structured docs |
| **Multi-stage** | Cheap recall → rerank | Large corpora |
| **Multi-query** | Several query variants | Ambiguous questions |
| **Parent retrieval** | Retrieve parent after child hit | Parent-child chunks |
| **Child retrieval** | Small chunks for precision | Fine-grained facts |

```mermaid
flowchart LR
    Q[Query] --> D[Dense]
    Q --> S[Sparse]
    D --> FUSE[RRF Fusion]
    S --> FUSE
    FUSE --> RER[Rerank]
```

**Production default:** Hybrid top-50 → rerank to top-8 → compress to budget.

## Navigation

- [BM25](bm25.md) · [Query Engineering](query-engineering.md) · [Reranking](reranking.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
