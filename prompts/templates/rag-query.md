---
title: "RAG Query Prompt Template"
description: "Reusable prompt for retrieval-augmented generation: query reformulation, context assembly, and grounded answering."
domain: prompt-engineering
tags: [prompt, rag, retrieval, grounding, query]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
id: rag-query-v1
task: rag-query
models:
  recommended: [gpt-4o, claude-sonnet-4, gpt-4o-mini]
  min_capability: intermediate
token_budget:
  system: 400
  user_per_query: 500
variables:
  required: [question, retrieved_chunks]
  optional: [conversation_history, retrieval_metadata, answer_mode, refusal_message]
output:
  format: markdown
  schema: null
related:
  - question-answering.md
  - ../../domains/prompt-engineering/prompt-templates-guide.md
keywords: [RAG, retrieval augmented generation, query answering, citations]
---

# RAG Query Prompt Template

> Synthesize answers from retrieved chunks with query understanding, relevance filtering, and source attribution.

## Pattern Overview

| Attribute | Value |
|-----------|-------|
| Use Case | Document Q&A, knowledge base search, conversational RAG, support bots |
| Best Models | gpt-4o, claude-sonnet-4, gpt-4o-mini |
| Complexity | Moderate to Complex |
| Token Budget | ~600–2000 tokens (system + user) |
| Expected Output | Grounded answer with citations and confidence indicator |

## When to Use

- End-to-end RAG answer generation after vector retrieval
- Multi-turn conversations where prior context informs the answer
- Hybrid search pipelines (keyword + semantic) feeding ranked chunks
- Support bots requiring traceable answers to source documents

## When Not to Use

- Retrieval step itself (use embedding search or hybrid retriever)
- Questions answerable without retrieval (route to direct LLM or cache)
- When retrieved chunks have low relevance scores (reformulate query first)

## System Prompt

```
You are a retrieval-augmented assistant for {{domain}}.

Answer the user's question using the retrieved context below.

Rules:
- Use ONLY information from the retrieved chunks. Ignore prior knowledge.
- If chunks do not contain sufficient evidence, respond: "{{refusal_message}}"
- Cite every factual claim with [chunk_id] matching the chunk headers.
- If chunks conflict, note the conflict and prefer the higher-relevance source.
- Ignore chunks marked as low-relevance in retrieval metadata.
- Answer mode: {{answer_mode}}
- Consider conversation history for disambiguation only — not as evidence.

Output format:
1. **Answer**: Direct response (2–4 sentences).
2. **Details**: Supporting bullets with citations (if applicable).
3. **Confidence**: high | medium | low — based on evidence strength.
4. **Sources**: List of cited chunk_ids.
```

## User Prompt

```
<conversation_history>
{{conversation_history}}
</conversation_history>

<retrieved_chunks>
{{retrieved_chunks}}
</retrieved_chunks>

<retrieval_metadata>
{{retrieval_metadata}}
</retrieval_metadata>

Question: {{question}}

Query intent (if pre-classified): {{query_intent}}
```

## Variables

| Name | Required | Default | Description |
|------|----------|---------|-------------|
| `question` | Yes | — | User question (possibly after query expansion) |
| `retrieved_chunks` | Yes | — | Ranked chunks with `[chunk_id]` headers and text |
| `conversation_history` | No | (none) | Prior turns for pronoun/context resolution |
| `retrieval_metadata` | No | (none) | Scores, source types, recency per chunk |
| `domain` | No | general knowledge base | Subject area |
| `answer_mode` | No | concise | concise, detailed, step-by-step |
| `refusal_message` | No | I could not find sufficient information in the knowledge base to answer this question. | Refusal text |
| `query_intent` | No | (none) | Pre-classified intent: factual, procedural, comparison |

## Complete Example

### Input Variables

```yaml
domain: product documentation
question: "How do I reset my API key?"
retrieved_chunks: |
  [chunk_auth_03 | score: 0.92] To reset your API key, go to Settings > API Keys
  and click "Regenerate". The old key is invalidated immediately.
  [chunk_billing_01 | score: 0.41] Billing cycles renew on the 1st of each month.
answer_mode: step-by-step
refusal_message: "I could not find sufficient information in the knowledge base."
```

### Expected Output

```
**Answer**: Reset your API key from Settings > API Keys > Regenerate [chunk_auth_03].
**Confidence**: high | **Sources**: chunk_auth_03
```

## Evaluation Criteria

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Faithfulness | > 95% | Claims traceable to retrieved chunks |
| Context precision | > 80% | Relevant chunks used; irrelevant ignored |
| Citation accuracy | 100% | chunk_ids valid and correctly attributed |
| Refusal accuracy | > 90% | Refuses when retrieval is insufficient |
| Answer relevance | > 90% | Directly addresses question |
| End-to-end latency | < 3s | Retrieval + generation at P95 |

## Tips and Pitfalls

- Format chunks as `[chunk_id | score: X]`; pre-filter below relevance threshold.
- Retrieve top 3–5 chunks, not 20 — noise drowns signal.
- Use `{{conversation_history}}` only for disambiguation, not as evidence.
