# Domains

> Knowledge organized by engineering domain — the core content of the AI Engineering Playbook.

**Status legend:** **Published** = substantive docs beyond the README · **Planned** = folder reserved, content still to come. Empty domains are kept on purpose; do not delete them.

Domains are grouped by **capability** (Foundations → Core → Retrieval & Agents → Production → Craft & Growth), matching the [Learning Roadmap](../meta/roadmap.md) and home page.

---

## How Domains Work

Each domain represents an area of AI engineering knowledge. Domains are named for **concepts**, not technologies — so `vector-databases/` contains content about any vector database, and `ai-agents/` covers agent development regardless of framework.

Documents within a domain follow the [style guide](../meta/style-guide.md) and use [templates](../meta/templates/) appropriate to the content type.

---

## Domain Map

```mermaid
flowchart TB
    subgraph Foundations
        F[foundations]
        PY[python-engineering]
        BE[backend-engineering]
        API[apis]
        FA[fastapi]
        DB[databases]
        SEC[security]
        PERF[performance-optimization]
    end

    subgraph Core [Core LLM Interaction]
        LLM[llm-engineering]
        PE[prompt-engineering]
        CE[context-engineering]
    end

    subgraph RA [Retrieval and Agents]
        EM[embeddings]
        VD[vector-databases]
        RAG[rag]
        AGT[ai-agents]
        AA[agent-architectures]
        MCP[mcp]
        A2A[a2a]
        WF[ai-workflows]
        MA[multi-agent-systems]
    end

    subgraph Production
        EVAL[ai-evaluation]
        SD[ai-system-design]
        DEP[ai-deployment]
        MI[model-integration]
        MS[model-serving]
        IO[inference-optimization]
        CLOUD[cloud-deployment]
        DOCK[docker]
        CI[cicd]
        MON[monitoring]
        LOG[logging]
        OBS[observability]
    end

    subgraph Craft [Craft and Growth]
        SAFE[ai-safety]
        DBG[debugging]
        CM[common-mistakes]
        INT[interview-preparation]
        PAP[papers]
    end

    F --> BE --> LLM --> PE --> CE --> RAG
    RAG --> AGT --> MCP
    RAG --> EVAL --> DEP
    DEP --> SAFE
    DEP --> DBG
```

---

## All Domains

### Foundations

| Domain | Description | Status |
|--------|-------------|--------|
| [foundations](foundations/) | Core concepts and prerequisites | Published |
| [python-engineering](python-engineering/) | Python for AI applications | Published |
| [backend-engineering](backend-engineering/) | Backend patterns and service design | Published |
| [apis](apis/) | API design for AI services | Published |
| [fastapi](fastapi/) | FastAPI framework | Published |
| [databases](databases/) | Database concepts and patterns | Published |
| [databases/sql](databases/sql/) | SQL for AI applications | Planned |
| [databases/postgresql](databases/postgresql/) | PostgreSQL | Published |
| [databases/redis](databases/redis/) | Redis caching and data store | Published |
| [security](security/) | Security practices | Published |
| [performance-optimization](performance-optimization/) | Performance tuning | Published |
| [software-architecture](software-architecture/) | Software architecture principles | Published |

### Core (LLM Interaction)

| Domain | Description | Status |
|--------|-------------|--------|
| [llm-engineering](llm-engineering/) | LLM integration and API usage | Published |
| [prompt-engineering](prompt-engineering/) | Prompt design and optimization | Published |
| [context-engineering](context-engineering/) | Context window and memory management | Published |

### Retrieval & Agents

| Domain | Description | Status |
|--------|-------------|--------|
| [rag](rag/) | Retrieval augmented generation | Published |
| [embeddings](embeddings/) | Vector embeddings and chunking | Planned |
| [vector-databases](vector-databases/) | Vector storage and similarity search | Planned |
| [ai-agents](ai-agents/) | AI agent development | Published |
| [agent-architectures](agent-architectures/) | Agent system design patterns | Planned |
| [mcp](mcp/) | Model Context Protocol | Published |
| [a2a](a2a/) | Agent-to-agent communication | Planned |
| [ai-workflows](ai-workflows/) | Workflow orchestration | Planned |
| [multi-agent-systems](multi-agent-systems/) | Multi-agent collaboration | Planned |

### Production

| Domain | Description | Status |
|--------|-------------|--------|
| [ai-evaluation](ai-evaluation/) | Evaluation and quality assurance | Published |
| [ai-system-design](ai-system-design/) | End-to-end system design | Published |
| [ai-deployment](ai-deployment/) | Production deployment | Published |
| [model-integration](model-integration/) | Model selection and integration | Planned |
| [model-serving](model-serving/) | Model deployment and serving | Planned |
| [inference-optimization](inference-optimization/) | Inference performance | Planned |
| [cloud-deployment](cloud-deployment/) | Cloud deployment strategies | Planned |
| [docker](docker/) | Containerization | Planned |
| [cicd](cicd/) | CI/CD pipelines | Planned |
| [monitoring](monitoring/) | Monitoring and alerting | Published |
| [logging](logging/) | Structured logging | Published |
| [observability](observability/) | Tracing and telemetry | Planned |
| [ai-application-architecture](ai-application-architecture/) | Application architecture | Planned |
| [design-patterns](design-patterns/) | Reusable design patterns | Planned |
| [distributed-systems](distributed-systems/) | Distributed system concepts | Planned |
| [data-engineering](data-engineering/) | Data pipelines for AI | Planned |
| [production-incidents](production-incidents/) | Incident postmortems | Planned |

### Craft & Growth

| Domain | Description | Status |
|--------|-------------|--------|
| [ai-safety](ai-safety/) | Safety and guardrails | Published |
| [debugging](debugging/) | Debugging AI applications | Published |
| [common-mistakes](common-mistakes/) | Mistakes and prevention | Published |
| [interview-preparation](interview-preparation/) | Interview preparation | Published |
| [papers](papers/) | Research paper summaries | Published |
| [research-notes](research-notes/) | Research notes | Planned |
| [career-notes](career-notes/) | Career development | Planned |
| [resources](resources/) | External resources | Planned |

---

## Adding a New Domain

See [CONTRIBUTING.md](../CONTRIBUTING.md#adding-a-new-domain). New domains are created only for genuinely new areas of AI engineering knowledge.

---

## See Also

- [Master Index](../meta/indexes/MASTER-INDEX.md)
- [Learning Roadmap](../meta/roadmap.md)
- [Architecture Overview](../meta/architecture-overview.md)
