---
title: "Query Engineering for RAG"
description: "Query preprocessing, rewriting, expansion, decomposition, routing, HyDE, and intent detection for retrieval."
domain: rag
tags: [rag, query-engineering, HyDE, rewriting, phase-7]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - retrieval-strategies.md
  - ../context-engineering/conversation-history.md
keywords: [query rewriting, HyDE, query decomposition, intent]
author: hp
---

# Query Engineering for RAG

## Overview

Section **11** of Phase 7. Raw user questions are poor retrieval queries — engineer them.

## Techniques

| Technique | Description |
|-----------|-------------|
| **Preprocessing** | Lowercase, strip noise, detect language |
| **Rewriting** | LLM: resolve pronouns using chat history |
| **Expansion** | Add synonyms, acronyms |
| **Decomposition** | Split multi-part questions into sub-queries |
| **Routing** | Send to specialized indexes by intent |
| **HyDE** | Generate hypothetical answer doc, embed that |
| **Intent detection** | Classify: factual / procedural / chitchat |

## HyDE Workflow

```mermaid
flowchart LR
    Q[User query] --> LLM[Generate hypothetical doc]
    LLM --> EMB[Embed hypothetical]
    EMB --> RET[Retrieve real docs]
```

Improves recall on vague queries; adds latency + cost.

## Python Example

```python
async def rewrite_query(history: list[dict], question: str, llm) -> str:
    prompt = f"Rewrite as standalone search query.\nHistory: {history}\nQuestion: {question}"
    return await llm.complete(prompt, temperature=0)
```

## Navigation

- [Retrieval Strategies](retrieval-strategies.md) · [Multi-query in examples](../../examples/rag/)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 7 Section 11 |
