# Code Examples

> Runnable, self-contained code examples organized by technology and pattern.

---

## Organization

Examples are organized by **technology or pattern**, not by domain. Each example directory is self-contained with its own README, dependencies, and instructions.

```
examples/
├── python/              # Python patterns and utilities
├── fastapi/             # FastAPI API examples
├── docker/              # Docker and containerization
├── sql/                 # SQL queries and patterns
├── redis/               # Redis caching patterns
├── llm-applications/    # LLM integration examples
├── prompt-engineering/  # Prompt patterns and pipelines
├── rag/                 # RAG pipeline examples
├── langgraph/           # LangGraph workflow examples
├── mcp/                 # MCP server and client examples
├── agents/              # AI agent examples
├── ai-evaluation/       # Evaluation framework examples
└── deployment/          # Deployment configuration examples
```

---

## Example Standards

Every example must include:

1. **README.md** — purpose, prerequisites, how to run
2. **Dependencies** — `requirements.txt` with pinned versions
3. **Runnable code** — or clearly marked as pseudocode
4. **Comments** — only for non-obvious logic

### Naming

| Type | Convention | Example |
|------|------------|---------|
| Single file | `example-{topic}.py` | `example-streaming-response.py` |
| Multi-file project | `{project-name}/` | `basic-rag-pipeline/` |

### Linking

- Link examples from relevant domain documents.
- Reference the domain document from the example README.

---

## Adding an Example

1. Choose or create the appropriate technology folder.
2. Add a README explaining the example.
3. Include pinned dependencies.
4. Test that the example runs.
5. Link from the relevant domain document.

See [CONTRIBUTING.md](../CONTRIBUTING.md#adding-code-examples).

---

## See Also

- [Domains](../domains/) — reference documentation
- [Tutorials](../meta/templates/tutorial.md) — step-by-step guides
- [Projects](../projects/) — full project case studies
