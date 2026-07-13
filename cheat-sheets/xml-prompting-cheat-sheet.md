# XML Prompting Cheat Sheet

> Quick reference for XML-structured prompts. See [Structured Prompting](../domains/prompt-engineering/structured-prompting.md).

## When to Use XML

- Claude and models trained on XML-heavy corpora
- Clear hierarchy: role → rules → context → task
- Parsing specific sections from responses

## Basic Structure

```xml
<role>Senior data analyst</role>

<rules>
  <rule>Answer only from provided data</rule>
  <rule>Output JSON inside <answer> tags</rule>
</rules>

<context>
  <document id="1">...</document>
</context>

<task>
  Summarize revenue trends for Q3.
</task>
```

## Response Parsing

```python
import xml.etree.ElementTree as ET

def parse_answer(xml_text: str) -> str:
    root = ET.fromstring(f"<root>{xml_text}</root>")
    el = root.find("answer")
    return el.text.strip() if el is not None and el.text else ""
```

## XML vs Other Formats

| Aspect | XML | JSON | Markdown |
|--------|-----|------|----------|
| Hierarchy | Strong | Strong | Weak |
| Human readability | Medium | Medium | High |
| Model preference | Claude++ | API tools | General |
| Parsing rigor | High | High | Low |

## Best Practices

- Consistent tag names across prompts (`<context>`, not `<ctx>` in one place)
- Nest related content; avoid flat tag soup
- Close all tags; malformed XML breaks parsers
- Request output in matching XML structure for symmetric parsing

## Anti-Patterns

- Over-nesting (>4 levels) without benefit
- Using XML for simple single-field extraction (use JSON)
- Tags that resemble HTML the model might render

## See Also

- [JSON Prompting Cheat Sheet](json-prompting-cheat-sheet.md)
- [Prompt Delimiters Cheat Sheet](prompt-delimiters-cheat-sheet.md)
