# Glossary

> Domain terminology used throughout the AI Engineering Playbook.
> Link to glossary terms on first use in any document.

---

## A

### Agent
An AI system that autonomously plans and executes tasks using an LLM for reasoning and tools for action. See [AI Agents](../domains/ai-agents/).

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
The practice of designing and managing what information an LLM sees in its context window. See [Context Engineering](../domains/context-engineering/).

### Context Window
The maximum number of tokens an LLM can process in a single request (input + output combined).

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

### Evaluation
Systematic measurement of AI system quality using metrics, benchmarks, and test datasets. See [AI Evaluation](../domains/ai-evaluation/).

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

## L

### LLM (Large Language Model)
A neural network trained on vast text data to understand and generate human language. See [LLM Engineering](../domains/llm-engineering/).

### LangGraph
A framework for building stateful, graph-based agent workflows. See [AI Workflows](../domains/ai-workflows/).

---

## M

### MCP (Model Context Protocol)
Open protocol for connecting AI models to external tools and data sources. See [MCP](../domains/mcp/).

### Multi-Agent System
Architecture where multiple specialized agents collaborate to solve complex tasks. See [Multi-Agent Systems](../domains/multi-agent-systems/).

---

## O

### Observability
The ability to understand system behavior through logs, metrics, and traces. See [Observability](../domains/observability/).

### Orchestrator
A component that coordinates workflow execution, routing tasks between agents or steps.

---

## P

### Prompt Engineering
The practice of designing effective prompts to get reliable, high-quality outputs from LLMs. See [Prompt Engineering](../domains/prompt-engineering/).

### Prompt Pattern
A reusable prompt template for a specific use case. See [Prompts](../prompts/).

---

## R

### RAG (Retrieval Augmented Generation)
Architecture pattern that retrieves relevant context from a knowledge base before generating a response. See [RAG](../domains/rag/).

### Reranking
Re-scoring retrieved documents with a more accurate (but slower) model to improve relevance.

### ReAct
Agent pattern combining Reasoning and Acting — the agent alternates between thinking and using tools.

---

## S

### Semantic Search
Search based on meaning rather than exact keyword matching, powered by embeddings.

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
