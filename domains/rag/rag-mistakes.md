---
title: "RAG Engineering Mistakes"
description: "Troubleshooting poor chunking, embeddings, retrieval, hallucinations, latency, citations, evaluation gaps."
domain: rag
tags: [rag, mistakes, troubleshooting, phase-7]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - rag-evaluation.md
  - chunking.md
keywords: [RAG mistakes, debugging, troubleshooting]
author: hp
---

# RAG Engineering Mistakes

## Overview

Section **21** of Phase 7.

| Issue | Symptoms | Root cause | Fix |
|-------|----------|------------|-----|
| **Poor chunking** | Right doc, wrong passage | Too large/small chunks | Tune size; parent-child |
| **Bad embeddings** | Semantic misses | Wrong model | Eval models; reindex |
| **Wrong metadata** | Leak or empty results | ACL bugs | Pre-filter tests |
| **Weak retrieval** | Low recall@K | Dense-only | Hybrid + rerank |
| **Duplicate chunks** | Wasted tokens | Overlap abuse | Dedup by hash |
| **Stale documents** | Old policy answers | No refresh | Incremental ingest |
| **Poor reranking** | Right doc rank 40 | Skip rerank | Cross-encoder top-50 |
| **Hallucinations** | Unsupported claims | Weak grounding | Citations + NLI check |
| **Expensive retrieval** | High bill | Huge top_k to LLM | Retrieve 50, rerank 8 |
| **Latency** | Slow p95 | Serial steps | Parallel + cache |
| **Missing citations** | Untrusted UI | No format rules | Structured output |
| **Poor evaluation** | Regressions ship | No CI eval | Golden set gate |
| **Embedding drift** | Quality cliff | Model swap | Versioned reindex |
| **Over-retrieval** | Noise in context | top_k too high | Rerank + compress |
| **Under-retrieval** | "Don't know" often | top_k too low / threshold high | Expand K; HyDE |

Each: **Diagnose** via retrieval trace; **Prevent** with eval gates.

## Navigation

- [RAG Comparison Guides](rag-comparison-guides.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 7 Section 21 |
