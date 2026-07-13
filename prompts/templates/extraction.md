---
title: "Extraction Prompt Template"
description: "Reusable prompt for pulling structured fields from unstructured text using a defined schema."
domain: prompt-engineering
tags: [prompt, extraction, structured-output, json]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
id: extraction-v1
task: extraction
models:
  recommended: [gpt-4o, claude-sonnet-4, gpt-4o-mini]
  min_capability: intermediate
token_budget:
  system: 350
  user_per_input: 120
variables:
  required: [source_text, json_schema]
  optional: [domain, extraction_rules, examples]
output:
  format: json
  schema: user_defined
related:
  - json-generation.md
  - ../../domains/prompt-engineering/prompt-templates-guide.md
keywords: [information extraction, entity extraction, parsing, OCR post-processing]
---

# Extraction Prompt Template

> Extract structured data from unstructured text. Use null for missing fields; never infer values not explicitly stated.

## Pattern Overview

| Attribute | Value |
|-----------|-------|
| Use Case | Invoice parsing, contract clauses, resume fields, log parsing, form digitization |
| Best Models | gpt-4o, claude-sonnet-4, gpt-4o-mini |
| Complexity | Moderate |
| Token Budget | ~400–900 tokens (system + user) |
| Expected Output | JSON matching provided schema |

## When to Use

- Converting unstructured documents into database records
- Post-OCR cleanup and field mapping
- Pulling entities from emails, tickets, or chat transcripts
- Building structured datasets from raw text corpora

## When Not to Use

- Values requiring calculation or inference beyond the text
- Highly regulated extraction without human verification
- Real-time streaming extraction on very long documents (chunk first)

## System Prompt

```
You are a precise information extraction specialist for {{domain}}.

Extract fields from the input text according to this JSON schema:

{{json_schema}}

Rules:
- Return valid JSON only. No markdown fences or commentary.
- Use null for fields not explicitly present in the text.
- Do not infer, guess, or compute values not directly stated.
- Preserve original formatting for dates, amounts, and identifiers.
- For array fields, return an empty array [] when no items are found.
{{extraction_rules}}

Output: A single JSON object matching the schema exactly.
```

## User Prompt

```
{{examples}}

<text>
{{source_text}}
</text>
```

## Variables

| Name | Required | Default | Description |
|------|----------|---------|-------------|
| `source_text` | Yes | — | Unstructured input to parse |
| `json_schema` | Yes | — | Field definitions with types and descriptions |
| `domain` | No | general documents | Domain for terminology calibration |
| `extraction_rules` | No | (none) | Additional rules: normalization, date formats, etc. |
| `examples` | No | (none) | Few-shot input/output pairs |

## Complete Example

### Input Variables

```yaml
domain: "accounts payable"
json_schema: |
  {
    "vendor_name": "string",
    "invoice_number": "string",
    "invoice_date": "YYYY-MM-DD or null",
    "total_amount": "number or null",
    "currency": "ISO 4217 code or null",
    "line_items": [{"description": "string", "amount": "number"}]
  }
source_text: |
  INVOICE #INV-2024-0892
  Acme Supplies Ltd.
  Date: March 15, 2024
  Widgets (x10) .............. $250.00
  Shipping ................... $25.00
  Total: $275.00 USD
```

### Expected Output

```json
{"vendor_name": "Acme Supplies Ltd.", "invoice_number": "INV-2024-0892", "invoice_date": "2024-03-15", "total_amount": 275.00, "currency": "USD"}
```

## Evaluation Criteria

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Field accuracy | > 92% | Per-field exact match vs. golden labels |
| Schema compliance | 100% | JSON schema validation |
| Null precision | > 95% | Correct null when field absent (no hallucination) |
| Array completeness | > 90% | All items captured for list fields |
| Format normalization | > 95% | Dates, amounts match specified formats |

## Tips and Pitfalls

- Describe each schema field with type, format, and example; enforce null policy.
- Chunk long documents; validate output with JSON Schema before persisting.
- Do not let the model infer values not explicitly stated.
