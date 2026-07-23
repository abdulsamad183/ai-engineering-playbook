---
title: "Agent Evaluation"
description: "Evaluating agents — task success, tool accuracy, planning quality, latency, cost, reliability, failure recovery."
domain: ai-agents
tags: [ai-agents, evaluation, metrics]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../rag/rag-evaluation.md
  - ../ai-evaluation/README.md
keywords: [agent evaluation, task success, tool accuracy]
author: hp
---

# Agent Evaluation

## Overview

Section **16**.

| Metric | Measures |
|--------|----------|
| **Task success** | End goal achieved |
| **Tool accuracy** | Correct tool + args |
| **Planning quality** | Steps minimal/valid |
| **Reflection quality** | Catches errors |
| **Latency** | Time to completion |
| **Cost** | Tokens + tool API $ |
| **Reliability** | Success rate over runs |
| **Recovery** | Recovers from injected failures |

## Evaluation Strategies

1. **Scenario suite** — scripted tasks with expected tool sequence
2. **LLM judge** — grade final artifact
3. **Human eval** — sample production traces
4. **Chaos testing** — fail tools randomly

## Golden Tasks

```yaml
- id: support-refund-01
  goal: "Process duplicate charge inquiry"
  expected_tools: [search_kb, get_account]
  success: "mentions 3 business days"
```

## Navigation

- [Production Agent Engineering](production-agent-engineering.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
