---
title: "Cleaning and Leakage Control"
description: "Removing PII, train-test leakage, prompt injection in labels, and near-duplicates from fine-tuning corpora."
domain: llm-fine-tuning
tags: [data, 03-cleaning-and-leakage]
status: published
created: 2026-08-12
updated: 2026-08-12
version: "1.0"
related:
  - ../../llm-engineering/README.md
  - ../README.md
---

# Cleaning and Leakage Control

> Removing PII, train-test leakage, prompt injection in labels, and near-duplicates from fine-tuning corpora.

## Table of Contents

- [Overview](#overview)
- [Definition](#definition)
- [Why It Matters](#why-it-matters)
- [Uses](#uses)
- [How It Works](#how-it-works)
- [Worked Example](#worked-example)
- [Python Examples](#python-examples)
- [Production Considerations](#production-considerations)
- [Performance Considerations](#performance-considerations)
- [Cost Considerations](#cost-considerations)
- [Security Considerations](#security-considerations)
- [Best Practices](#best-practices)
- [Common Mistakes](#common-mistakes)
- [Interview Preparation](#interview-preparation)
- [Navigation](#navigation)

---

## Overview

This lesson covers **Cleaning and Leakage Control** inside the `data` section of the `llm-fine-tuning` handbook. Treat it as production engineering guidance: clear definitions, when to apply the idea, system shape, and code you can adapt.

---

## Definition

**Cleaning and Leakage Control** — Removing PII, train-test leakage, prompt injection in labels, and near-duplicates from fine-tuning corpora.

---

## Why It Matters

Leakage inflates eval scores; poisoned labels teach unsafe behavior.

Without a clear model for this topic, teams ship demos that fail under load, cost, or correctness pressure.

---

## Uses

| Use case | How this applies |
|----------|------------------|
| PII | redaction pipelines |
| Eval integrity | hash dedupe vs test |
| Security | strip secrets from traces |

---

## How It Works

Never train on the frozen golden set. Scan for eval n-grams.

```mermaid
flowchart LR
  Corpus --> Redact --> Dedupe --> LeakCheck[Leak check] --> TrainSet
```

---

## Worked Example

Found 3% of train chats overlapping eval; removed before LoRA.

---

## Python Examples

```python
def ngram_overlap(a: str, b: str, n: int = 8) -> float:
    def grams(s):
        toks = s.lower().split()
        return set(tuple(toks[i:i+n]) for i in range(max(0, len(toks)-n+1)))
    A, B = grams(a), grams(b)
    return len(A & B) / max(1, len(A))

```

---

## Production Considerations

- Log request IDs across orchestration steps.
- Fail closed on auth and policy; degrade only where product explicitly allows it.
- Keep feature flags for prompt/model swaps.

## Performance Considerations

- Bound concurrency to the model provider.
- Stream when UX needs time-to-first-token.
- Cache stable sub-results carefully with invalidation rules.

## Cost Considerations

- Track tokens and tool calls per feature / tenant.
- Prefer smaller models for routers and classifiers.
- Cap max tokens and tool-loop iterations.

## Security Considerations

- Never put secrets in prompts.
- Treat model output as untrusted until validated.
- Enforce tenant isolation on retrieval and tools.

---

## Best Practices

1. Prefer explicit interfaces over prompt-only business logic.
2. Measure latency, cost, and quality together.
3. Keep prompts and configs versioned.

---

## Common Mistakes

- Shipping without golden evals.
- Hiding critical state only inside the model context.
- No timeouts or budget limits on model calls.

---

## Interview Preparation

**Q: What belongs in the app vs the prompt?**

A: Deterministic rules, auth, billing, and validation stay in code; stylistic and interpretive behavior can live in prompts.

**Q: How do you roll out a change safely?**

A: Version it, shadow or A/B on a slice, watch eval + online metrics, keep a one-click rollback.

---

## Navigation

- **Section hub:** [README](README.md)
- **Topic hub:** [../README.md](../README.md)
