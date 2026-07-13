---
title: "Citations and Grounding"
description: "Source attribution, evidence, confidence, traceability, and explainability in RAG answers."
domain: rag
tags: [rag, citations, grounding, traceability, phase-7]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - hallucination-prevention.md
  - rag-prompt-assembly.md
keywords: [citations, source attribution, explainability]
author: hp
---

# Citations and Grounding

## Overview

Section **15** of Phase 7. Enterprise RAG requires **traceable** answers.

## Citation Models

| Style | Example |
|-------|---------|
| Inline ID | `Refunds take 3 days [chunk-44]` |
| Footnote | `...¹` with source list |
| Structured JSON | `{claim, chunk_ids, quote}` |

## Traceability Chain

```
answer span → chunk_id → doc_id → source_uri → version
```

## Confidence

Expose retrieval scores to UI; low max score → warn user.

## Python Example

```python
def build_citation_footer(chunks: list) -> str:
    lines = ["## Sources"]
    for c in chunks:
        lines.append(f"- [{c.chunk_id}] {c.metadata.get('title', c.doc_id)}")
    return "\n".join(lines)
```

## Navigation

- [Hallucination Prevention](hallucination-prevention.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 7 Section 15 |
