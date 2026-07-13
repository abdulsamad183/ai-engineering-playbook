# JSON Prompting Cheat Sheet

> Quick reference for schema-based JSON prompts. See [Structured Prompting](../domains/prompt-engineering/structured-prompting.md).

## JSON Prompt Stack

```
System: role + rules + embedded JSON Schema
User:   task + variable data (not in schema)
API:    response_format / tool_choice
Code:   parse → validate → retry
```

## Minimal Schema in Prompt

```json
{
  "type": "object",
  "required": ["label", "confidence"],
  "properties": {
    "label": { "type": "string", "enum": ["billing", "technical", "other"] },
    "confidence": { "type": "number", "minimum": 0, "maximum": 1 },
    "rationale": { "type": "string", "maxLength": 200 }
  },
  "additionalProperties": false
}
```

## Python Validation

```python
from pydantic import BaseModel, Field

class ClassificationResult(BaseModel):
    label: str
    confidence: float = Field(ge=0, le=1)
    rationale: str = Field(max_length=200)
```

## Provider Integration

| Provider | Structured output |
|----------|-------------------|
| OpenAI | `response_format: {"type": "json_schema", ...}` |
| Anthropic | Tool use with `input_schema` |
| Generic | Schema in system + `json.loads` + retry |

## Retry on Parse Failure

```python
messages.append({"role": "assistant", "content": raw})
messages.append({
    "role": "user",
    "content": f"Invalid JSON: {error}. Return only valid JSON per schema.",
})
```

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Markdown fences in output | "No ```json fences" in system |
| Extra commentary | "Output ONLY the JSON object" |
| Schema drift | Version schema with prompt ID |
| Optional fields omitted | Mark required explicitly |

## See Also

- [Output Constraints Cheat Sheet](prompt-output-constraints-cheat-sheet.md)
- [JSON Generation Template](../prompts/templates/json-generation.md)
