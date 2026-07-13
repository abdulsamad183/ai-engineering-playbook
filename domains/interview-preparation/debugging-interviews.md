---
title: "Debugging Interviews for AI Engineers"
description: "Debug scenarios — slow APIs, hallucinations, retrieval, agents, Docker, streaming."
domain: interview-preparation
tags: [interview, debugging, troubleshooting, phase-13]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../ai-evaluation/evaluation-mistakes.md
  - production-ai-interviews.md
keywords: [debugging interview, production failure, root cause]
author: hp
---

# Debugging Interviews for AI Engineers

## Overview

Section **19**.

## Scenario Playbook

### Slow API (p95 8s → SLO 3s)

| Step | Action |
|------|--------|
| Symptoms | Traces show LLM 6s |
| Diagnosis | Compare retrieval vs generation time |
| Fix | Cache retrieval; smaller model; parallel embed+classify |
| Prevention | Latency budgets in CI |

### Hallucinations after deploy

| Step | Action |
|------|--------|
| Symptoms | Faithfulness metric −15% |
| Diagnosis | Prompt version? Index stale? |
| Fix | Rollback prompt; re-index |
| Prevention | Eval gate on PR |

### Poor retrieval

| Step | Action |
|------|--------|
| Symptoms | Right answer in corpus, wrong chunks |
| Diagnosis | Chunk size, embed model mismatch |
| Fix | Tune chunk overlap; hybrid BM25 |

### Broken agent loop

| Step | Action |
|------|--------|
| Symptoms | Repeats same tool |
| Diagnosis | Log trajectories; max steps? |
| Fix | Duplicate detection; better stop condition |

### Docker works locally, fails prod

| Step | Action |
|------|--------|
| Diagnosis | Env vars, network DNS, `0.0.0.0` bind |
| Fix | Readiness probe dependencies |

### Streaming stalls

| Step | Action |
|------|--------|
| Diagnosis | Proxy buffering SSE; blocking sync code |
| Fix | Disable buffer header; async generator |

## Interview Method

State **hypothesis → experiment → fix → prevent** aloud.

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Section 19 |
