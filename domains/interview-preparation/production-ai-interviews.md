---
title: "Production AI Interviews"
description: "Production interview questions — Docker, CI/CD, observability, reliability, security."
domain: interview-preparation
tags: [interview, production, docker, observability, phase-13]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../ai-deployment/README.md
keywords: [production interview, OpenTelemetry, CI/CD eval gate]
author: hp
---

# Production AI Interviews

## Overview

Section **16**.

## FAQ

**Q: CI/CD for AI vs traditional software?**

> Add eval regression gate; pin prompt/model versions; canary on quality metrics not just errors.

**Q: What trace in LLM app?**

> Request ID → retrieval span → LLM span (model, tokens) → tool spans.

**Q: Circuit breaker on LLM provider?**

> Open after error threshold; failover or cached response; half-open retry.

**Q: Cost spike overnight?**

> Check traffic; loop agent; model change; cache invalidation; embed batch job.

## Scenario

Deploy caused faithfulness drop — steps?

> Rollback; diff prompt/index version; run golden eval; trace sample failures.

## Further Reading

- [Production AI](../ai-deployment/README.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Section 16 |
