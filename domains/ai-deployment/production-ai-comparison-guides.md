---
title: "Production AI Comparison Guides"
description: "Deployment, monitoring, observability, caching, retry, logging comparisons."
domain: ai-deployment
tags: [production-ai, comparison, phase-12]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - production-ai-overview.md
keywords: [deployment comparison, observability tools]
author: hp
---

# Production AI Comparison Guides

## Deployment Strategies

| Strategy | Downtime | Rollback speed |
|----------|----------|----------------|
| Rolling | Minimal | Redeploy prev |
| Blue/Green | Switch instant | Flip traffic |
| Canary | None | Stop ramp |

## Observability Tools

| Tool | Best for |
|------|----------|
| OpenTelemetry | Vendor-neutral traces |
| LangFuse | LLM cost + prompts |
| Phoenix | RAG retrieval debug |

## Caching Strategies

| Layer | Hit rate potential | Staleness risk |
|-------|-------------------|----------------|
| Response | High | High |
| Retrieval | Medium | Medium |
| Embedding | High | Low |

## Retry Strategies

| Idempotent read | Write/mutate |
|-----------------|--------------|
| Aggressive retry | No retry or careful |

## Container Deployment

| Docker Compose | Kubernetes |
|----------------|------------|
| Dev/staging | Production scale |

## Navigation

- [Production Overview](production-ai-overview.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 12 comparisons |
