---
title: "CrewAI for Agents"
description: "CrewAI — role-based agents, tasks, crews, production considerations."
domain: ai-agents
tags: [ai-agents, CrewAI, framework, phase-8]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - multi-agent-systems.md
keywords: [CrewAI, crew, role-based agents]
author: hp
---

# CrewAI for Agents

## Overview

**CrewAI** organizes **crews** of role-defined agents with tasks and sequential/hierarchical process.

| Aspect | Detail |
|--------|--------|
| **Strengths** | Fast multi-agent prototyping, clear roles |
| **Weaknesses** | Less low-level control than LangGraph |
| **Production** | Good for demos → need custom observability for prod |
| **Best for** | Research/writing crews, marketing ops |

## Python Example

```python
from crewai import Agent, Task, Crew

researcher = Agent(role="Researcher", goal="Find facts", backstory="...")
writer = Agent(role="Writer", goal="Draft report", backstory="...")
task1 = Task(description="Research X", agent=researcher)
task2 = Task(description="Write report", agent=writer)
crew = Crew(agents=[researcher, writer], tasks=[task1, task2])
result = crew.kickoff()
```

## Navigation

- [LangGraph](langgraph.md)
