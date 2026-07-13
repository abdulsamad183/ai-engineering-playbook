---
title: "Documentation Prompt Template"
description: "Reusable prompt for generating technical documentation from code, APIs, or specifications."
domain: prompt-engineering
tags: [prompt, documentation, technical-writing, markdown]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
id: documentation-v1
task: documentation
models:
  recommended: [gpt-4o, claude-sonnet-4, gpt-4o-mini]
  min_capability: intermediate
token_budget:
  system: 350
  user_per_input: 200
variables:
  required: [source_material, doc_type]
  optional: [audience, sections, style_guide, existing_docs]
output:
  format: markdown
  schema: null
related:
  - markdown-generation.md
  - code-review.md
  - ../../domains/prompt-engineering/prompt-templates-guide.md
keywords: [documentation, API docs, README, runbooks, technical writing]
---

# Documentation Prompt Template

> Generate accurate, audience-appropriate technical documentation from source code, API specs, or design notes.

## Pattern Overview

| Attribute | Value |
|-----------|-------|
| Use Case | API reference, README sections, runbooks, architecture notes, onboarding guides |
| Best Models | gpt-4o, claude-sonnet-4, gpt-4o-mini |
| Complexity | Moderate |
| Token Budget | ~500–1200 tokens (system + user) |
| Expected Output | Markdown documentation with required sections |

## When to Use

- Drafting API reference from OpenAPI specs or handler code
- Expanding sparse README sections from implementation details
- Creating runbooks from incident notes or operational procedures
- Onboarding guides from architecture diagrams and code structure

## When Not to Use

- Documentation requiring verified production metrics not in source material
- Legal or compliance documents without human legal review
- Replacing auto-generated API docs where OpenAPI/Swagger is authoritative

## System Prompt

```
You are a senior technical writer for {{audience}}.

Generate {{doc_type}} documentation from the provided source material.

Rules:
- Document only what is present in the source. Do not invent endpoints, parameters, or behavior.
- Use clear headings, short paragraphs, and code blocks for examples.
- Follow this style guide: {{style_guide}}
- Include these sections (omit empty sections): {{sections}}
- Mark uncertain details with "[VERIFY]" rather than guessing.
- Use present tense and active voice.

Output format:
- Valid Markdown only
- No preamble or meta-commentary
- Code examples must be syntactically valid for the stated language
```

## User Prompt

```
<existing_docs>
{{existing_docs}}
</existing_docs>

<source_material>
{{source_material}}
</source_material>

Additional context: {{additional_context}}
```

## Variables

| Name | Required | Default | Description |
|------|----------|---------|-------------|
| `source_material` | Yes | — | Code, OpenAPI JSON, design notes, or specs |
| `doc_type` | Yes | — | API reference, README, runbook, architecture overview |
| `audience` | No | software engineers | Target reader skill level and role |
| `sections` | No | Overview, Usage, Parameters, Examples, Errors | Required doc sections |
| `style_guide` | No | Google developer documentation style | Tone, terminology, formatting rules |
| `existing_docs` | No | (none) | Prior docs to extend or avoid duplicating |
| `additional_context` | No | (none) | Product context, naming conventions, links |

## Complete Example

### Input Variables

```yaml
doc_type: API reference
audience: backend engineers integrating the billing service
source_material: |
  POST /v1/invoices — creates invoice. Body: customer_id (uuid), line_items (array).
  Returns 201 with invoice object. 400 if customer_id missing. 402 if payment method invalid.
sections: Overview, Request, Response, Error codes, Example
```

### Expected Output

```markdown
## POST /v1/invoices

Creates a new invoice for a customer.

### Request

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `customer_id` | uuid | Yes | Customer identifier |
| `line_items` | array | Yes | Invoice line items |

### Response

`201 Created` — Returns the invoice object.

### Error codes

| Code | Condition |
|------|-----------|
| 400 | `customer_id` missing |
| 402 | Payment method invalid |

### Example

[VERIFY] Request/response example not present in source.
```

## Evaluation Criteria

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Accuracy | 100% | Every documented fact traceable to source |
| Completeness | > 90% | Required sections present |
| Hallucination rate | 0% | No invented endpoints, fields, or behavior |
| Readability | Subjective | Peer review or readability score |

## Tips and Pitfalls

- Provide OpenAPI or typed interfaces when available — reduces hallucinated parameters.
- Use `[VERIFY]` markers for gaps; never fabricate examples.
- Split large codebases into module-scoped documentation calls.
