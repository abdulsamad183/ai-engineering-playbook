---
title: "OpenAI Agents SDK"
description: "OpenAI Agents SDK — agents, handoffs, guardrails, tracing."
domain: ai-agents
tags: [ai-agents, OpenAI, Agents SDK, framework]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../llm-engineering/providers/openai.md
  - tool-use.md
keywords: [OpenAI Agents SDK, handoffs, guardrails]
author: hp
---

# OpenAI Agents SDK

## Overview

**OpenAI Agents SDK** provides first-party patterns for **multi-agent handoffs**, tool use, and tracing on OpenAI models.

| Aspect | Detail |
|--------|--------|
| **Strengths** | Native OpenAI integration, handoffs, built-in tracing |
| **Weaknesses** | Vendor coupling |
| **Best for** | OpenAI-first products, rapid agent MVP |

## Python Example

```python
from agents import Agent, Runner

support = Agent(name="Support", instructions="Help users.", tools=[...])
result = Runner.run_sync(support, "Reset my password flow")
```

## Navigation

- [Build Your Own Framework](../build-your-own-agent-framework.md)
