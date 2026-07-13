# Prompt Patterns Cheat Sheet

> When to use each pattern. See [Prompt Patterns](../domains/prompt-engineering/prompt-patterns.md).

| Pattern | Use When | Avoid When |
|---------|----------|------------|
| **Role** | Need consistent persona | Task is purely mechanical |
| **Persona** | Tone/voice matters | Adds tokens without value |
| **Goal** | Clarify objective | Goal is obvious |
| **Instruction** | Step-by-step tasks | Over-constraining creative tasks |
| **Delimiter** | Separate sections in long prompts | Simple short prompts |
| **Constraint** | Hard boundaries (format, length) | Too many constraints conflict |
| **Style** | Brand voice, audience level | Factual extraction |
| **Output format** | Structured responses | Free-form chat |
| **Step-by-step** | Complex multi-step reasoning | Simple lookups |
| **Expert** | Domain-specific depth | General knowledge tasks |
| **Multi-role** | Debate, review from angles | Single clear answer needed |

## Quick Combos

| Task | Stack |
|------|-------|
| Code review | Role + Constraint + Output format (JSON) |
| RAG Q&A | Role + Delimiter + Constraint ("cite sources") |
| Classification | Instruction + Output format + Few-shot |
| Agent planning | Goal + Step-by-step + Tool definitions |

## See Also

- [Templates](../prompts/templates/)
- [Structured Prompting](../domains/prompt-engineering/structured-prompting.md)
