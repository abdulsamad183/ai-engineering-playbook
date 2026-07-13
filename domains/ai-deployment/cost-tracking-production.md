---
title: "Production Cost Tracking"
description: "Token, embedding, agent, infrastructure costs — dashboards and optimization."
domain: ai-deployment
tags: [cost, production, finops, phase-12]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../ai-evaluation/cost-evaluation.md
  - ../../examples/production-ai/example-cost-tracking.py
keywords: [cost tracking, token cost, FinOps]
author: hp
---

# Production Cost Tracking

## Overview

Section **9** of Phase 12.

## Cost Dimensions

- LLM input/output tokens per request
- Embedding batch jobs
- Vector DB storage + QPS tier
- Agent multi-step multiply
- GPU/CPU container hours

## Dashboards

- Cost per feature flag / model
- Cost per successful task
- Anomaly detection (2σ spike)

## Optimization Levers

- Model routing (small vs large)
- Cache prompts and embeddings
- Batch embed jobs off-peak

## Navigation

- [Reliability](reliability-for-ai.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 12 Section 9 |
