## [Unreleased]

## [1.5.0] - 2026-07-23

### Changed

- Removed curriculum **Phase N** numbering across the playbook
- Reorganized navigation around five **capability groups**: Foundations, Core (LLM Interaction), Retrieval & Agents, Production, Craft & Growth
- Rewrote [Learning Roadmap](meta/roadmap.md) without phase stages
- Restructured [Master Index](meta/indexes/MASTER-INDEX.md) and home [README](README.md) to match capability groups
- Stripped `phase-N` / `phase-papers` frontmatter tags and phase suffixes from handbook prose

## [1.4.1] - 2026-07-23

### Changed

- Home page rewritten: playbook overview, organization layers, three use paths, clear learning sequence
- Learning roadmap simplified with at-a-glance map and staged table
- MkDocs nav reduced to **Home · Learn · Handbooks · Build · Reference**

## [1.4.0] - 2026-07-23

### Added

- **MkDocs Material documentation site** with sidebar/tabs navigation, search, and Mermaid support
- `docs/` symlink tree (content stays in `domains/`, `meta/`, etc.)
- GitHub Actions workflow [`.github/workflows/docs.yml`](.github/workflows/docs.yml) → GitHub Pages
- [docs-site.md](docs-site.md) — local preview and Pages setup guide

## [1.3.0] - 2026-07-23

### Added

- **AI Safety handbook** — introduction, prompt injection, guardrails, safe tool use, production checklist
- **Debugging handbook** — RAG/agent/API debugging + triage playbook
- RAG and agent starter unit tests
- Knowledge lesson: RAG citations beat longer context
- Resource bookmarks (`tools.md`, `documentation.md`)
- `meta/templates/case-study.md` (replaces project case-study workflow)

### Fixed

- Broken relative links in roadmap, engineering template READMEs, capstone, embeddings, tool-calling, Redis, Docker, logging, observability paths
- Backend engineering example links pointing at missing files
- Domains overview now marks Published vs Planned

### Removed

- `projects/` directory (earlier); `project.md` template deprecated in favor of case-study + knowledge retrospectives

## [1.2.1] - 2026-07-13

### Added

- [Capstone Walkthrough](meta/capstone-walkthrough.md) — end-to-end RAG chat API tutorial (templates → eval → Docker → CI)

### Removed

- `projects/` directory — project case studies no longer part of the playbook

### Changed

- Main README extended with capstone links; repository map updated

## [1.2.0] - 2026-07-13

### Added

- **Engineering Templates & Reusable Assets** — 14 template sections
  - FastAPI, RAG, agent, and MCP starters with tests and CI
  - Docker, GitHub Actions, logging, monitoring, deployment configs
  - Prompt library, evaluation harnesses, boilerplates, utilities, architecture diagrams
- **AI Research Papers & Literature Review** — 10 handbook sections
  - Transformer foundations through future research directions
  - Agent reasoning, retrieval, prompting, DSPy, and SWE-Agent summaries
  - Comparison guides, engineering takeaways, and evolution timeline
- 6 research cheat sheets (transformers, reasoning, retrieval, agents, comparisons, timeline)

## [1.1.0] - 2026-07-13

### Added

- **AI Engineering Interview Handbook** — 22 documents
  - Sections 1–20: strategy through behavioral interviews
  - Mock interview packs (Junior, Mid, Senior, Staff)
  - Company interview patterns for AI product organizations
- 12 interview cheat sheets (Python through system design)

## [1.0.0] - 2026-07-13

### Added

- **AI System Design** — 18 documents
  - Sections 1–17: fundamentals through interview prep
  - 12 product/system design case studies (ChatGPT, Cursor, Copilot, Perplexity, etc.)
  - Comparison guides and scaling patterns
- **Production AI & AI Platform Engineering** — 16 documents
  - Sections 1–15: Docker through production readiness
  - Comparison guides for deployment and observability
- 12 production Python examples + Dockerfile + CI workflow reference
- 12 cheat sheets (4 system design + 8 production)

## [0.9.0] - 2026-07-13

### Added

- **AI Evaluation & LLMOps Evaluation** — 26 documents
  - Sections 1–20: introduction through case studies
  - 5 framework guides (RAGAS, DeepEval, LangSmith, Phoenix, OpenAI Evals)
  - Comparison guides and production evaluation coverage
- 12 Python evaluation examples
- 9 evaluation cheat sheets

## [0.8.0] - 2026-07-13

### Added

- **Model Context Protocol (MCP) & AI Protocol Engineering** — 21 documents
  - Sections 1–20: introduction through real-world architectures
  - Comparison guides for transports, primitives, and integration strategies
- 13 Python MCP examples (server, client, transports, multi-server, auth, FastAPI)
- 9 MCP cheat sheets

## [0.7.0] - 2026-07-13

### Added

- **AI Agents & Agent Engineering** — 27 documents
  - Sections 1–20: introduction through case studies
  - 6 framework guides (LangGraph, CrewAI, AutoGen, Semantic Kernel, PydanticAI, OpenAI Agents SDK)
  - Build-your-own-agent-framework reference
- 6 Python agent examples, 8 cheat sheets

## [0.6.0] - 2026-07-13

### Added

- **Retrieval-Augmented Generation (RAG)** — 29 documents forming the largest handbook module
  - Sections 1–21: introduction through production system design
  - 7 vector database provider guides (FAISS, Chroma, PGVector, Pinecone, Milvus, Weaviate, Qdrant)
  - Comparison guides and advanced architecture coverage (GraphRAG, Self-RAG, agentic RAG)
- 13 Python examples including complete pipeline and FastAPI endpoint
- 9 RAG cheat sheets

## [0.5.0] - 2026-07-13

### Added

- **Context Engineering** — 21 documents forming a complete context engineering handbook
  - Sections 1–20: introduction through production (architecture, memory, ranking, compression, security)
  - Comparison guides for context engineering strategies
- 11 Python examples (memory, assembly, ranking, budgeting, caching, pruning)
- 7 context engineering cheat sheets

## [0.4.0] - 2026-07-13

### Added

- **Prompt Engineering** — 19 documents forming a complete prompt engineering handbook
  - Sections 1–18: introduction through production (anatomy, patterns, structured prompting, reasoning, chaining, lifecycle, testing, evaluation, security)
  - Comparison guides for prompting strategies
- 16 reusable prompt templates in `prompts/templates/`
- 9 Python examples (loader, chaining, few-shot, XML, evaluation, RAG, tools, chatbot, document analysis)
- 9 prompt engineering cheat sheets

## [0.3.0] - 2026-07-13

### Added

- LLM Engineering

## [0.2.0] - 2026-07-13

### Added

- Backend Engineering

## [0.1.0] - 2026-07-13

### Added

- Repository foundation and AI Engineering Foundations

[Unreleased]: https://github.com/hp/ai-engineering-playbook/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/hp/ai-engineering-playbook/releases/tag/v1.1.0
[1.0.0]: https://github.com/hp/ai-engineering-playbook/releases/tag/v1.0.0
[0.9.0]: https://github.com/hp/ai-engineering-playbook/releases/tag/v0.9.0
[0.8.0]: https://github.com/hp/ai-engineering-playbook/releases/tag/v0.8.0
[0.7.0]: https://github.com/hp/ai-engineering-playbook/releases/tag/v0.7.0
[0.6.0]: https://github.com/hp/ai-engineering-playbook/releases/tag/v0.6.0
[0.5.0]: https://github.com/hp/ai-engineering-playbook/releases/tag/v0.5.0
[0.4.0]: https://github.com/hp/ai-engineering-playbook/releases/tag/v0.4.0
[0.3.0]: https://github.com/hp/ai-engineering-playbook/releases/tag/v0.3.0
[0.2.0]: https://github.com/hp/ai-engineering-playbook/releases/tag/v0.2.0
[0.1.0]: https://github.com/hp/ai-engineering-playbook/releases/tag/v0.1.0
