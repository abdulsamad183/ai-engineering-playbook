---
title: "Shorter retrieved citations beat longer context"
description: "A production RAG lesson: top-k citations with reranking outperformed stuffing more chunks into the prompt."
domain: knowledge/lessons-learned
tags: [rag, citations, reranking, context-window, retrieval]
status: published
created: 2026-07-23
updated: 2026-07-23
version: "1.0"
related:
  - ../../domains/rag/citations-and-grounding.md
  - ../../domains/rag/reranking.md
  - ../../domains/rag/chunking.md
keywords: [citations, reranking, context quality, RAG]
author: hp
---

# Shorter retrieved citations beat longer context

> Stuffing the prompt with more retrieved chunks looked safer. Measured quality and latency both got worse until we cut context and reranked harder.

## What Happened

We shipped an internal support RAG that answered policy questions with citations. After a few noisy tickets, the instinctive fix was to raise `top_k` from 5 to 12 and pass every hit into the prompt so the model would "have more evidence."

On a 40-question golden set:

| Config | Faithfulness | Citation precision | p95 latency |
|--------|--------------|--------------------|-------------|
| top_k=12, no rerank | 0.71 | 0.58 | 2.4s |
| top_k=8 → rerank to 3 | **0.86** | **0.81** | **1.6s** |

The long-context run often cited peripheral chunks (edge cases, outdated annexes) and diluted the answer. The short-citation run answered from the three best-scored passages and grounded claims cleanly.

## Why

- **Lost-in-the-middle:** Extra chunks buried the relevant sentence; the model attended to noise.
- **Citation dilution:** More sources in context made the model hedge or pick weakly related IDs.
- **Token tax:** Longer prompts raised cost and latency without improving recall of the *right* fact.
- **Reranking selects evidence:** Bi-encoder retrieval is good at recall; a cross-encoder (or lightweight lexical rerank) is what makes the final context precise.

## Recommendation

1. Retrieve generously (`top_k` 20–50 if the index is large), then **rerank and keep 2–5** chunks for the prompt.
2. Require **inline citations** tied to chunk IDs; refuse or warn when max retrieval score is low.
3. Evaluate with faithfulness + citation precision, not only answer similarity.
4. Prefer compression (extractive quotes) over dumping full parent documents unless the question needs them.

## Links

- [Citations and Grounding](../../domains/rag/citations-and-grounding.md)
- [Reranking](../../domains/rag/reranking.md)
- [Chunking](../../domains/rag/chunking.md)
- [Hallucination Prevention](../../domains/rag/hallucination-prevention.md)
- [RAG Prompt Assembly](../../domains/rag/rag-prompt-assembly.md)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-23 | Initial lesson |
