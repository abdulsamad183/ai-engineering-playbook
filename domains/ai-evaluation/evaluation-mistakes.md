---
title: "AI Evaluation Mistakes"
description: "Troubleshooting — weak datasets, metric misuse, stale evals, missing regression, business metrics."
domain: ai-evaluation
tags: [ai-evaluation, mistakes, troubleshooting, phase-10]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - introduction-to-ai-evaluation.md
  - continuous-evaluation.md
keywords: [eval mistakes, troubleshooting]
author: hp
---

# AI Evaluation Mistakes

## Overview

Section **19** of Phase 10.

## Issue Catalog

### Evaluating Only Accuracy

| | |
|---|---|
| **Symptoms** | High accuracy, users complain |
| **Root cause** | Wrong metric for generative task |
| **Fix** | Add faithfulness, latency, cost |
| **Prevention** | Metric selection checklist |

### Ignoring Latency

| | |
|---|---|
| **Symptoms** | Timeouts in prod despite good quality |
| **Root cause** | Eval harness not measuring P95 |
| **Fix** | Add latency budgets to CI |
| **Prevention** | [Latency Evaluation](latency-evaluation.md) |

### Weak Datasets

| | |
|---|---|
| **Symptoms** | Regressions slip to prod |
| **Root cause** | 20 trivial golden cases |
| **Fix** | Mine failures; expand slices |
| **Prevention** | Monthly dataset review |

### Metric Misuse

| | |
|---|---|
| **Symptoms** | BLEU high, answers wrong |
| **Root cause** | N-gram metrics on open QA |
| **Fix** | LLM-judge + human spot check |

### Stale Evaluation Datasets

| | |
|---|---|
| **Symptoms** | New product features untested |
| **Fix** | Continuous mining from support tickets |

### Missing Regression Tests

| | |
|---|---|
| **Symptoms** | Same bug recurs |
| **Fix** | Add case per incident; CI gate |

### Ignoring Business Metrics

| | |
|---|---|
| **Symptoms** | Engineering metrics up, revenue flat |
| **Fix** | Tie eval to task success + conversion proxies |

## Navigation

- [Case Studies](evaluation-case-studies.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 10 Section 19 |
