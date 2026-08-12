---
title: "PE vs RAG vs Fine-Tuning"
description: "A comparison of prompt engineering, retrieval-augmented generation, and fine-tuning as levers for LLM product quality."
domain: llm-fine-tuning
tags: [decision, 02-pe-vs-rag-vs-ft]
status: published
created: 2026-08-12
updated: 2026-08-12
version: "1.0"
related:
  - ../../llm-engineering/README.md
  - ../README.md
---

# PE vs RAG vs Fine-Tuning

> A comparison of prompt engineering, retrieval-augmented generation, and fine-tuning as levers for LLM product quality.

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

This lesson covers **PE vs RAG vs Fine-Tuning** inside the `decision` section of the `llm-fine-tuning` handbook. Treat it as production engineering guidance: clear definitions, when to apply the idea, system shape, and code you can adapt.

---

## Definition

**PE vs RAG vs Fine-Tuning** — A comparison of prompt engineering, retrieval-augmented generation, and fine-tuning as levers for LLM product quality.

---

## Why It Matters

Pick the cheapest lever that hits the bar. Mixing levers without hierarchy wastes data and compute.

Without a clear model for this topic, teams ship demos that fail under load, cost, or correctness pressure.

---

## Uses

| Use case | How this applies |
|----------|------------------|
| Facts change weekly | RAG |
| Tone and format | PE or light FT |
| New skill on small model | FT |

---

## How It Works

Start left; move right only with measured gaps.

```mermaid
flowchart LR
  PE[Prompt Engineering] --> RAG[RAG]
  RAG --> FT[Fine-Tuning]
```

---

## Worked Example

Legal Q&A: PE for format, RAG for statutes, FT only for citation style consistency.

---

## Python Examples

```python
def choose_lever(needs_fresh_facts: bool, needs_style: bool, pe_ok: bool) -> str:
    if needs_fresh_facts:
        return "rag"
    if not pe_ok and needs_style:
        return "fine_tune"
    return "prompt"

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
