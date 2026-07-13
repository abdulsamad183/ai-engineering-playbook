# Engineering Templates

> Production-ready starter code and reusable assets for AI engineering.

---

## Purpose

This module transforms the playbook from documentation into a **practical engineering toolkit**. Copy any template into a new repository and customize — each asset follows modern software engineering practices used in production AI systems.

---

## Sections

| # | Section | Path | Description |
|---|---------|------|-------------|
| 1 | [FastAPI Starter](engineering/fastapi-starter/README.md) | `engineering/fastapi-starter/` | Modular API with auth, middleware, Docker, CI |
| 2 | [RAG Starter](engineering/rag-starter/README.md) | `engineering/rag-starter/` | Ingestion → retrieval → citations → eval |
| 3 | [Agent Starter](engineering/agent-starter/README.md) | `engineering/agent-starter/` | Planner, executor, memory, tools, checkpointing |
| 4 | [MCP Starter](engineering/mcp-starter/README.md) | `engineering/mcp-starter/` | Server, client, tool/resource/prompt registration |
| 5 | [Docker Starter](engineering/docker/README.md) | `engineering/docker/` | Multi-stage builds, Compose dev/prod |
| 6 | [GitHub Actions](engineering/github-actions/README.md) | `engineering/github-actions/` | CI, lint, Docker, security, deploy |
| 7 | [Logging](engineering/logging/README.md) | `engineering/logging/` | Structured JSON, correlation IDs, rotation |
| 8 | [Monitoring](engineering/monitoring/README.md) | `engineering/monitoring/` | OpenTelemetry, LangFuse, Phoenix hooks |
| 9 | [Prompt Library](engineering/prompts/README.md) | `engineering/prompts/` | Parameterized prompts (+ [prompts/templates](../prompts/templates/)) |
| 10 | [Evaluation](engineering/evaluation/README.md) | `engineering/evaluation/` | Prompt, RAG, agent, model comparison |
| 11 | [Deployment](engineering/deployment/README.md) | `engineering/deployment/` | Render, Railway, Vercel, nginx, VM |
| 12 | [Boilerplates](engineering/boilerplates/README.md) | `engineering/boilerplates/` | Chat, RAG, agent, search, API, SaaS, MCP |
| 13 | [Utilities](engineering/utilities/README.md) | `engineering/utilities/` | Retry, cache, tokens, cost, config |
| 14 | [Architecture](engineering/architecture/README.md) | `engineering/architecture/` | Reusable Mermaid diagrams |

---

## How to Use

1. **Pick a starter** matching your product (API, RAG, agent, MCP).
2. **Copy the folder** into a new git repository.
3. **Wire configuration** via `.env` and provider credentials.
4. **Compose** utilities, logging, monitoring, and CI from sibling templates.
5. **Cross-link** to domain handbooks for depth ([RAG](../domains/rag/README.md), [Agents](../domains/ai-agents/README.md), [MCP](../domains/mcp/README.md)).

---

## Related

- [Document scaffolds](../meta/templates/) — markdown templates for writing docs
- [Examples](../examples/README.md) — focused runnable snippets
- [Production AI](../domains/ai-deployment/README.md) — deployment handbook
- [Research Papers](../domains/papers/README.md) — theory behind the templates

---

## See Also

- [Master Index](../meta/indexes/MASTER-INDEX.md)
- [Learning Roadmap](../meta/roadmap.md)
