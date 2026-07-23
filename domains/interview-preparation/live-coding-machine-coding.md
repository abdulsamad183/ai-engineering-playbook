---
title: "Live Coding & Machine Coding Interviews"
description: "Practical exercises — FastAPI, SQL, RAG, agents, streaming, auth, workers."
domain: interview-preparation
tags: [interview, live-coding, machine-coding]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - fastapi-interviews.md
  - rag-interviews.md
keywords: [live coding, machine coding, coding interview]
author: hp
---

# Live Coding & Machine Coding Interviews

## Overview

Section **18**.

## Exercise Catalog

| Exercise | Time | Solution outline |
|----------|------|------------------|
| **FastAPI health + CRUD** | 45m | App, Pydantic, in-memory or SQLite |
| **SQL analytics** | 30m | JOIN + GROUP BY + window |
| **Mini RAG** | 60m | Embed function mock → cosine top-k → prompt template |
| **Tool agent loop** | 60m | while steps < N: parse tool call → execute mock |
| **SSE streaming** | 45m | `StreamingResponse` generator |
| **Redis cache decorator** | 30m | hash key, get/set with TTL |
| **JWT auth dependency** | 45m | `Depends` verify token |
| **Background embed job** | 60m | queue list + worker stub |

## Live Coding Tips

- Clarify inputs/outputs first
- Happy path → tests → edge cases
- Stub LLM with fixed string — explain where real call goes

## Machine Coding Tips

- Prioritize working API over perfect abstractions
- README with run instructions scores points

## Evaluation Criteria (what interviewers score)

| Criteria | Weight |
|----------|--------|
| Correctness | High |
| Code clarity | High |
| Error handling | Medium |
| Tests | Medium |
| Production awareness | Senior+ |

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Section 18 |
