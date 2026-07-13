# Prompt Output Constraints Cheat Sheet

> Quick reference for constraining LLM output shape. See [Prompt Anatomy](../domains/prompt-engineering/prompt-anatomy.md) and [Structured Prompting](../domains/prompt-engineering/structured-prompting.md).

## Constraint Layers

| Layer | Where | Example |
|-------|-------|---------|
| **Natural language** | System prompt | "Return only valid JSON" |
| **Schema** | System + API | JSON Schema, Pydantic model |
| **API mode** | Provider | `response_format: json_object` |
| **Parser** | Application | `json.loads`, regex, XML parser |
| **Validator** | Post-process | Pydantic, jsonschema, retry loop |

## Common Output Formats

| Format | Best For | Validate With |
|--------|----------|---------------|
| JSON | APIs, agents, pipelines | jsonschema, Pydantic |
| XML | Hierarchical prompts, parsing | lxml, ElementTree |
| Markdown | Human-readable docs | markdownlint |
| Plain enum | Classification | Allowlist check |
| Tool calls | Function calling | Provider tool schema |

## JSON Contract Template

```
Output ONLY valid JSON matching this schema. No markdown fences. No preamble.

{
  "field": "string",
  "confidence": 0.0-1.0,
  "items": ["string"]
}
```

## Retry Pattern

```
1. Call LLM with schema in system prompt
2. Parse response
3. On failure: append error + schema to messages, retry (max 2)
4. On final failure: return structured error to caller
```

## Sampling for Structured Output

| Goal | temperature | top_p |
|------|-------------|-------|
| Strict JSON | 0.0–0.2 | 1.0 |
| Classification | 0.0 | 1.0 |
| Creative + structure | 0.3–0.5 | 0.9 |

See [LLM Sampling Parameters](llm-sampling-parameters.md).

## Anti-Patterns

- "Be creative" + strict JSON — conflicting instructions
- Schema only in user message — put in system for stability
- Parsing without validation — always validate before use

## See Also

- [JSON Prompting Cheat Sheet](json-prompting-cheat-sheet.md)
- [Structured Prompting Cheat Sheet](structured-prompting-cheat-sheet.md)
