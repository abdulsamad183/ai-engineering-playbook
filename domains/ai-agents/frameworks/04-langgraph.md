---
title: "LangGraph for Agents"
description: "LangGraph — graph execution, checkpointing, state, production patterns."
domain: ai-agents
tags: [ai-agents, LangGraph, framework]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - task-graphs.md
  - agent-state-management.md
keywords: [LangGraph, state graph, checkpointing]
author: hp
---

# LangGraph for Agents

## Overview

**LangGraph** models agents as **state graphs** — nodes (functions), edges (transitions), conditional routing, built-in checkpointing.

| Aspect | Detail |
|--------|--------|
| **Execution** | Pregel-style supersteps |
| **Strengths** | Checkpointing, cycles, observability, LangChain ecosystem |
| **Weaknesses** | Learning curve; abstraction overhead |
| **Production** | Strong with LangSmith tracing |
| **Best for** | Complex workflows with loops and HITL |

## Python Example

```python
from langgraph.graph import StateGraph, END

def research_node(state): ...
def write_node(state): ...

graph = StateGraph(dict)
graph.add_node("research", research_node)
graph.add_node("write", write_node)
graph.add_edge("research", "write")
graph.add_edge("write", END)
app = graph.compile()
```

## Navigation

- [CrewAI](crewai.md) · [Build Your Own Framework](../build-your-own-agent-framework.md)
