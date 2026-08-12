---
title: "ROI and Readiness Checklist"
description: "Estimating label cost, training cost, serving cost, and organizational readiness before starting a fine-tune."
domain: llm-fine-tuning
tags: [decision, 03-roi-and-readiness]
status: published
created: 2026-08-12
updated: 2026-08-12
version: "1.0"
related:
  - ../../llm-engineering/README.md
  - ../README.md
---

# ROI and Readiness Checklist

> Estimating label cost, training cost, serving cost, and organizational readiness before starting a fine-tune.

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

This lesson covers **ROI and Readiness Checklist** inside the `decision` section of the `llm-fine-tuning` handbook. Treat it as production engineering guidance: clear definitions, when to apply the idea, system shape, and code you can adapt.

---

## Definition

**ROI and Readiness Checklist** — Estimating label cost, training cost, serving cost, and organizational readiness before starting a fine-tune.

---

## Why It Matters

Many FT projects fail from missing evals, unclear owners, or no serving plan — not from LoRA math.

Without a clear model for this topic, teams ship demos that fail under load, cost, or correctness pressure.

---

## Uses

| Use case | How this applies |
|----------|------------------|
| Startup | LoRA on open model |
| Enterprise | Governed data plus eval gates |
| Regulated | Training data lineage |

---

## How It Works

Gate each stage with exit criteria.

```mermaid
flowchart TB
  Data[Data ready] --> Eval[Eval ready]
  Eval --> Train[Train budget]
  Train --> Serve[Serving plan]
```

---

## Worked Example

Team has 2k pairs, golden set of 200, staging GPU, and rollback to base model.

---

## Python Examples

```python
def readiness(n_pairs: int, n_eval: int, has_rollback: bool) -> list[str]:
    gaps = []
    if n_pairs < 500:
        gaps.append("more SFT data")
    if n_eval < 100:
        gaps.append("larger golden set")
    if not has_rollback:
        gaps.append("rollback plan")
    return gaps

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
