---
title: "Agent Architectures Papers Cheat Sheet"
description: "Quick reference mapping agent research papers to production patterns — ReAct, Reflexion, Voyager, CAMEL, SWE-Agent."
domain: papers
tags: [cheat-sheet, agents, ReAct, SWE-Agent, CAMEL]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../domains/papers/agent-reasoning-papers.md
  - ../domains/papers/swe-agent.md
keywords: [agent architectures, ReAct, SWE-Agent, Voyager, CAMEL]
author: hp
---

# Agent Architectures Papers Cheat Sheet

> See [Agent Reasoning Papers](../domains/papers/agent-reasoning-papers.md) · [SWE-Agent](../domains/papers/swe-agent.md).

## Paper → Production Mapping

| Paper | Production Pattern | Framework |
|-------|-------------------|-----------|
| ReAct | Tool-calling agent loop | LangGraph, OpenAI functions |
| Reflexion | Generate → test → reflect → retry | Custom + evaluator |
| ToT | Offline deliberation only | Custom (rare) |
| Voyager | Skill library + retrieval | Custom code library |
| CAMEL | Role-based multi-agent | CrewAI, AutoGen |
| SWE-Agent | ACI (windowed view, precise edit) | Cursor, Devin, OpenHands |

## Agent Loop Defaults

| Setting | Value |
|---------|-------|
| Max iterations | 10-15 |
| Max tool calls | 20 |
| Timeout per tool | 30s |
| Retry on tool failure | Yes (replan) |
| Reflection retries | 2-3 (if evaluator exists) |

## SWE-Agent ACI Commands

| Command | Purpose |
|---------|---------|
| `open file` | Windowed file view |
| `goto line` | Jump to line |
| `edit start:end` | Precise line replacement |
| `search query` | Code search |
| `run command` | Execute in sandbox |

## Multi-Agent Checklist

- [ ] Specialized roles with clear boundaries
- [ ] External verification (tests, HITL)
- [ ] Explicit termination conditions
- [ ] Max turns per agent conversation
- [ ] Tool access per role (least privilege)

## Do's and Don'ts

| Do | Don't |
|----|-------|
| ReAct as default agent loop | ToT as default |
| ACI for coding agents | Raw shell (`cat`, `sed`) |
| Docker sandbox for code execution | Run on host machine |
| Evaluate on SWE-bench | Claim agents work without benchmarks |
| 2-agent (generator + verifier) first | 10-agent orchestration |

## Useful Links

- [Agent Reasoning Papers](../domains/papers/agent-reasoning-papers.md)
- [SWE-Agent](../domains/papers/swe-agent.md)
- [AI Agents Domain](../domains/ai-agents/README.md)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial cheat sheet |
