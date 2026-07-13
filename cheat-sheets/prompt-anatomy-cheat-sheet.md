# Prompt Anatomy Cheat Sheet

> Quick reference for prompt components. See [Prompt Anatomy](../domains/prompt-engineering/prompt-anatomy.md).

## Components (in typical order)

| Component | Purpose | Example |
|-----------|---------|---------|
| **Role** | Who the model acts as | "You are a senior code reviewer" |
| **Goal** | What to accomplish | "Identify security vulnerabilities" |
| **Instructions** | How to behave | "Be concise. Cite line numbers." |
| **Context** | Background data | Retrieved docs, user profile |
| **Constraints** | Boundaries | "Max 200 words. No PII in output." |
| **Input** | User's request | The actual task data |
| **Output format** | Response shape | JSON schema, markdown structure |
| **Examples** | Few-shot demos | Input/output pairs |

## Layered Architecture

```
System message  → Role + persistent rules + output format
User message    → Context + input + task-specific instructions
Assistant       → Prior turns (conversation history)
Tool message    → Execution results (agents)
```

## Rules

- Put **stable** rules in system; put **variable** data in user.
- One primary goal per prompt.
- Output format in system, validated in code.

## See Also

- [Message Types](../domains/prompt-engineering/message-types.md)
- [Prompt Design Principles](../domains/prompt-engineering/prompt-design-principles.md)
