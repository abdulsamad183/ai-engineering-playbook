# Personal Knowledge Base

> Lessons learned, mistakes, experiments, and production experiences.
> This is one of the most valuable parts of the playbook over time.

---

## Purpose

The `knowledge/` directory captures **experience-based knowledge** that reference documentation cannot provide — the judgment, tradeoffs, and hard-won lessons from building real AI systems.

Unlike `domains/` (curated reference content), knowledge entries are:

- **Personal** — based on direct experience
- **Chronological** — dated for context
- **Honest** — including failures and mistakes
- **Increasingly valuable** — compound in worth over years

---

## Categories

| Category | What to Document | Naming |
|----------|-----------------|--------|
| [lessons-learned](lessons-learned/) | Insights from building AI systems | `YYYY-MM-DD-topic.md` |
| [mistakes](mistakes/) | Errors made and how to avoid them | `YYYY-MM-DD-topic.md` |
| [experiments](experiments/) | Technical experiments and results | `YYYY-MM-DD-topic.md` |
| [retrospectives](retrospectives/) | Project retrospectives | `YYYY-MM-DD-project-name.md` |
| [debugging-stories](debugging-stories/) | How specific bugs were found and fixed | `YYYY-MM-DD-topic.md` |
| [architecture-decisions](architecture-decisions/) | ADRs (Architecture Decision Records) | `ADR-NNN-title.md` |
| [tradeoffs](tradeoffs/) | Design tradeoff analyses | `YYYY-MM-DD-topic.md` |
| [benchmarks](benchmarks/) | Performance benchmark results | `YYYY-MM-DD-topic.md` |
| [deployments](deployments/) | Deployment experiences | `YYYY-MM-DD-topic.md` |
| [production-challenges](production-challenges/) | Production issues and resolutions | `YYYY-MM-DD-topic.md` |

---

## Writing Knowledge Entries

1. Use the same front matter as domain documents (see [style guide](../meta/style-guide.md)).
2. Include the date in the filename for chronological sorting.
3. Be specific — include numbers, timelines, and concrete outcomes.
4. Link to related domain documents and projects.
5. For ADRs, use sequential numbering: `ADR-001`, `ADR-002`, etc.

### What Makes a Good Entry

- **Specific:** "RAG chunk size of 512 tokens gave 23% better recall than 256" not "chunk size matters"
- **Actionable:** What would you do differently? What should others do?
- **Honest:** Document failures, not just successes
- **Linked:** Connect to domain docs, projects, and other knowledge entries

---

## Architecture Decision Records (ADRs)

ADRs document significant architectural decisions:

```
knowledge/architecture-decisions/ADR-001-vector-store-selection.md
knowledge/architecture-decisions/ADR-002-agent-framework-choice.md
```

Each ADR should capture:
- **Context** — what situation prompted the decision
- **Options** — what alternatives were considered
- **Decision** — what was chosen and why
- **Consequences** — tradeoffs accepted

---

## See Also

- [Domains](../domains/) — reference documentation
- [Projects](../projects/) — project case studies
- [Contributing Guide](../CONTRIBUTING.md#adding-personal-knowledge)
