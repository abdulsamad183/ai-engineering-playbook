---
title: "Production RAG"
description: "Production RAG operations — caching, incremental indexing, reindexing, monitoring, multi-tenant, permissions, security."
domain: rag
tags: [rag, production, monitoring, scaling]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - rag-evaluation.md
  - metadata-engineering.md
  - ../context-engineering/context-caching.md
keywords: [production RAG, incremental indexing, multi-tenant]
author: hp
---

# Production RAG

## Overview

Section **19**.

## Operations Checklist

| Area | Practice |
|------|----------|
| **Caching** | Query embed, retrieval results, prompt prefix |
| **Incremental index** | Upsert changed docs only |
| **Reindexing** | Blue/green collections on model change |
| **Freshness** | CDC webhooks from CMS |
| **Monitoring** | recall proxy, latency, empty retrieval % |
| **Retries** | Idempotent upsert; DLQ for ingest failures |
| **Scaling** | Stateless API + sharded vector DB |
| **Multi-tenant** | Filter + optional separate collections |
| **Permissions** | ACL metadata enforced every query |
| **Security** | Encrypt at rest, audit logs |

```mermaid
flowchart TB
    subgraph Deploy
        BLUE[Index v7 - live]
        GREEN[Index v8 - building]
    end
    GREEN -->|eval pass| CUTOVER[Cutover]
    CUTOVER --> BLUE
```

## Navigation

- [RAG System Design](rag-system-design.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
