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

### Context Engineering — Phase 6

| Document | Status | Description |
|----------|--------|-------------|
| [Phase 6 Index](../../domains/context-engineering/README.md) | Published | Module hub and learning path |
| [Introduction to Context Engineering](../../domains/context-engineering/introduction-to-context-engineering.md) | Published | CE as engineering discipline |
| [Context Architecture](../../domains/context-engineering/context-architecture.md) | Published | Pipeline and component design |
| [Context Windows](../../domains/context-engineering/context-windows.md) | Published | Application-level window engineering |
| [Conversation State](../../domains/context-engineering/conversation-state.md) | Published | Session and agent state |
| [Memory Systems](../../domains/context-engineering/memory-systems.md) | Published | Six memory types |
| [Conversation History](../../domains/context-engineering/conversation-history.md) | Published | Pruning, summarization, threads |
| [Context Selection](../../domains/context-engineering/context-selection.md) | Published | Filtering and prioritization |
| [Context Ranking](../../domains/context-engineering/context-ranking.md) | Published | Hybrid ranking strategies |
| [Dynamic Context](../../domains/context-engineering/dynamic-context.md) | Published | Runtime context assembly |
| [Context Compression](../../domains/context-engineering/context-compression.md) | Published | Token reduction techniques |
| [Long Context Strategies](../../domains/context-engineering/long-context-strategies.md) | Published | Map-reduce, hierarchical, hybrid |
| [Retrieval Context](../../domains/context-engineering/retrieval-context.md) | Published | Knowledge injection foundation |
| [Context Budgeting](../../domains/context-engineering/context-budgeting.md) | Published | Token and cost allocation |
| [Context Caching](../../domains/context-engineering/context-caching.md) | Published | Latency and cost caching |
| [Context Personalization](../../domains/context-engineering/context-personalization.md) | Published | Profiles and preferences |
| [Multi-Agent Context Sharing](../../domains/context-engineering/multi-agent-context-sharing.md) | Published | Blackboard and coordination |
| [Context Quality](../../domains/context-engineering/context-quality.md) | Published | Context metrics |
| [Context Security](../../domains/context-engineering/context-security.md) | Published | PII, isolation, leakage |
| [Production Context Engineering](../../domains/context-engineering/production-context-engineering.md) | Published | Observability, A/B testing |
| [Context Engineering Mistakes](../../domains/context-engineering/context-engineering-mistakes.md) | Published | Troubleshooting guide |
| [Context Comparison Guides](../../domains/context-engineering/context-comparison-guides.md) | Published | Strategy comparison tables |

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

### RAG — Phase 7

| Document | Status | Description |
|----------|--------|-------------|
| [Phase 7 Index](../../domains/rag/README.md) | Published | Module hub — largest handbook section |
| [Introduction to RAG](../../domains/rag/introduction-to-rag.md) | Published | RAG fundamentals and types |
| [End-to-End RAG Architecture](../../domains/rag/end-to-end-rag-architecture.md) | Published | Complete pipeline |
| [Document Ingestion Pipeline](../../domains/rag/document-ingestion-pipeline.md) | Published | PDF, code, web ingestion |
| [Chunking](../../domains/rag/chunking.md) | Published | All chunking strategies |
| [Metadata Engineering](../../domains/rag/metadata-engineering.md) | Published | ACL, filtering, lineage |
| [Embeddings for RAG](../../domains/rag/embeddings-for-rag.md) | Published | Models, metrics, versioning |
| [Vector Databases](../../domains/rag/vector-databases.md) | Published | ANN, HNSW, IVF fundamentals |
| [Retrieval Strategies](../../domains/rag/retrieval-strategies.md) | Published | Dense, hybrid, multi-hop |
| [BM25](../../domains/rag/bm25.md) | Published | Lexical retrieval |
| [Query Engineering](../../domains/rag/query-engineering.md) | Published | HyDE, rewriting, routing |
| [Reranking](../../domains/rag/reranking.md) | Published | Cross-encoders, API rerankers |
| [RAG Context Compression](../../domains/rag/rag-context-compression.md) | Published | Passage budgeting |
| [RAG Prompt Assembly](../../domains/rag/rag-prompt-assembly.md) | Published | Context formatting |
| [Citations and Grounding](../../domains/rag/citations-and-grounding.md) | Published | Attribution, traceability |
| [Hallucination Prevention](../../domains/rag/hallucination-prevention.md) | Published | Abstention, validation |
| [RAG Evaluation](../../domains/rag/rag-evaluation.md) | Published | Metrics, RAGAS, golden sets |
| [Advanced RAG Architectures](../../domains/rag/advanced-rag-architectures.md) | Published | GraphRAG, Self-RAG, agentic |
| [Production RAG](../../domains/rag/production-rag.md) | Published | Ops, scaling, multi-tenant |
| [RAG System Design](../../domains/rag/rag-system-design.md) | Published | Enterprise patterns |
| [RAG Mistakes](../../domains/rag/rag-mistakes.md) | Published | Troubleshooting |
| [RAG Comparison Guides](../../domains/rag/rag-comparison-guides.md) | Published | Decision matrices |
| [Vector DB Providers](../../domains/rag/providers/README.md) | Published | FAISS, Chroma, PGVector, Pinecone, Milvus, Weaviate, Qdrant |

[Domain index →](../../domains/rag/README.md)

### AI Agents — Phase 8

| Document | Status | Description |
|----------|--------|-------------|
| [Phase 8 Index](../../domains/ai-agents/README.md) | Published | Agent engineering handbook hub |
| [Introduction to Agent Engineering](../../domains/ai-agents/introduction-to-agent-engineering.md) | Published | Agents as software discipline |
| [Agent Architecture](../../domains/ai-agents/agent-architecture.md) | Published | Planner-executor-reflection stack |
| [Agent Fundamentals](../../domains/ai-agents/agent-fundamentals.md) | Published | Goals, perception, action |
| [Reasoning Patterns](../../domains/ai-agents/agent-reasoning-patterns.md) | Published | ReAct, reflection, ToT |
| [Agent Planning](../../domains/ai-agents/agent-planning.md) | Published | Decomposition, replanning |
| [Agent Memory Systems](../../domains/ai-agents/agent-memory-systems.md) | Published | Layered agent memory |
| [Tool Use](../../domains/ai-agents/tool-use.md) | Published | Registry, execution, permissions |
| [Agent State Management](../../domains/ai-agents/agent-state-management.md) | Published | Checkpointing, recovery |
| [Task Graphs](../../domains/ai-agents/task-graphs.md) | Published | DAG execution |
| [Event-Driven Agents](../../domains/ai-agents/event-driven-agents.md) | Published | Pub/sub, triggers |
| [Multi-Agent Systems](../../domains/ai-agents/multi-agent-systems.md) | Published | Supervisor, swarm, debate |
| [Human-in-the-Loop](../../domains/ai-agents/human-in-the-loop.md) | Published | Approval, escalation |
| [Agent Communication](../../domains/ai-agents/agent-communication.md) | Published | Coordination patterns |
| [Agent Frameworks](../../domains/ai-agents/frameworks/README.md) | Published | 6 framework guides |
| [Build Your Own Framework](../../domains/ai-agents/build-your-own-agent-framework.md) | Published | Minimal agent framework |
| [Agent Evaluation](../../domains/ai-agents/agent-evaluation.md) | Published | Task success, tool accuracy |
| [Production Agent Engineering](../../domains/ai-agents/production-agent-engineering.md) | Published | Observability, scaling |
| [Agent Security](../../domains/ai-agents/agent-security.md) | Published | Sandboxing, injection |
| [Agent Engineering Mistakes](../../domains/ai-agents/agent-engineering-mistakes.md) | Published | Troubleshooting |
| [Agent Case Studies](../../domains/ai-agents/agent-case-studies.md) | Published | Coding, research, support |
| [Agent Comparison Guides](../../domains/ai-agents/agent-comparison-guides.md) | Published | Framework & pattern matrices |

[Domain index →](../../domains/ai-agents/README.md)

### Agent Architectures

| Document | Status | Description |
|----------|--------|-------------|
| [Multi-Agent Systems](../../domains/ai-agents/multi-agent-systems.md) | Published | Architecture catalog (Phase 8) |
| [Agent Case Studies](../../domains/ai-agents/agent-case-studies.md) | Published | Real-world patterns |

[Domain index →](../../domains/agent-architectures/README.md)

[Domain index →](../../domains/agent-architectures/README.md)

### MCP — Phase 9

| Document | Status | Description |
|----------|--------|-------------|
| [Phase 9 Index](../../domains/mcp/README.md) | Published | MCP engineering handbook hub |
| [Introduction to MCP](../../domains/mcp/introduction-to-mcp.md) | Published | Why MCP exists, ecosystem |
| [MCP Architecture](../../domains/mcp/mcp-architecture.md) | Published | Client, transport, server layers |
| [MCP Lifecycle](../../domains/mcp/mcp-lifecycle.md) | Published | Initialize through termination |
| [MCP Core Concepts](../../domains/mcp/mcp-core-concepts.md) | Published | Clients, servers, primitives |
| [MCP Client](../../domains/mcp/mcp-client.md) | Published | Connection, discovery, retries |
| [MCP Server](../../domains/mcp/mcp-server.md) | Published | Registration, routing, shutdown |
| [MCP Resources](../../domains/mcp/mcp-resources.md) | Published | URI design, discovery, caching |
| [MCP Prompts](../../domains/mcp/mcp-prompts.md) | Published | Templates, registry, validation |
| [MCP Tools](../../domains/mcp/mcp-tools.md) | Published | Schemas, permissions, streaming |
| [Transport Layer](../../domains/mcp/mcp-transport-layer.md) | Published | STDIO, HTTP, SSE, WebSockets |
| [Message Protocol](../../domains/mcp/mcp-message-protocol.md) | Published | JSON-RPC messages |
| [Authentication](../../domains/mcp/mcp-authentication.md) | Published | OAuth, RBAC, secrets |
| [Streaming](../../domains/mcp/mcp-streaming.md) | Published | Partial results, cancellation |
| [Multi-Server MCP](../../domains/mcp/multi-server-mcp.md) | Published | Routing, federation, failover |
| [Build an MCP Server](../../domains/mcp/build-an-mcp-server.md) | Published | Production server tutorial |
| [Build an MCP Client](../../domains/mcp/build-an-mcp-client.md) | Published | Production client tutorial |
| [Production MCP](../../domains/mcp/production-mcp.md) | Published | Observability, scaling, HA |
| [MCP Security](../../domains/mcp/mcp-security.md) | Published | Sandboxing, audit, injection |
| [MCP Mistakes](../../domains/mcp/mcp-engineering-mistakes.md) | Published | Troubleshooting playbook |
| [Real-World Architectures](../../domains/mcp/mcp-real-world-architectures.md) | Published | Six production patterns |
| [MCP Comparison Guides](../../domains/mcp/mcp-comparison-guides.md) | Published | Decision matrices |

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

### AI Evaluation — Phase 10

| Document | Status | Description |
|----------|--------|-------------|
| [Phase 10 Index](../../domains/ai-evaluation/README.md) | Published | AI evaluation handbook hub |
| [Introduction to AI Evaluation](../../domains/ai-evaluation/introduction-to-ai-evaluation.md) | Published | Offline vs online, LLMOps |
| [Evaluation Architecture](../../domains/ai-evaluation/evaluation-architecture.md) | Published | End-to-end pipeline |
| [Evaluation Datasets](../../domains/ai-evaluation/evaluation-datasets.md) | Published | Golden sets, versioning |
| [Core Metrics](../../domains/ai-evaluation/core-metrics.md) | Published | Accuracy, F1, BLEU, ROUGE |
| [LLM Evaluation Metrics](../../domains/ai-evaluation/llm-evaluation-metrics.md) | Published | Faithfulness, relevance |
| [Hallucination Detection](../../domains/ai-evaluation/hallucination-detection.md) | Published | Types and strategies |
| [RAG Evaluation](../../domains/ai-evaluation/rag-evaluation.md) | Published | RAGAS, retrieval metrics |
| [Prompt Evaluation](../../domains/ai-evaluation/prompt-evaluation.md) | Published | Regression, robustness |
| [Agent Evaluation](../../domains/ai-evaluation/agent-evaluation.md) | Published | Task completion, tools |
| [Evaluation Frameworks](../../domains/ai-evaluation/evaluation-frameworks.md) | Published | Framework selection |
| [Human Evaluation](../../domains/ai-evaluation/human-evaluation.md) | Published | Rubrics, agreement |
| [Latency Evaluation](../../domains/ai-evaluation/latency-evaluation.md) | Published | P95, TTFT budgets |
| [Cost Evaluation](../../domains/ai-evaluation/cost-evaluation.md) | Published | Token and infra cost |
| [Benchmarking](../../domains/ai-evaluation/benchmarking.md) | Published | Public and internal benches |
| [A/B Testing](../../domains/ai-evaluation/ab-testing.md) | Published | Experiments, canary |
| [Continuous Evaluation](../../domains/ai-evaluation/continuous-evaluation.md) | Published | CI/CD, drift detection |
| [Evaluation Dashboards](../../domains/ai-evaluation/evaluation-dashboards.md) | Published | Quality and exec views |
| [Production Evaluation](../../domains/ai-evaluation/production-evaluation.md) | Published | Scale, governance |
| [Evaluation Mistakes](../../domains/ai-evaluation/evaluation-mistakes.md) | Published | Troubleshooting |
| [Evaluation Case Studies](../../domains/ai-evaluation/evaluation-case-studies.md) | Published | Real-world patterns |
| [Comparison Guides](../../domains/ai-evaluation/ai-evaluation-comparison-guides.md) | Published | Decision matrices |
| [Framework Guides](../../domains/ai-evaluation/frameworks/README.md) | Published | RAGAS, DeepEval, etc. |

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
