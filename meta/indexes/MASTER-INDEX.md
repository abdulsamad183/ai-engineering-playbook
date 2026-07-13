# Master Index

> Complete index of all published documents in the AI Engineering Playbook.
> Last updated: 2026-07-13

---

## How to Use This Index

- Browse by domain below, or use topic/technology indexes for cross-cutting views.
- Documents marked *(planned)* are placeholders for future content.
- See [indexing strategy](../indexing-strategy.md) for how to add new entries.

---

## Meta

| Document | Description |
|----------|-------------|
| [Style Guide](../style-guide.md) | Documentation standards |
| [Naming Conventions](../naming-conventions.md) | File, folder, and tag naming rules |
| [Indexing Strategy](../indexing-strategy.md) | How documents are indexed and discovered |
| [Mermaid Conventions](../mermaid-conventions.md) | Diagram standards |
| [Glossary](../glossary.md) | Domain terminology |
| [Architecture Overview](../architecture-overview.md) | Repository structure and design philosophy |
| [Learning Roadmap](../roadmap.md) | Recommended learning path |
| [Templates](../templates/) | Document templates |

---

## Foundations — Phase 2

| Document | Status | Description |
|----------|--------|-------------|
| [Phase 2 Index](../../domains/foundations/README.md) | Published | Module hub and learning path |
| [AI Engineering Overview](../../domains/foundations/ai-engineering-overview.md) | Published | Role definition, stack, production principles |
| [Software Engineering for AI](../../domains/foundations/software-engineering-for-ai.md) | Published | Clean architecture, SOLID, patterns |
| [AI Application Lifecycle](../../domains/foundations/ai-application-lifecycle.md) | Published | Idea to iteration lifecycle |
| [Development Workflow](../../domains/foundations/development-workflow.md) | Published | Professional engineering workflow |
| [Configuration and Secrets](../../domains/foundations/configuration-and-secrets.md) | Published | Env vars, secrets, Pydantic settings |
| [Testing Fundamentals](../../domains/foundations/testing-fundamentals.md) | Published | pytest, mocking, API testing |
| [Git and GitHub Workflow](../../domains/foundations/git-github-workflow.md) | Published | Branching, PRs, CI/CD, releases |
| [Engineering Best Practices](../../domains/foundations/engineering-best-practices.md) | Published | Code reviews, naming, maintainability |

[Domain index →](../../domains/foundations/README.md)

---

## Engineering

### Python Engineering

| Document | Status | Description |
|----------|--------|-------------|
| [Python for AI Engineering](../../domains/python-engineering/python-for-ai-engineering.md) | Published | Async, typing, Pydantic, project layout |

[Domain index →](../../domains/python-engineering/README.md)

### Backend Engineering — Phase 2

| Document | Status | Description |
|----------|--------|-------------|
| [Backend Fundamentals for AI](../../domains/backend-engineering/backend-fundamentals-for-ai.md) | Published | Request lifecycle, middleware, async, streaming |

### Backend Engineering — Phase 3

| Document | Status | Description |
|----------|--------|-------------|
| [Backend Architecture for AI](../../domains/backend-engineering/backend-architecture-for-ai.md) | Published | Layered, clean, hexagonal architecture |
| [HTTP Clients for AI Backends](../../domains/backend-engineering/http-clients-for-ai-backends.md) | Published | httpx, retries, pooling, streaming, LLM APIs |
| [Validation for AI APIs](../../domains/backend-engineering/validation-for-ai-apis.md) | Published | Pydantic v2, validators, response validation |
| [Error Handling for AI Backends](../../domains/backend-engineering/error-handling-for-ai-backends.md) | Published | Exception hierarchy, fallbacks, degradation |
| [Async Programming for AI Backends](../../domains/backend-engineering/async-programming-for-ai-backends.md) | Published | asyncio, event loop, concurrency patterns |
| [File Handling for AI](../../domains/backend-engineering/file-handling-for-ai.md) | Published | Uploads, object storage, multimodal formats |
| [Background Processing for AI](../../domains/backend-engineering/background-processing-for-ai.md) | Published | Celery, ARQ, workers, ingestion jobs |
| [Configuration Management for Backends](../../domains/backend-engineering/configuration-management-for-backends.md) | Published | Phase 3 — settings, env separation, feature flags |
| [Testing Backend for AI](../../domains/backend-engineering/testing-backend-for-ai.md) | Published | pytest, API/integration tests, mocking, coverage |

[Domain index →](../../domains/backend-engineering/README.md)

### APIs

| Document | Status | Description |
|----------|--------|-------------|
| [HTTP Fundamentals for AI](../../domains/apis/http-fundamentals-for-ai.md) | Published | REST, auth, JWT, streaming, rate limiting |

[Domain index →](../../domains/apis/README.md)

### FastAPI

| Document | Status | Description |
|----------|--------|-------------|
| [FastAPI Foundation](../../domains/fastapi/fastapi-foundation.md) | Published | FastAPI patterns for AI applications |

[Domain index →](../../domains/fastapi/README.md)

### Databases — Phase 2

| Document | Status | Description |
|----------|--------|-------------|
| [Databases for AI Applications](../../domains/databases/databases-for-ai-applications.md) | Published | SQL, Redis, object storage, vector DB overview |
| [PostgreSQL for AI](../../domains/databases/postgresql/postgresql-for-ai.md) | Published | pgvector, JSONB, production tuning |
| [Redis for AI](../../domains/databases/redis/redis-for-ai.md) | Published | Caching, rate limiting, sessions |

### Databases — Phase 3

| Document | Status | Description |
|----------|--------|-------------|
| [SQLAlchemy for AI Applications](../../domains/databases/postgresql/sqlalchemy-for-ai-applications.md) | Published | Async ORM, models, repositories, schema design |
| [Alembic Migrations for AI](../../domains/databases/postgresql/alembic-migrations-for-ai.md) | Published | Migrations, rollbacks, zero-downtime, CI |
| [Redis Backend Patterns for AI](../../domains/databases/redis/redis-backend-patterns-for-ai.md) | Published | Backend services, jobs, locks, performance |

[Domain index →](../../domains/databases/README.md)

---

## LLM Systems

### LLM Engineering — Phase 4

| Document | Status | Description |
|----------|--------|-------------|
| [Phase 4 Index](../../domains/llm-engineering/README.md) | Published | Module hub and learning path |
| [Introduction to LLM Engineering](../../domains/llm-engineering/introduction-to-llm-engineering.md) | Published | LLM fundamentals and ecosystem |
| [How LLMs Work](../../domains/llm-engineering/how-llms-work.md) | Published | Inference pipeline internals |
| [Tokens and Tokenization](../../domains/llm-engineering/tokens-and-tokenization.md) | Published | BPE, counting, cost |
| [Context Windows](../../domains/llm-engineering/context-windows.md) | Published | Budgeting and truncation |
| [Embeddings — LLM Perspective](../../domains/llm-engineering/embeddings-llm-perspective.md) | Published | Vectors and similarity |
| [Transformer Intuition](../../domains/llm-engineering/transformer-intuition.md) | Published | Decoder architecture |
| [Attention Mechanism](../../domains/llm-engineering/attention-mechanism.md) | Published | Q/K/V and long context |
| [KV Cache](../../domains/llm-engineering/kv-cache.md) | Published | Prefill, decode, memory |
| [LLM Inference](../../domains/llm-engineering/llm-inference.md) | Published | Batching, streaming, latency |
| [Sampling and Decoding](../../domains/llm-engineering/sampling-and-decoding.md) | Published | Temperature, top-p, penalties |
| [Structured Outputs](../../domains/llm-engineering/structured-outputs.md) | Published | JSON mode, Pydantic |
| [Function Calling and Tools](../../domains/llm-engineering/function-calling-and-tools.md) | Published | Tool orchestration |
| [LLM Streaming](../../domains/llm-engineering/llm-streaming.md) | Published | SSE and UX |
| [Vision and Multimodal](../../domains/llm-engineering/vision-and-multimodal-models.md) | Published | Images, audio, video |
| [Model Comparison Guide](../../domains/llm-engineering/model-comparison-guide.md) | Published | 9 model families |
| [LLM Cost Optimization](../../domains/llm-engineering/llm-cost-optimization.md) | Published | Token and cost control |
| [LLM Performance Optimization](../../domains/llm-engineering/llm-performance-optimization.md) | Published | Latency and routing |
| [LLM Security Fundamentals](../../domains/llm-engineering/llm-security-fundamentals.md) | Published | Injection, secrets |
| [LLM Engineering Mistakes](../../domains/llm-engineering/llm-engineering-mistakes.md) | Published | 12 failure patterns |
| [OpenAI Provider](../../domains/llm-engineering/providers/openai.md) | Published | OpenAI API guide |
| [Google Gemini Provider](../../domains/llm-engineering/providers/google-gemini.md) | Published | Gemini API guide |
| [Anthropic Claude Provider](../../domains/llm-engineering/providers/anthropic-claude.md) | Published | Claude API guide |
| [Groq Provider](../../domains/llm-engineering/providers/groq.md) | Published | Groq fast inference |
| [OpenRouter Provider](../../domains/llm-engineering/providers/openrouter.md) | Published | Multi-provider routing |
| [Ollama Provider](../../domains/llm-engineering/providers/ollama.md) | Published | Local inference |

[Domain index →](../../domains/llm-engineering/README.md)

### Prompt Engineering — Phase 5

| Document | Status | Description |
|----------|--------|-------------|
| [Phase 5 Index](../../domains/prompt-engineering/README.md) | Published | Module hub and learning path |
| [Introduction to Prompt Engineering](../../domains/prompt-engineering/introduction-to-prompt-engineering.md) | Published | PE as software discipline |
| [Prompt Anatomy](../../domains/prompt-engineering/prompt-anatomy.md) | Published | Components of production prompts |
| [Message Types](../../domains/prompt-engineering/message-types.md) | Published | System, user, assistant, tool |
| [Prompt Design Principles](../../domains/prompt-engineering/prompt-design-principles.md) | Published | Clarity, decomposition, constraints |
| [Prompt Patterns](../../domains/prompt-engineering/prompt-patterns.md) | Published | 11 reusable patterns |
| [Prompt Templates Guide](../../domains/prompt-engineering/prompt-templates-guide.md) | Published | Template library guide |
| [Structured Prompting](../../domains/prompt-engineering/structured-prompting.md) | Published | XML, JSON, Markdown, tags |
| [Prompting Strategies](../../domains/prompt-engineering/prompting-strategies.md) | Published | Zero-shot through few-shot |
| [Advanced Reasoning Strategies](../../domains/prompt-engineering/advanced-reasoning-strategies.md) | Published | CoT, ReAct, ToT, reflection |
| [Prompt Chaining](../../domains/prompt-engineering/prompt-chaining.md) | Published | Multi-step pipelines |
| [Prompt Lifecycle](../../domains/prompt-engineering/prompt-lifecycle.md) | Published | Design through iteration |
| [Prompt Versioning](../../domains/prompt-engineering/prompt-versioning.md) | Published | Version control, A/B testing |
| [Prompt Testing](../../domains/prompt-engineering/prompt-testing.md) | Published | Golden datasets, regression |
| [Prompt Evaluation](../../domains/prompt-engineering/prompt-evaluation.md) | Published | Quality metrics, automated eval |
| [Prompt Optimization](../../domains/prompt-engineering/prompt-optimization.md) | Published | Tokens, latency, consistency |
| [Prompt Security](../../domains/prompt-engineering/prompt-security.md) | Published | Injection, hardening |
| [Prompt Engineering Mistakes](../../domains/prompt-engineering/prompt-engineering-mistakes.md) | Published | 12 failure patterns |
| [Production Prompt Engineering](../../domains/prompt-engineering/production-prompt-engineering.md) | Published | Repos, caching, observability |
| [Prompt Comparison Guides](../../domains/prompt-engineering/prompt-comparison-guides.md) | Published | Strategy comparison tables |

[Domain index →](../../domains/prompt-engineering/README.md)

### Context Engineering

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/context-engineering/README.md)

### Embeddings

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/embeddings/README.md)

### Vector Databases

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/vector-databases/README.md)

---

## Retrieval and Agents

### RAG

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/rag/README.md)

### AI Agents

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/ai-agents/README.md)

### Agent Architectures

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/agent-architectures/README.md)

### MCP

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/mcp/README.md)

### A2A (Agent-to-Agent)

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/a2a/README.md)

### AI Workflows

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/ai-workflows/README.md)

### Multi-Agent Systems

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/multi-agent-systems/README.md)

---

## Production

### AI Evaluation

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/ai-evaluation/README.md)

### AI Safety

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/ai-safety/README.md)

### Model Integration

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/model-integration/README.md)

### Model Serving

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/model-serving/README.md)

### Inference Optimization

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/inference-optimization/README.md)

### AI Deployment

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/ai-deployment/README.md)

### Cloud Deployment

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/cloud-deployment/README.md)

### Docker

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/docker/README.md)

### CI/CD

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/cicd/README.md)

### Monitoring

| Document | Status | Description |
|----------|--------|-------------|
| [Monitoring Foundation for AI Backends](../../domains/monitoring/monitoring-foundation-for-ai-backends.md) | Published | Phase 3 — health, metrics, tracing, OTel, Prometheus, Grafana |

[Domain index →](../../domains/monitoring/README.md)

### Logging

| Document | Status | Description |
|----------|--------|-------------|
| [Logging and Error Handling](../../domains/logging/logging-and-error-handling.md) | Published | Structured logs, retries, graceful failures |
| [Backend Logging for AI](../../domains/logging/backend-logging-for-ai.md) | Published | Phase 3 — JSON logs, correlation IDs, audit logging |

[Domain index →](../../domains/logging/README.md)

### Observability

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/observability/README.md)

### Security — Phase 3

| Document | Status | Description |
|----------|--------|-------------|
| [Authentication and Authorization for AI](../../domains/security/authentication-authorization-for-ai.md) | Published | JWT, OAuth2, API keys, RBAC, protected routes |
| [Security for AI Backends](../../domains/security/security-for-ai-backends.md) | Published | HTTPS, CORS, injection, SSRF, rate limiting, headers |

[Domain index →](../../domains/security/README.md)

### Performance Optimization — Phase 3

| Document | Status | Description |
|----------|--------|-------------|
| [Backend Performance for AI](../../domains/performance-optimization/backend-performance-for-ai.md) | Published | Profiling, caching, pooling, pagination, streaming |

[Domain index →](../../domains/performance-optimization/README.md)

---

## Architecture

### AI System Design

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/ai-system-design/README.md)

### AI Application Architecture

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/ai-application-architecture/README.md)

### Software Architecture

| Document | Status | Description |
|----------|--------|-------------|
| [Architecture Patterns Foundation](../../domains/software-architecture/architecture-patterns-foundation.md) | Published | Client-server, layered, event-driven, monolith |

[Domain index →](../../domains/software-architecture/README.md)

### Design Patterns

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/design-patterns/README.md)

### Distributed Systems

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/distributed-systems/README.md)

---

## Data and Operations

### Data Engineering

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/data-engineering/README.md)

### Debugging

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/debugging/README.md)

### Common Mistakes

| Document | Status | Description |
|----------|--------|-------------|
| [Common Engineering Mistakes](../../domains/common-mistakes/common-engineering-mistakes.md) | Published | 20 mistakes with bad vs good patterns |

[Domain index →](../../domains/common-mistakes/README.md)

### Production Incidents

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/production-incidents/README.md)

---

## Career and Research

### Interview Preparation

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/interview-preparation/README.md)

### Papers

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/papers/README.md)

### Research Notes

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/research-notes/README.md)

### Career Notes

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/career-notes/README.md)

### Resources

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/resources/README.md)

---

## Cross-Cutting Indexes

- [Topic Indexes](topics/)
- [Tag Registry](tags/tag-registry.md)
- [Technology Indexes](technologies/)
- [Architecture Pattern Indexes](patterns/)
- [Comparison Indexes](comparisons/)
- [Keyword Index](keyword-index.md)

---

## See Also

- [Domains Overview](../../domains/README.md)
- [Learning Roadmap](../roadmap.md)
