---
title: "Production Readiness Checklist"
description: "Comprehensive checklist — deploy, monitor, security, eval, DR, compliance."
domain: ai-deployment
tags: [production, checklist, readiness]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - production-ai-overview.md
  - ../../cheat-sheets/production-readiness-checklist.md
keywords: [production readiness, go-live checklist]
author: hp
---

# Production Readiness Checklist

## Overview

Section **15**.

## Deployment

- [ ] Docker image scanned
- [ ] Health + readiness probes
- [ ] Canary/rollback tested
- [ ] Secrets from vault

## Monitoring & Observability

- [ ] Dashboards: latency, errors, cost, quality
- [ ] Alerts with runbooks
- [ ] Distributed tracing enabled
- [ ] SLO defined

## Security

- [ ] Auth on all endpoints
- [ ] Rate limits configured
- [ ] Tenant isolation verified
- [ ] PII handling documented

## Evaluation

- [ ] Golden set in CI
- [ ] Online eval sampling
- [ ] Regression owners assigned

## Scaling & DR

- [ ] Load test at 2× expected peak
- [ ] DB backups + restore tested
- [ ] Multi-AZ or failover plan

## Compliance & Logging

- [ ] Audit log for sensitive actions
- [ ] Data retention policy
- [ ] Structured logs with correlation IDs

## Navigation

- [Hub](README.md) · [Cheat Sheet](../../cheat-sheets/production-readiness-checklist.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
