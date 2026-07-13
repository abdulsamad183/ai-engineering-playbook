---
title: "Context Engineering Mistakes"
description: "Troubleshooting guide for context failures — overflow, irrelevant context, stale memory, duplication, ranking, compression, and personalization drift."
domain: context-engineering
tags: [context-engineering, mistakes, troubleshooting, anti-patterns, phase-6]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - introduction-to-context-engineering.md
  - context-quality.md
  - context-windows.md
  - ../common-mistakes/README.md
keywords: [context mistakes, troubleshooting, context overflow, stale memory]
author: hp
---

# Context Engineering Mistakes

> Troubleshooting guide for the most common production context failures — symptoms, root cause, diagnosis, fix, and prevention.

## Table of Contents

- [Overview](#overview)
- [Context Overflow](#context-overflow)
- [Irrelevant Context](#irrelevant-context)
- [Stale Memory](#stale-memory)
- [Duplicated Context](#duplicated-context)
- [Excessive History](#excessive-history)
- [Poor Ranking](#poor-ranking)
- [Weak Compression](#weak-compression)
- [Memory Drift](#memory-drift)
- [Inconsistent Personalization](#inconsistent-personalization)
- [Expensive Context Assembly](#expensive-context-assembly)
- [Interview Preparation](#interview-preparation)
- [Navigation](#navigation)

---

## Overview

Section **20** of Phase 6 — practical diagnostics when context systems fail in production.

---

## Context Overflow

| | |
|---|---|
| **Symptoms** | API errors, truncated system prompt, model "forgets" instructions |
| **Root cause** | No pre-flight token count; unbounded history or retrieval |
| **Diagnosis** | Log `token_count` per layer; check truncation flags |
| **Fix** | Enforce [Context Budgeting](context-budgeting.md); compress before call |
| **Prevention** | CI tests with max-fill fixtures |

---

## Irrelevant Context

| | |
|---|---|
| **Symptoms** | Confused answers, wrong topic, citation of unrelated docs |
| **Root cause** | Low retrieval threshold, bad embeddings, no reranking |
| **Diagnosis** | Inspect retrieved IDs and scores in trace |
| **Fix** | Raise min score, add reranker, query rewrite |
| **Prevention** | Offline recall@K eval; human context audits |

---

## Stale Memory

| | |
|---|---|
| **Symptoms** | Outdated preferences, wrong account status |
| **Root cause** | No TTL/decay; cache without invalidation |
| **Diagnosis** | Compare memory `updated_at` to source systems |
| **Fix** | Invalidate on profile update; decay low-confidence facts |
| **Prevention** | Event-driven cache bust; periodic reconciliation |

---

## Duplicated Context

| | |
|---|---|
| **Symptoms** | Token waste, repetitive answers, attention dilution |
| **Root cause** | Same doc in memory and retrieval; overlapping chunks |
| **Diagnosis** | Hash chunk contents in trace |
| **Fix** | Deduplicate in [Context Selection](context-selection.md) |
| **Prevention** | Cross-source dedup in assembly pipeline |

---

## Excessive History

| | |
|---|---|
| **Symptoms** | Slow, costly, old turns overshadow current question |
| **Root cause** | Full transcript sent every turn |
| **Diagnosis** | History token % of total > 40% |
| **Fix** | Prune + summarize; importance scoring |
| **Prevention** | Hard history budget in config |

---

## Poor Ranking

| | |
|---|---|
| **Symptoms** | Right doc retrieved but not in top slots used |
| **Root cause** | Wrong fusion weights; no recency decay |
| **Diagnosis** | Log full ranked list vs included set |
| **Fix** | Tune hybrid weights; add business boosts |
| **Prevention** | Labeled ranking eval set |

---

## Weak Compression

| | |
|---|---|
| **Symptoms** | Lost numbers, wrong summaries, hallucinated compression |
| **Root cause** | Aggressive abstractive summarize without validation |
| **Diagnosis** | Entity diff compressed vs source |
| **Fix** | Extractive first; validate entities; drop vs corrupt |
| **Prevention** | Faithfulness checks on compression output |

---

## Memory Drift

| | |
|---|---|
| **Symptoms** | Model "remembers" things user never said |
| **Root cause** | Unvalidated memory writes from model output |
| **Diagnosis** | Audit memory provenance |
| **Fix** | Write only explicit/validated facts; user memory UI |
| **Prevention** | Confidence thresholds; human confirm for high impact |

---

## Inconsistent Personalization

| | |
|---|---|
| **Symptoms** | Tone varies randomly; wrong tier policies |
| **Root cause** | Profile cache staleness; race conditions |
| **Diagnosis** | Compare profile version in trace vs DB |
| **Fix** | Short TTL + event invalidation; version stamp in context |
| **Prevention** | Integration tests per tier/locale |

---

## Expensive Context Assembly

| | |
|---|---|
| **Symptoms** | High p95 latency and cost before LLM call |
| **Root cause** | Serial fetches, no caching, compress every turn |
| **Diagnosis** | Break down assembly timings in trace |
| **Fix** | Parallel fetch, [Context Caching](context-caching.md), threshold compression |
| **Prevention** | SLO on assembly latency; cache hit rate dashboards |

---

## Interview Preparation

**Q: User says bot forgot earlier message — debug steps?**

> Check session persistence, history pruning rules, summary faithfulness, separate state vs transcript, trace what was actually sent.

---

## Navigation

### Prerequisites

- All Phase 6 sections; start with [Introduction](introduction-to-context-engineering.md)

### Related Topics

- [Context Quality](context-quality.md)
- [Common Mistakes](../common-mistakes/README.md)

### Future Reading

- [Context Comparison Guides](context-comparison-guides.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication — Phase 6 Section 20 |
