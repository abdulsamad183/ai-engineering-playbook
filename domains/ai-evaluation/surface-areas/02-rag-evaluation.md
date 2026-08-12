---
title: "RAG Evaluation"
description: "Evaluating retrieval and grounded generation — recall, faithfulness, citations, and end-to-end task success."
domain: ai-evaluation
tags: [rag, evaluation]
status: published
created: 2026-08-11
updated: 2026-08-12
version: "2.1"
related:
  - 01-prompt-evaluation.md
  - ../../rag/evaluation-and-production/01-rag-evaluation.md
  - ../metrics/01-core-metrics.md
---

# RAG Evaluation

> RAG quality is two systems: **retrieval** and **generation**. Measure both or you will optimize the wrong half.

## Metric stack

| Stage | Metrics |
|-------|---------|
| Retrieval | recall@k, nDCG@k, MRR |
| Context | citation coverage, compression loss |
| Generation | faithfulness, answer relevance, task success |
| Ops | p95 latency, $/query |

## Labeled data

Prefer query → relevant chunk IDs for retrieval. For generation, use rubrics or human prefs; LLM judges need spot checks.

```python
def recall_at_k(relevant: set[str], retrieved: list[str], k: int) -> float:
    hit = relevant & set(retrieved[:k])
    return len(hit) / max(1, len(relevant))
```

## Failure diagnosis

| Symptom | Likely layer |
|---------|--------------|
| Wrong facts, good citations | Generator / prompt |
| Fluent lies, weak citations | Retrieval / chunking |
| Good offline, bad prod | Filters, drift, stale index |

## Production

Shadow new indexes; gate on retrieval + faithfulness floors; monitor abstain rate.

## Interview

**Q: Why not only faithfulness?** A model can be faithful to irrelevant context — pair with relevance and task success.


## End-to-end harness outline

1. Index fixture corpus
2. Run queries
3. Score retrieval + answer
4. Fail CI under floors

See also [RAG evaluation lesson](../../rag/evaluation-and-production/01-rag-evaluation.md) and the [capstone eval step](../../../meta/capstone-walkthrough.md).

## Slice ideas

- Multi-hop questions
- Exact SKU / id lookups (need BM25)
- ACL-denied docs must never appear

## Navigation

- [Prompt evaluation](01-prompt-evaluation.md) · [RAG handbook eval](../../rag/evaluation-and-production/01-rag-evaluation.md)
- Offline demo eval mindset: [mini RAG](../../../examples/rag/FROM_MINI_TO_STARTER.md)
- [Section hub](README.md) · [Eval hub](../README.md)
