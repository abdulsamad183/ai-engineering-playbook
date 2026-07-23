# Prompt Library

> Reusable prompt patterns for common AI engineering tasks.

---

## Organization

```
prompts/
├── templates/         # 16 production templates
│   ├── question-answering.md
│   ├── classification.md
│   ├── agent-planning.md
│   └── ...
├── patterns/          # Pattern catalog (see domain docs)
└── README.md
```

Prompt patterns follow the [Prompt Pattern template](../meta/templates/prompt-pattern.md).

---

## Prompt Pattern Standards

Each prompt pattern includes:

- **When to use** — scenarios where this pattern applies
- **Template** — system and user prompt templates with placeholders
- **Complete example** — filled-in example with expected output
- **Variations** — alternative approaches
- **Model compatibility** — which models work best
- **Evaluation criteria** — how to measure effectiveness

---

## Adding a Prompt Pattern

1. Copy [prompt-pattern.md](../meta/templates/prompt-pattern.md) to `patterns/`.
2. Name with kebab-case: `{use-case}-prompt.md`.
3. Test the prompt with at least two models.
4. Document evaluation results.
5. Link from [prompt-engineering](../domains/prompt-engineering/) domain.

---

## See Also

- [Prompt Engineering Domain](../domains/prompt-engineering/)
- [Context Engineering Domain](../domains/context-engineering/)
- [Prompt Pattern Template](../meta/templates/prompt-pattern.md)
