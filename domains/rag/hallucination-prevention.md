---
title: "Hallucination Prevention in RAG"
description: "Grounding, confidence, answer refusal, source validation, consistency checks, retrieval thresholds."
domain: rag
tags: [rag, hallucination, grounding, safety]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - citations-and-grounding.md
  - rag-evaluation.md
  - retrieval-strategies.md
keywords: [hallucination prevention, grounding, abstention]
author: hp
---

# Hallucination Prevention in RAG

## Overview

Section **16**.

## Failure Modes

| Cause | Mitigation |
|-------|------------|
| Retrieval miss | Lower threshold alert; expand query |
| Wrong chunk | Rerank; hybrid search |
| Model ignores context | Strong system prompt; lower temperature |
| Overconfident answer | Require citations; post-validate |

## Techniques

- **Retrieval threshold** — abstain if max score < τ
- **Answer refusal** — "Not found in knowledge base"
- **Source validation** — NLI model: claim entailed by chunk?
- **Consistency** — Sample twice; disagree → abstain
- **Citation check** — every claim maps to retrieved ID

## Navigation

- [RAG Evaluation](rag-evaluation.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
