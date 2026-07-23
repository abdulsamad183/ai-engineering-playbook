---
title: "Agent Comparison Guides"
description: "Agent vs workflow, ReAct vs reflection, supervisor vs swarm, framework comparison, memory and planning strategies."
domain: ai-agents
tags: [ai-agents, comparison, frameworks]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - frameworks/README.md
  - multi-agent-systems.md
keywords: [comparison, agent frameworks, supervisor vs swarm]
author: hp
---

# Agent Comparison Guides

## Agent vs Workflow

| | Agent | Workflow |
|---|-------|----------|
| Flexibility | High | Low |
| Predictability | Lower | High |
| Cost | Variable | Stable |
| Use | Open tasks | Fixed pipelines |

## ReAct vs Reflection

| | ReAct | Reflection |
|---|-------|------------|
| Latency | Lower | Higher |
| Quality | Good | Better for artifacts |
| Cost | Medium | High |

## Supervisor vs Swarm

| | Supervisor | Swarm |
|---|------------|-------|
| Control | Centralized | Distributed |
| Failure mode | Supervisor error | Coordination chaos |
| Scale | Medium teams | Parallel research |

## Framework Comparison

| Framework | Learning | Production | Multi-agent | Checkpoint |
|-----------|----------|------------|-------------|------------|
| LangGraph | Medium | High | Yes | Built-in |
| CrewAI | Low | Medium | Yes | Limited |
| AutoGen | Medium | Medium | Yes | Custom |
| PydanticAI | Low | High | Emerging | Custom |
| OpenAI SDK | Low | High | Handoffs | Tracing |
| Custom | High | You own it | You design | You build |

## Single vs Multi-Agent

Use **single** until eval proves need for specialization. Multi-agent adds coordination cost.

## Navigation

- [Introduction](introduction-to-agent-engineering.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
