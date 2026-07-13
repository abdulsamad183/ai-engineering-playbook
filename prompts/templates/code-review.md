---
title: "Code Review Prompt Template"
description: "Reusable prompt for structured code review covering bugs, security, performance, and maintainability."
domain: prompt-engineering
tags: [prompt, code-review, security, quality]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
id: code-review-v1
task: code-review
models:
  recommended: [gpt-4o, claude-sonnet-4]
  min_capability: advanced
token_budget:
  system: 400
  user_per_file: 300
variables:
  required: [code, language]
  optional: [review_focus, project_context, severity_levels, output_format]
output:
  format: json
  schema: review_findings
related:
  - code-generation.md
  - evaluation-judge.md
  - ../../domains/prompt-engineering/prompt-templates-guide.md
keywords: [code review, static analysis, security audit, PR review]
---

# Code Review Prompt Template

> Analyze code for defects, security vulnerabilities, and maintainability issues. Return prioritized findings with actionable fixes.

## Pattern Overview

| Attribute | Value |
|-----------|-------|
| Use Case | PR review automation, pre-commit checks, security scanning, onboarding feedback |
| Best Models | gpt-4o, claude-sonnet-4 |
| Complexity | Moderate to Complex |
| Token Budget | ~600–1500 tokens (system + user) |
| Expected Output | JSON array of findings |

## When to Use

- Automated first-pass review on pull requests
- Security-focused audits before release
- Teaching code quality with structured feedback
- Supplementing human reviewers on large diffs

## When Not to Use

- Final approval gate without human review
- Reviewing code without sufficient context (architecture, threat model)
- Binary or generated artifacts not meant for human reading

## System Prompt

```
You are a senior code reviewer specializing in {{language}}.

Review the provided code for:
{{review_focus}}

Project context:
{{project_context}}

Severity levels (use exactly these):
{{severity_levels}}

Rules:
- Report only genuine issues — no style nitpicks unless they affect correctness or security.
- Cite specific line numbers or code snippets for each finding.
- Provide a concrete fix suggestion for every issue.
- If no issues found, return an empty findings array with a brief positive summary.
- Do not rewrite the entire file; suggest minimal targeted fixes.

Output format (valid JSON only):
{{output_format}}
```

## User Prompt

```
Review this {{language}} code:

```
{{code}}
```

Change description (if PR): {{change_description}}
Files changed: {{files_changed}}
```

## Variables

| Name | Required | Default | Description |
|------|----------|---------|-------------|
| `code` | Yes | — | Source code or diff to review |
| `language` | Yes | — | Programming language |
| `review_focus` | No | bugs, security, performance, maintainability | Areas to prioritize |
| `project_context` | No | (none) | Architecture, frameworks, threat model |
| `severity_levels` | No | critical, high, medium, low, info | Allowed severity values |
| `output_format` | No | see below | JSON schema for findings |
| `change_description` | No | (none) | PR description for context |
| `files_changed` | No | (none) | List of files in the change set |

Default `output_format`: `{"summary": "...", "findings": [{"severity": "...", "category": "...", "location": "...", "issue": "...", "suggestion": "..."}]}`

## Complete Example

### Input

```yaml
language: Python
code: "def get_user(user_id): return db.execute(f'SELECT * FROM users WHERE id = {user_id}')"
```

### Expected Output

```json
{"summary": "Critical SQL injection.", "findings": [{"severity": "critical", "category": "security", "issue": "SQL injection via f-string", "suggestion": "Use parameterized queries"}]}
```

## Evaluation Criteria

| Metric | Target | How to Measure |
|--------|--------|----------------|
| True positive rate | > 80% | Human validates findings on sample PRs |
| False positive rate | < 15% | Noise ratio on clean code samples |
| Critical recall | > 95% | Known vulnerabilities detected in golden set |
| Format compliance | 100% | JSON schema validation |
| Actionability | > 4/5 | Reviewers rate fix suggestions as useful |

## Tips and Pitfalls

- Provide `{{project_context}}` and review diffs, not entire files.
- Combine with static analyzers; filter CI output to critical/high only.
- Treat output as assistant feedback, not merge approval.
