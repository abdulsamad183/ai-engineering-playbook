# Structured Prompting Cheat Sheet

> XML vs JSON vs Markdown vs tags. See [Structured Prompting](../domains/prompt-engineering/structured-prompting.md).

## When to Use

| Style | Best For |
|-------|----------|
| **XML** | Complex hierarchy, nested context, RAG documents |
| **JSON** | Schema contracts, API integration, tool args |
| **Markdown** | Human-readable instructions, docs generation |
| **Tags** | Simple section separation (`###`, `---`, `[INST]`) |

## XML Template

```xml
<task>
  <role>...</role>
  <context>...</context>
  <instructions>...</instructions>
  <input>...</input>
</task>
```

## JSON Contract

```json
{"category": "string", "confidence": 0.0-1.0, "rationale": "string"}
```

Use provider `response_format` + Pydantic validation in code.

## Delimiters

| Delimiter | Use |
|-----------|-----|
| `"""` or `---` | Section breaks |
| `<document>` | Injected context |
| `###` | Markdown sections |

## See Also

- [Structured Outputs (LLM)](../domains/llm-engineering/structured-outputs.md)
- [example-structured-xml-prompt.py](../examples/prompt-engineering/example-structured-xml-prompt.py)
