---
title: "RAG Evaluation"
description: "RAG metrics — Precision@K, Recall@K, MRR, NDCG, faithfulness, RAGAS, DeepEval, golden datasets, regression testing."
domain: rag
tags: [rag, evaluation, RAGAS, metrics]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - hallucination-prevention.md
  - ../prompt-engineering/prompt-evaluation.md
  - ../ai-evaluation/README.md
keywords: [RAG evaluation, RAGAS, NDCG, faithfulness, golden dataset]
author: hp
---

# RAG Evaluation

> Measure retrieval and generation separately — the largest operational discipline in RAG.

## Overview

Section **17**.

```mermaid
flowchart LR
    subgraph Retrieval
        P[Precision@K]
        R[Recall@K]
        N[NDCG]
    end
    subgraph Generation
        F[Faithfulness]
        REL[Relevance]
        COR[Correctness]
    end
```

## Retrieval Metrics

| Metric | Meaning |
|--------|---------|
| **Precision@K** | % of top-K relevant |
| **Recall@K** | % of all relevant found in top-K |
| **MRR** | Mean reciprocal rank of first hit |
| **NDCG** | Graded relevance with position discount |
| **Hit Rate** | % queries with ≥1 relevant in K |

## Generation Metrics

| Metric | Meaning |
|--------|---------|
| **Faithfulness** | Answer supported by context |
| **Relevance** | Answers the question |
| **Correctness** | Matches gold answer |
| **Groundedness** | Claims ⊆ sources |
| **Context Precision** | Retrieved context useful |
| **Context Recall** | Retrieved context complete |

## Frameworks

| Framework | Focus |
|-----------|-------|
| **RAGAS** | Faithfulness, answer relevance, context precision/recall |
| **DeepEval** | pytest-style LLM eval |
| **ARES** | Automated RAG evaluation research toolkit |
| **Custom golden set** | Domain-specific — **required** |

## Golden Dataset

```yaml
- id: q-001
  question: "What is the refund SLA?"
  gold_doc_ids: [policy-refund-v3]
  gold_answer: "3 business days for duplicate charges."
```

Target ≥100 cases for production CI; stratify by topic.

## Regression Testing

Run eval on every index/prompt/reranker change. Block deploy if recall@5 drops >2%.

## Python Example

```python
def recall_at_k(retrieved_ids: list[str], gold_ids: set[str], k: int) -> float:
    top = set(retrieved_ids[:k])
    if not gold_ids:
        return 1.0
    return len(top & gold_ids) / len(gold_ids)
```

## Navigation

- [Advanced RAG Architectures](advanced-rag-architectures.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
