---
title: "Classification Prompt Template"
description: "Reusable prompt for assigning labels from a predefined taxonomy with confidence and rationale."
domain: prompt-engineering
tags: [prompt, classification, labeling, json]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
id: classification-v1
task: classification
models:
  recommended: [gpt-4o-mini, gpt-4o, claude-sonnet-4]
  min_capability: intermediate
token_budget:
  system: 300
  user_per_input: 100
variables:
  required: [text, categories]
  optional: [classification_mode, examples, output_schema]
output:
  format: json
  schema: classification_result
related:
  - json-generation.md
  - ../../domains/prompt-engineering/prompt-templates-guide.md
keywords: [classification, intent detection, sentiment, routing]
---

# Classification Prompt Template

> Assign one or more labels from a closed taxonomy. Return structured JSON with confidence scores and brief rationale.

## Pattern Overview

| Attribute | Value |
|-----------|-------|
| Use Case | Intent routing, sentiment, topic labeling, ticket triage, content moderation |
| Best Models | gpt-4o-mini, gpt-4o, claude-sonnet-4 |
| Complexity | Simple to Moderate |
| Token Budget | ~350–700 tokens (system + user) |
| Expected Output | JSON with label(s), confidence, rationale |

## When to Use

- Routing customer messages to the correct team or workflow
- Content moderation with predefined violation categories
- Intent detection for conversational agents
- Batch labeling for dataset creation or quality monitoring

## When Not to Use

- Open-ended tagging without a defined taxonomy
- Classification requiring external knowledge not in the label definitions
- High-stakes decisions without human review (use as triage, not final arbiter)

## System Prompt

```
You are an expert text classifier for {{domain}}.

Classify the input using {{classification_mode}} from exactly these categories:

{{categories}}

Rules:
- Choose only from the categories listed above.
- If no category fits, use the fallback label: {{fallback_label}}
- Base your decision only on the input text and category definitions.
- Provide a confidence score between 0.0 and 1.0.
- Keep rationale to 1–2 sentences citing specific phrases from the input.

Output format (valid JSON only, no markdown fences):
{{output_schema}}
```

## User Prompt

```
{{examples}}

<input>
{{text}}
</input>
```

## Variables

| Name | Required | Default | Description |
|------|----------|---------|-------------|
| `text` | Yes | — | Text to classify |
| `categories` | Yes | — | Category list with definitions (one per line) |
| `domain` | No | general text classification | Domain context for disambiguation |
| `classification_mode` | No | exactly one label | "exactly one label" or "one or more labels" |
| `fallback_label` | No | other | Label when no category fits |
| `examples` | No | (none) | Few-shot examples in Input/Output pairs |
| `output_schema` | No | see below | JSON schema string for expected output |

Default `output_schema`: `{"label": "<category>", "confidence": 0.0, "rationale": "..."}`

## Complete Example

### Input

```yaml
categories: "billing, technical, account, other"
text: "I was charged twice for my Pro plan this month."
```

### Expected Output

```json
{"label": "billing", "confidence": 0.97, "rationale": "Duplicate charge for subscription plan."}
```

## Evaluation Criteria

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Accuracy | > 90% | Compare to labeled golden set |
| Format compliance | 100% | JSON schema validation |
| Confidence calibration | ECE < 0.1 | Reliability diagram vs. actual accuracy |
| Fallback rate | Monitor | Track `other` frequency for taxonomy gaps |
| Latency | < 1s | API response time at P95 |

## Tips and Pitfalls

- Define categories with examples and boundary cases; add few-shot via `{{examples}}`.
- Use schema-constrained generation; monitor class distribution drift.
- Sharpen overlapping category definitions to reduce label flipping.
