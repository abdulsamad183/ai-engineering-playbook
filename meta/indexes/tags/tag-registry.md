# Tag Registry

> Canonical list of approved tags for the AI Engineering Playbook.
> All document tags must come from this registry. Propose new tags via pull request.

---

## How to Use Tags

1. Select 3–8 tags from this registry for each document.
2. Combine tags from different layers (domain + technology + stage).
3. Do not create synonyms — use the canonical tag listed here.
4. To add a new tag, add it to this file with a definition.

---

## Domain Tags

Tags representing areas of AI engineering knowledge.

| Tag | Definition |
|-----|------------|
| `foundations` | Core concepts and prerequisites |
| `python` | Python language and ecosystem |
| `backend` | Backend engineering practices |
| `api` | API design and development |
| `database` | Database concepts and usage |
| `sql` | SQL queries and patterns |
| `llm` | Large language model engineering |
| `prompt` | Prompt design and optimization |
| `context` | Context window management and engineering |
| `embeddings` | Vector embeddings |
| `vector-search` | Vector database and similarity search |
| `rag` | Retrieval augmented generation |
| `agents` | AI agent development |
| `agent-architecture` | Agent system design patterns |
| `mcp` | Model Context Protocol |
| `a2a` | Agent-to-agent communication |
| `workflows` | AI workflow orchestration |
| `multi-agent` | Multi-agent system design |
| `evaluation` | AI system evaluation and testing |
| `safety` | AI safety and guardrails |
| `system-design` | End-to-end system design |
| `architecture` | Software and AI architecture |
| `model-serving` | Model deployment and serving |
| `inference` | Inference optimization |
| `deployment` | Application deployment |
| `cloud` | Cloud deployment concepts |
| `docker` | Containerization |
| `cicd` | Continuous integration and deployment |
| `monitoring` | System monitoring |
| `logging` | Logging practices |
| `observability` | Observability and tracing |
| `security` | Security practices |
| `performance` | Performance optimization |
| `distributed-systems` | Distributed system concepts |
| `data-engineering` | Data pipelines for AI |
| `debugging` | Debugging AI applications |
| `interview` | Interview preparation |

---

## Technology Tags

Tags for specific tools, frameworks, and services.

| Tag | Definition |
|-----|------------|
| `fastapi` | FastAPI web framework |
| `postgresql` | PostgreSQL database |
| `pgvector` | pgvector extension |
| `redis` | Redis cache and data store |
| `langgraph` | LangGraph agent framework |
| `langchain` | LangChain framework |
| `openai` | OpenAI APIs and models |
| `anthropic` | Anthropic APIs and models |
| `pinecone` | Pinecone vector database |
| `weaviate` | Weaviate vector database |
| `chroma` | ChromaDB vector database |
| `qdrant` | Qdrant vector database |
| `github-actions` | GitHub Actions CI/CD |
| `uvicorn` | Uvicorn ASGI server |
| `pydantic` | Pydantic data validation |
| `gemini` | Google Gemini APIs and models |
| `groq` | Groq inference platform |
| `pytest` | Pytest testing framework |

> Add new technology tags as you document them. Remove tags only when no documents reference them.

---

## Pattern Tags

Tags for design and architectural patterns.

| Tag | Definition |
|-----|------------|
| `pattern` | General design pattern |
| `retry-pattern` | Retry with backoff |
| `circuit-breaker` | Circuit breaker pattern |
| `caching` | Caching strategies |
| `streaming` | Streaming response patterns |
| `batch-processing` | Batch processing patterns |
| `fallback` | Fallback and degradation patterns |
| `guardrails` | Output guardrails and validation |
| `human-in-the-loop` | Human review and approval patterns |
| `prompt-pattern` | Reusable prompt template |

---

## Stage Tags

Tags indicating where in the lifecycle the content applies.

| Tag | Definition |
|-----|------------|
| `development` | Local development practices |
| `production` | Production deployment and operations |
| `testing` | Testing strategies |
| `troubleshooting` | Diagnostic and fix guides |
| `postmortem` | Incident reviews |
| `planning` | Design and planning phase |

---

## Content Type Tags

Tags indicating the type of document.

| Tag | Definition |
|-----|------------|
| `concept` | Conceptual explanation |
| `tutorial` | Hands-on tutorial |
| `cheat-sheet` | Quick reference |
| `case-study` | Project case study |
| `paper` | Research paper summary |
| `project` | Project documentation |
| `framework` | Framework guide |
| `guide` | General guide |

---

## Difficulty Tags

| Tag | Definition |
|-----|------------|
| `beginner` | No prior AI engineering experience needed |
| `intermediate` | Familiarity with AI concepts required |
| `advanced` | Deep expertise expected |

---

## Adding a New Tag

1. Check this registry for an existing tag that covers your concept.
2. If none exists, add a row to the appropriate table above.
3. Include a clear, one-sentence definition.
4. Include the tag addition in your commit message.

---

## See Also

- [Indexing Strategy](../../indexing-strategy.md)
- [Keyword Index](../keyword-index.md)
