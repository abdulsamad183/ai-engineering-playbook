---
title: "OpenAI Evals"
description: "OpenAI Evals overview — eval registry, templates, strengths and limitations."
domain: ai-evaluation
tags: [ai-evaluation, openai, evals, framework, phase-10]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../evaluation-frameworks.md
  - ../benchmarking.md
keywords: [OpenAI Evals, eval registry]
author: hp
---

# OpenAI Evals

## Overview

**OpenAI Evals** is a framework for evaluating OpenAI models with composable eval templates.

## Strengths

- Registry of community evals
- Model-graded and deterministic checks
- Good for comparing OpenAI model versions

## Limitations

- OpenAI API centric
- Less RAG/agent-specific than RAGAS/DeepEval
- Self-hosted registry maintenance

## Ideal Use Cases

- Model upgrade regression (GPT-4 → GPT-4.1)
- Instruction-following suites
- Custom completion evals

## Python Pattern

```python
# Conceptual: eval template + completion fn + graders
def grade_exact_match(sample, output) -> bool:
    return output.strip() == sample["ideal"].strip()
```

## Navigation

- [Benchmarking](../benchmarking.md) · [Evaluation Frameworks](../evaluation-frameworks.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | OpenAI Evals overview |
