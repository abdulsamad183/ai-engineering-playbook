# Documentation Style Guide

> Standards for every document in the AI Engineering Playbook.
> Read this before creating or editing any content.

---

## Purpose

This style guide ensures consistency, discoverability, and maintainability across a knowledge base designed to grow to 1000+ documents over many years. Every contributor — including future you — should be able to write a new document without guessing at conventions.

---

## Document Anatomy

Every document follows a predictable structure. Required sections vary by template (see [`meta/templates/`](templates/)), but all documents share these elements:

### 1. Front Matter (Required)

Every document begins with YAML front matter:

```yaml
---
title: "Human-Readable Title"
description: "One-sentence summary for indexes and search."
domain: llm-engineering          # Primary domain folder name
tags: [llm, inference, production]
status: draft                    # draft | review | published | deprecated
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../other-domain/some-doc.md
  - ../../meta/glossary.md#term
author: hp
---
```

| Field | Required | Description |
|-------|----------|-------------|
| `title` | Yes | Display title. Use title case. |
| `description` | Yes | ≤ 160 characters. Used in indexes and previews. |
| `domain` | Yes | Primary domain from `domains/`. |
| `tags` | Yes | 3–8 tags from the [tag registry](indexes/tags/tag-registry.md). |
| `status` | Yes | Document lifecycle state. |
| `created` | Yes | ISO 8601 date (`YYYY-MM-DD`). |
| `updated` | Yes | ISO 8601 date. Update on every substantive edit. |
| `version` | Yes | Semantic version of the document content. |
| `related` | Recommended | Relative paths to related documents. |
| `author` | Optional | Author identifier. |

### 2. Title and Overview

```markdown
# Document Title

> One-paragraph overview explaining what this document covers and who should read it.
```

The overview is mandatory. It answers: **What is this?** and **When do I need it?**

### 3. Table of Contents

Include a TOC for documents longer than ~300 lines. Use anchor links:

```markdown
## Table of Contents

- [Section One](#section-one)
- [Section Two](#section-two)
```

### 4. Body Sections

Use a logical heading hierarchy. Never skip levels (`#` → `###`).

| Level | Usage |
|-------|-------|
| `#` | Document title (once) |
| `##` | Major sections |
| `###` | Subsections |
| `####` | Detail blocks (use sparingly) |

### 5. Footer (Recommended)

```markdown
---

## See Also

- [Related Document](../path/to/doc.md)
- [Domain Index](../../domains/llm-engineering/README.md)

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial version |
```

---

## Naming Conventions

See [naming-conventions.md](naming-conventions.md) for full rules. Summary:

| Element | Convention | Example |
|---------|------------|---------|
| Files | `kebab-case.md` | `streaming-responses.md` |
| Folders | `kebab-case` | `vector-databases/` |
| Images | `{domain}-{topic}-{descriptor}.{ext}` | `rag-pipeline-overview.png` |
| Diagrams | `{type}-{subject}-{version}.mmd` | `sequence-agent-tool-call-v1.mmd` |
| Code examples | `example-{topic}.py` | `example-rag-retrieval.py` |

---

## Folder Conventions

### Domain Folders (`domains/`)

- One folder per knowledge domain.
- Each domain has a `README.md` index listing all documents in that domain.
- Documents live directly in the domain folder unless volume warrants subfolders (e.g., `databases/postgresql/`).
- Subfolders appear only when a domain exceeds ~20 documents.

### Knowledge Folders (`knowledge/`)

- Personal, experience-based content.
- Same front matter and style rules apply.
- Filename prefix with date for chronological entries: `2026-07-13-incident-description.md`.

### Example Folders (`examples/`)

- Organized by technology or pattern, not by domain.
- Each example is self-contained with its own `README.md`.
- Include a `requirements.txt` or equivalent when applicable.

---

## Markdown Conventions

### General Rules

1. **One sentence per line** in body text (improves diffs and reviews).
2. **80-character soft wrap** for prose; code blocks are exempt.
3. Use **reference-style links** for repeated URLs.
4. Prefer **relative links** for internal documents.
5. Use **fenced code blocks** with language identifiers.

### Code Blocks

Always specify the language:

````markdown
```python
from fastapi import FastAPI

app = FastAPI()
```
````

For shell commands:

````markdown
```bash
docker compose up -d
```
````

For output that is not executable:

````markdown
```text
Status: 200 OK
```
````

### Inline Code

Use backticks for: file names, commands, variable names, API endpoints, configuration keys.

```markdown
Set the `OPENAI_API_KEY` environment variable before running `uvicorn main:app`.
```

### Links

```markdown
<!-- Internal — always relative -->
See [RAG Overview](../rag/retrieval-augmented-generation.md).

<!-- External — descriptive text -->
Read the [FastAPI documentation](https://fastapi.tiangolo.com/) for details.

<!-- Anchor links within a document -->
Jump to [Production Checklist](#production-checklist).
```

### Tables

Use tables for structured comparisons. Always include a header row:

```markdown
| Feature | Option A | Option B |
|---------|----------|----------|
| Latency | Low | Medium |
| Cost | High | Low |
```

Align columns for readability in source (optional but preferred).

### Lists

- Use `-` for unordered lists.
- Use `1.` for ordered lists (auto-numbering).
- Nest with two-space indentation.
- Keep list items parallel in structure.

---

## Callout Blocks

Use blockquotes with a type prefix for callouts:

### Note

```markdown
> **Note:** This applies to OpenAI-compatible APIs as of July 2026.
```

### Tip

```markdown
> **Tip:** Cache embeddings at ingestion time to reduce query latency by 40–60%.
```

### Warning

```markdown
> **Warning:** Never log raw prompts containing PII in production environments.
```

### Important

```markdown
> **Important:** This pattern is deprecated as of v2.0. See [Migration Guide](migration.md).
```

### Example

```markdown
> **Example:** A typical RAG pipeline processes 500 documents in under 3 minutes
> using batch embedding with `text-embedding-3-small`.
```

### Production Standard

```markdown
> **Production Standard:** All LLM API calls must include request timeouts (≤ 30s)
> and retry logic with exponential backoff.
```

---

## Image Organization

Images live in `assets/images/` organized by domain:

```
assets/images/
├── llm-engineering/
├── rag/
├── agents/
└── deployment/
```

### Rules

1. Use descriptive file names: `{domain}-{topic}-{descriptor}.png`.
2. Prefer PNG for screenshots, SVG for icons and simple graphics.
3. Keep images under 500 KB when possible.
4. Always include alt text:

```markdown
![RAG pipeline architecture showing ingestion, embedding, and retrieval stages](../../assets/images/rag/rag-pipeline-overview.png)
```

5. Reference images with relative paths from the document location.

---

## Diagram Organization

Diagrams use Mermaid (inline or standalone `.mmd` files).
See [mermaid-conventions.md](mermaid-conventions.md) for full rules.

**Inline diagrams** — for simple, document-specific diagrams.
**Standalone `.mmd` files** — for complex or reusable diagrams in `assets/diagrams/`.

---

## Code Organization

### Examples Directory (`examples/`)

```
examples/
├── python/
│   ├── README.md
│   └── example-async-patterns.py
├── rag/
│   ├── README.md
│   ├── requirements.txt
│   └── basic-rag-pipeline/
│       ├── README.md
│       ├── main.py
│       └── config.py
```

### Rules

1. Every example directory has a `README.md` explaining purpose, prerequisites, and how to run.
2. Code must be runnable or clearly marked as pseudocode.
3. Pin dependency versions in `requirements.txt`.
4. Include comments only for non-obvious logic.
5. Follow the language's standard style (PEP 8 for Python).

### Code in Documents

- Keep code snippets short (< 40 lines). Link to full examples for longer code.
- Show imports. Do not use `...` to skip imports unless demonstrating a partial snippet.
- Include expected output when helpful.

---

## Versioning Strategy

### Document Versioning

Documents use semantic versioning in front matter:

| Change Type | Version Bump | Example |
|-------------|-------------|---------|
| Typo, formatting | Patch (`1.0` → `1.0.1`) | Fix broken link |
| New section, updated info | Minor (`1.0` → `1.1`) | Add new API endpoint |
| Restructure, major rewrite | Major (`1.0` → `2.0`) | Complete redesign |

### Deprecation

When deprecating a document:

1. Set `status: deprecated` in front matter.
2. Add a warning callout at the top pointing to the replacement.
3. Keep the document accessible for 6+ months before removal.

---

## Cross-Referencing Strategy

### Link Types

| Type | Syntax | When to Use |
|------|--------|-------------|
| Related docs | `related:` in front matter | Documents covering adjacent topics |
| Inline links | `[text](../path/doc.md)` | Contextual references in body |
| See Also | Footer section | Additional reading |
| Glossary | `[term](../glossary.md#term)` | First use of domain-specific terms |
| Index | Domain `README.md` | Navigation within a domain |

### Rules

1. Every document links to at least one related document.
2. Link to the glossary on first use of specialized terms.
3. Avoid orphan documents — if nothing links to a doc, add it to the appropriate index.
4. Use bidirectional linking: if A links to B, B should link to A (in `related` or See Also).

---

## Production Documentation Standards

Documents describing production systems or practices must include:

1. **Prerequisites** — what the reader needs before applying this knowledge.
2. **Production checklist** — actionable items before going live.
3. **Monitoring guidance** — what to watch after deployment.
4. **Failure modes** — what can go wrong and how to detect it.
5. **Cost implications** — when the approach affects infrastructure spend.

Use the [Production Guide template](templates/production-guide.md) for these documents.

---

## Review Checklist

Before marking a document as `published`:

- [ ] Front matter is complete and valid
- [ ] Overview paragraph answers "what" and "who"
- [ ] Tags are from the tag registry
- [ ] Code examples are tested or marked as pseudocode
- [ ] Images have alt text and live in `assets/`
- [ ] Internal links resolve correctly
- [ ] Related documents are linked bidirectionally
- [ ] Document is listed in the domain `README.md`
- [ ] Document is added to relevant indexes
- [ ] Changelog footer is updated

---

## See Also

- [Naming Conventions](naming-conventions.md)
- [Indexing Strategy](indexing-strategy.md)
- [Mermaid Conventions](mermaid-conventions.md)
- [Document Templates](templates/)
- [Glossary](glossary.md)
