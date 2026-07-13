# Naming Conventions

> Consistent naming is the foundation of discoverability at scale.
> These rules apply to files, folders, assets, tags, and identifiers across the repository.

---

## Principles

1. **Predictable** — given a topic, you should know where to find it and what to name it.
2. **Stable** — names do not change when technologies evolve; domains do not rename for trend cycles.
3. **Readable** — names are human-friendly in URLs, file explorers, and git diffs.
4. **Sortable** — date prefixes and numeric ordering enable chronological and priority sorting.

---

## Files

### Documents

| Rule | Convention | Example |
|------|------------|---------|
| Format | `kebab-case.md` | `streaming-llm-responses.md` |
| Length | 2–6 words preferred | `agent-memory-patterns.md` |
| No dates | Unless in `knowledge/` | — |
| No version suffixes | Version in front matter | ~~`rag-v2.md`~~ → `rag-pipeline-design.md` |
| No technology prefix | Unless disambiguation needed | `fastapi-dependency-injection.md` |

### Knowledge Base Entries

Personal knowledge documents include a date prefix for chronological sorting:

```
knowledge/
├── lessons-learned/
│   └── 2026-07-13-rag-chunk-size-tradeoffs.md
├── mistakes/
│   └── 2026-06-20-forgot-embedding-dimension-mismatch.md
└── architecture-decisions/
    └── 2026-05-01-chose-pgvector-over-pinecone.md
```

Format: `YYYY-MM-DD-{descriptive-kebab-case}.md`

### Templates

```
meta/templates/{type}.md
```

Examples: `concept.md`, `production-guide.md`, `postmortem.md`

### Indexes

```
meta/indexes/{index-name}.md
meta/indexes/topics/{topic-name}.md
```

Use `UPPER-CASE` for top-level index files: `MASTER-INDEX.md`, `TAG-REGISTRY.md`.

---

## Folders

| Rule | Convention | Example |
|------|------------|---------|
| Format | `kebab-case` | `vector-databases/` |
| Depth | Max 3 levels from repo root | `domains/databases/postgresql/` |
| No numbering | Except `examples/` ordering | `domains/rag/` not `domains/03-rag/` |
| Plural for collections | When folder holds many items | `examples/`, `templates/`, `papers/` |
| Singular for concepts | When folder is a topic area | `knowledge/`, `meta/` |

### When to Create a Subfolder

Create a subfolder within a domain when:

- The domain has more than ~20 documents, OR
- A natural sub-topic grouping exists (e.g., `databases/postgresql/`), OR
- Documents share a common template type (e.g., `papers/`)

Do **not** create subfolders preemptively. Start flat, subdivide when needed.

---

## Images

```
assets/images/{domain}/{domain}-{topic}-{descriptor}.{ext}
```

| Component | Rule | Example |
|-----------|------|---------|
| Domain folder | Matches `domains/` name | `assets/images/rag/` |
| File name | `{domain}-{topic}-{descriptor}` | `rag-chunking-strategies-comparison.png` |
| Extension | `.png` screenshots, `.svg` icons/diagrams | |
| No spaces | Ever | |

---

## Diagrams

### Standalone Mermaid Files

```
assets/diagrams/{type}/{type}-{subject}-{version}.mmd
```

| Type Folder | Purpose |
|-------------|---------|
| `flowcharts/` | Decision flows, process flows |
| `sequence/` | API interactions, agent tool calls |
| `architecture/` | System architecture, component diagrams |
| `class/` | Data models, class relationships |
| `er/` | Database entity-relationship diagrams |
| `workflows/` | AI workflow orchestration |
| `agent-interactions/` | Multi-agent communication patterns |

Examples:

```
assets/diagrams/architecture/architecture-rag-system-v1.mmd
assets/diagrams/sequence/sequence-agent-tool-call-v2.mmd
assets/diagrams/workflows/workflow-document-ingestion-v1.mmd
```

### Versioning Diagrams

- Append `-v1`, `-v2` when the diagram represents a specific iteration.
- Do not version for minor visual tweaks; version for semantic changes.

---

## Code Examples

```
examples/{technology}/example-{topic}.{ext}
examples/{technology}/{project-name}/
```

| Rule | Example |
|------|---------|
| Prefix with `example-` for single files | `example-streaming-response.py` |
| Use project folders for multi-file examples | `examples/rag/basic-rag-pipeline/` |
| README in every example directory | `examples/rag/README.md` |

---

## Tags

| Rule | Convention | Example |
|------|------------|---------|
| Format | `kebab-case` | `vector-search` |
| Register in | `meta/indexes/tags/tag-registry.md` | |
| Count per doc | 3–8 tags | |
| No synonyms | One canonical tag per concept | Use `rag`, not `retrieval-augmented-generation` |

### Tag Categories

| Category | Prefix (optional) | Examples |
|----------|-------------------|---------|
| Technology | none | `fastapi`, `postgresql`, `langgraph` |
| Pattern | none | `retry-pattern`, `circuit-breaker` |
| Stage | none | `development`, `production`, `debugging` |
| Difficulty | none | `beginner`, `intermediate`, `advanced` |
| Domain | none | `llm`, `agents`, `deployment` |

---

## Keywords

Keywords differ from tags — they are free-form terms used in the search index and document front matter for discoverability.

```yaml
keywords: [streaming, server-sent events, token latency, real-time inference]
```

| Rule | Convention |
|------|------------|
| Format | Lowercase, natural language phrases |
| Source | Extracted from document content |
| Registry | Listed in `meta/indexes/keyword-index.md` |
| Max per doc | 10 keywords |

---

## Identifiers

### Document IDs

Each document has an implicit ID derived from its file path:

```
domains/rag/hybrid-search.md → id: domains/rag/hybrid-search
```

Use this ID in cross-references and indexes. Do not create separate ID fields.

### ADR (Architecture Decision Record) IDs

```
knowledge/architecture-decisions/ADR-001-vector-store-selection.md
```

Format: `ADR-{NNN}-{kebab-case-title}.md` where NNN is a zero-padded sequential number.

---

## Anti-Patterns

| Avoid | Why | Instead |
|-------|-----|---------|
| `notes.md`, `temp.md`, `draft.md` | Non-descriptive | `topic-specific-name.md` |
| `RAG_Pipeline.md` | Mixed case, underscores | `rag-pipeline.md` |
| `final-v3-UPDATED.md` | Version in filename | Version in front matter |
| `gpt4-tips.md` | Technology-coupled | `llm-prompting-strategies.md` |
| Deep nesting (`a/b/c/d/e/`) | Hard to navigate | Flatten to max 3 levels |
| Dates in domain docs | Breaks sort-by-topic | Dates only in `knowledge/` |

---

## See Also

- [Style Guide](style-guide.md)
- [Indexing Strategy](indexing-strategy.md)
- [Tag Registry](indexes/tags/tag-registry.md)
