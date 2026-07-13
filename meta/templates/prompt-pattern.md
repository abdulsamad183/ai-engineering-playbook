---
title: "{Pattern Name} Prompt Pattern"
description: "Reusable prompt pattern for {use case description}."
domain: prompt-engineering
tags: [prompt, prompt-pattern, {tag1}]
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
version: "1.0"
related: []
keywords: []
---

# {Pattern Name} Prompt Pattern

> When and how to use this prompt pattern for {use case}.

## Pattern Overview

| Attribute | Value |
|-----------|-------|
| Use Case | |
| Best Models | gpt-4o, claude-sonnet-4, etc. |
| Complexity | Simple / Moderate / Complex |
| Token Budget | ~X tokens (system + user) |
| Expected Output | Structured / Free-form / JSON |

## When to Use

- Scenario 1
- Scenario 2

## When Not to Use

- Anti-scenario 1
- Anti-scenario 2

## Pattern Structure

```
[Role/Persona]
{role definition}

[Context]
{background information}

[Task]
{specific instruction}

[Constraints]
{rules and limitations}

[Output Format]
{expected structure}

[Examples] (optional)
{few-shot examples}
```

## Template

### System Prompt

```
You are a {role}. Your task is to {primary task}.

Rules:
- Rule 1
- Rule 2
- Rule 3

Output format:
{format specification}
```

### User Prompt

```
{Context about the specific request}

Task: {specific task for this invocation}

Input:
{variable input data}
```

## Complete Example

### Input

```
{example input data}
```

### Prompt

```
System: You are an expert code reviewer. Analyze the provided code for bugs,
security issues, and performance problems. Return findings as a JSON array.

User: Review the following Python function:

def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return db.execute(query)
```

### Expected Output

```json
[
  {
    "severity": "critical",
    "category": "security",
    "issue": "SQL injection vulnerability",
    "suggestion": "Use parameterized queries"
  }
]
```

## Variations

### Variation A: {Name}

When to use this variation and how it differs.

### Variation B: With Few-Shot Examples

```
System: {system prompt}

User: Example 1:
Input: {example input}
Output: {example output}

Example 2:
Input: {example input}
Output: {example output}

Now process:
Input: {actual input}
```

## Tips for Best Results

> **Tip:** Specific tips for getting the best output from this pattern.

- Tip 1
- Tip 2
- Tip 3

## Common Pitfalls

- Pitfall 1 — how to avoid
- Pitfall 2 — how to avoid

## Evaluation

How to measure if this prompt pattern is working:

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Accuracy | > 90% | Manual review sample |
| Format compliance | 100% | Schema validation |
| Latency | < 2s | API response time |

## Model Compatibility

| Model | Works Well | Notes |
|-------|-----------|-------|
| gpt-4o | Yes | Best format compliance |
| gpt-4o-mini | Partial | May need simpler format |
| claude-sonnet-4 | Yes | Strong instruction following |

---

## See Also

- [Prompt Engineering Guide](../../domains/prompt-engineering/)
- [Prompt Library](../../prompts/)
- [Context Engineering](../../domains/context-engineering/)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | YYYY-MM-DD | Initial version |
