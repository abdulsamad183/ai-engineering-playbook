---
title: "Retrieval Papers Cheat Sheet"
description: "Quick reference for advanced RAG papers — Self-RAG, GraphRAG, RAPTOR, CRAG selection guide."
domain: papers
tags: [cheat-sheet, rag, Self-RAG, GraphRAG, RAPTOR, CRAG, phase-papers]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../domains/papers/retrieval-papers.md
  - ../domains/rag/advanced-rag-architectures.md
keywords: [Self-RAG, GraphRAG, RAPTOR, CRAG, retrieval]
author: hp
---

# Retrieval Papers Cheat Sheet

> See [Retrieval Papers](../domains/papers/retrieval-papers.md).

## Pattern Selection

| Problem | Pattern | Priority |
|---------|---------|----------|
| Irrelevant retrieval | **CRAG** evaluator | Implement first |
| Claim not supported | **Self-RAG** verification | High-stakes apps |
| Long single documents | **RAPTOR** tree | Narrative docs |
| Cross-doc themes | **GraphRAG** | 1K+ doc corpora |
| Stale knowledge | **CRAG** web fallback | Dynamic domains |

## Quick Comparison

| Pattern | Index Cost | Query Cost | Best Corpus |
|---------|-----------|-----------|-------------|
| Naive RAG | Low | Low | Small, clean |
| CRAG | Low | Medium | Any (adds evaluator) |
| Self-RAG | Medium | High | Noisy |
| RAPTOR | High | Low | Long docs |
| GraphRAG | Very high | Medium | Large, multi-doc |

## CRAG Grades

| Grade | Action |
|-------|--------|
| Correct | Generate with retrieved docs |
| Ambiguous | Rewrite query → re-retrieve |
| Incorrect | Discard → web search fallback |

## Implementation Order

1. Hybrid search (dense + BM25) + rerank
2. CRAG retrieval evaluator
3. Citation / grounding checks
4. RAPTOR (if long docs) or GraphRAG (if large corpus)
5. Self-RAG claim verification (high-stakes)

## Do's and Don'ts

| Do | Don't |
|----|-------|
| Add CRAG evaluator first | Jump to GraphRAG for small corpora |
| Measure retrieval precision separately | Only measure end-to-end accuracy |
| Use hybrid search as default | Dense-only for keyword-heavy data |
| Budget for GraphRAG re-indexing | Run GraphRAG indexing per-query |

## Useful Links

- [Retrieval Papers](../domains/papers/retrieval-papers.md)
- [Advanced RAG Architectures](../domains/rag/advanced-rag-architectures.md)
- [RAG Domain](../domains/rag/README.md)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial cheat sheet |
