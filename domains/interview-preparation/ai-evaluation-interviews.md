---
title: "AI Evaluation Interviews"
description: "Evaluation interviews — metrics, RAGAS, hallucination, A/B testing, latency, cost."
domain: interview-preparation
tags: [interview, evaluation, ragas, metrics]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../ai-evaluation/README.md
keywords: [evaluation interview, faithfulness, RAGAS, A/B test]
author: hp
---

# AI Evaluation Interviews

## Overview

Section **14**.

## FAQ

**Q: Offline vs online evaluation?**

> Offline: golden set pre-deploy. Online: sampled production — real distribution, drift.

**Q: Faithfulness vs correctness?**

> Faithfulness: supported by context. Correctness: true in world — need external knowledge.

**Q: RAGAS metrics explain.**

> Context precision/recall, faithfulness, answer relevancy — LLM-judge assisted.

**Q: When A/B test prompts?**

> Canary traffic; define primary metric; sufficient sample size.

**Scenario:** Quality dropped after deploy — diagnose?

> Compare eval scores; check prompt/model version; retrieval index age; latency timeouts causing truncations.

## Further Reading

- [AI Evaluation](../ai-evaluation/README.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Section 14 |
