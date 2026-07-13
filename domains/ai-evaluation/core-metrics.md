---
title: "Core Evaluation Metrics"
description: "Accuracy, precision, recall, F1, exact match, BLEU, ROUGE, BERTScore — when to use and when they mislead."
domain: ai-evaluation
tags: [ai-evaluation, metrics, accuracy, f1, phase-10]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - llm-evaluation-metrics.md
  - ai-evaluation-comparison-guides.md
keywords: [accuracy, F1, exact match, BLEU, ROUGE]
author: hp
---

# Core Evaluation Metrics

## Overview

Section **4** of Phase 10. Classical metrics still apply to classification and extraction tasks.

## Metric Guide

| Metric | Formula intuition | Good for | Misleading when |
|--------|-------------------|----------|-----------------|
| **Accuracy** | Correct / total | Balanced classification | Imbalanced classes |
| **Precision** | TP / (TP+FP) | Minimize false positives | Ignoring recall |
| **Recall** | TP / (TP+FN) | Minimize false negatives | Ignoring precision |
| **F1** | Harmonic mean P/R | Single balance score | Need asymmetric costs |
| **Exact Match** | String equality | Short answers, IDs | Paraphrases valid |
| **BLEU** | n-gram overlap | Machine translation | Semantic equivalence |
| **ROUGE** | Recall-oriented overlap | Summarization | Factual correctness |
| **BERTScore** | Embedding similarity | Semantic similarity | Hallucinated fluency |

## When to Use

- **Structured extraction** → Exact match + field-level F1
- **Classification routing** → Precision/recall per class
- **Summarization** → ROUGE + faithfulness judge
- **Open-ended QA** → Avoid BLEU alone; use LLM metrics

## Python Example

```python
def f1(precision: float, recall: float) -> float:
    if precision + recall == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)

def exact_match(pred: str, gold: str) -> bool:
    return pred.strip().lower() == gold.strip().lower()
```

## Best Practices

- Report confidence intervals on small sets
- Per-slice metrics (language, domain, difficulty)

## Anti-Patterns

- Single accuracy number on imbalanced data
- BLEU for conversational agents

## Interview Preparation

**Q: Why is exact match insufficient for LLM eval?**

> Valid paraphrases fail EM; use semantic metrics or task-specific judges while keeping EM for IDs and codes.

## Navigation

- [LLM Evaluation Metrics](llm-evaluation-metrics.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 10 Section 4 |
