---
title: "Reasoning Methods Cheat Sheet"
description: "Quick reference for agent reasoning patterns — ReAct, ToT, Reflexion, CoT, and when to use each."
domain: papers
tags: [cheat-sheet, reasoning, ReAct, ToT, Reflexion]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../domains/papers/agent-reasoning-papers.md
  - ../domains/papers/research-comparison-guides.md
keywords: [ReAct, tree of thoughts, reflexion, chain of thought, reasoning]
author: hp
---

# Reasoning Methods Cheat Sheet

> See [Agent Reasoning Papers](../domains/papers/agent-reasoning-papers.md).

## Pattern Selection

| I need... | Use | Cost |
|-----------|-----|------|
| Tool-using agent | **ReAct** | Medium |
| Better code quality | **ReAct + Reflexion** | High |
| Multi-step reasoning (no tools) | **Chain-of-Thought** | Medium |
| Explore multiple solution paths | **Tree of Thoughts** | Very high |
| Reduce answer variance | **Self-Consistency** | High |
| Open-ended skill building | **Voyager** (skill library) | High setup |

## Quick Comparison

| Pattern | Loop | Backtrack | Needs Evaluator |
|---------|------|-----------|-----------------|
| CoT | Think → Answer | No | No |
| ReAct | Thought → Action → Obs | No | No |
| ToT | Branch → Evaluate → Prune | Yes | Yes |
| Reflexion | Act → Eval → Reflect → Retry | Yes (retry) | Yes |
| Self-Consistency | Sample N → Vote | No | No |

## ReAct Template

```
Thought: [reason about next step]
Action: [tool_name]
Action Input: [JSON args]
Observation: [injected by system]
... repeat ...
Final Answer: [response]
```

## Production Defaults

- **Agent loop:** ReAct with max 10-15 iterations
- **Reasoning:** CoT for complex, direct for simple
- **Quality boost:** Reflexion with 2-3 retries (when evaluator exists)
- **Never default:** Tree of Thoughts (offline only)

## Do's and Don'ts

| Do | Don't |
|----|-------|
| Cap agent iterations | Allow unlimited loops |
| Hide reasoning from users | Expose raw thought traces |
| Replan on tool failure | Ignore failed tool calls |
| Use Reflexion with automated tests | Retry without evaluation |

## Useful Links

- [Agent Reasoning Papers](../domains/papers/agent-reasoning-papers.md)
- [Comparison Guides](../domains/papers/research-comparison-guides.md)
- [Agent Reasoning Patterns](../domains/ai-agents/agent-reasoning-patterns.md)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial cheat sheet |
