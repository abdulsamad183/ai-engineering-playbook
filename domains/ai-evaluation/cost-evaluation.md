---
title: "Cost Evaluation"
description: "Token, embedding, retrieval, tool, infrastructure, agent costs — per request and per task."
domain: ai-evaluation
tags: [ai-evaluation, cost, tokens, optimization, phase-10]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - latency-evaluation.md
  - ../llm-engineering/llm-cost-optimization.md
keywords: [cost per request, token cost, eval cost]
author: hp
---

# Cost Evaluation

## Overview

Section **13** of Phase 10.

## Cost Components

| Component | Typical driver |
|-----------|----------------|
| **Tokens** | Input + output LLM |
| **Embeddings** | Index + query embed |
| **Retrieval** | Vector DB, reranker API |
| **Tools** | External API fees |
| **Infrastructure** | GPU, containers |
| **Agent** | Multi-step token multiply |
| **Eval** | LLM-judge runs |

## Key Metrics

- **Cost per request** — avg $/call
- **Cost per successful task** — $/completed workflow
- **Eval cost per run** — budget for CI

## Python Example

```python
def request_cost(input_tokens: int, output_tokens: int, price_in: float, price_out: float) -> float:
    return (input_tokens * price_in + output_tokens * price_out) / 1_000_000
```

## Optimization

- Cache embeddings and retrieval
- Smaller judge model for eval
- Stratified eval sampling

## Navigation

- [Benchmarking](benchmarking.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 10 Section 13 |
