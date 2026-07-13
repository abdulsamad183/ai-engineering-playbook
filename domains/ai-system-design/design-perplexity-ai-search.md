---
title: "Design: Perplexity-style AI Search"
description: "AI search — web retrieval, citations, multi-query, answer synthesis, freshness."
domain: ai-system-design
tags: [system-design, perplexity, search, citations, phase-11]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - design-ai-search-engine.md
  - ../rag/retrieval-strategies.md
keywords: [Perplexity, AI search, citations, web retrieval]
author: hp
---

# Design: Perplexity-style AI Search

## Problem Statement

Answer open-web questions with cited sources, fresh data, and low hallucination.

## Functional Requirements

- Web search orchestration
- Inline citations `[1][2]`
- Follow-up questions with context
- Pro search (deeper multi-step)

## Architecture

```mermaid
flowchart LR
    Q[Query] --> QU[Query understanding]
    QU --> MQ[Multi-query expansion]
    MQ --> WEB[Web retrieval]
    WEB --> RANK[Source ranking]
    RANK --> SYN[Answer synthesis]
    SYN --> OUT[Cited answer]
```

## Components

- **Search orchestration** — parallel API calls (Bing, Brave, custom crawler)
- **Source ranking** — relevance, authority, freshness, dedup
- **Citation generation** — map claims → source spans
- **Freshness** — TTL on cache; bypass for news queries

## Multi-Query Retrieval

Decompose "Compare X vs Y 2026" → sub-queries → merge results.

## Tradeoffs

| Crawl own | Search API |
|-----------|------------|
| Control | Legal/ops burden | Fast to ship |

## Failure Handling

- No results → say unknown; suggest refine
- Source conflict → present both views

## Interview Questions

- How verify citations? → Post-hoc entailment check on source text

## Navigation

- [Deep Research System](design-deep-research-system.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 11 Section 6 |
