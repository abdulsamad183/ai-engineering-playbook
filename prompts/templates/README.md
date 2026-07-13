# Prompt Templates

> Reusable prompt templates for common AI engineering tasks. Each template follows the [prompt pattern structure](../../meta/templates/prompt-pattern.md) with YAML front matter, system/user prompt blocks, variables, examples, and evaluation criteria.

---

## Template Library

| Template | File | Primary Output | Use Case |
|----------|------|----------------|----------|
| Question Answering | [`question-answering.md`](question-answering.md) | Markdown with citations | Grounded Q&A over provided context |
| Summarization | [`summarization.md`](summarization.md) | Condensed text | Document compression for target audiences |
| Classification | [`classification.md`](classification.md) | JSON label + confidence | Intent routing, triage, labeling |
| Extraction | [`extraction.md`](extraction.md) | Structured JSON | Pull fields from unstructured text |
| Translation | [`translation.md`](translation.md) | Translated text | Localization with glossary support |
| Code Generation | [`code-generation.md`](code-generation.md) | Source code | Feature implementation, scaffolding |
| Code Review | [`code-review.md`](code-review.md) | JSON findings | PR review, security and quality checks |
| Documentation | [`documentation.md`](documentation.md) | Markdown | API docs, README, runbooks |
| Brainstorming | [`brainstorming.md`](brainstorming.md) | Structured ideas | Product discovery, ideation |
| Email Generation | [`email-generation.md`](email-generation.md) | Email draft | Support, outreach, follow-ups |
| SQL Generation | [`sql-generation.md`](sql-generation.md) | SQL query | Natural language to SQL |
| JSON Generation | [`json-generation.md`](json-generation.md) | Validated JSON | Schema-constrained structured output |
| Markdown Generation | [`markdown-generation.md`](markdown-generation.md) | Formatted Markdown | Reports, structured documents |
| Agent Planning | [`agent-planning.md`](agent-planning.md) | JSON plan | Multi-step task decomposition with tools |
| Evaluation Judge | [`evaluation-judge.md`](evaluation-judge.md) | JSON scores | LLM-as-judge quality evaluation |
| RAG Query | [`rag-query.md`](rag-query.md) | Grounded answer | Retrieval-augmented answer synthesis |

---

## Organization

```
prompts/templates/
├── question-answering.md
├── summarization.md
├── classification.md
├── extraction.md
├── translation.md
├── code-generation.md
├── code-review.md
├── sql-generation.md
├── json-generation.md
├── agent-planning.md
├── evaluation-judge.md
├── rag-query.md
├── documentation.md
├── brainstorming.md
├── email-generation.md
├── markdown-generation.md
└── README.md
```

Templates are versioned assets. Store production prompts here — not inline in application code.

---

## Template Standards

Each template file includes:

| Section | Purpose |
|---------|---------|
| **YAML front matter** | ID, version, models, variables, token budget |
| **Pattern overview** | Use case, complexity, expected output |
| **When to use / not to use** | Applicability guidance |
| **System prompt** | Role, constraints, output format with `{{variables}}` |
| **User prompt** | Task instruction with `{{placeholders}}` |
| **Variables** | Required and optional input fields |
| **Complete example** | Filled invocation with expected output |
| **Evaluation criteria** | Metrics, targets, measurement methods |

---

## Variable Injection

Templates use `{{variable}}` placeholders. Render at runtime:

```python
from pathlib import Path
import re

PROMPT_DIR = Path("prompts/templates")


def render_template(name: str, variables: dict[str, str]) -> tuple[str, str]:
    """Load a template and substitute {{variables}}."""
    content = (PROMPT_DIR / f"{name}.md").read_text()
    # Extract system and user blocks from markdown code fences
    # (or split into .system.txt / .user.txt sidecars for production)
    def substitute(text: str) -> str:
        for key, value in variables.items():
            text = text.replace(f"{{{{{key}}}}}", value)
        return text
    return substitute(system_block), substitute(user_block)
```

Validate required variables before rendering. Use provider JSON mode for templates with structured output.

---

## Adding a Template

1. Copy the structure from [`meta/templates/prompt-pattern.md`](../../meta/templates/prompt-pattern.md).
2. Name with kebab-case: `{use-case}.md`.
3. Keep templates between 80–150 lines.
4. Test with at least two models before marking `status: published`.
5. Add an entry to this README and link from the [Prompt Templates Guide](../../domains/prompt-engineering/prompt-templates-guide.md).

---

## See Also

- [Prompt Templates Guide](../../domains/prompt-engineering/prompt-templates-guide.md)
- [Prompt Patterns](../../domains/prompt-engineering/prompt-patterns.md)
- [Prompt Pattern Template](../../meta/templates/prompt-pattern.md)
