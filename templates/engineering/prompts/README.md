# Engineering Prompt Library

> Parameterized prompt templates for copy-paste use.

---

## Purpose

Extend the main [prompts/templates](../../prompts/templates/) library with agent, reflection, and report templates using `{{variable}}` placeholders.

---

## Templates

| File | Use case |
|------|----------|
| `chat.md` | Conversational assistant |
| `rag.md` | Citation-grounded QA |
| `planning.md` | Agent step planning |
| `reflection.md` | Self-critique loops |
| `report-generation.md` | Structured reports |

Load with [utilities/playbook_utils/prompts.py](../utilities/playbook_utils/prompts.py) or your own loader.

---

## Related

- [Prompt Templates Guide](../../domains/prompt-engineering/prompt-templates-guide.md)
- [Full prompt library](../../prompts/templates/README.md)
