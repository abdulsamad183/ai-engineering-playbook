# Contributing to the AI Engineering Playbook

> How to add, update, and maintain content in this knowledge base.

---

## Principles

1. **Quality over quantity** — one excellent document beats five mediocre ones.
2. **Follow the standards** — consistency is what makes this scalable.
3. **Link generously** — every document should connect to related content.
4. **Write for production** — include operational guidance, not just theory.
5. **Update indexes** — undocumented content is undiscoverable content.

---

## Adding a New Document

### Step 1: Choose a Domain

Browse [domains/](domains/README.md) and find the best-fit domain for your topic. If no domain fits, propose a new one (see [Adding a New Domain](#adding-a-new-domain)).

### Step 2: Select a Template

Copy the appropriate template from [meta/templates/](meta/templates/):

| Content Type | Template |
|-------------|----------|
| Concept or mental model | `concept.md` |
| Technology (DB, library) | `technology.md` |
| AI service or tool | `ai-tool.md` |
| Design pattern | `architecture-pattern.md` |
| Research paper summary | `research-paper.md` |
| API reference | `api.md` |
| Framework guide | `framework.md` |
| System design | `ai-system-design.md` |
| Production practices | `production-guide.md` |
| Deployment instructions | `deployment-guide.md` |
| Hands-on tutorial | `tutorial.md` |
| Project case study | `project.md` |
| Incident review | `postmortem.md` |
| Interview prep | `interview-topic.md` |
| Quick reference | `cheat-sheet.md` |
| Diagnostic guide | `troubleshooting-guide.md` |
| Prompt template | `prompt-pattern.md` |
| Agent workflow | `agent-workflow.md` |

### Step 3: Name the File

Follow [naming conventions](meta/naming-conventions.md):

- Documents: `kebab-case.md`
- Knowledge entries: `YYYY-MM-DD-description.md`
- No version numbers or dates in domain document names

### Step 4: Write Content

Follow the [style guide](meta/style-guide.md):

- Complete all front matter fields
- Write the overview paragraph
- Use callout blocks (Note, Tip, Warning, Production Standard)
- Include code examples with language identifiers
- Add Mermaid diagrams where they clarify architecture or flow
- Link to glossary terms on first use

### Step 5: Update Indexes

Before marking as `published`:

1. Add entry to the domain `README.md`
2. Add entry to [meta/indexes/MASTER-INDEX.md](meta/indexes/MASTER-INDEX.md)
3. Register new tags in [tag registry](meta/indexes/tags/tag-registry.md)
4. Add keywords to [keyword index](meta/indexes/keyword-index.md)
5. Add to relevant topic, technology, or pattern indexes
6. Add bidirectional links in related documents

### Step 6: Review

Complete the [review checklist](meta/style-guide.md#review-checklist) before setting `status: published`.

---

## Adding Personal Knowledge

Personal knowledge goes in `knowledge/` — lessons learned, mistakes, experiments, ADRs, benchmarks, and production experiences.

### Naming

```
knowledge/{category}/YYYY-MM-DD-{description}.md
```

### Categories

| Folder | Content |
|--------|---------|
| `lessons-learned/` | Insights from building AI systems |
| `mistakes/` | Errors made and how to avoid them |
| `experiments/` | Technical experiments and results |
| `retrospectives/` | Project retrospectives |
| `debugging-stories/` | How specific bugs were found and fixed |
| `architecture-decisions/` | ADRs (Architecture Decision Records) |
| `tradeoffs/` | Design tradeoff analyses |
| `benchmarks/` | Performance benchmark results |
| `deployments/` | Deployment experiences |
| `production-challenges/` | Production issues and resolutions |

### ADR Format

Architecture Decision Records use sequential numbering:

```
knowledge/architecture-decisions/ADR-001-vector-store-selection.md
```

---

## Adding Code Examples

Examples go in `examples/{technology}/`:

1. Create or use an existing technology folder.
2. Add a `README.md` explaining the example.
3. Include `requirements.txt` with pinned versions.
4. Ensure code is runnable or clearly marked as pseudocode.
5. Link from relevant domain documents.

---

## Adding a New Domain

Create a new domain only when an entirely new area of AI engineering knowledge emerges:

1. Create `domains/{domain-name}/README.md` using the domain README template.
2. Add the domain to [domains/README.md](domains/README.md).
3. Add the domain to [MASTER-INDEX.md](meta/indexes/MASTER-INDEX.md).
4. Add relevant tags to the [tag registry](meta/indexes/tags/tag-registry.md).
5. Update the [roadmap](meta/roadmap.md) if the domain represents a new learning capability.

Do **not** create domains for specific technologies — use technology tags and indexes instead.

---

## Adding a New Tag

1. Check the [tag registry](meta/indexes/tags/tag-registry.md) for existing tags.
2. If none exists, add it with a clear definition.
3. Include the tag addition in your commit.

---

## Document Status Lifecycle

```
draft → review → published → deprecated → removed
```

| Status | When to Use |
|--------|------------|
| `draft` | Work in progress |
| `review` | Content complete, needs review |
| `published` | Indexed and discoverable |
| `deprecated` | Superseded by another document |

---

## Commit Messages

Use conventional commit format:

```
docs(domain): add document title

docs(rag): add hybrid search guide
docs(meta): update tag registry with new tags
fix(links): correct broken cross-references in llm-engineering
```

---

## Questions

- **Where does X content go?** Check [domains/README.md](domains/README.md) and the [architecture overview](meta/architecture-overview.md).
- **Which template do I use?** See the [template selection guide](meta/templates/README.md).
- **How do I name files?** See [naming conventions](meta/naming-conventions.md).
- **What tags are available?** See [tag registry](meta/indexes/tags/tag-registry.md).

---

## See Also

- [Style Guide](meta/style-guide.md)
- [Architecture Overview](meta/architecture-overview.md)
- [Templates](meta/templates/)
