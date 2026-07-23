# AI Engineering Playbook

> A production-oriented handbook for building, deploying, evaluating, and operating modern AI applications.

**New here?** Pick one path below — every link goes to a module hub with its own table of contents.

---

## Start Here

Choose what you need right now:

| Your goal | Go to... | What you'll find |
|-----------|---------|------------------|
| **Browse as a website** | [GitHub Pages site](https://abdulsamad183.github.io/ai-engineering-playbook/) | Sidebar nav, search, Mermaid rendering |
| **Build your first end-to-end app** | [Capstone Walkthrough](meta/capstone-walkthrough.md) | RAG chat API from templates → Docker → CI |
| **Learn AI engineering** (structured path) | [Learning Roadmap](meta/roadmap.md) | Phases 1–15 in order, with milestones |
| **Learn a specific topic** | [Handbooks below ↓](#complete-handbooks) | 15 complete modules — jump to any topic |
| **Build something today** | [Engineering Templates](templates/README.md) | Copy-paste FastAPI, RAG, agent, MCP starters |
| **Prepare for interviews** | [Interview Handbook](domains/interview-preparation/README.md) | Coding, system design, RAG, agents, mocks |
| **Look something up fast** | [Cheat Sheets](cheat-sheets/README.md) | One-page references for 90+ topics |
| **Find any document** | [Master Index](meta/indexes/MASTER-INDEX.md) | Full searchable index of all content |

---

## Complete Handbooks

These are the **main learning modules**. Each hub has sections, examples, and cross-links — start at the README in each folder.

### Foundations & Backend

| Topic | Handbook | Best for |
|-------|----------|----------|
| AI engineering basics | [Foundations](domains/foundations/README.md) | Lifecycle, testing, Git, config, best practices |
| Python for AI | [Python Engineering](domains/python-engineering/README.md) | Async, typing, Pydantic, project layout |
| Backend patterns | [Backend Engineering](domains/backend-engineering/README.md) | Architecture, HTTP clients, validation, errors |
| APIs & HTTP | [APIs](domains/apis/README.md) | REST, auth, JWT, streaming, rate limiting |
| FastAPI | [FastAPI](domains/fastapi/README.md) | Routes, DI, middleware, AI endpoints |
| Databases | [Databases](domains/databases/README.md) | PostgreSQL, Redis, pgvector, SQLAlchemy |

### LLM Systems

| Topic | Handbook | Best for |
|-------|----------|----------|
| LLM integration | [LLM Engineering](domains/llm-engineering/README.md) | Tokens, inference, tools, providers, cost |
| Prompt design | [Prompt Engineering](domains/prompt-engineering/README.md) | Patterns, testing, versioning, security |
| Context & memory | [Context Engineering](domains/context-engineering/README.md) | Windows, ranking, compression, budgeting |

### Retrieval & Agents

| Topic | Handbook | Best for |
|-------|----------|----------|
| RAG pipelines | [RAG](domains/rag/README.md) | Chunking, retrieval, reranking, evaluation |
| AI agents | [AI Agents](domains/ai-agents/README.md) | Planning, tools, memory, frameworks |
| MCP protocol | [MCP](domains/mcp/README.md) | Servers, clients, transports, security |

### Production & Design

| Topic | Handbook | Best for |
|-------|----------|----------|
| Evaluation & LLMOps | [AI Evaluation](domains/ai-evaluation/README.md) | Metrics, RAGAS, regression, CI gates |
| System design | [AI System Design](domains/ai-system-design/README.md) | Architecture, scaling, case studies |
| Deployment & ops | [Production AI](domains/ai-deployment/README.md) | Docker, CI/CD, monitoring, incidents |
| AI safety | [AI Safety](domains/ai-safety/README.md) | Injection, guardrails, safe tool use |
| Debugging | [Debugging](domains/debugging/README.md) | RAG/agent/API triage playbooks |

### Research & Career

| Topic | Handbook | Best for |
|-------|----------|----------|
| Research papers (engineering view) | [AI Research Papers](domains/papers/README.md) | Transformers, ReAct, RAG papers, DSPy |
| Interview preparation | [Interview Handbook](domains/interview-preparation/README.md) | Technical + behavioral + mock interviews |

> **Planned domains** (workflows, cloud, multi-agent depth, etc.) are listed in [Domains Overview](domains/README.md) with status **Planned**. Prefer published handbooks above.

---

## Recommended Learning Order

Follow this if you want a **sequential path** from zero to production:

```
Foundations → Backend & FastAPI → LLM Engineering → Prompt Engineering
    → Context Engineering → RAG → AI Agents → MCP
    → AI Evaluation → System Design → Production AI
```

| Step | Module | Link |
|------|--------|------|
| 0 | **Capstone (hands-on)** | [RAG Chat API walkthrough](meta/capstone-walkthrough.md) |
| 1 | Foundations | [domains/foundations/](domains/foundations/README.md) |
| 2 | Backend + FastAPI | [domains/backend-engineering/](domains/backend-engineering/README.md) · [domains/fastapi/](domains/fastapi/README.md) |
| 3 | LLM Engineering | [domains/llm-engineering/](domains/llm-engineering/README.md) |
| 4 | Prompt Engineering | [domains/prompt-engineering/](domains/prompt-engineering/README.md) |
| 5 | Context Engineering | [domains/context-engineering/](domains/context-engineering/README.md) |
| 6 | RAG | [domains/rag/](domains/rag/README.md) |
| 7 | AI Agents | [domains/ai-agents/](domains/ai-agents/README.md) |
| 8 | MCP | [domains/mcp/](domains/mcp/README.md) |
| 9 | Evaluation | [domains/ai-evaluation/](domains/ai-evaluation/README.md) |
| 10 | System Design | [domains/ai-system-design/](domains/ai-system-design/README.md) |
| 11 | Production | [domains/ai-deployment/](domains/ai-deployment/README.md) |

[Full roadmap with timelines and milestones →](meta/roadmap.md)

---

## Build Toolkit

Use these when you are **writing code**, not reading theory:

| Resource | Link | Contents |
|----------|------|----------|
| **Starter templates** | [templates/](templates/README.md) | FastAPI, RAG, agent, MCP, Docker, CI/CD, deploy configs |
| **Code examples** | [examples/](examples/README.md) | Runnable Python by topic (RAG, agents, MCP, eval, production) |
| **Prompt templates** | [prompts/](prompts/README.md) | 16+ parameterized prompts (RAG, agents, SQL, code) |
| **Common mistakes** | [common-mistakes/](domains/common-mistakes/common-engineering-mistakes.md) | 20 pitfalls with fixes |

### Templates at a glance

| Template | Use when |
|----------|----------|
| [FastAPI Starter](templates/engineering/fastapi-starter/README.md) | New AI API service |
| [RAG Starter](templates/engineering/rag-starter/README.md) | Document Q&A pipeline |
| [Agent Starter](templates/engineering/agent-starter/README.md) | Tool-using agent |
| [MCP Starter](templates/engineering/mcp-starter/README.md) | MCP server or client |
| [Boilerplates](templates/engineering/boilerplates/README.md) | Chat, RAG, SaaS, search apps |

---

## Quick Reference

| Need | Link |
|------|------|
| Cheat sheets (90+) | [cheat-sheets/](cheat-sheets/README.md) |
| Glossary | [meta/glossary.md](meta/glossary.md) |
| Master index (all docs) | [meta/indexes/MASTER-INDEX.md](meta/indexes/MASTER-INDEX.md) |
| Topic indexes | [meta/indexes/topics/](meta/indexes/topics/) |
| Comparison tables | [meta/indexes/comparisons/](meta/indexes/comparisons/) |

---

## I Want To…

Quick answers — no hunting:

| I want to… | Go to |
|------------|-------|
| Build a RAG app | [Capstone Walkthrough](meta/capstone-walkthrough.md) → [RAG Handbook](domains/rag/README.md) → [RAG Starter](templates/engineering/rag-starter/README.md) |
| Build an AI agent | [AI Agents Handbook](domains/ai-agents/README.md) → [Agent Starter](templates/engineering/agent-starter/README.md) |
| Integrate an LLM API | [LLM Engineering](domains/llm-engineering/README.md) → [Provider guides](domains/llm-engineering/README.md#providers-section-15) |
| Write better prompts | [Prompt Engineering](domains/prompt-engineering/README.md) → [Prompt templates](prompts/templates/) |
| Deploy to production | [Production AI](domains/ai-deployment/README.md) → [Deployment templates](templates/engineering/deployment/README.md) |
| Evaluate my AI app | [AI Evaluation](domains/ai-evaluation/README.md) → [Eval templates](templates/engineering/evaluation/README.md) |
| Design a system (interview) | [System Design](domains/ai-system-design/README.md) → [Interview mocks](domains/interview-preparation/mock-interviews.md) |
| Understand a research paper | [Research Papers](domains/papers/README.md) → [Comparison guides](domains/papers/research-comparison-guides.md) |
| Debug a production issue | [Debugging Handbook](domains/debugging/README.md) → [Common mistakes](domains/common-mistakes/common-engineering-mistakes.md) |
| Harden against prompt injection | [AI Safety](domains/ai-safety/README.md) → [Prompt security](domains/prompt-engineering/prompt-security.md) |

---

## Repository Map

```
ai-engineering-playbook/
├── domains/       ← Handbooks (main content) — start at README in each folder
├── templates/     ← Production starter code (copy into new projects)
├── examples/      ← Runnable code snippets by technology
├── prompts/       ← Reusable prompt templates
├── cheat-sheets/  ← One-page quick references
├── meta/          ← Roadmap, glossary, indexes, style guide
├── knowledge/     ← Lessons learned, ADRs, benchmarks
└── assets/        ← Diagrams and images
```

[How the repository is designed →](meta/architecture-overview.md)

---

## Who This Is For

- **AI Engineers** shipping LLM apps, RAG, and agents to production
- **Backend Engineers** adding AI to existing systems
- **Technical Leaders** designing AI architectures
- **Interview candidates** preparing for AI engineering roles

This is **not** a machine learning research course. Theory appears only where it helps you build and operate real systems.

---

## Contributing

1. Pick a [domain](domains/README.md) and copy a [document template](meta/templates/).
2. Follow the [style guide](meta/style-guide.md).
3. Add your doc to the domain README and [master index](meta/indexes/MASTER-INDEX.md).

[Full contributing guide →](CONTRIBUTING.md)

---

## Project Status

**15 handbook phases complete** (Foundations through Research Papers). See [Changelog](CHANGELOG.md) for version history.

---

## License

[MIT License](LICENSE)
