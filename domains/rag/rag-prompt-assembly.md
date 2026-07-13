---
title: "RAG Prompt Assembly"
description: "Formatting retrieved chunks, citations, grounding instructions, and LLM messages for RAG."
domain: rag
tags: [rag, prompt-assembly, context-formatting, phase-7]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - citations-and-grounding.md
  - ../../prompts/templates/rag-query.md
  - ../context-engineering/retrieval-context.md
keywords: [prompt assembly, RAG prompt, context formatting]
author: hp
---

# RAG Prompt Assembly

## Overview

Section **14** of Phase 7.

```mermaid
flowchart TD
    CHK[Ranked chunks] --> FMT[Format with IDs]
    FMT --> SYS[System: grounding rules]
    FMT --> USR[User: question + context]
    SYS --> LLM[LLM]
    USR --> LLM
```

## Assembly Template

```
System: Answer only from <sources>. Cite [chunk_id] inline. If insufficient, say so.

<sources>
<source id="chunk-1" doc="policy.pdf">...</source>
</sources>

User: {question}
```

Use [RAG query template](../../prompts/templates/rag-query.md).

## Navigation

- [Citations and Grounding](citations-and-grounding.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 7 Section 14 |
