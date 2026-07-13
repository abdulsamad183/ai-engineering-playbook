---
title: "RAG Context Compression"
description: "Passage compression, filtering, summarization, redundancy removal, token budgeting for retrieved context."
domain: rag
tags: [rag, compression, token-budget, phase-7]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - rag-prompt-assembly.md
  - ../context-engineering/context-compression.md
keywords: [context compression, passage selection, token budget]
author: hp
---

# RAG Context Compression

## Overview

Section **13** of Phase 7. After reranking, fit passages into retrieval token budget without losing answer-critical sentences.

## Techniques

- Drop lowest rerank scores until under budget
- Extractive sentence selection per passage
- Merge adjacent chunks from same doc
- Remove redundant headers/footers
- LLM summarize only if still over budget (validate entities)

See [Context Compression](../context-engineering/context-compression.md) for general patterns.

## Navigation

- [RAG Prompt Assembly](rag-prompt-assembly.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 7 Section 13 |
