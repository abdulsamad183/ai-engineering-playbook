---
title: "Summarization Prompt Template"
description: "Reusable prompt for condensing documents while preserving key facts, numbers, and structure."
domain: prompt-engineering
tags: [prompt, summarization, compression, abstractive]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
id: summarization-v1
task: summarization
models:
  recommended: [gpt-4o-mini, claude-sonnet-4, gpt-4o]
  min_capability: intermediate
token_budget:
  system: 200
  user_per_1k_input: 40
variables:
  required: [document]
  optional: [audience, max_words, focus_areas, summary_format, language]
output:
  format: markdown
  schema: null
related:
  - ../../domains/prompt-engineering/prompt-templates-guide.md
keywords: [summarization, executive summary, document compression]
---

# Summarization Prompt Template

> Condense long documents for a target audience while preserving numbers, dates, names, and action items exactly as stated.

## Pattern Overview

| Attribute | Value |
|-----------|-------|
| Use Case | Executive briefings, technical digests, meeting notes, report condensation |
| Best Models | gpt-4o-mini, claude-sonnet-4, gpt-4o |
| Complexity | Simple to Moderate |
| Token Budget | ~250–600 tokens (system + user) |
| Expected Output | Markdown summary within word limit |

## When to Use

- Leadership briefings from long reports or meeting transcripts
- Technical document digests for engineers who need the essentials
- Pre-processing long inputs before downstream classification or extraction
- Map-reduce summarization (per-chunk calls with this template)

## When Not to Use

- Legal or compliance extractive quoting (use extraction with verbatim fields)
- Documents exceeding ~80% of model context (use map-reduce or hierarchical summarization)
- Tasks requiring new analysis not present in the source

## System Prompt

```
You are an expert summarizer for {{audience}}.

Rules:
- Summarize the document in at most {{max_words}} words.
- Preserve all numbers, dates, currency amounts, and proper nouns exactly as written.
- Do not add information, opinions, or conclusions not present in the document.
- Omit boilerplate, repetition, and tangential details.
- Write in {{language}}.
- Use {{summary_format}} format.

Output format:
{{format_specification}}
```

## User Prompt

```
<document>
{{document}}
</document>

Focus areas (prioritize these if present): {{focus_areas}}

Exclude from summary: {{exclude_topics}}
```

## Variables

| Name | Required | Default | Description |
|------|----------|---------|-------------|
| `document` | Yes | — | Full text or chunk to summarize |
| `audience` | No | a general professional audience | Reader persona: executives, engineers, customers |
| `max_words` | No | 200 | Hard word limit for the summary |
| `focus_areas` | No | key decisions, action items, risks | Topics to emphasize |
| `exclude_topics` | No | (none) | Topics to omit |
| `summary_format` | No | bullet points | bullets, paragraphs, structured sections |
| `format_specification` | No | 3–5 bullet points, each one sentence | Detailed output structure |
| `language` | No | English | Output language |

## Complete Example

### Input Variables

```yaml
document: |
  Q3 revenue reached $4.2M, up 18% YoY. The platform team shipped
  SSO on September 12. Three enterprise deals ($500K ARR each) are
  in legal review. Hiring freeze extended through December 31.
audience: "executive leadership"
max_words: 80
focus_areas: "revenue, key shipments, pipeline risks"
summary_format: bullet points
```

### Expected Output

```
- Q3 revenue was $4.2M, an 18% year-over-year increase.
- SSO shipped on September 12.
- Three enterprise deals worth $500K ARR each remain in legal review.
- The hiring freeze is extended through December 31.
```

## Evaluation Criteria

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Faithfulness | > 95% | No facts added or distorted vs. source |
| Numeric preservation | 100% | All numbers/dates match source exactly |
| Conciseness | Within budget | Word count ≤ {{max_words}} |
| Coverage | > 85% | Key focus_areas present in summary |
| ROUGE-L (optional) | Baseline-dependent | Overlap with reference summaries |

## Tips and Pitfalls

- Specify audience and `{{max_words}}`; preserve numbers and dates exactly.
- Chunk long documents before one-shot summarization.
- Eval faithfulness separately from fluency.
