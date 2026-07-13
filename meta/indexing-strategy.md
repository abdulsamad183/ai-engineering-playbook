# Indexing Strategy

> How documents are discovered, organized, and cross-linked across the AI Engineering Playbook.

---

## Overview

As this repository grows to hundreds and then thousands of documents, structured indexing prevents content from becoming a needle-in-a-haystack problem. The indexing system uses multiple complementary strategies so documents can be found by topic, technology, pattern, tag, or keyword.

---

## Index Types

### 1. Master Index

**Location:** `meta/indexes/MASTER-INDEX.md`

The single entry point for all repository content. Organized by domain with links to every published document. Updated whenever a new document is published.

Structure:

```markdown
## Domain Name
- [Document Title](path/to/doc.md) — one-line description
```

### 2. Domain Indexes

**Location:** `domains/{domain}/README.md`

Each domain folder maintains its own index in its `README.md`. This is the primary navigation surface within a domain.

### 3. Topic Indexes

**Location:** `meta/indexes/topics/`

Cross-cutting topic collections that span multiple domains:

```
meta/indexes/topics/
├── README.md
├── streaming.md              # All docs about streaming
├── cost-optimization.md      # All docs about cost
├── security.md               # Security across all domains
└── testing.md                # Testing strategies
```

Topic indexes are created when a theme appears in 3+ domains.

### 4. Tag Registry

**Location:** `meta/indexes/tags/tag-registry.md`

Canonical list of all approved tags. Documents must use tags from this registry. New tags are proposed via pull request.

### 5. Technology Index

**Location:** `meta/indexes/technologies/`

Maps technologies to relevant documents across domains:

```
meta/indexes/technologies/
├── README.md
├── fastapi.md
├── postgresql.md
├── langgraph.md
└── openai.md
```

### 6. Architecture Pattern Index

**Location:** `meta/indexes/patterns/`

Catalog of architecture and design patterns:

```
meta/indexes/patterns/
├── README.md
├── rag-patterns.md
├── agent-patterns.md
├── api-patterns.md
└── deployment-patterns.md
```

### 7. Comparison Indexes

**Location:** `meta/indexes/comparisons/`

Technology and approach comparison matrices:

```
meta/indexes/comparisons/
├── README.md
├── vector-databases.md
├── embedding-models.md
├── agent-frameworks.md
└── llm-providers.md
```

### 8. Keyword Index

**Location:** `meta/indexes/keyword-index.md`

Alphabetical listing of keywords extracted from document front matter, linking to all documents that use each keyword.

---

## Tag Strategy

### Tag Rules

1. **Canonical** — one tag per concept; no synonyms.
2. **Registered** — all tags must appear in the tag registry before use.
3. **Bounded** — 3–8 tags per document.
4. **Layered** — combine domain, technology, and stage tags.

### Tag Layers

| Layer | Purpose | Examples |
|-------|---------|----------|
| Domain | What area of AI engineering | `llm`, `rag`, `agents`, `deployment` |
| Technology | Specific tool or framework | `fastapi`, `postgresql`, `langgraph` |
| Pattern | Design or architectural pattern | `retry-pattern`, `circuit-breaker` |
| Stage | Where in the lifecycle | `development`, `production`, `debugging` |
| Difficulty | Reader experience level | `beginner`, `intermediate`, `advanced` |

### Adding a New Tag

1. Check the tag registry for an existing tag.
2. If none exists, add it to `tag-registry.md` with a definition.
3. Use it in your document's front matter.
4. Include the tag addition in your commit.

---

## Keyword Strategy

Keywords supplement tags with natural-language terms that readers might search for.

```yaml
keywords: [server-sent events, token streaming, real-time LLM, latency optimization]
```

### Keyword Rules

1. Extracted from document content, not invented.
2. Lowercase, except proper nouns.
3. Max 10 per document.
4. Added to `keyword-index.md` when a document is published.

---

## Related Document Links

Every document maintains relationships through three mechanisms:

### Front Matter `related` Field

```yaml
related:
  - ../rag/hybrid-search.md
  - ../embeddings/embedding-models-overview.md
  - ../../knowledge/lessons-learned/2026-07-13-chunk-size-tradeoffs.md
```

### Inline Cross-References

Contextual links within the document body.

### See Also Footer

Curated list of additional reading at the document bottom.

### Bidirectional Linking

When document A references document B, document B should reference A in its `related` field or See Also section.

---

## Index Maintenance Workflow

When publishing a new document:

1. Add entry to the domain `README.md`.
2. Add entry to `MASTER-INDEX.md`.
3. Add to relevant topic indexes (if applicable).
4. Add to technology index (if technology-specific).
5. Add to pattern index (if describing a pattern).
6. Register any new tags in `tag-registry.md`.
7. Add keywords to `keyword-index.md`.
8. Update related documents with bidirectional links.

---

## Future: Automated Indexing

As the repository grows, consider:

- A script that generates indexes from document front matter.
- Full-text search via a static site generator (MkDocs, Docusaurus).
- Tag and keyword validation in CI.

The current manual approach is intentional — it ensures curation quality at small scale and provides a clear schema for future automation.

---

## See Also

- [Master Index](indexes/MASTER-INDEX.md)
- [Tag Registry](indexes/tags/tag-registry.md)
- [Naming Conventions](naming-conventions.md)
- [Style Guide](style-guide.md)
