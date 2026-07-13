---
title: "RAG Comparison Guides"
description: "Decision matrices — chunking, embeddings, vector DBs, retrieval, rerankers, advanced architectures, eval frameworks."
domain: rag
tags: [rag, comparison, decision-matrix, phase-7]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - introduction-to-rag.md
  - vector-databases.md
keywords: [comparison, chunking, vector database, reranker]
author: hp
---

# RAG Comparison Guides

## Chunking Strategies

| Strategy | Quality | Cost | Best for |
|----------|---------|------|----------|
| Fixed | Low | Low | Prototype |
| Recursive | Med | Low | General |
| Semantic | High | High | Mixed docs |
| Parent-child | High | Med | Enterprise KB |

## Embedding Models

See [Embeddings for RAG](embeddings-for-rag.md) — match model to language, domain, hosting.

## Vector Databases

| DB | Ops | Scale | Hybrid | Best for |
|----|-----|-------|--------|----------|
| Chroma | Low | S-M | Basic | Dev/MVP |
| pgvector | Med | M | SQL+BM25 | PG shops |
| Qdrant | Med | L | Filters | Self-host prod |
| Pinecone | Low | L | Filters | Managed SaaS |
| Milvus | High | XL | Yes | Billion scale |
| FAISS | High | XL | DIY | Custom |

## BM25 vs Dense

| | BM25 | Dense |
|---|------|-------|
| Exact terms | ✓✓ | ✗ |
| Paraphrase | ✗ | ✓✓ |
| **Use** | Hybrid | Hybrid |

## Rerankers

| | API (Cohere) | Open (BGE) |
|---|--------------|------------|
| Ops | Low | GPU |
| Quality | High | High |

## Eval Frameworks

| | RAGAS | Custom golden |
|---|-------|---------------|
| Setup | Fast | Effort |
| Domain fit | General | **Best** |

## Navigation

- [Introduction to RAG](introduction-to-rag.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 7 comparisons |
