# Master Index

> Complete index of all published documents in the AI Engineering Playbook.
> Last updated: 2026-07-23

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
| [Capstone Walkthrough](../capstone-walkthrough.md) | End-to-end RAG chat API tutorial |
| [Templates](../templates/) | Document templates |

---

## Foundations

### Foundations

| Document | Status | Description |
|----------|--------|-------------|
| [Module hub](../../domains/foundations/README.md) | Published | Module hub and learning path |
| [AI Engineering Overview](../../domains/foundations/ai-engineering-overview.md) | Published | Role definition, stack, production principles |
| [Software Engineering for AI](../../domains/foundations/software-engineering-for-ai.md) | Published | Clean architecture, SOLID, patterns |
| [AI Application Lifecycle](../../domains/foundations/ai-application-lifecycle.md) | Published | Idea to iteration lifecycle |
| [Development Workflow](../../domains/foundations/development-workflow.md) | Published | Professional engineering workflow |
| [Configuration and Secrets](../../domains/foundations/configuration-and-secrets.md) | Published | Env vars, secrets, Pydantic settings |
| [Testing Fundamentals](../../domains/foundations/testing-fundamentals.md) | Published | pytest, mocking, API testing |
| [Git and GitHub Workflow](../../domains/foundations/git-github-workflow.md) | Published | Branching, PRs, CI/CD, releases |
| [Engineering Best Practices](../../domains/foundations/engineering-best-practices.md) | Published | Code reviews, naming, maintainability |

[Domain index →](../../domains/foundations/README.md)

### Python Engineering

| Document | Status | Description |
|----------|--------|-------------|
| [Python for AI Engineering](../../domains/python-engineering/python-for-ai-engineering.md) | Published | Async, typing, Pydantic, project layout |

[Domain index →](../../domains/python-engineering/README.md)

### Backend Engineering

| Document | Status | Description |
|----------|--------|-------------|
| [Backend Fundamentals for AI](../../domains/backend-engineering/backend-fundamentals-for-ai.md) | Published | Request lifecycle, middleware, async, streaming |
| [Backend Architecture for AI](../../domains/backend-engineering/backend-architecture-for-ai.md) | Published | Layered, clean, hexagonal architecture |
| [HTTP Clients for AI Backends](../../domains/backend-engineering/http-clients-for-ai-backends.md) | Published | httpx, retries, pooling, streaming, LLM APIs |
| [Validation for AI APIs](../../domains/backend-engineering/validation-for-ai-apis.md) | Published | Pydantic v2, validators, response validation |
| [Error Handling for AI Backends](../../domains/backend-engineering/error-handling-for-ai-backends.md) | Published | Exception hierarchy, fallbacks, degradation |
| [Async Programming for AI Backends](../../domains/backend-engineering/async-programming-for-ai-backends.md) | Published | asyncio, event loop, concurrency patterns |
| [File Handling for AI](../../domains/backend-engineering/file-handling-for-ai.md) | Published | Uploads, object storage, multimodal formats |
| [Background Processing for AI](../../domains/backend-engineering/background-processing-for-ai.md) | Published | Celery, ARQ, workers, ingestion jobs |
| [Configuration Management for Backends](../../domains/backend-engineering/configuration-management-for-backends.md) | Published | settings, env separation, feature flags |
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

### Databases

| Document | Status | Description |
|----------|--------|-------------|
| [Databases for AI Applications](../../domains/databases/databases-for-ai-applications.md) | Published | SQL, Redis, object storage, vector DB overview |
| [PostgreSQL for AI](../../domains/databases/postgresql/postgresql-for-ai.md) | Published | pgvector, JSONB, production tuning |
| [Redis for AI](../../domains/databases/redis/redis-for-ai.md) | Published | Caching, rate limiting, sessions |
| [SQLAlchemy for AI Applications](../../domains/databases/postgresql/sqlalchemy-for-ai-applications.md) | Published | Async ORM, models, repositories, schema design |
| [Alembic Migrations for AI](../../domains/databases/postgresql/alembic-migrations-for-ai.md) | Published | Migrations, rollbacks, zero-downtime, CI |
| [Redis Backend Patterns for AI](../../domains/databases/redis/redis-backend-patterns-for-ai.md) | Published | Backend services, jobs, locks, performance |

[Domain index →](../../domains/databases/README.md)

### Security

| Document | Status | Description |
|----------|--------|-------------|
| [Authentication and Authorization for AI](../../domains/security/authentication-authorization-for-ai.md) | Published | JWT, OAuth2, API keys, RBAC, protected routes |
| [Security for AI Backends](../../domains/security/security-for-ai-backends.md) | Published | HTTPS, CORS, injection, SSRF, rate limiting, headers |

[Domain index →](../../domains/security/README.md)

### Performance Optimization

| Document | Status | Description |
|----------|--------|-------------|
| [Backend Performance for AI](../../domains/performance-optimization/backend-performance-for-ai.md) | Published | Profiling, caching, pooling, pagination, streaming |

[Domain index →](../../domains/performance-optimization/README.md)

---

### Software Architecture

| Document | Status | Description |
|----------|--------|-------------|
| [Architecture Patterns Foundation](../../domains/software-architecture/architecture-patterns-foundation.md) | Published | Client-server, layered, event-driven, monolith |

[Domain index →](../../domains/software-architecture/README.md)

---

## Core (LLM Interaction)

### LLM Engineering

| Document | Status | Description |
|----------|--------|-------------|
| [Module hub](../../domains/llm-engineering/README.md) | Published | Module hub and learning path |
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

### Prompt Engineering

| Document | Status | Description |
|----------|--------|-------------|
| [Module hub](../../domains/prompt-engineering/README.md) | Published | Module hub and learning path |
| [Introduction to Prompt Engineering](../../domains/prompt-engineering/foundations/01-introduction-to-prompt-engineering.md) | Published | PE as software discipline |
| [Prompt Anatomy](../../domains/prompt-engineering/foundations/02-prompt-anatomy.md) | Published | Components of production prompts |
| [Message Types](../../domains/prompt-engineering/foundations/03-message-types.md) | Published | System, user, assistant, tool |
| [Prompt Design Principles](../../domains/prompt-engineering/foundations/04-prompt-design-principles.md) | Published | Clarity, decomposition, constraints |
| [Prompt Patterns](../../domains/prompt-engineering/craft/01-prompt-patterns.md) | Published | 11 reusable patterns |
| [Prompt Templates Guide](../../domains/prompt-engineering/craft/02-prompt-templates-guide.md) | Published | Template library guide |
| [Structured Prompting](../../domains/prompt-engineering/craft/03-structured-prompting.md) | Published | XML, JSON, Markdown, tags |
| [Prompting Strategies](../../domains/prompt-engineering/craft/04-prompting-strategies.md) | Published | Zero-shot through few-shot |
| [Advanced Reasoning Strategies](../../domains/prompt-engineering/reasoning-strategies/01-advanced-reasoning-strategies.md) | Published | CoT, ReAct, ToT, reflection |
| [Prompt Chaining](../../domains/prompt-engineering/reasoning-strategies/02-prompt-chaining.md) | Published | Multi-step pipelines |
| [Prompt Lifecycle](../../domains/prompt-engineering/prompt-operations/01-prompt-lifecycle.md) | Published | Design through iteration |
| [Prompt Versioning](../../domains/prompt-engineering/prompt-operations/02-prompt-versioning.md) | Published | Version control, A/B testing |
| [Prompt Testing](../../domains/prompt-engineering/prompt-operations/03-prompt-testing.md) | Published | Golden datasets, regression |
| [Prompt Evaluation](../../domains/prompt-engineering/prompt-operations/04-prompt-evaluation.md) | Published | Quality metrics, automated eval |
| [Prompt Optimization](../../domains/prompt-engineering/prompt-operations/05-prompt-optimization.md) | Published | Tokens, latency, consistency |
| [Prompt Security](../../domains/prompt-engineering/production-and-safety/01-prompt-security.md) | Published | Injection, hardening |
| [Prompt Engineering Mistakes](../../domains/prompt-engineering/production-and-safety/02-prompt-engineering-mistakes.md) | Published | 12 failure patterns |
| [Production Prompt Engineering](../../domains/prompt-engineering/production-and-safety/03-production-prompt-engineering.md) | Published | Repos, caching, observability |
| [Prompt Comparison Guides](../../domains/prompt-engineering/production-and-safety/04-prompt-comparison-guides.md) | Published | Strategy comparison tables |

[Domain index →](../../domains/prompt-engineering/README.md)

### Context Engineering

| Document | Status | Description |
|----------|--------|-------------|
| [Module hub](../../domains/context-engineering/README.md) | Published | Module hub and learning path |
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

---

## Retrieval & Agents

### RAG

| Document | Status | Description |
|----------|--------|-------------|
| [Module hub](../../domains/rag/README.md) | Published | Module hub — largest handbook section |
| [Introduction to RAG](../../domains/rag/foundations/01-introduction-to-rag.md) | Published | RAG fundamentals and types |
| [End-to-End RAG Architecture](../../domains/rag/foundations/02-end-to-end-rag-architecture.md) | Published | Complete pipeline |
| [Document Ingestion Pipeline](../../domains/rag/ingestion/01-document-ingestion-pipeline.md) | Published | PDF, code, web ingestion |
| [Chunking](../../domains/rag/ingestion/02-chunking.md) | Published | All chunking strategies |
| [Metadata Engineering](../../domains/rag/ingestion/03-metadata-engineering.md) | Published | ACL, filtering, lineage |
| [Embeddings for RAG](../../domains/rag/retrieval/01-embeddings-for-rag.md) | Published | Models, metrics, versioning |
| [Vector Databases](../../domains/rag/retrieval/02-vector-databases.md) | Published | ANN, HNSW, IVF fundamentals |
| [Retrieval Strategies](../../domains/rag/retrieval/04-retrieval-strategies.md) | Published | Dense, hybrid, multi-hop |
| [BM25](../../domains/rag/retrieval/03-bm25.md) | Published | Lexical retrieval |
| [Query Engineering](../../domains/rag/retrieval/05-query-engineering.md) | Published | HyDE, rewriting, routing |
| [Reranking](../../domains/rag/retrieval/06-reranking.md) | Published | Cross-encoders, API rerankers |
| [RAG Context Compression](../../domains/rag/generation-and-grounding/04-rag-context-compression.md) | Published | Passage budgeting |
| [RAG Prompt Assembly](../../domains/rag/generation-and-grounding/01-rag-prompt-assembly.md) | Published | Context formatting |
| [Citations and Grounding](../../domains/rag/generation-and-grounding/02-citations-and-grounding.md) | Published | Attribution, traceability |
| [Hallucination Prevention](../../domains/rag/generation-and-grounding/03-hallucination-prevention.md) | Published | Abstention, validation |
| [RAG Evaluation](../../domains/rag/evaluation-and-production/01-rag-evaluation.md) | Published | Metrics, RAGAS, golden sets |
| [Advanced RAG Architectures](../../domains/rag/foundations/03-advanced-rag-architectures.md) | Published | GraphRAG, Self-RAG, agentic |
| [Production RAG](../../domains/rag/evaluation-and-production/02-production-rag.md) | Published | Ops, scaling, multi-tenant |
| [RAG System Design](../../domains/rag/evaluation-and-production/03-rag-system-design.md) | Published | Enterprise patterns |
| [RAG Mistakes](../../domains/rag/evaluation-and-production/04-rag-mistakes.md) | Published | Troubleshooting |
| [RAG Comparison Guides](../../domains/rag/evaluation-and-production/05-rag-comparison-guides.md) | Published | Decision matrices |
| [Vector DB Providers](../../domains/rag/providers/README.md) | Published | FAISS, Chroma, PGVector, Pinecone, Milvus, Weaviate, Qdrant |

[Domain index →](../../domains/rag/README.md)

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

### AI Agents

| Document | Status | Description |
|----------|--------|-------------|
| [Module hub](../../domains/ai-agents/README.md) | Published | Agent engineering handbook hub |
| [Introduction to Agent Engineering](../../domains/ai-agents/foundations/01-introduction-to-agent-engineering.md) | Published | Agents as software discipline |
| [Agent Architecture](../../domains/ai-agents/foundations/03-agent-architecture.md) | Published | Planner-executor-reflection stack |
| [Agent Fundamentals](../../domains/ai-agents/foundations/02-agent-fundamentals.md) | Published | Goals, perception, action |
| [Reasoning Patterns](../../domains/ai-agents/cognition/01-agent-reasoning-patterns.md) | Published | ReAct, reflection, ToT |
| [Agent Planning](../../domains/ai-agents/cognition/02-agent-planning.md) | Published | Decomposition, replanning |
| [Agent Memory Systems](../../domains/ai-agents/cognition/04-agent-memory-systems.md) | Published | Layered agent memory |
| [Tool Use](../../domains/ai-agents/tools-and-action/01-tool-use.md) | Published | Registry, execution, permissions |
| [Agent State Management](../../domains/ai-agents/cognition/03-agent-state-management.md) | Published | Checkpointing, recovery |
| [Task Graphs](../../domains/ai-agents/cognition/05-task-graphs.md) | Published | DAG execution |
| [Event-Driven Agents](../../domains/ai-agents/tools-and-action/03-event-driven-agents.md) | Published | Pub/sub, triggers |
| [Multi-Agent Systems](../../domains/ai-agents/multi-agent-preview/01-multi-agent-systems.md) | Published | Supervisor, swarm, debate |
| [Human-in-the-Loop](../../domains/ai-agents/tools-and-action/02-human-in-the-loop.md) | Published | Approval, escalation |
| [Agent Communication](../../domains/ai-agents/tools-and-action/04-agent-communication.md) | Published | Coordination patterns |
| [Agent Frameworks](../../domains/ai-agents/frameworks/README.md) | Published | 6 framework guides |
| [Build Your Own Framework](../../domains/ai-agents/eval-security-production/07-build-your-own-agent-framework.md) | Published | Minimal agent framework |
| [Agent Evaluation](../../domains/ai-agents/eval-security-production/01-agent-evaluation.md) | Published | Task success, tool accuracy |
| [Production Agent Engineering](../../domains/ai-agents/eval-security-production/04-production-agent-engineering.md) | Published | Observability, scaling |
| [Agent Security](../../domains/ai-agents/eval-security-production/02-agent-security.md) | Published | Sandboxing, injection |
| [Agent Engineering Mistakes](../../domains/ai-agents/eval-security-production/03-agent-engineering-mistakes.md) | Published | Troubleshooting |
| [Agent Case Studies](../../domains/ai-agents/eval-security-production/05-agent-case-studies.md) | Published | Coding, research, support |
| [Agent Comparison Guides](../../domains/ai-agents/eval-security-production/06-agent-comparison-guides.md) | Published | Framework & pattern matrices |

[Domain index →](../../domains/ai-agents/README.md)

### Agent Architectures

| Document | Status | Description |
|----------|--------|-------------|
| [Multi-Agent Systems](../../domains/ai-agents/multi-agent-preview/01-multi-agent-systems.md) | Published | Architecture catalog |
| [Agent Case Studies](../../domains/ai-agents/eval-security-production/05-agent-case-studies.md) | Published | Real-world patterns |

[Domain index →](../../domains/agent-architectures/README.md)

### MCP

| Document | Status | Description |
|----------|--------|-------------|
| [Module hub](../../domains/mcp/README.md) | Published | MCP engineering handbook hub |
| [Introduction to MCP](../../domains/mcp/foundations/01-introduction-to-mcp.md) | Published | Why MCP exists, ecosystem |
| [MCP Architecture](../../domains/mcp/foundations/02-mcp-architecture.md) | Published | Client, transport, server layers |
| [MCP Lifecycle](../../domains/mcp/foundations/03-mcp-lifecycle.md) | Published | Initialize through termination |
| [MCP Core Concepts](../../domains/mcp/foundations/04-mcp-core-concepts.md) | Published | Clients, servers, primitives |
| [MCP Client](../../domains/mcp/client-and-server/01-mcp-client.md) | Published | Connection, discovery, retries |
| [MCP Server](../../domains/mcp/client-and-server/02-mcp-server.md) | Published | Registration, routing, shutdown |
| [MCP Resources](../../domains/mcp/primitives/01-mcp-resources.md) | Published | URI design, discovery, caching |
| [MCP Prompts](../../domains/mcp/primitives/02-mcp-prompts.md) | Published | Templates, registry, validation |
| [MCP Tools](../../domains/mcp/primitives/03-mcp-tools.md) | Published | Schemas, permissions, streaming |
| [Transport Layer](../../domains/mcp/transport-and-auth/01-mcp-transport-layer.md) | Published | STDIO, HTTP, SSE, WebSockets |
| [Message Protocol](../../domains/mcp/primitives/04-mcp-message-protocol.md) | Published | JSON-RPC messages |
| [Authentication](../../domains/mcp/transport-and-auth/03-mcp-authentication.md) | Published | OAuth, RBAC, secrets |
| [Streaming](../../domains/mcp/transport-and-auth/02-mcp-streaming.md) | Published | Partial results, cancellation |
| [Multi-Server MCP](../../domains/mcp/transport-and-auth/04-multi-server-mcp.md) | Published | Routing, federation, failover |
| [Build an MCP Server](../../domains/mcp/client-and-server/03-build-an-mcp-server.md) | Published | Production server tutorial |
| [Build an MCP Client](../../domains/mcp/client-and-server/04-build-an-mcp-client.md) | Published | Production client tutorial |
| [Production MCP](../../domains/mcp/production/01-production-mcp.md) | Published | Observability, scaling, HA |
| [MCP Security](../../domains/mcp/production/02-mcp-security.md) | Published | Sandboxing, audit, injection |
| [MCP Mistakes](../../domains/mcp/production/03-mcp-engineering-mistakes.md) | Published | Troubleshooting playbook |
| [Real-World Architectures](../../domains/mcp/production/04-mcp-real-world-architectures.md) | Published | Six production patterns |
| [MCP Comparison Guides](../../domains/mcp/production/05-mcp-comparison-guides.md) | Published | Decision matrices |

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

| Document | Status | Description |
|----------|--------|-------------|
| [Module hub](../../domains/ai-evaluation/README.md) | Published | AI evaluation handbook hub |
| [Introduction to AI Evaluation](../../domains/ai-evaluation/foundations/01-introduction-to-ai-evaluation.md) | Published | Offline vs online, LLMOps |
| [Evaluation Architecture](../../domains/ai-evaluation/foundations/02-evaluation-architecture.md) | Published | End-to-end pipeline |
| [Evaluation Datasets](../../domains/ai-evaluation/foundations/03-evaluation-datasets.md) | Published | Golden sets, versioning |
| [Core Metrics](../../domains/ai-evaluation/metrics/01-core-metrics.md) | Published | Accuracy, F1, BLEU, ROUGE |
| [LLM Evaluation Metrics](../../domains/ai-evaluation/metrics/02-llm-evaluation-metrics.md) | Published | Faithfulness, relevance |
| [Hallucination Detection](../../domains/ai-evaluation/metrics/03-hallucination-detection.md) | Published | Types and strategies |
| [RAG Evaluation](../../domains/ai-evaluation/surface-areas/02-rag-evaluation.md) | Published | RAGAS, retrieval metrics |
| [Prompt Evaluation](../../domains/ai-evaluation/surface-areas/01-prompt-evaluation.md) | Published | Regression, robustness |
| [Agent Evaluation](../../domains/ai-evaluation/surface-areas/03-agent-evaluation.md) | Published | Task completion, tools |
| [Evaluation Frameworks](../../domains/ai-evaluation/case-studies/04-evaluation-frameworks.md) | Published | Framework selection |
| [Human Evaluation](../../domains/ai-evaluation/surface-areas/04-human-evaluation.md) | Published | Rubrics, agreement |
| [Latency Evaluation](../../domains/ai-evaluation/metrics/04-latency-evaluation.md) | Published | P95, TTFT budgets |
| [Cost Evaluation](../../domains/ai-evaluation/metrics/05-cost-evaluation.md) | Published | Token and infra cost |
| [Benchmarking](../../domains/ai-evaluation/foundations/04-benchmarking.md) | Published | Public and internal benches |
| [A/B Testing](../../domains/ai-evaluation/online-systems/01-ab-testing.md) | Published | Experiments, canary |
| [Continuous Evaluation](../../domains/ai-evaluation/online-systems/02-continuous-evaluation.md) | Published | CI/CD, drift detection |
| [Evaluation Dashboards](../../domains/ai-evaluation/online-systems/04-evaluation-dashboards.md) | Published | Quality and exec views |
| [Production Evaluation](../../domains/ai-evaluation/online-systems/03-production-evaluation.md) | Published | Scale, governance |
| [Evaluation Mistakes](../../domains/ai-evaluation/case-studies/02-evaluation-mistakes.md) | Published | Troubleshooting |
| [Evaluation Case Studies](../../domains/ai-evaluation/case-studies/01-evaluation-case-studies.md) | Published | Real-world patterns |
| [Comparison Guides](../../domains/ai-evaluation/case-studies/03-ai-evaluation-comparison-guides.md) | Published | Decision matrices |
| [Framework Guides](../../domains/ai-evaluation/frameworks/README.md) | Published | RAGAS, DeepEval, etc. |

[Domain index →](../../domains/ai-evaluation/README.md)

### AI System Design

| Document | Status | Description |
|----------|--------|-------------|
| [Module hub](../../domains/ai-system-design/README.md) | Published | AI system design handbook hub |
| [Fundamentals](../../domains/ai-system-design/foundations/01-ai-system-design-fundamentals.md) | Published | Principles, capacity, budgeting |
| [Common Components](../../domains/ai-system-design/foundations/02-common-ai-components.md) | Published | Reference production stack |
| [ChatGPT-like Design](../../domains/ai-system-design/consumer-products/01-design-chatgpt-like-system.md) | Published | Conversational AI |
| [Cursor-like Design](../../domains/ai-system-design/developer-tools/01-design-cursor-like-system.md) | Published | IDE coding assistant |
| [GitHub Copilot Design](../../domains/ai-system-design/developer-tools/02-design-github-copilot.md) | Published | Inline completions |
| [Perplexity Design](../../domains/ai-system-design/consumer-products/02-design-perplexity-ai-search.md) | Published | AI search + citations |
| [Deep Research Design](../../domains/ai-system-design/consumer-products/04-design-deep-research-system.md) | Published | Multi-agent research |
| [AI Search Engine](../../domains/ai-system-design/consumer-products/03-design-ai-search-engine.md) | Published | Hybrid enterprise search |
| [Customer Support AI](../../domains/ai-system-design/enterprise-assistants/01-design-ai-customer-support.md) | Published | Support + escalation |
| [Coding Assistant](../../domains/ai-system-design/developer-tools/03-design-ai-coding-assistant.md) | Published | AST, PRs, review |
| [PDF Chat](../../domains/ai-system-design/developer-tools/04-design-ai-pdf-chat.md) | Published | OCR, tables, cites |
| [Email Assistant](../../domains/ai-system-design/enterprise-assistants/02-design-ai-email-assistant.md) | Published | Triage + drafts |
| [CRM Assistant](../../domains/ai-system-design/enterprise-assistants/03-design-ai-crm-assistant.md) | Published | Sales intelligence |
| [Voice Agent](../../domains/ai-system-design/enterprise-assistants/04-design-ai-voice-agent.md) | Published | STT/TTS realtime |
| [Scaling AI Systems](../../domains/ai-system-design/scale-and-interviews/01-scaling-ai-systems.md) | Published | Horizontal scale, queues |
| [Architecture Patterns](../../domains/ai-system-design/foundations/03-ai-architecture-patterns.md) | Published | Agentic, event-driven |
| [Design Interviews](../../domains/ai-system-design/scale-and-interviews/02-ai-system-design-interviews.md) | Published | Whiteboard prep |
| [Comparison Guides](../../domains/ai-system-design/scale-and-interviews/03-ai-system-design-comparison-guides.md) | Published | Decision matrices |

[Domain index →](../../domains/ai-system-design/README.md)

### AI Deployment (Production AI)

| Document | Status | Description |
|----------|--------|-------------|
| [Module hub](../../domains/ai-deployment/README.md) | Published | Production AI handbook hub |
| [Production Overview](../../domains/ai-deployment/foundations/01-production-ai-overview.md) | Published | Lifecycle, platform architecture |
| [Docker for AI](../../domains/ai-deployment/packaging-and-release/01-docker-for-ai.md) | Published | Containers for AI services |
| [Deployment Strategies](../../domains/ai-deployment/packaging-and-release/02-ai-deployment-strategies.md) | Published | Canary, blue/green |
| [CI/CD for AI](../../domains/ai-deployment/packaging-and-release/03-cicd-for-ai.md) | Published | Eval gates, rollback |
| [Secrets Management](../../domains/ai-deployment/packaging-and-release/04-secrets-management-for-ai.md) | Published | API keys, Vault |
| [Monitoring](../../domains/ai-deployment/observability/01-monitoring-ai-systems.md) | Published | SLO, alerts, health |
| [Logging](../../domains/ai-deployment/observability/02-logging-for-ai.md) | Published | Structured JSON logs |
| [Observability](../../domains/ai-deployment/observability/03-observability-for-ai.md) | Published | OTEL, LangFuse, Phoenix |
| [Cost Tracking](../../domains/ai-deployment/observability/04-cost-tracking-production.md) | Published | Production FinOps |
| [Reliability](../../domains/ai-deployment/reliability-and-perf/01-reliability-for-ai.md) | Published | Retry, circuit breaker |
| [Caching](../../domains/ai-deployment/reliability-and-perf/02-caching-for-ai.md) | Published | Redis, prompt cache |
| [Security](../../domains/ai-deployment/security-and-ops/01-security-production-ai.md) | Published | Auth, rate limits |
| [Performance](../../domains/ai-deployment/reliability-and-perf/03-performance-optimization-production.md) | Published | Streaming, routing |
| [AI Operations](../../domains/ai-deployment/security-and-ops/02-ai-operations.md) | Published | Incidents, runbooks |
| [Production Readiness](../../domains/ai-deployment/foundations/02-production-readiness-checklist.md) | Published | Go-live checklist |
| [Comparison Guides](../../domains/ai-deployment/security-and-ops/03-production-ai-comparison-guides.md) | Published | Deploy, observability |

[Domain index →](../../domains/ai-deployment/README.md)

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

### Cloud Deployment

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/cloud-deployment/README.md)

### Docker

| Document | Status | Description |
|----------|--------|-------------|
| [Docker for AI](../../domains/ai-deployment/packaging-and-release/01-docker-for-ai.md) | Published | AI container handbook section |

[Domain index →](../../domains/docker/README.md)

### CI/CD

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/cicd/README.md)

### Monitoring

| Document | Status | Description |
|----------|--------|-------------|
| [Monitoring Foundation for AI Backends](../../domains/monitoring/monitoring-foundation-for-ai-backends.md) | Published | health, metrics, tracing, OTel, Prometheus, Grafana |

[Domain index →](../../domains/monitoring/README.md)

### Logging

| Document | Status | Description |
|----------|--------|-------------|
| [Logging and Error Handling](../../domains/logging/logging-and-error-handling.md) | Published | Structured logs, retries, graceful failures |
| [Backend Logging for AI](../../domains/logging/backend-logging-for-ai.md) | Published | JSON logs, correlation IDs, audit logging |

[Domain index →](../../domains/logging/README.md)

### Observability

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/observability/README.md)

### Data Engineering

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/data-engineering/README.md)

### Production Incidents

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/production-incidents/README.md)

---

### AI Application Architecture

| Document | Status |
|----------|--------|
| *(No documents yet)* | — |

[Domain index →](../../domains/ai-application-architecture/README.md)

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

## Craft & Growth

### AI Safety

| Document | Status | Description |
|----------|--------|-------------|
| [AI Safety Index](../../domains/ai-safety/README.md) | Published | Safety handbook hub |
| [Introduction to AI Safety](../../domains/ai-safety/introduction-to-ai-safety.md) | Published | Why safety matters for engineers |
| [Prompt Injection & Jailbreaks](../../domains/ai-safety/prompt-injection-and-jailbreaks.md) | Published | Attacks and defenses |
| [Guardrails & Content Filtering](../../domains/ai-safety/guardrails-and-content-filtering.md) | Published | Layered guardrails, PII |
| [Safe Tool Use](../../domains/ai-safety/safe-tool-use.md) | Published | Allowlists, HITL, least privilege |
| [Production Safety Checklist](../../domains/ai-safety/production-ai-safety-checklist.md) | Published | Ship checklist |

[Domain index →](../../domains/ai-safety/README.md)

### Debugging

| Document | Status | Description |
|----------|--------|-------------|
| [Debugging Index](../../domains/debugging/README.md) | Published | Debugging handbook hub |
| [Introduction to AI Debugging](../../domains/debugging/introduction-to-ai-debugging.md) | Published | Non-determinism, triage mindset |
| [Debugging RAG Pipelines](../../domains/debugging/debugging-rag-pipelines.md) | Published | Retrieval and hallucination failures |
| [Debugging Agents](../../domains/debugging/debugging-agents.md) | Published | Loops, tools, bad plans |
| [Debugging LLM APIs](../../domains/debugging/debugging-llm-apis.md) | Published | Timeouts, rate limits, streaming |
| [AI Debugging Playbook](../../domains/debugging/ai-debugging-playbook.md) | Published | Step-by-step triage |

[Domain index →](../../domains/debugging/README.md)

### Common Mistakes

| Document | Status | Description |
|----------|--------|-------------|
| [Common Engineering Mistakes](../../domains/common-mistakes/common-engineering-mistakes.md) | Published | 20 mistakes with bad vs good patterns |

[Domain index →](../../domains/common-mistakes/README.md)

### Interview Preparation

| Document | Status | Description |
|----------|--------|-------------|
| [Interview Handbook Index](../../domains/interview-preparation/README.md) | Published | AI engineering interview hub |
| [Interview Strategy](../../domains/interview-preparation/interview-strategy.md) | Published | Process and roadmap |
| [Python Interviews](../../domains/interview-preparation/python-interviews.md) | Published | Coding + async |
| [FastAPI Interviews](../../domains/interview-preparation/fastapi-interviews.md) | Published | API + streaming |
| [SQL Interviews](../../domains/interview-preparation/sql-interviews.md) | Published | Joins, windows |
| [PostgreSQL Interviews](../../domains/interview-preparation/postgresql-interviews.md) | Published | MVCC, pgvector |
| [Redis Interviews](../../domains/interview-preparation/redis-interviews.md) | Published | Cache, rate limits |
| [Docker Interviews](../../domains/interview-preparation/docker-interviews.md) | Published | Containers |
| [LLM Interviews](../../domains/interview-preparation/llm-engineering-interviews.md) | Published | Tokens, tools |
| [Prompt Interviews](../../domains/interview-preparation/prompt-engineering-interviews.md) | Published | ReAct, eval |
| [Context Interviews](../../domains/interview-preparation/context-engineering-interviews.md) | Published | Memory, assembly |
| [RAG Interviews](../../domains/interview-preparation/rag-interviews.md) | Published | Hybrid, GraphRAG |
| [Agent Interviews](../../domains/interview-preparation/ai-agents-interviews.md) | Published | ReAct, frameworks |
| [MCP Interviews](../../domains/interview-preparation/mcp-interviews.md) | Published | Protocol depth |
| [Evaluation Interviews](../../domains/interview-preparation/ai-evaluation-interviews.md) | Published | RAGAS, A/B |
| [System Design Interviews](../../domains/interview-preparation/system-design-interview-guide.md) | Published | Whiteboard exercises |
| [Production Interviews](../../domains/interview-preparation/production-ai-interviews.md) | Published | Ops, observability |
| [Resume & Projects](../../domains/interview-preparation/resume-project-interviews.md) | Published | Deep dives |
| [Live Coding](../../domains/interview-preparation/live-coding-machine-coding.md) | Published | Machine coding |
| [Debugging Interviews](../../domains/interview-preparation/debugging-interviews.md) | Published | Prod scenarios |
| [Behavioral](../../domains/interview-preparation/behavioral-leadership-interviews.md) | Published | STAR, leadership |
| [Mock Interviews](../../domains/interview-preparation/mock-interviews.md) | Published | Junior → Staff |
| [Company Patterns](../../domains/interview-preparation/company-interview-patterns.md) | Published | AI org types |

[Domain index →](../../domains/interview-preparation/README.md)

### Papers

| Document | Status | Description |
|----------|--------|-------------|
| [Papers Index](../../domains/papers/README.md) | Published | Research handbook hub |
| [Attention Is All You Need](../../domains/papers/attention-is-all-you-need.md) | Published | Transformer foundations |
| [Agent Reasoning Papers](../../domains/papers/agent-reasoning-papers.md) | Published | ReAct, ToT, Reflexion, Voyager, CAMEL |
| [Retrieval Papers](../../domains/papers/retrieval-papers.md) | Published | Self-RAG, GraphRAG, RAPTOR, CRAG |
| [Prompt Engineering Papers](../../domains/papers/prompt-engineering-papers.md) | Published | CoT, few-shot, instruction tuning |
| [DSPy](../../domains/papers/dspy.md) | Published | Programming model and optimization |
| [SWE-Agent](../../domains/papers/swe-agent.md) | Published | Software engineering agents |
| [Research Evolution](../../domains/papers/research-evolution.md) | Published | Historical timeline |
| [Research Comparison Guides](../../domains/papers/research-comparison-guides.md) | Published | Paper comparison tables |
| [Engineering Takeaways](../../domains/papers/engineering-takeaways.md) | Published | What to implement and avoid |
| [Future Research](../../domains/papers/future-research.md) | Published | Open problems and directions |

[Domain index →](../../domains/papers/README.md)

### Engineering Templates

| Asset | Status | Description |
|-------|--------|-------------|
| [Templates Hub](../../templates/README.md) | Published | Engineering toolkit hub |
| [FastAPI Starter](../../templates/engineering/fastapi-starter/README.md) | Published | Modular AI API scaffold |
| [RAG Starter](../../templates/engineering/rag-starter/README.md) | Published | Retrieval pipeline template |
| [Agent Starter](../../templates/engineering/agent-starter/README.md) | Published | Planner/executor agent |
| [MCP Starter](../../templates/engineering/mcp-starter/README.md) | Published | Server and client |
| [Docker Starter](../../templates/engineering/docker/README.md) | Published | Compose and multi-stage |
| [GitHub Actions](../../templates/engineering/github-actions/README.md) | Published | CI/CD workflows |
| [Logging](../../templates/engineering/logging/README.md) | Published | Structured JSON logging |
| [Monitoring](../../templates/engineering/monitoring/README.md) | Published | OTEL, LangFuse, Phoenix |
| [Prompt Library](../../templates/engineering/prompts/README.md) | Published | Parameterized prompts |
| [Evaluation](../../templates/engineering/evaluation/README.md) | Published | Eval harnesses |
| [Deployment](../../templates/engineering/deployment/README.md) | Published | Render, Railway, Vercel |
| [Boilerplates](../../templates/engineering/boilerplates/README.md) | Published | Product scaffolds |
| [Utilities](../../templates/engineering/utilities/README.md) | Published | Shared helpers |
| [Architecture Diagrams](../../templates/engineering/architecture/README.md) | Published | Mermaid templates |

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
