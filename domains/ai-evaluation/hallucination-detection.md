---
title: "Hallucination Detection"
description: "Hallucination types, detection strategies, automated and human review, confidence estimation."
domain: ai-evaluation
tags: [ai-evaluation, hallucination, faithfulness, detection]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - llm-evaluation-metrics.md
  - rag-evaluation.md
  - ../rag/hallucination-prevention.md
keywords: [hallucination, fabrication, groundedness, citation hallucination]
author: hp
---

# Hallucination Detection

## Overview

Section **6**.

## Hallucination Types

| Type | Description | Common in |
|------|-------------|-----------|
| **Retrieval** | Ignores or misuses retrieved context | RAG |
| **Reasoning** | Invalid logical steps | Agents, CoT |
| **Citation** | Fake or wrong sources | RAG with citations |
| **Fabrication** | Invented entities/facts | Open QA |
| **Unsupported claims** | Plausible but unverifiable | Summaries |

## Detection Strategies

```mermaid
flowchart TB
    OUT[Output] --> NLI[NLI / entailment check]
    OUT --> CITE[Citation verification]
    OUT --> JUDGE[LLM judge]
    OUT --> HUM[Human review queue]
    NLI & CITE & JUDGE --> SCORE[Hallucination score]
```

| Strategy | Pros | Cons |
|----------|------|------|
| **NLI entailment** | Fast | brittle on long context |
| **LLM-as-judge** | Flexible | Cost, bias |
| **Citation match** | Objective for RAG | Needs structured cites |
| **Human review** | Gold standard | Slow |

## Confidence Estimation

- Token logprobs (when available)
- Self-consistency across samples
- Retrieval score thresholds → abstain

## Production Workflow

1. Auto-score all outputs in eval
2. Route low faithfulness to human queue
3. Cluster failure modes → fix retrieval or prompt

## Python Example

```python
def citation_hallucination(answer: str, valid_ids: set[str]) -> list[str]:
    import re
    cited = set(re.findall(r"\[(\d+)\]", answer))
    return list(cited - valid_ids)
```

## Navigation

- [RAG Evaluation](rag-evaluation.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
