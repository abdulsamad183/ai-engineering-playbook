# AI Engineering Playbook

> A production-oriented knowledge base for building, deploying, evaluating, and maintaining modern AI-powered applications.

---

## Vision

The AI Engineering Playbook is a long-term, curated knowledge base designed to grow over years into a comprehensive reference for AI engineers. It is structured like the internal documentation of an experienced AI engineering team — not a collection of notes, but a systematic, discoverable, and maintainable engineering resource.

**This repository focuses on what AI engineers actually do:** integrate LLMs, build RAG systems, design agents, deploy to production, monitor costs, debug failures, and ship reliable AI-powered software.

---

## Who This Is For

- **AI Engineers** building production LLM applications, agents, and RAG systems
- **Backend Engineers** transitioning into AI application development
- **Software Engineers** who need practical AI integration knowledge
- **Technical Leaders** designing AI system architectures
- **Anyone** preparing for AI engineering interviews or roles

This is **not** a machine learning research repository or a deep learning theory course. ML/DL concepts appear only where they directly support practical engineering workflows.

---

## Quick Navigation

| I want to... | Go to... |
|--------------|----------|
| Start learning | [Phase 9 MCP](domains/mcp/README.md) |
| Find a topic | [Master Index](meta/indexes/MASTER-INDEX.md) |
| Browse by domain | [Domains](domains/README.md) |
| Write a new document | [Templates](meta/templates/) + [Style Guide](meta/style-guide.md) |
| See code examples | [Examples](examples/README.md) |
| Find prompt templates | [Prompts](prompts/README.md) |
| Quick reference | [Cheat Sheets](cheat-sheets/README.md) |
| Read lessons learned | [Personal Knowledge](knowledge/README.md) |
| Look up a term | [Glossary](meta/glossary.md) |
| Understand the structure | [Architecture Overview](meta/architecture-overview.md) |

---

## Repository Organization

```
ai-engineering-playbook/
├── domains/          # 40+ knowledge domains (the core content)
├── meta/             # Standards, templates, indexes, roadmap
├── knowledge/        # Personal lessons, mistakes, ADRs, benchmarks
├── examples/         # Runnable code examples by technology
├── projects/         # Project case studies
├── prompts/          # Reusable prompt patterns
├── cheat-sheets/     # Quick reference cards
├── assets/           # Diagrams, images, slides
└── resources/        # Bookmarks and external links
```

### Knowledge Domains

Content is organized by **engineering domain**, not by technology:

| Category | Domains |
|----------|---------|
| **Foundations** | Python, backend, APIs, databases |
| **LLM Systems** | LLM engineering, prompts, context, embeddings, vector DBs |
| **Retrieval & Agents** | RAG, agents, MCP, A2A, workflows, multi-agent |
| **Production** | Evaluation, safety, deployment, Docker, CI/CD, monitoring, security |
| **Architecture** | System design, application architecture, patterns |
| **Operations** | Debugging, incidents, data engineering |
| **Growth** | Interviews, papers, career, resources |

[Browse all domains →](domains/README.md)

---

## Learning Roadmap

The recommended path from programming foundations to production AI systems:

1. Programming foundations (Python, Git, engineering principles)
2. Backend engineering (HTTP, FastAPI, authentication)
3. APIs and databases (SQL, PostgreSQL, Redis)
4. LLM fundamentals (API integration, streaming, model selection)
5. Prompt engineering (design, structured outputs, patterns)
6. Context engineering (window management, memory)
7. Embeddings and retrieval (vectors, chunking, search)
8. RAG systems (pipelines, evaluation, advanced patterns)
9. AI agents (tools, architectures, MCP)
10. AI workflows (orchestration, multi-agent)
11. Evaluation (metrics, LLM-as-judge, CI integration)
12. Production deployment (Docker, cloud, CI/CD)
13. Monitoring and optimization (logging, observability, cost)

[Full roadmap with milestones →](meta/roadmap.md)

---

## Philosophy

### Build for Production

Every document considers the path from development to production. Concepts include production checklists, failure modes, and operational guidance — not just "how it works" but "how to run it reliably."

### Domain Over Technology

Domains are named for engineering concepts (`vector-databases/`, `ai-agents/`), not for specific tools (`pinecone/`, `langchain/`). Technologies are indexed and compared within domains. When a new framework emerges, it fits into existing domains without restructuring.

### Experience Is Knowledge

The `knowledge/` directory captures lessons learned, mistakes, architecture decisions, and production experiences. These become increasingly valuable over time and represent real engineering judgment that reference docs cannot provide.

### Consistency at Scale

Templates, style guides, naming conventions, and indexing strategies ensure the repository remains organized after thousands of commits. Every document follows the same structure.

### Extensible by Design

The structure accommodates future technologies — multimodal AI, new agent protocols, inference improvements, new databases — without requiring reorganization. New content extends; it does not restructure.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full workflow. Summary:

1. Choose or create a domain for your topic.
2. Copy the appropriate [template](meta/templates/).
3. Follow the [style guide](meta/style-guide.md) and [naming conventions](meta/naming-conventions.md).
4. Add your document to the domain index and [master index](meta/indexes/MASTER-INDEX.md).
5. Register any new tags in the [tag registry](meta/indexes/tags/tag-registry.md).

---

## Roadmap

### Foundation (Phase 2 — Complete)

- [x] AI Engineering Foundations (15 topics)

### Phase 3: Backend Engineering (Complete)

- [x] Backend architecture, FastAPI complete guide, API design, auth
- [x] SQLAlchemy, Alembic, Redis backend patterns
- [x] Background processing, async, file handling, HTTP clients
- [x] Validation, error handling, logging, monitoring foundation
- [x] Configuration, testing, security, performance
- [x] Project structure, reference architectures, mistakes guide
- [x] 10 backend templates, 8+ code examples

### Phase 4: LLM Engineering (Complete)

- [x] 26 documents — fundamentals through production (Sections 1–20)
- [x] 6 provider guides (OpenAI, Gemini, Claude, Groq, OpenRouter, Ollama)
- [x] 12 API integration examples, 3 cheat sheets

### Phase 5: Prompt Engineering (Complete)

- [x] 19 documents — handbook from introduction through production
- [x] 16 prompt templates in `prompts/templates/`
- [x] 9 Python examples, 9 cheat sheets

### Phase 6: Context Engineering (Complete)

- [x] 21 documents — handbook from introduction through production
- [x] 11 Python examples, 7 cheat sheets

### Phase 7: RAG (Complete)

- [x] 29 documents, 13 examples, 9 cheat sheets

### Phase 8: AI Agents (Complete)

- [x] 27 documents (20 sections + 6 frameworks + comparisons)
- [x] 6 Python examples, 8 cheat sheets

### Phase 9: MCP & AI Protocol Engineering (Complete)

- [x] 21 documents (20 sections + comparisons)
- [x] 13 Python examples, 9 cheat sheets

### Phase 10: A2A & Multi-Agent Protocols

- [ ] A2A protocols
- [ ] Multi-agent communication depth

### Phase 10: Production AI

- [ ] Deployment guides (Docker, cloud)
- [ ] AI evaluation frameworks
- [ ] Advanced observability and safety

### Ongoing Depth

- [ ] System design case studies
- [ ] Interview preparation guides
- [ ] Research paper summaries
- [ ] Production incident postmortems
- [ ] Technology comparison matrices

### Ongoing

- [ ] Personal knowledge entries (lessons, mistakes, ADRs)
- [ ] Project case studies
- [ ] Code examples for every major topic
- [ ] Cheat sheets for quick reference

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## See Also

- [Architecture Overview](meta/architecture-overview.md)
- [Glossary](meta/glossary.md)
- [Changelog](CHANGELOG.md)
