---
title: "SQL Interviews for AI Engineers"
description: "SQL interview guide — joins, window functions, CTEs, indexes, transactions, optimization."
domain: interview-preparation
tags: [interview, sql, database]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - postgresql-interviews.md
  - ../databases/sql/README.md
keywords: [SQL interview, joins, window functions, query optimization]
author: hp
---

# SQL Interviews for AI Engineers

## Overview

Section **4**. AI apps store conversations, users, eval results, and metadata in **relational DBs**.

## Core Concepts

| Topic | AI use case |
|-------|-------------|
| **Joins** | Users ↔ conversations ↔ messages |
| **Aggregations** | Daily token usage per tenant |
| **Window functions** | Rank retrieval hits per query |
| **CTEs** | Readable analytics pipelines |
| **Indexes** | `user_id`, `created_at` on messages |
| **Transactions** | Atomic conversation + message insert |
| **Isolation** | Read committed default; know anomalies |

## FAQ

**Q: Write query — top 3 users by message count last 7 days.**

```sql
SELECT user_id, COUNT(*) AS msg_count
FROM messages
WHERE created_at >= NOW() - INTERVAL '7 days'
GROUP BY user_id
ORDER BY msg_count DESC
LIMIT 3;
```

**Follow-up:** Add rolling 7-day average per user?

> Window: `AVG(COUNT(*)) OVER (PARTITION BY user_id ORDER BY date ROWS 6 PRECEDING)`

**Q: Why index `(tenant_id, created_at)` for chat logs?**

> Queries filter by tenant then time range — composite index supports both.

## Coding Problems

| Problem | Skill |
|---------|-------|
| Second highest salary (classic) | subquery / window |
| Deduplicate embeddings metadata | `DISTINCT ON` / group by |
| Find users with no conversations | `LEFT JOIN ... WHERE NULL` |

## Trick Question

**Q: `COUNT(*)` vs `COUNT(column)`?**

> `COUNT(*)` counts rows; `COUNT(col)` ignores NULLs in col.

## Further Reading

- [PostgreSQL Interviews](postgresql-interviews.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Section 4 |
