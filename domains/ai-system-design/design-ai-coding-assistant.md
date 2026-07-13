---
title: "Design: AI Coding Assistant"
description: "Code assistant architecture — AST, code graph, refactoring, PR generation, code review."
domain: ai-system-design
tags: [system-design, coding-assistant, ast, refactoring, phase-11]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - design-cursor-like-system.md
  - design-github-copilot.md
keywords: [code graph, refactoring, pull request]
author: hp
---

# Design: AI Coding Assistant

## Problem Statement

General-purpose coding assistant beyond inline complete — refactor, review, generate PRs across repos.

## Architecture

```mermaid
flowchart TB
    REPO[Repository] --> AST[AST parser]
    AST --> GRAPH[Code graph]
    GRAPH --> IDX[Semantic index]
    USER[Developer] --> AGENT[Coding agent]
    AGENT --> IDX
    AGENT --> TOOLS[git, test, lint]
    AGENT --> PR[PR generator]
```

## Capabilities

| Feature | Approach |
|---------|----------|
| **AST parsing** | tree-sitter per language |
| **Code graph** | defs, refs, call graph |
| **Semantic search** | embed functions/classes |
| **Refactoring** | symbol-aware edits |
| **Multi-file** | graph neighborhood retrieval |
| **Code review** | diff + policy rules + LLM |
| **PR generation** | branch, commits, description template |

## Evaluation

- Unit test pass rate on generated code
- Human accept rate on diffs

## Navigation

- [AI PDF Chat](design-ai-pdf-chat.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 11 Section 10 |
