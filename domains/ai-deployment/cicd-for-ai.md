---
title: "CI/CD for AI Applications"
description: "GitHub Actions, build/test/deploy pipelines, eval gates, rollback."
domain: ai-deployment
tags: [cicd, github-actions, regression]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../ai-evaluation/continuous-evaluation.md
  - ../../examples/production-ai/.github-workflows-ci.yml
keywords: [CI/CD, GitHub Actions, eval gate]
author: hp
---

# CI/CD for AI Applications

## Overview

Section **4**.

```mermaid
flowchart LR
    PR[Pull Request] --> TEST[Unit tests]
    TEST --> EVAL[AI eval suite]
    EVAL --> BUILD[Docker build]
    BUILD --> DEPLOY[Deploy staging]
    DEPLOY --> SMOKE[Smoke + eval]
```

## Pipeline Stages

1. **Lint + unit tests**
2. **AI regression eval** — golden set; fail if metrics drop
3. **Build & push image**
4. **Deploy staging**
5. **Integration eval**
6. **Manual/auto promote prod**

## GitHub Actions Pattern

See [`.github-workflows-ci.yml`](../../examples/production-ai/.github-workflows-ci.yml) example.

## Rollback

- Keep previous image tag
- Revert prompt flag instantly
- Re-run eval on rollback build

## Navigation

- [Secrets Management](secrets-management-for-ai.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
