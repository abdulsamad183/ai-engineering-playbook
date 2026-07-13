---
title: "Retrieval Context"
description: "Retrieval as context injection — documents, knowledge pipelines, citations, freshness, relevance, and grounding without full RAG implementation."
domain: context-engineering
tags: [context-engineering, retrieval, grounding, citations, phase-6]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - context-ranking.md
  - context-selection.md
  - ../rag/README.md
  - ../embeddings/README.md
  - ../../prompts/templates/rag-query.md
keywords: [retrieval context, knowledge injection, grounding, citations, RAG]
author: hp
---

# Retrieval Context

> How retrieved knowledge enters the context window — pipeline, formatting, grounding, and quality signals. Full RAG implementation is covered in the RAG phase.

## Table of Contents

- [Overview](#overview)
- [Retrieved Documents as Context](#retrieved-documents-as-context)
- [Knowledge Injection](#knowledge-injection)
- [Retrieval Pipelines](#retrieval-pipelines)
- [Citations](#citations)
- [Freshness](#freshness)
- [Relevance](#relevance)
- [Grounding](#grounding)
- [Production Considerations](#production-considerations)
- [Security Considerations](#security-considerations)
- [Python Examples](#python-examples)
- [Interview Preparation](#interview-preparation)
- [Navigation](#navigation)

---

## Overview

**Retrieval context** is external knowledge fetched at query time and injected into the prompt. It is the primary way applications supply facts the model was not trained on.

Section **12** of Phase 6 — conceptual foundation for [RAG](../rag/README.md).

```mermaid
flowchart LR
    Q[Query] --> RW[Query rewrite]
    RW --> EMB[Embed]
    EMB --> VDB[Vector search]
    VDB --> RERANK[Rerank]
    RERANK --> FMT[Format blocks]
    FMT --> CTX[Context window]
```

---

## Retrieved Documents as Context

Each chunk becomes a **ContextBlock**:

```xml
<source id="policy-44" score="0.89" updated="2026-06-01">
Refund policy: duplicate charges refunded within 3 business days...
</source>
```

Attribute metadata for debugging, citations, and freshness decay.

---

## Knowledge Injection

Injection points:

| Location | Content |
|----------|---------|
| System | Retrieval instructions, citation rules |
| User/context | Retrieved chunks |
| Not | Mixed into system as facts without attribution |

Use [RAG query template](../../prompts/templates/rag-query.md) for answer synthesis behavior.

---

## Retrieval Pipelines

1. **Query formulation** — rewrite with conversation context
2. **Retrieval** — vector + optional keyword
3. **Rerank** — cross-encoder or LLM reranker
4. **Filter** — permissions, language, min score
5. **Format** — delimited blocks with IDs
6. **Budget** — trim to retrieval token allocation

---

## Citations

Require model to cite `source id` inline. Enables:

- User verification
- Hallucination detection (citation not in retrieved set)
- Analytics on useful documents

---

## Freshness

Index `updated_at` metadata. Boost or filter stale content. Re-embed on document update with version keys for cache invalidation.

---

## Relevance

Minimum similarity threshold. Empty retrieval → explicit "no relevant documents" block — prevents model from ignoring absence.

---

## Grounding

| Technique | Purpose |
|-----------|---------|
| "Answer only from context" | Reduce hallucination |
| Citation requirement | Traceability |
| Abstain instruction | When context insufficient |
| Post-check | Verify claims ⊆ retrieved text |

Grounding is split between **prompt** (Phase 5) and **retrieval quality** (this section + RAG phase).

---

## Production Considerations

- Log retrieved IDs and scores per request
- Monitor retrieval hit rate and empty rate
- Separate indexes per tenant where required

---

## Security Considerations

- ACL filter at retrieval time, not post-hoc
- Prevent cross-tenant leakage in shared indexes
- Sanitize document content before injection

---

## Python Examples

```python
@dataclass
class RetrievedChunk:
    doc_id: str
    text: str
    score: float
    updated_at: str


def format_retrieval_context(chunks: list[RetrievedChunk]) -> str:
    if not chunks:
        return "<context>No relevant documents found.</context>"
    parts = []
    for c in chunks:
        parts.append(
            f'<source id="{c.doc_id}" score="{c.score:.2f}" updated="{c.updated_at}">\n'
            f"{c.text}\n</source>"
        )
    return "<context>\n" + "\n".join(parts) + "\n</context>"
```

---

## Interview Preparation

**Q: Difference between retrieval context and memory?**

> Retrieval: org knowledge base, shared docs. Memory: user-specific learned facts. Both inject into context with different stores and policies.

---

## Navigation

### Prerequisites

- [Context Selection](context-selection.md)
- [Embeddings](../embeddings/README.md)

### Related Topics

- [RAG](../rag/README.md) — Phase 7+
- [Context Ranking](context-ranking.md)

### Next

- [Context Budgeting](context-budgeting.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication — Phase 6 Section 12 |
