---
title: "AI System Design Interviews"
description: "Whiteboard questions, senior scenarios, tradeoffs, capacity exercises."
domain: ai-system-design
tags: [system-design, interview, whiteboard]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ai-system-design-fundamentals.md
  - ../interview-preparation/README.md
keywords: [AI interview, system design interview, capacity estimation]
author: hp
---

# AI System Design Interviews

## Overview

Section **17** — interview preparation hub.

## Whiteboard Framework

1. **Clarify** requirements (5 min)
2. **Estimate** scale (5 min)
3. **High-level diagram** (10 min)
4. **Deep dive** 2–3 components (15 min)
5. **Bottlenecks, tradeoffs, monitoring** (10 min)

## Senior Scenarios

| Prompt | Key topics |
|--------|------------|
| Design ChatGPT | Streaming, memory, tools, scale |
| Design Perplexity | Web search, citations, freshness |
| Design Copilot | Latency, FIM, privacy |
| Design enterprise RAG | ACL, hybrid search, eval |
| Design coding agent | Index, MCP, sandbox |
| Design voice assistant | STT/TTS pipeline, interruptions |

## Tradeoff Discussions

- RAG vs fine-tuning vs long context
- Sync vs async agents
- Single vs multi-model
- Build vs buy vector DB

## Capacity Exercises

Given: 500K DAU, 10 messages/session, 2K tokens/msg average → tokens/day, QPS, storage for 30-day history.

## Follow-Up Questions

- How migrate models without regression?
- How handle provider outage?
- How measure quality in production?

## Coding Interview Ideas

- Implement rate limiter for LLM API
- Design conversation trim to token budget
- Parse tool call JSON from stream

## Navigation

- [Comparison Guides](ai-system-design-comparison-guides.md) · [All designs](README.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
