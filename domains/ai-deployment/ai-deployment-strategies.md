---
title: "AI Deployment Strategies"
description: "Local, VM, cloud, container deployment — blue/green, canary, rolling."
domain: ai-deployment
tags: [deployment, canary, blue-green]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - cicd-for-ai.md
  - ../cloud-deployment/README.md
keywords: [canary deployment, rolling deploy, blue green]
author: hp
---

# AI Deployment Strategies

## Overview

Section **3**.

```mermaid
flowchart LR
    V1[v1 90%] --> LB[Load Balancer]
    V2[v2 10% canary] --> LB
```

## Strategies

| Strategy | Risk | Use |
|----------|------|-----|
| **Rolling** | Medium | Default K8s |
| **Blue/Green** | Low | Instant switchback |
| **Canary** | Lowest | AI prompt/model changes |

## AI-Specific Concerns

- Run eval on canary before ramp
- Compare latency/cost metrics v1 vs v2
- Feature flag prompt template

## Environments

| Env | Purpose |
|-----|---------|
| Local | Docker Compose |
| Staging | Prod-like + synthetic traffic |
| Prod | Real users |

## Navigation

- [CI/CD for AI](cicd-for-ai.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
