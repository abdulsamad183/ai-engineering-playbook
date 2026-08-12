---
title: "License and Data Risk"
description: "Legal and compliance constraints on training data, base model licenses, and output ownership."
domain: llm-fine-tuning
tags: [pitfalls, 03-license-and-data-risk]
status: published
created: 2026-08-12
updated: 2026-08-12
version: "1.0"
related:
  - ../../llm-engineering/README.md
  - ../README.md
---

# License and Data Risk

> Legal and compliance constraints on training data, base model licenses, and output ownership.

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

This lesson covers **License and Data Risk** inside the `pitfalls` section of the `llm-fine-tuning` handbook. Treat it as production engineering guidance: clear definitions, when to apply the idea, system shape, and code you can adapt.

---

## Definition

**License and Data Risk** — Legal and compliance constraints on training data, base model licenses, and output ownership.

---

## Why It Matters

A great adapter trained on forbidden data is a liability.

Without a clear model for this topic, teams ship demos that fail under load, cost, or correctness pressure.

---

## Uses

| Use case | How this applies |
|----------|------------------|
| Licenses | check base and data ToS |
| PII | minimize and redact |
| Provenance | dataset cards |

---

## How It Works

Document sources; exclude confidential dumps without contracts.

```mermaid
flowchart TB
  Sources --> LegalReview --> Approved --> Train
```

---

## Worked Example

Blocked training on scraped competitor help center.

---

## Python Examples

```python
def allowed_source(license: str, has_contract: bool) -> bool:
    if license in {"proprietary_customer", "internal_ok"}:
        return has_contract or license == "internal_ok"
    return license.startswith("allow_")

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
