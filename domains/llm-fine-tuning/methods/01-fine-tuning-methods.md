---
title: "Fine-Tuning Methods Overview"
description: "A map of full fine-tuning, parameter-efficient methods (LoRA/QLoRA), and preference optimization approaches."
domain: llm-fine-tuning
tags: [methods, 01-fine-tuning-methods]
status: published
created: 2026-08-12
updated: 2026-08-12
version: "1.0"
related:
  - ../../llm-engineering/README.md
  - ../README.md
---

# Fine-Tuning Methods Overview

> A map of full fine-tuning, parameter-efficient methods (LoRA/QLoRA), and preference optimization approaches.

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

This lesson covers **Fine-Tuning Methods Overview** inside the `methods` section of the `llm-fine-tuning` handbook. Treat it as production engineering guidance: clear definitions, when to apply the idea, system shape, and code you can adapt.

---

## Definition

**Fine-Tuning Methods Overview** — A map of full fine-tuning, parameter-efficient methods (LoRA/QLoRA), and preference optimization approaches.

---

## Why It Matters

Method choice drives GPU cost, catastrophic forgetting risk, and serving complexity.

Without a clear model for this topic, teams ship demos that fail under load, cost, or correctness pressure.

---

## Uses

| Use case | How this applies |
|----------|------------------|
| Domain SFT | LoRA on instruct base |
| Mobile | QLoRA then merge/quantize |
| Policy | DPO after SFT |

---

## How It Works

Default path: strong base to LoRA SFT to optional preference stage to eval gate.

```mermaid
flowchart TB
  Base[Base model] --> SFT[SFT / LoRA]
  SFT --> Pref[DPO / ORPO]
  Pref --> Serve[Deploy]
```

---

## Worked Example

Customer support LoRA beats full FT on cost/quality tradeoff.

---

## Python Examples

```python
def pick_method(params_b: float, gpu_gb: int) -> str:
    if gpu_gb < 24:
        return "qlora"
    if params_b >= 70:
        return "lora"
    return "lora_or_full"

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
