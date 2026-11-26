---
title: "AI System Design Interview Guide"
description: "Whiteboard exercises — ChatGPT, Cursor, Copilot, Perplexity, RAG, voice, support systems."
domain: interview-preparation
tags: [interview, system-design, whiteboard]
status: published
created: 2026-07-13
updated: 2026-11-22
version: "1.1"
related:
  - ../ai-system-design/README.md
  - ../ai-system-design/ai-system-design-interviews.md
keywords: [system design interview, ChatGPT design, capacity estimation]
author: hp
---

# AI System Design Interview Guide

## Overview

Section **15** — interview exercises linked to [designs](../ai-system-design/README.md).

## Whiteboard Framework (45 min)

1. Requirements (5) — functional + NFR + scale
2. Estimate (5) — QPS, storage, tokens/day
3. Diagram (10) — clients, API, data, LLM
4. Deep dives (20) — 2–3 components
5. Wrap (5) — bottlenecks, monitoring, failures

## System Exercise Index

| System | Design doc | Key interview focus |
|--------|------------|---------------------|
| **ChatGPT** | [design-chatgpt-like](../ai-system-design/consumer-products/01-design-chatgpt-like-system.md) | Streaming, memory, tools |
| **Cursor** | [design-cursor-like](../ai-system-design/developer-tools/01-design-cursor-like-system.md) | Indexing, agent edits |
| **Copilot** | [design-github-copilot](../ai-system-design/developer-tools/02-design-github-copilot.md) | Latency, FIM |
| **Perplexity** | [design-perplexity](../ai-system-design/consumer-products/02-design-perplexity-ai-search.md) | Citations, web search |
| **Deep Research** | [design-deep-research](../ai-system-design/consumer-products/04-design-deep-research-system.md) | Long jobs, multi-agent |
| **AI Search** | [design-ai-search-engine](../ai-system-design/consumer-products/03-design-ai-search-engine.md) | Hybrid retrieval |
| **Support** | [design-ai-customer-support](../ai-system-design/enterprise-assistants/01-design-ai-customer-support.md) | Escalation, CRM |
| **PDF Chat** | [design-ai-pdf-chat](../ai-system-design/developer-tools/04-design-ai-pdf-chat.md) | Ingestion, OCR |
| **Voice** | [design-ai-voice-agent](../ai-system-design/enterprise-assistants/04-design-ai-voice-agent.md) | STT/TTS pipeline |

## ChatGPT Exercise (sample)

**Requirements:** 1M DAU, multi-turn, streaming, tools.

**Capacity:** ~30–100 QPS peak; tokens/day = DAU × sessions × tokens.

**Architecture:**

```mermaid
flowchart TB
    C[Client] --> API[Chat API]
    API --> R[Redis sessions]
    API --> PG[(Postgres)]
    API --> LLM[LLM router]
    API --> TOOLS[Tool sandbox]
```

**Tradeoffs:** Server-side history vs client-only.

**Failures:** LLM 503 → fallback model; stream disconnect → resume token.

**Follow-up — reconnect without replaying work:**

- A resume cursor restores event delivery, not execution. Reconnecting must never re-run Send, Stop, a tool call, or an action the user already approved.
- Keep stable identities for each command, message, and stream, and store the last accepted event sequence. A retried command with a known ID returns the existing result instead of starting new work (see [Idempotency and Dedup](../llm-application-development/reliability/02-idempotency-and-dedup.md#streaming-turns)).
- Ignore events from superseded turns: if the user stopped, edited, or regenerated, late events from the old turn are dropped rather than rendered.
- When the client cannot tell whether a turn finished, reconcile from an authoritative server snapshot before offering Retry (see [Web Chat streaming details](../chatbots/channels/01-web-chat.md#streaming-ux-details)).

## Capacity Estimation Template

```
Peak QPS = DAU × sessions/day × turns / 86400 × peak_factor
Postgres storage ≈ messages × avg_bytes × retention
```

## Further Reading

- [AI System Design Handbook](../ai-system-design/README.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.1 | 2026-11-22 | ChatGPT exercise: reconnect follow-up |
| 1.0 | 2026-07-13 | Section 15 |
