---
title: "AI Research Timeline Cheat Sheet"
description: "Quick reference for AI research evolution — transformers to agents to MCP."
domain: papers
tags: [cheat-sheet, timeline, evolution]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../domains/papers/research-evolution.md
keywords: [timeline, transformers, RAG, agents, MCP]
author: hp
---

# AI Research Timeline Cheat Sheet

> See [Research Evolution](../domains/papers/research-evolution.md).

## Era Summary

| Era | Years | Key Papers | Engineering Unlock |
|-----|-------|-----------|-------------------|
| Transformers | 2017-19 | Attention, BERT, GPT-2 | LLM APIs, embeddings |
| Scale + Prompting | 2020-21 | GPT-3, FLAN, Codex | Prompt engineering |
| Alignment + Reasoning | 2022 | RLHF, CoT, ReAct | Chat models, tool use |
| RAG + Agents | 2023 | RAG, ToT, Reflexion, CAMEL | Vector DBs, agent frameworks |
| Advanced Patterns | 2024 | Self-RAG, GraphRAG, SWE-Agent, DSPy | Advanced RAG, coding agents |
| Protocols | 2025 | MCP, A2A | Standardized tool servers |
| Future | 2026+ | Eval-driven, compound systems | Reliable production AI |

## Key Milestones

| Year | Paper/System | One-Line Impact |
|------|-------------|-----------------|
| 2017 | Attention Is All You Need | Parallel attention architecture |
| 2020 | GPT-3 | Few-shot in-context learning |
| 2022 | InstructGPT / RLHF | Aligned chat models |
| 2022 | Chain-of-Thought | Step-by-step reasoning |
| 2022 | ReAct | Tool-using agent loop |
| 2023 | Reflexion | Learn from failure via memory |
| 2023 | CAMEL | Multi-agent role play |
| 2024 | CRAG / Self-RAG | Retrieval quality gates |
| 2024 | GraphRAG | Knowledge graph retrieval |
| 2024 | SWE-Agent | Agent-Computer Interface |
| 2024 | DSPy | Programmatic prompt optimization |
| 2025 | MCP | Standardized tool protocol |

## Layer Stack

```
Future:     Compound systems + eval-driven dev
Protocols:  MCP tool servers
Advanced:   GraphRAG, SWE-Agent, DSPy
RAG+Agents: Vector DB + ReAct loop
Reasoning:  CoT + function calling
Prompting:  Few-shot + instructions
Foundation: Transformer APIs
```

## Interview Quick Answers

| Question | Answer |
|----------|--------|
| Why RAG after ChatGPT? | Hallucination + knowledge cutoffs |
| Why agents after RAG? | Autonomous multi-step actions |
| Why MCP? | Fragmented tool interfaces |
| What's next? | Reliable eval + compound systems |
| Highest ROI pattern? | CRAG evaluator + ReAct loop |

## Useful Links

- [Research Evolution](../domains/papers/research-evolution.md)
- [Future Research](../domains/papers/future-research.md)
- [Papers Domain](../domains/papers/README.md)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial cheat sheet |
