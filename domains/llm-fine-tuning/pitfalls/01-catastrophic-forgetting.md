---
title: "Catastrophic Forgetting"
description: "Loss of prior capabilities when fine-tuning updates weights away from the base distribution."
domain: llm-fine-tuning
tags: [pitfalls, 01-catastrophic-forgetting]
status: published
created: 2026-08-12
updated: 2026-08-12
version: "1.0"
related:
  - ../../llm-engineering/README.md
  - ../README.md
---

# Catastrophic Forgetting

> Loss of prior capabilities when fine-tuning updates weights away from the base distribution.

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

This lesson covers **Catastrophic Forgetting** inside the `pitfalls` section of the `llm-fine-tuning` handbook. Treat it as production engineering guidance: clear definitions, when to apply the idea, system shape, and code you can adapt.

---

## Definition

**Catastrophic Forgetting** — Loss of prior capabilities when fine-tuning updates weights away from the base distribution.

---

## Why It Matters

Forgetting shows up as broken refusals, worse coding, or odd formatting regressions.

Without a clear model for this topic, teams ship demos that fail under load, cost, or correctness pressure.

---

## Uses

| Use case | How this applies |
|----------|------------------|
| Mitigate | PEFT, replay data, lower LR |
| Detect | general smoke suite |
| Recover | rollback adapter |

---

## How It Works

Always keep a general capability pack in CI for adapters.

```mermaid
flowchart TB
  FT --> Smoke[General smoke] -->|drop| Rollback
  Smoke -->|ok| Continue
```

---

## Worked Example

After FT, JSON mode broke — add format examples and lower LR.

---

## Python Examples

```python
def forgetting_alert(base: dict, ft: dict, keys: list[str], max_drop=0.03) -> list[str]:
    return [k for k in keys if base[k] - ft[k] > max_drop]

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
