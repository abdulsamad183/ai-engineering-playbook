---
title: "AI Operations"
description: "Incident response, debugging, RCA, runbooks, postmortems, playbooks."
domain: ai-deployment
tags: [aiops, incident, runbook, postmortem]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../production-incidents/README.md
  - monitoring-ai-systems.md
keywords: [incident response, runbook, root cause analysis]
author: hp
---

# AI Operations

## Overview

Section **14**.

## Incident Response

1. Detect (alert on SLO breach)
2. Triage (quality vs latency vs cost)
3. Mitigate (rollback, flag off, scale)
4. RCA (traces, recent deploys)
5. Postmortem + golden case

## Production Debugging

- Trace ID → spans → slow retrieval?
- Compare eval scores pre/post deploy
- Sample bad outputs

## Runbook Template

| Symptom | Check | Action |
|---------|-------|--------|
| High latency | LLM provider status | Failover |
| Quality drop | Prompt version | Rollback flag |
| Cost spike | Traffic / model change | Rate limit |

## Navigation

- [Production Readiness](production-readiness-checklist.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
