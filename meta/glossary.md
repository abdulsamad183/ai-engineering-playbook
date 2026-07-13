# Glossary

> Domain terminology used throughout the AI Engineering Playbook.
> Link to glossary terms on first use in any document.

---

## A

### Agent
An autonomous software system that pursues goals through perceive-decide-act loops using LLMs for reasoning and tools for action. See [Agent Engineering](../domains/ai-agents/README.md).

### Agent Engineering
The discipline of designing, orchestrating, evaluating, and operating production AI agent systems. See [AI Agents](../domains/ai-agents/README.md).

### AI Engineering
The discipline of designing, building, deploying, evaluating, and maintaining software systems that integrate AI models into production applications. See [AI Engineering Overview](../domains/foundations/ai-engineering-overview.md).

### Agent Loop
The iterative cycle of an agent: receive input → reason → select tool → execute → observe result → repeat or respond.

### A2A (Agent-to-Agent)
Protocols and patterns for communication between autonomous AI agents. See [A2A](../domains/a2a/).

### Async (Asynchronous)
Programming pattern where operations can run concurrently without blocking. Critical for AI APIs that involve I/O-bound LLM calls.

---

## B

### Backend
Server-side application logic that handles business rules, data persistence, and API endpoints. See [Backend Engineering](../domains/backend-engineering/).

### Batch Processing
Processing multiple items together rather than one at a time. Used for embedding generation and bulk inference.

---

## C

### Chain-of-Thought (CoT)
Prompting technique where the model shows its reasoning steps before producing a final answer.

### Chunking
Splitting documents into smaller segments for embedding and retrieval. See [Embeddings](../domains/embeddings/).

### Context Engineering
The discipline of designing systems that determine what information an LLM receives, how it is organized within token budgets, and how it evolves over time. Distinct from prompt engineering. See [Context Engineering](../domains/context-engineering/README.md).

### Context Window
The maximum number of tokens an LLM can process in a single request (input + output combined). Application-level management is covered in [Context Windows](../domains/context-engineering/context-windows.md).

### Clean Architecture
Software architecture pattern that separates business logic from frameworks and infrastructure via dependency inversion. AI orchestration lives in the domain layer. See [Software Engineering for AI](../domains/foundations/software-engineering-for-ai.md).

### Connection Pooling
Reusing a pool of pre-established database connections to avoid connection setup overhead on every request. Critical for AI apps that hold connections during slow LLM calls. See [Databases for AI](../domains/databases/databases-for-ai-applications.md).

### CI/CD
Continuous Integration and Continuous Deployment — automated pipelines for testing and deploying code. See [CI/CD](../domains/cicd/).

---

## D

### Dependency Injection
Design pattern where dependencies are provided to a component rather than created internally. Core to FastAPI's architecture.

### Docker
Containerization platform for packaging applications with their dependencies. See [Docker](../domains/docker/).

---

## E

### Embedding
A dense vector representation of text (or other data) that captures semantic meaning. See [Embeddings](../domains/embeddings/).

### AI Evaluation
Systematic measurement of AI system quality — LLMs, prompts, RAG, agents, latency, cost, and business impact — using metrics, benchmarks, golden datasets, and continuous monitoring. See [AI Evaluation Handbook](../domains/ai-evaluation/README.md).

### LLMOps
Operational practices for deploying and maintaining LLM applications: versioning, evaluation, monitoring, and continuous improvement. See [Introduction to AI Evaluation](../domains/ai-evaluation/introduction-to-ai-evaluation.md).

### Golden Dataset
Curated, versioned evaluation set with ground truth used for regression testing and quality gates. See [Evaluation Datasets](../domains/ai-evaluation/evaluation-datasets.md).

### Faithfulness (RAG)
Metric measuring whether generated answers are supported by retrieved context. See [LLM Evaluation Metrics](../domains/ai-evaluation/llm-evaluation-metrics.md).

### RAGAS
Retrieval Augmented Generation Assessment framework for RAG pipeline metrics. See [RAGAS Guide](../domains/ai-evaluation/frameworks/ragas.md).

### AI Platform Engineering
Operational discipline for deploying, monitoring, securing, and scaling LLM applications in production. See [Production AI Handbook](../domains/ai-deployment/README.md).

### Latency Budget
Allocated time per layer (API, retrieval, LLM, tools) in an AI request path. See [AI System Design Fundamentals](../domains/ai-system-design/ai-system-design-fundamentals.md).

---

## F

### Few-Shot Prompting
Providing example input-output pairs in the prompt to guide model behavior.

### Function Calling
LLM capability to invoke predefined functions/tools based on user input. Also called tool use.

---

## G

### Guardrails
Safety mechanisms that validate, filter, or constrain AI outputs before they reach users. See [AI Safety](../domains/ai-safety/).

---

## H

### Hallucination
When an LLM generates plausible but factually incorrect information.

### Human-in-the-Loop (HITL)
Pattern where human review or approval is required at specific points in an AI workflow.

### Hybrid Search
Combining vector similarity search with traditional keyword search (BM25) for improved retrieval.

---

## I

### Inference
The process of running a model to generate predictions or outputs. See [Inference Optimization](../domains/inference-optimization/).

### Ingestion Pipeline
The process of loading, processing, chunking, embedding, and storing documents for retrieval.

---

## J

### JWT (JSON Web Token)
Compact, URL-safe token format for transmitting claims between parties. Commonly used for stateless API authentication. See [HTTP Fundamentals for AI](../domains/apis/http-fundamentals-for-ai.md).

---

## L

### KV Cache
Key-value cache storing attention keys and values from prior tokens during autoregressive generation, avoiding recomputation and dramatically reducing decode latency. See [KV Cache](../domains/llm-engineering/kv-cache.md).

### LLM Engineering
The discipline of integrating, optimizing, and operating large language models in production — inference, tokenization, context, provider APIs, cost control. See [LLM Engineering](../domains/llm-engineering/README.md).

### LLM (Large Language Model)
A neural network trained on vast text data to understand and generate human language. See [Introduction to LLM Engineering](../domains/llm-engineering/introduction-to-llm-engineering.md).

### LangGraph
A framework for building stateful, graph-based agent workflows. See [AI Workflows](../domains/ai-workflows/).

---

### MCP (Model Context Protocol)
Open protocol specification for standardized communication between AI hosts and servers exposing **tools**, **resources**, and **prompts** over pluggable transports (STDIO, HTTP). See [MCP Handbook](../domains/mcp/README.md).

### MCP Host
Application embedding an MCP client (IDE, agent runtime, chat app). Discovers capabilities and invokes servers on behalf of the user or agent.

### MCP Server
Process exposing tools, resources, and prompts via the MCP message protocol. See [Build an MCP Server](../domains/mcp/build-an-mcp-server.md).

### MCP Tool
Named, schema-defined capability invoked via `tools/call` — the protocol primitive for agent actions. See [MCP Tools](../domains/mcp/mcp-tools.md).

### MCP Resource
URI-addressable read-only context fetched via `resources/read`. See [MCP Resources](../domains/mcp/mcp-resources.md).

### Multi-Agent System
Architecture where multiple specialized agents collaborate to solve complex tasks. See [Multi-Agent Systems](../domains/multi-agent-systems/).

---

## O

### OAuth
Open authorization standard for delegated access — allowing applications to access resources on behalf of a user without sharing credentials. See [HTTP Fundamentals for AI](../domains/apis/http-fundamentals-for-ai.md).

### Observability
The ability to understand system behavior through logs, metrics, and traces. See [Observability](../domains/observability/).

### Orchestrator
A component that coordinates workflow execution, routing tasks between agents or steps.

---

## P

### Prompt Engineering
The discipline of designing, testing, versioning, and optimizing prompts as maintainable software artifacts in production AI systems. See [Prompt Engineering](../domains/prompt-engineering/README.md).

### Prompt Injection
Attack where untrusted input attempts to override system instructions. See [Prompt Security](../domains/prompt-engineering/prompt-security.md).

### Few-Shot Prompting
Providing a small number of input-output examples in the prompt to demonstrate desired behavior. See [Prompting Strategies](../domains/prompt-engineering/prompting-strategies.md).

### Prompt Chaining
Connecting multiple prompt steps in sequence, passing intermediate outputs between stages. See [Prompt Chaining](../domains/prompt-engineering/prompt-chaining.md).

### Prompt Pattern
A reusable prompt structure for a specific task type. See [Prompt Patterns](../domains/prompt-engineering/prompt-patterns.md) and [Prompt Templates](../prompts/templates/).

### Repository Pattern
Design pattern that abstracts data access behind a domain-friendly interface, enabling swappable storage implementations and testable services. See [Software Engineering for AI](../domains/foundations/software-engineering-for-ai.md).

### REST (Representational State Transfer)
Architectural style for designing networked APIs using HTTP methods, stateless requests, and resource-based URLs. See [HTTP Fundamentals for AI](../domains/apis/http-fundamentals-for-ai.md).

### RAG (Retrieval Augmented Generation)
Architecture pattern that retrieves relevant knowledge from an index before generating LLM responses. Full handbook: [RAG](../domains/rag/README.md).

### Retrieval
The process of finding candidate documents or passages from an index for a given query. See [Retrieval Strategies](../domains/rag/retrieval-strategies.md).

### Reranking
Re-scoring retrieved documents with a more accurate (but slower) model to improve relevance. See [Reranking](../domains/rag/reranking.md).

### ReAct
Agent pattern combining Reasoning and Acting — the agent alternates between thinking and using tools.

---

## S

### Service Layer
Application layer that orchestrates domain logic and coordinates between repositories and external services. Routes delegate to services; services do not know about HTTP. See [Software Engineering for AI](../domains/foundations/software-engineering-for-ai.md).

### Semantic Search
Search based on meaning rather than exact keyword matching, powered by embeddings.

### SSE (Server-Sent Events)
HTTP-based streaming protocol for pushing real-time updates from server to client. Used for streaming LLM token output. See [HTTP Fundamentals for AI](../domains/apis/http-fundamentals-for-ai.md).

### Streaming
Delivering LLM output token-by-token rather than waiting for the complete response.

### System Prompt
Instructions given to the LLM that define its role, behavior, and constraints for a conversation.

---

## T

### Temperature
LLM parameter controlling randomness in output. Lower values (0–0.3) produce deterministic output; higher values (0.7–1.0) increase creativity.

### Token
The basic unit of text processing for LLMs. Roughly 4 characters or 0.75 words in English.

### Tool Use
The ability of an LLM to call external functions, APIs, or services during inference.

### Tracing
Recording the full path of a request through a system, including all LLM calls, tool invocations, and retrieval steps.

---

## V

### Vector Database
Database optimized for storing and searching high-dimensional vectors (embeddings). See [Vector Databases](../domains/vector-databases/).

---

## Contributing to the Glossary

1. Add new terms in alphabetical order.
2. Include a concise definition (1–2 sentences).
3. Link to the relevant domain folder.
4. Update this file when introducing new specialized terms in documents.

---

## See Also

- [Master Index](indexes/MASTER-INDEX.md)
- [Domains Overview](../domains/README.md)
