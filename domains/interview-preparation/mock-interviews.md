---
title: "Mock AI Engineering Interviews"
description: "Complete mock interview sets — Junior, Mid, Senior, Staff with agendas and rubrics."
domain: interview-preparation
tags: [interview, mock, practice]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - interview-strategy.md
  - system-design-interview-guide.md
keywords: [mock interview, junior AI engineer, staff interview]
author: hp
---

# Mock AI Engineering Interviews

## Overview

Four complete mock sets with **agenda**, **questions**, **follow-ups**, **expected answers**, and **evaluation criteria**.

---

## Junior AI Engineer (90 min)

### Agenda

| Block | Time | Type |
|-------|------|------|
| Python basics | 20m | Coding |
| LLM fundamentals | 15m | Conceptual |
| Mini RAG explain | 15m | Architecture |
| Behavioral | 10m | STAR |
| Q&A | 10m | — |

### Questions

1. **Python:** Reverse words in string. Follow-up: handle unicode?
2. **LLM:** What is a token? How reduce cost?
3. **RAG:** Draw ingest → query flow. What is embedding?
4. **Behavioral:** Tell me about a project you built.

### Evaluation Rubric

| Pass | Needs work |
|------|------------|
| Working code with edge cases | Syntax errors |
| Clear token definition | Vague "AI magic" |
| Names 4+ RAG steps | Skips retrieval |

---

## Mid-Level AI Engineer (2 hr)

### Agenda

| Block | Time |
|-------|------|
| FastAPI live coding | 45m |
| SQL + data modeling | 20m |
| RAG deep dive | 30m |
| Debugging scenario | 15m |
| Behavioral | 10m |

### Questions

1. Build POST `/chat` with Pydantic validation.
2. SQL: messages per user last 30 days.
3. Hybrid search — why both BM25 and vector?
4. **Debug:** Faithfulness dropped after index update.
5. **Follow-up:** How evaluate prompt change?

### Expected answer (debug)

> Compare embed model version; rerun golden set; check chunk boundaries.

### Rubric

- Ships working endpoint
- Explains hybrid retrieval tradeoff
- Structured debug approach

---

## Senior AI Engineer (2.5 hr)

### Agenda

| Block | Time |
|-------|------|
| System design: Support chatbot | 45m |
| Agent + tools architecture | 30m |
| Production + eval | 20m |
| Code review discussion | 15m |
| Behavioral / leadership | 20m |

### System Design Prompt

Design AI support for 50K tickets/day with KB RAG and CRM tools.

**Expected:** API, vector index, ACL, escalation queue, eval faithfulness, rate limits.

### Follow-ups

- Multi-tenant isolation?
- Cost per ticket estimate?

### Rubric

- Capacity estimate attempted
- Names monitoring + rollback
- Tool permission model

---

## Staff AI Engineer (3 hr)

### Agenda

| Block | Time |
|-------|------|
| Platform architecture | 60m |
| Cross-team tradeoffs | 30m |
| Org-level eval strategy | 30m |
| Behavioral / vision | 30m |

### Prompt

Design internal AI platform for 20 product teams — shared retrieval, model routing, governance.

**Expected:** Multi-tenant platform, golden eval CI, cost allocation, MCP or tool registry, SLOs.

### Rubric

- Platform not single product
- Governance + safety
- Clear migration path for teams

---

## How to Use Mocks

1. Partner plays interviewer with rubric only
2. Record yourself; review filler words
3. Grade honestly; redo weak sections

## Navigation

- [Interview Strategy](interview-strategy.md) · [Company Patterns](company-interview-patterns.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Mock interviews |
