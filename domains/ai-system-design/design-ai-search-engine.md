---
title: "Design: AI Search Engine"
description: "Enterprise/knowledge search — query understanding, hybrid retrieval, ranking, feedback."
domain: ai-system-design
tags: [system-design, search, hybrid-retrieval, ranking]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - design-perplexity-ai-search.md
  - ../rag/end-to-end-rag-architecture.md
keywords: [AI search, hybrid search, query understanding]
author: hp
---

# Design: AI Search Engine

## Problem Statement

Search internal corpus + optional web with ranked results and generative answers.

## Architecture

```mermaid
flowchart LR
    Q[Query] --> QU[Query understanding]
    QU --> HY[Hybrid retrieval]
    HY --> BM25[BM25]
    HY --> VEC[Vector]
    BM25 & VEC --> FUSE[Fusion + rerank]
    FUSE --> RAG[RAG answer optional]
    FUSE --> RESULTS[Result list]
```

## Query Understanding

- Intent: navigational vs informational
- Entity extraction for filters
- Query rewriting for typos/synonyms

## User Feedback

- Click logs → reranker training
- Thumbs on answers → eval dataset

## Tradeoffs

| Generative answer | Snippets only |
|-------------------|---------------|
| Better UX | Lower hallucination risk |

## Navigation

- [Customer Support](design-ai-customer-support.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
