---
title: "Statistics for Evaluation"
description: "How to measure model quality without fooling yourself — metrics, variance, and experiments."
domain: mathematics-statistics
tags: [mathematics-statistics]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Statistics for Evaluation

> How to measure model quality without fooling yourself — metrics, variance, and experiments.

## Definition

Evaluation statistics turn noisy observations (user ratings, task scores) into decisions: is system B better than A? Key ideas: sampling error, confidence intervals, significance, and metric choice (precision/recall/F1, win rate, etc.).

## Why it matters

Shipping on vibes causes regressions. Lightweight stats prevent celebrating noise as progress.

## How it works

```mermaid
flowchart LR
  D[Dataset / traffic] --> M[Metric]
  M --> C[Compare variants]
  C --> Dec{Decision}
  Dec -->| Ship
  Dec -->| Iterate
  Dec -->| Need more data
```

## Key principles

1. **Fix the metric to the job** — Support bots ≠ creative writing.
2. **Estimate uncertainty** — Small n → wide confidence intervals.
3. **Segment results** — Overall averages hide failure modes.

## Common applications

| Application | Description |
|-------------|-------------|
| Offline eval | Golden sets and CI gates |
| Online experiments | A/B tests on latent/quality metrics |
| RAG scoring | Retrieval + answer faithfulness |

## Common mistakes

- Declaring a winner on 20 examples
- Optimizing a proxy metric that users do not care about

## Further reading

- [LLM Evaluation](../ai-evaluation/README.md)
- [RAG Evaluation](../rag/rag-evaluation.md)
