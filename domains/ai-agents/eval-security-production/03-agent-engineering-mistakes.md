---
title: "Agent Engineering Mistakes"
description: "Troubleshooting infinite loops, poor planning, tool misuse, stale memory, race conditions, retry storms."
domain: ai-agents
tags: [ai-agents, mistakes, troubleshooting]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - agent-evaluation.md
keywords: [agent mistakes, infinite loop, retry storm]
author: hp
---

# Agent Engineering Mistakes

## Overview

Section **19**.

| Issue | Symptoms | Fix |
|-------|----------|-----|
| **Infinite loops** | max steps hit always | Termination conditions; detect repeated actions |
| **Poor planning** | Wrong tool order | Explicit planner; eval scenarios |
| **Tool misuse** | Wrong args | Schema validation; examples in tool desc |
| **Stale memory** | Wrong context | TTL; version stamps |
| **Race conditions** | Corrupt shared state | Locks; immutable artifacts |
| **State corruption** | Resume fails | Schema versioning; migrations |
| **Weak supervision** | Bad writes ship | HITL on destructive tools |
| **Context explosion** | Token errors | Summarize observations; truncate tool output |
| **Hallucinated tools** | Invalid tool name | Strict registry; reject unknown |
| **Retry storms** | API outage amplifies | Circuit breaker; jitter |
| **Over-engineering** | 5 agents for 1 task | Start single ReAct |
| **Excessive latency** | User timeout | Parallel tools; faster models for routing |

Each: **Diagnose** via trace; **Prevent** via eval + budgets.

## Navigation

- [Case Studies](agent-case-studies.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
