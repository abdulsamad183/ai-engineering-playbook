---
title: "Markdown Generation Prompt Template"
description: "Reusable prompt for structured Markdown output with headings, tables, lists, and code blocks."
domain: prompt-engineering
tags: [prompt, markdown, formatting, structured-output]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
id: markdown-generation-v1
task: markdown-generation
models:
  recommended: [gpt-4o-mini, gpt-4o, claude-sonnet-4]
  min_capability: basic
token_budget:
  system: 280
  user_per_input: 120
variables:
  required: [content_source, document_structure]
  optional: [heading_levels, include_toc, table_columns, code_language]
output:
  format: markdown
  schema: null
related:
  - documentation.md
  - json-generation.md
  - ../../domains/prompt-engineering/structured-prompting.md
keywords: [markdown, formatting, reports, structured documents]
---

# Markdown Generation Prompt Template

> Transform raw content into well-structured Markdown with consistent heading hierarchy and formatting.

## Pattern Overview

| Attribute | Value |
|-----------|-------|
| Use Case | Reports, meeting notes formatting, data presentation, changelog drafts |
| Best Models | gpt-4o-mini, gpt-4o, claude-sonnet-4 |
| Complexity | Simple |
| Token Budget | ~350–700 tokens |
| Expected Output | Valid Markdown matching specified structure |

## When to Use

- Converting unstructured notes into publishable Markdown
- Standardizing report format across a team or pipeline
- Generating comparison tables from bullet lists or JSON
- Preparing content for static site generators or wikis

## When Not to Use

- When JSON or HTML is the required downstream format (convert in code instead)
- Content requiring complex diagrams (use Mermaid in a dedicated step)
- Documents where exact verbatim quoting is legally required (use extraction)

## System Prompt

```
You are a document formatter. Convert the input into valid Markdown.

Structure to follow:
{{document_structure}}

Formatting rules:
- Use heading levels {{heading_levels}} only (do not skip levels).
- {{include_toc}}
- Tables use GitHub-flavored Markdown pipe syntax.
- Code blocks use language tag: {{code_language}}
- Use bullet lists for unordered items; numbered lists for sequences.
- Do not wrap output in markdown code fences.
- Do not add content not present in the source unless structure requires section headers.

Table columns (when applicable): {{table_columns}}
```

## User Prompt

```
<content>
{{content_source}}
</content>

Formatting notes: {{formatting_notes}}
```

## Variables

| Name | Required | Default | Description |
|------|----------|---------|-------------|
| `content_source` | Yes | — | Raw text, bullets, or JSON to format |
| `document_structure` | Yes | — | Section outline with heading names |
| `heading_levels` | No | H1–H3 | Allowed heading depth |
| `include_toc` | No | Omit table of contents | Include TOC after H1 |
| `table_columns` | No | (auto) | Column headers for tabular data |
| `code_language` | No | python | Default fenced code language |
| `formatting_notes` | No | (none) | Bold terms, link placeholders, etc. |

## Complete Example

### Input Variables

```yaml
document_structure: |
  # Weekly Status
  ## Highlights
  ## Risks
  ## Metrics (table)
content_source: |
  Highlights: shipped SSO, closed 3 enterprise deals.
  Risks: hiring freeze extended.
  Metrics: ARR 4.2M, churn 2.1%
table_columns: Metric, Value
```

### Expected Output

```markdown
# Weekly Status

## Highlights

- Shipped SSO
- Closed 3 enterprise deals

## Risks

- Hiring freeze extended

## Metrics

| Metric | Value |
|--------|-------|
| ARR | 4.2M |
| Churn | 2.1% |
```

## Evaluation Criteria

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Valid Markdown | 100% | Lint with markdown parser |
| Structure match | 100% | Required sections present |
| Faithfulness | > 95% | No facts added to source |
| Heading hierarchy | Valid | No skipped levels |

## Tips and Pitfalls

- Specify `document_structure` explicitly — models default to generic outlines.
- Validate Markdown in CI with a linter (markdownlint, mdformat).
- For nested documents, use XML or JSON prompting for stricter structure.
