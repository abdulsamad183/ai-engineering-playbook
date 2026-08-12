# Code Examples

> Runnable, self-contained code examples organized by technology and pattern.

---

## Start here (offline, no API keys)

| Demo | Command | Graduate to starter |
|------|---------|---------------------|
| Mini RAG | `python3 examples/rag/mini_rag/run.py` | [RAG path](rag/FROM_MINI_TO_STARTER.md) |
| Mini ReAct agent | `python3 examples/agents/mini_react/run.py` | [Agent path](agents/FROM_MINI_TO_STARTER.md) |
| Mini chat API | `python3 examples/llm-applications/mini_chat_api/server.py` then `client.py` | [API path](llm-applications/FROM_MINI_TO_STARTER.md) |
| Mini GenAI sampling | `python3 examples/generative-ai/mini_sample.py` | [Generative AI handbook](../domains/generative-ai/README.md) |

Then follow the [Capstone Walkthrough](../meta/capstone-walkthrough.md) for an end-to-end RAG Chat API. For interviews, see [Interview prep path](../meta/interview-path.md).

## Organization

Examples are organized by **technology or pattern**, not by domain. Each example directory is self-contained with its own README, dependencies, and instructions.

```
examples/
├── python/              # Python patterns and utilities
├── fastapi/             # FastAPI API examples
├── docker/              # Docker and containerization
├── sql/                 # SQL queries and patterns
├── redis/               # Redis caching patterns
├── llm-applications/    # LLM integration examples (+ mini_chat_api)
├── generative-ai/       # Tiny generative demos
├── prompt-engineering/  # Prompt patterns and pipelines
├── context-engineering/ # Context assembly and memory
├── rag/                 # RAG pipeline examples (+ mini_rag)
├── agents/              # AI agent patterns (+ mini_react)
├── langgraph/           # LangGraph workflow examples
├── mcp/                 # MCP server and client examples
├── ai-evaluation/       # Evaluation framework examples
├── production-ai/       # Docker, CI/CD, observability
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
- [Capstone Walkthrough](../meta/capstone-walkthrough.md) — end-to-end RAG API tutorial
