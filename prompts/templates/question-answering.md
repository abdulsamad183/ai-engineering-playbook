---
title: "Question Answering Prompt Template"
description: "Reusable prompt for grounded Q&A over provided context with citations and refusal behavior."
domain: prompt-engineering
tags: [prompt, qa, rag, grounding, citations]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
id: question-answering-v1
task: question-answering
models:
  recommended: [gpt-4o, claude-sonnet-4, gpt-4o-mini]
  min_capability: intermediate
token_budget:
  system: 250
  user_per_1k_context: 80
variables:
  required: [context, question]
  optional: [refusal_message, answer_style, language]
output:
  format: markdown
  schema: null
related:
  - rag-query.md
  - ../../domains/prompt-engineering/prompt-templates-guide.md
keywords: [question answering, grounded QA, citations, refusal]
---

# Question Answering Prompt Template

> Answer user questions using only provided context. Refuse when evidence is insufficient and cite sources for every factual claim.

## Pattern Overview

| Attribute | Value |
|-----------|-------|
| Use Case | Grounded Q&A over documents, knowledge bases, or retrieved chunks |
| Best Models | gpt-4o, claude-sonnet-4, gpt-4o-mini |
| Complexity | Moderate |
| Token Budget | ~300–800 tokens (system + user) |
| Expected Output | Markdown answer with inline citations |

## When to Use

- Customer support bots answering from a knowledge base
- Internal "ask your docs" features over policy or technical content
- Compliance Q&A where answers must be traceable to source material
- Post-retrieval answer synthesis in RAG pipelines

## When Not to Use

- Open-ended creative writing without grounding requirements
- Tasks requiring real-time data not present in context
- Multi-hop reasoning across dozens of documents (use agent planning instead)

## System Prompt

```
You are a precise question-answering assistant specializing in {{domain}}.

Rules:
- Answer using ONLY the information in the provided context.
- If the context does not contain enough information to answer, respond exactly with: "{{refusal_message}}"
- Cite every factual claim inline using [source_id] matching the IDs in the context blocks.
- Do not speculate, infer beyond the text, or use outside knowledge.
- If the question is ambiguous, state your interpretation before answering.
- Write in {{language}} using a {{answer_style}} tone.

Output format:
- Direct answer first (1–3 sentences).
- Supporting details as bullet points, each with citations.
- End with a "Sources" line listing cited source IDs.
```

## User Prompt

```
<context>
{{context}}
</context>

Question: {{question}}

Additional instructions: {{additional_instructions}}
```

## Variables

| Name | Required | Default | Description |
|------|----------|---------|-------------|
| `domain` | No | general knowledge | Subject area for tone calibration |
| `context` | Yes | — | Retrieved or provided text with `[source_id]` headers |
| `question` | Yes | — | User question to answer |
| `refusal_message` | No | I don't have enough information to answer that. | Exact text when context is insufficient |
| `answer_style` | No | concise and professional | Tone: concise, detailed, executive, technical |
| `language` | No | English | Output language |
| `additional_instructions` | No | (none) | Extra constraints per request |

## Complete Example

### Input

```yaml
context: "[doc_01] Refunds take 5-7 business days."
question: "How long do refunds take?"
```

### Expected Output

```
Refunds take 5-7 business days after approval [doc_01].
Sources: doc_01
```

## Evaluation Criteria

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Faithfulness | > 95% | Compare claims to source chunks; no hallucinated facts |
| Citation accuracy | 100% | Every claim maps to a valid source_id in context |
| Refusal precision | > 90% | Correctly refuses unanswerable questions |
| Answer relevance | > 90% | Human or LLM-judge scores directness to question |
| Format compliance | 100% | Contains answer, bullets, and Sources line |

## Tips and Pitfalls

- Prefix every context chunk with a source ID; set `temperature=0` for factual QA.
- Retrieve narrowly before answering — overlong context dilutes signal.
- Use a fixed `{{refusal_message}}` string for downstream detection.
