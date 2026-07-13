---
title: "Design: Deep Research System"
description: "Multi-agent research — planning, crawling, citations, long-running tasks, reports."
domain: ai-system-design
tags: [system-design, research, multi-agent, citations, phase-11]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - design-perplexity-ai-search.md
  - ../ai-agents/multi-agent-systems.md
keywords: [deep research, report generation, citation graph]
author: hp
---

# Design: Deep Research System

## Problem Statement

Produce long-form researched reports with verifiable citations from web and docs — minutes to hours runtime.

## Architecture

```mermaid
flowchart TB
    GOAL[Research goal] --> PLAN[Planner agent]
    PLAN --> SEARCH[Search agents]
    PLAN --> READ[Reader agents]
    SEARCH & READ --> GRAPH[Citation graph]
    GRAPH --> WRITE[Writer agent]
    WRITE --> REPORT[Report + bibliography]
```

## Components

- **Research planning** — outline, sub-questions, stopping criteria
- **Web crawling** — rate-limited fetch, extract main content
- **Multi-agent** — parallel sub-topic researchers
- **Citation graph** — claim → source nodes; detect unsupported edges
- **Long-running tasks** — job queue; progress UI; email on complete
- **Memory** — scratchpad + structured notes per section
- **Evaluation** — faithfulness, coverage rubric

## Scaling

- Worker pool for fetch + embed
- Checkpoint each section

## Cost

- Cap searches per report; use smaller models for summarize steps

## Navigation

- [AI Search Engine](design-ai-search-engine.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 11 Section 7 |
