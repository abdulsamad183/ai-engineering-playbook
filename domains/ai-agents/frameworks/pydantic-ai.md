---
title: "PydanticAI for Agents"
description: "PydanticAI — type-safe agents, structured outputs, dependency injection."
domain: ai-agents
tags: [ai-agents, PydanticAI, framework, phase-8]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - tool-use.md
  - ../llm-engineering/structured-outputs.md
keywords: [PydanticAI, type-safe agents, structured output]
author: hp
---

# PydanticAI for Agents

## Overview

**PydanticAI** builds agents with **Pydantic models** for tools, deps, and results — strong typing for production Python.

| Aspect | Detail |
|--------|--------|
| **Strengths** | Type safety, validation, clean Python API |
| **Weaknesses** | Newer ecosystem vs LangGraph |
| **Production** | Excellent for typed microservice agents |
| **Best for** | FastAPI shops wanting validated agent I/O |

## Python Example

```python
from pydantic_ai import Agent

agent = Agent("openai:gpt-4o", system_prompt="You are a helpful assistant.")

@agent.tool
def lookup_policy(query: str) -> str:
    return "Refund in 3 days"

result = agent.run_sync("What is refund policy?")
```

## Navigation

- [OpenAI Agents SDK](openai-agents-sdk.md)
