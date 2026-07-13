# Prompt Debugging Checklist

> When prompts behave unexpectedly. See [Prompt Engineering Mistakes](../domains/prompt-engineering/prompt-engineering-mistakes.md).

## Symptom → Check

| Symptom | First Checks |
|---------|-------------|
| Wrong format | Output format in system? `response_format` set? Parser handles edge cases? |
| Ignores instructions | Conflicting instructions? User message overriding system? |
| Hallucinations | Missing context? "Only use provided docs" constraint? |
| Inconsistent outputs | Temperature > 0 on deterministic task? Vague constraints? |
| Too verbose | Max tokens? "Be concise" constraint? Output format limits fields? |
| Too expensive | System prompt bloat? Redundant examples? Cacheable prefix? |
| Works in playground, fails in prod | Different model? Different temperature? Missing system message? |

## Debug Workflow

1. **Isolate** — test system and user messages separately
2. **Minimize** — remove components until failure disappears (binary search)
3. **Log** — request ID, model, token counts (not raw prompts with PII)
4. **Compare** — diff prompt versions side by side
5. **Replay** — same input against old and new prompt version

## Ablation Order

Remove one at a time: examples → context → constraints → role → instructions

## See Also

- [Prompt Optimization](../domains/prompt-engineering/prompt-optimization.md)
- [Prompt Versioning](../domains/prompt-engineering/prompt-versioning.md)
