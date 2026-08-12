---
title: "AI System Design Comparison Guides"
description: "Decision matrices for architecture patterns, RAG vs fine-tuning, deployment topology."
domain: ai-system-design
tags: [system-design, comparison, decision-matrix]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ai-architecture-patterns.md
keywords: [system design comparison, build vs buy]
author: hp
---

# AI System Design Comparison Guides

## RAG vs Fine-Tuning vs Long Context

| Approach | Best when | Cost |
|----------|-----------|------|
| **RAG** | Dynamic knowledge | Infra + retrieval |
| **Fine-tuning** | Style/format stable | Training + redeploy |
| **Long context** | Few large docs | Per-request tokens |

## Monolith vs Microservices (AI)

| Monolith | Microservices |
|----------|---------------|
| Faster MVP | Independent scale |
| Single deploy | Team autonomy |

## Streaming Protocols

| SSE | WebSocket |
|-----|-----------|
| One-way stream | Bidirectional |
| Simpler | Voice, collaborative |

## Storage for Conversations

| Postgres | NoSQL |
|----------|-------|
| ACID, joins | Flexible schema at huge scale |

## Navigation

- [Fundamentals](ai-system-design-fundamentals.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
