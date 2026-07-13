---
title: "Paper Comparison Matrix Cheat Sheet"
description: "Quick side-by-side decisions — ReAct vs Reflexion, GraphRAG vs RAPTOR, DSPy vs PE, and more."
domain: papers
tags: [cheat-sheet, comparison, papers, phase-papers]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../domains/papers/research-comparison-guides.md
keywords: [comparison, ReAct, GraphRAG, DSPy, SWE-Agent]
author: hp
---

# Paper Comparison Matrix Cheat Sheet

> See [Research Comparison Guides](../domains/papers/research-comparison-guides.md).

## Agent Reasoning

| vs | Winner When | Loser When |
|----|------------|------------|
| ReAct > ToT | Production, tool use, latency matters | Need multi-path search |
| Reflexion > ReAct | Have evaluator, quality > speed | No pass/fail criteria |
| ReAct > Reflexion | General tasks, no evaluator | Code with test suite |

## Retrieval

| vs | Winner When | Loser When |
|----|------------|------------|
| CRAG > Self-RAG | Quick production win | Need per-claim verification |
| GraphRAG > RAPTOR | Many docs, global questions | Few long single docs |
| RAPTOR > GraphRAG | Long narratives, hierarchical | Cross-document entities |
| CRAG > naive RAG | Always (add evaluator) | — |

## Prompting & Tools

| vs | Winner When | Loser When |
|----|------------|------------|
| DSPy > manual PE | Have labeled data, multi-step | Single prompt, no data |
| ACI > raw shell | Code editing agents | Non-code tasks |
| CAMEL > single agent | Task needs role decomposition | Simple single-step task |
| CrewAI > raw CAMEL | Production multi-agent | Research / synthetic data |

## Master Decision Table

| I need to... | Use | Not |
|-------------|-----|-----|
| Tool agent | ReAct | ToT |
| Better code gen | ReAct + Reflexion | ToT |
| Fix bad retrieval | CRAG | GraphRAG (first) |
| Cross-doc themes | GraphRAG | Flat RAG |
| Long doc Q&A | RAPTOR | Standard chunks |
| Optimize prompts | DSPy | Manual iteration |
| Coding agent | ACI | Raw shell |
| Multi-agent pipeline | CrewAI/LangGraph | Raw CAMEL |

## ROI Ranking

1. CRAG evaluator (low cost, high impact)
2. ReAct agent loop (low cost, high impact)
3. Hybrid + rerank (medium cost, high impact)
4. Reflexion for code (medium cost, high for code)
5. DSPy optimization (high setup, medium-high impact)
6. GraphRAG (very high cost, situational)

## Useful Links

- [Research Comparison Guides](../domains/papers/research-comparison-guides.md)
- [Engineering Takeaways](../domains/papers/engineering-takeaways.md)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial cheat sheet |
