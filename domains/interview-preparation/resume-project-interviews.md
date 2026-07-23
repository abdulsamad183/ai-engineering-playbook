---
title: "Resume & Project Interviews"
description: "Discuss projects — architecture, tradeoffs, failures, scaling, evaluator follow-ups."
domain: interview-preparation
tags: [interview, resume, portfolio, behavioral]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - behavioral-leadership-interviews.md
  - interview-strategy.md
keywords: [resume interview, project deep dive, portfolio]
author: hp
---

# Resume & Project Interviews

## Overview

Section **17**.

## Project Story Structure (5 min)

1. **Context** — business problem, users
2. **Your role** — what you owned
3. **Architecture** — diagram in words
4. **Tradeoffs** — what you chose vs alternatives
5. **Impact** — metrics (latency, quality, cost, revenue)
6. **Failures** — what broke; what you learned

## Interviewer Follow-Ups

| They ask | You demonstrate |
|----------|-----------------|
| "Why RAG not fine-tune?" | Data freshness, cost, iteration speed |
| "Hardest bug?" | Concrete debug story with traces |
| "What would you redo?" | Honest architectural improvement |
| "How measure success?" | Eval metrics + business KPI |
| "Team conflict?" | Link to behavioral section |

## Resume Tips for AI Roles

- Quantify: QPS, dataset size, faithfulness score, cost reduction
- Name stack: FastAPI, pgvector, LangGraph, RAGAS
- One **system design** bullet per major project

## Red Flags to Avoid

- "We used AI" without your contribution
- No evaluation methodology
- Can't explain data pipeline

## Exercise

Write one-page architecture for your best project using playbook section headings.

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Section 17 |
