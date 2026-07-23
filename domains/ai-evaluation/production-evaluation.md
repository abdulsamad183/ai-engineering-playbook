---
title: "Production Evaluation"
description: "Eval at scale, multi-model, enterprise, observability, governance, auditability."
domain: ai-evaluation
tags: [ai-evaluation, production, enterprise, governance]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - continuous-evaluation.md
  - evaluation-dashboards.md
keywords: [production evaluation, governance, audit]
author: hp
---

# Production Evaluation

## Overview

Section **18**.

## At Scale

- Distributed eval workers
- Queue-based LLM-judge jobs
- Partition golden sets by domain

## Multi-Model / Multi-Agent

- Same dataset across models — comparison table
- Agent eval: trace replay in sandbox

## Enterprise Evaluation

- Per-tenant golden sets
- RBAC on eval data
- Compliance retention policies

## Observability Integration

- OpenTelemetry spans → eval scores
- Link `trace_id` to `eval_run_id`

## Version Tracking

Every run records: `prompt_hash`, `model_id`, `index_version`, `code_sha`

## Governance

- Approval for production prompt changes
- Audit log of human ratings

## Best Practices

- Tiered eval: smoke (1 min) → full (1 hr) → weekly deep

## Navigation

- [Evaluation Mistakes](evaluation-mistakes.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
