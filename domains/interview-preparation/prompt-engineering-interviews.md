---
title: "Prompt Engineering Interviews"
description: "Prompt interview questions — few-shot, chaining, ReAct, testing, evaluation, optimization."
domain: interview-preparation
tags: [interview, prompt-engineering, react, phase-13]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../prompt-engineering/README.md
  - context-engineering-interviews.md
keywords: [prompt interview, few-shot, ReAct, prompt evaluation]
author: hp
---

# Prompt Engineering Interviews

## Overview

Section **9**.

## FAQ

**Q: Zero-shot vs few-shot?**

> Zero-shot: instructions only. Few-shot: examples in prompt — improves format adherence; costs tokens.

**Q: What is ReAct?**

> Reason + Act interleaved — model thinks, calls tool, observes, repeats. See [Agent interviews](ai-agents-interviews.md).

**Q: How evaluate prompt changes?**

> Golden set regression; A/B online; instruction-following pass rate — [Evaluation phase](../ai-evaluation/prompt-evaluation.md).

**Scenario:** Model ignores JSON format.

> Add schema in API; few-shot example; post-validate + repair pass; lower temperature.

## Whiteboard

Draw prompt lifecycle: template → variables → LLM → validate → log version.

## Further Reading

- [Prompt Engineering](../prompt-engineering/README.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Section 9 |
