---
title: "JSON Generation Prompt Template"
description: "Reusable prompt for producing schema-valid JSON output with strict format compliance."
domain: prompt-engineering
tags: [prompt, json, structured-output, schema]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
id: json-generation-v1
task: json-generation
models:
  recommended: [gpt-4o, claude-sonnet-4, gpt-4o-mini]
  min_capability: intermediate
token_budget:
  system: 300
  user_per_request: 150
variables:
  required: [task_description, json_schema]
  optional: [examples, constraints, null_policy]
output:
  format: json
  schema: user_defined
related:
  - classification.md
  - extraction.md
  - ../../domains/prompt-engineering/prompt-templates-guide.md
keywords: [JSON, structured output, schema validation, API response]
---

# JSON Generation Prompt Template

> Generate valid JSON that conforms exactly to a provided schema. No markdown fences, commentary, or trailing text.

## Pattern Overview

| Attribute | Value |
|-----------|-------|
| Use Case | API response shaping, structured LLM outputs, tool inputs, config generation |
| Best Models | gpt-4o, claude-sonnet-4, gpt-4o-mini |
| Complexity | Simple to Moderate |
| Token Budget | ~350–700 tokens (system + user) |
| Expected Output | Raw JSON matching schema |

## When to Use

- Any pipeline step requiring machine-parseable structured output
- Feeding LLM output into downstream validators or databases
- Generating tool/function call arguments
- Standardizing responses across multiple prompt variants

## When Not to Use

- Human-readable prose responses
- Schemas too complex for reliable one-shot generation (split into steps)
- When native structured output / JSON mode is available but not configured

## System Prompt

```
You are a structured data generator.

Your task: {{task_description}}

Produce output that conforms exactly to this JSON schema:

{{json_schema}}

Rules:
- Output valid JSON only. No markdown code fences, no explanation before or after.
- Use null for missing optional fields per this policy: {{null_policy}}
- Match field types exactly: strings quoted, numbers unquoted, booleans lowercase.
- Do not include fields not defined in the schema.
- Enum fields must use only allowed values from the schema.
{{constraints}}

If you cannot fulfill the task within schema constraints, return:
{"error": "<brief reason>"}
```

## User Prompt

```
{{examples}}

Input data:
{{input_data}}

Additional instructions: {{additional_instructions}}
```

## Variables

| Name | Required | Default | Description |
|------|----------|---------|-------------|
| `task_description` | Yes | — | What JSON to produce |
| `json_schema` | Yes | — | JSON Schema or field spec with types |
| `input_data` | No | (none) | Source data to transform into JSON |
| `examples` | No | (none) | Few-shot input → output pairs |
| `constraints` | No | (none) | Extra rules: max lengths, required fields |
| `null_policy` | No | use null for absent optional fields | How to handle missing data |
| `additional_instructions` | No | (none) | Per-request overrides |

## Complete Example

### Input Variables

```yaml
task_description: "Extract contact info from the text into structured JSON."
json_schema: |
  {
    "name": "string",
    "email": "string or null",
    "phone": "string or null",
    "company": "string or null"
  }
input_data: "Jane Doe, jane@acme.io, works at Acme Corp"
null_policy: use null for absent optional fields
```

### Expected Output

```json
{"name": "Jane Doe", "email": "jane@acme.io", "phone": null, "company": "Acme Corp"}
```

## Evaluation Criteria

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Schema compliance | 100% | JSON Schema validation (ajv, pydantic) |
| Parse success | 100% | `json.loads()` without errors |
| Type correctness | 100% | Field types match schema |
| No extra fields | 100% | `additionalProperties: false` check |
| Semantic accuracy | > 90% | Content matches task on golden set |

## Tips and Pitfalls

- Enable provider JSON mode; keep schemas flat when possible.
- Validate with the same parser your production pipeline uses.
- Define `{{null_policy}}` explicitly to avoid empty strings vs. null confusion.
