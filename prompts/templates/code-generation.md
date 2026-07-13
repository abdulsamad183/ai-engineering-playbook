---
title: "Code Generation Prompt Template"
description: "Reusable prompt for generating production-quality source code with constraints, tests, and documentation."
domain: prompt-engineering
tags: [prompt, code-generation, software-engineering]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
id: code-generation-v1
task: code-generation
models:
  recommended: [gpt-4o, claude-sonnet-4, gpt-4o-mini]
  min_capability: advanced
token_budget:
  system: 350
  user_per_request: 200
variables:
  required: [task_description, language]
  optional: [framework, constraints, existing_code, test_requirements, output_format]
output:
  format: markdown
  schema: null
related:
  - code-review.md
  - ../../domains/prompt-engineering/prompt-templates-guide.md
keywords: [code generation, implementation, scaffolding, boilerplate]
---

# Code Generation Prompt Template

> Generate correct, idiomatic source code that follows project conventions, handles edge cases, and includes tests when requested.

## Pattern Overview

| Attribute | Value |
|-----------|-------|
| Use Case | Feature implementation, boilerplate scaffolding, algorithm solutions, API clients |
| Best Models | gpt-4o, claude-sonnet-4 |
| Complexity | Moderate to Complex |
| Token Budget | ~500–2000 tokens (system + user) |
| Expected Output | Code blocks with optional explanation |

## When to Use

- Scaffolding new functions, classes, or modules from specifications
- Generating API integrations from OpenAPI specs or documentation
- Prototyping algorithms with clear input/output contracts
- Creating test fixtures and unit tests alongside implementation

## When Not to Use

- Modifying large legacy codebases without providing sufficient context
- Security-critical crypto implementations without expert review
- Tasks where the spec is ambiguous — clarify requirements first

## System Prompt

```
You are a senior software engineer expert in {{language}}.
Framework/library: {{framework}}.

Rules:
- Write production-quality, idiomatic {{language}} code.
- Follow these constraints:
{{constraints}}
- Handle edge cases: null/empty inputs, boundary values, and error conditions.
- Do not use deprecated APIs or insecure patterns (eval, string-concat SQL, hardcoded secrets).
- Prefer clarity over cleverness. No unnecessary abstractions.
- If the task is ambiguous, state assumptions briefly before the code.
{{test_requirements}}

Output format:
{{output_format}}
```

## User Prompt

```
Task: {{task_description}}

Existing code (extend or modify, do not rewrite unrelated parts):
```
{{existing_code}}
```

Additional context:
{{additional_context}}

Acceptance criteria:
{{acceptance_criteria}}
```

## Variables

| Name | Required | Default | Description |
|------|----------|---------|-------------|
| `task_description` | Yes | — | What to build or change |
| `language` | Yes | — | Programming language: Python, TypeScript, Go, etc. |
| `framework` | No | none | Framework or library context |
| `constraints` | No | follow language best practices | Style, patterns, dependencies to use/avoid |
| `existing_code` | No | (none) | Code to extend; model should make minimal diffs |
| `test_requirements` | No | (none) | e.g., "Include pytest unit tests" |
| `output_format` | No | Code block(s) then brief usage notes | Structure of response |
| `additional_context` | No | (none) | API docs, types, environment details |
| `acceptance_criteria` | No | (none) | Testable conditions for correctness |

## Complete Example

### Input Variables

```yaml
task_description: "Write a function that validates email addresses and returns normalized lowercase form."
language: Python
framework: none
constraints: |
  - Use only stdlib (re module allowed)
  - Raise ValueError with descriptive message on invalid input
test_requirements: Include 3 pytest test cases covering valid, invalid, and edge cases.
acceptance_criteria: |
  - Returns lowercase trimmed email for valid input
  - Raises ValueError for missing @ or invalid format
```

### Expected Output

```python
def normalize_email(email: str) -> str:
    # validates and returns lowercase trimmed email; raises ValueError on invalid
    ...
```

Plus tests per `{{test_requirements}}`.

## Evaluation Criteria

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Correctness | 100% on spec | Unit tests pass |
| Constraint adherence | 100% | Lint, dependency, and style checks |
| Security | Zero critical issues | Static analysis (bandit, semgrep) |
| Idiomaticity | Human review | Matches language conventions |
| Test coverage | Per requirements | Coverage on generated functions |

## Tips and Pitfalls

- List `{{acceptance_criteria}}` as testable statements; include `{{existing_code}}` for edits.
- Specify allowed dependencies in `{{constraints}}`; run linter and tests before merge.
- Avoid underspecified tasks — the model will invent requirements.
