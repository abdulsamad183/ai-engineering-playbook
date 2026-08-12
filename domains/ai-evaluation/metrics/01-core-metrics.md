---
title: "Core Metrics"
description: "Foundational quality, calibration, and operational metrics for LLM and classical ML evaluation."
domain: ai-evaluation
tags: [metrics, evaluation]
status: published
created: 2026-08-11
updated: 2026-08-12
version: "2.1"
related:
  - 02-llm-evaluation-metrics.md
  - ../foundations/01-introduction-to-ai-evaluation.md
  - ../surface-areas/01-prompt-evaluation.md
---

# Core Metrics

> Metrics turn model behavior into decisions: ship, block, or rollback. Pick metrics that match the **cost of errors**, not vanity scores.

## Families

| Family | Examples | Use when |
|--------|----------|----------|
| Task success | accuracy, exact match, pass@k | Clear labels |
| Ranking | nDCG, recall@k, MRR | Retrieval |
| Generative quality | rubrics, preference win-rate | Open-ended text |
| Faithfulness | citation support, entailment | RAG / grounded |
| Ops | latency p95, $/success, error rate | Production |
| Safety | toxicity, jailbreak rate, PII leak | Guardrails |

## Selection rules

1. One **primary** offline metric for gating.
2. Secondary metrics for slices (locales, intents, tenants).
3. Online twin of the primary (thumbs, task completion).
4. Never optimize a metric you cannot compute in CI.

## Example gate

```python
def ship(scores: dict[str, float]) -> bool:
    return (
        scores["task_success"] >= 0.85
        and scores["faithfulness"] >= 0.90
        and scores["p95_latency_ms"] <= 2500
        and scores["jailbreak_rate"] <= 0.01
    )
```

## Calibration & slices

Overall accuracy can hide failures on refunds or a language. Always report slice tables for critical intents.

## Mistakes

- Reporting train accuracy.
- LLM-as-judge without agreement checks.
- Changing labels and metrics in the same release.

## Interview

**Q: Accuracy vs recall?** For support deflection, false closes (precision) may hurt CSAT more — choose metrics from product cost, not defaults.


## Worked example: support bot

Primary offline: task_success on 200 dialogues.
Secondary: faithfulness on grounded answers; refusal quality on unsafe asks.
Online: CSAT + containment; page on jailbreak_rate spike.

## Statistical caution

Small golden sets need paired comparisons and confidence intervals — a 2% bump on 30 cases may be noise.

## Dashboard sketch

| Panel | Signal |
|-------|--------|
| Quality | primary metric trend |
| Safety | policy hits |
| Cost | $ / successful task |
| Latency | p95 by route |

## Navigation

- [LLM metrics](02-llm-evaluation-metrics.md) · [Prompt evaluation](../surface-areas/01-prompt-evaluation.md)
- [Section hub](README.md) · [Eval hub](../README.md)
