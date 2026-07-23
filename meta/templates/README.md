# Document Templates

> Reusable templates for every content type in the AI Engineering Playbook.
> Copy a template, fill in the placeholders, and follow the [style guide](../style-guide.md).

---

## How to Use Templates

1. Choose the template that matches your content type.
2. Copy the template file to the appropriate domain folder.
3. Rename using [naming conventions](../naming-conventions.md).
4. Fill in all `{placeholder}` values and front matter fields.
5. Remove sections that don't apply (but keep the structure predictable).
6. Follow the [review checklist](../style-guide.md#review-checklist) before publishing.

---

## Available Templates

| Template | Use For | File |
|----------|---------|------|
| **Concept** | Core ideas and mental models | [concept.md](concept.md) |
| **Technology** | Databases, libraries, infrastructure | [technology.md](technology.md) |
| **AI Tool** | LLM providers, vector DBs, AI services | [ai-tool.md](ai-tool.md) |
| **Architecture Pattern** | Reusable design patterns | [architecture-pattern.md](architecture-pattern.md) |
| **Research Paper** | Paper summaries and takeaways | [research-paper.md](research-paper.md) |
| **API** | API reference and integration guides | [api.md](api.md) |
| **Framework** | Agent frameworks, web frameworks | [framework.md](framework.md) |
| **AI System Design** | End-to-end system design documents | [ai-system-design.md](ai-system-design.md) |
| **Production Guide** | Production practices and checklists | [production-guide.md](production-guide.md) |
| **Deployment Guide** | Step-by-step deployment instructions | [deployment-guide.md](deployment-guide.md) |
| **Tutorial** | Hands-on learning guides | [tutorial.md](tutorial.md) |
| **Case Study** | Project case studies and retrospectives (`knowledge/retrospectives/`) | [case-study.md](case-study.md) |
| **Postmortem** | Incident reviews and action items | [postmortem.md](postmortem.md) |
| **Interview Topic** | Interview preparation guides | [interview-topic.md](interview-topic.md) |
| **Cheat Sheet** | Quick reference documents | [cheat-sheet.md](cheat-sheet.md) |
| **Troubleshooting Guide** | Diagnostic and fix guides | [troubleshooting-guide.md](troubleshooting-guide.md) |
| **Prompt Pattern** | Reusable prompt templates | [prompt-pattern.md](prompt-pattern.md) |
| **Agent Workflow** | Agent workflow designs | [agent-workflow.md](agent-workflow.md) |

### Backend Code Templates (Phase 3)

| Template | Use For | File |
|----------|---------|------|
| **FastAPI Application** | New project scaffold | [backend/fastapi-application.md](backend/fastapi-application.md) |
| **API Endpoint** | Single route handler | [backend/api-endpoint.md](backend/api-endpoint.md) |
| **Repository** | Data access layer | [backend/repository.md](backend/repository.md) |
| **Service** | Business logic layer | [backend/service.md](backend/service.md) |
| **Database Model** | SQLAlchemy model | [backend/database-model.md](backend/database-model.md) |
| **API Response** | Response envelope | [backend/api-response.md](backend/api-response.md) |
| **Auth Module** | Authentication setup | [backend/authentication-module.md](backend/authentication-module.md) |
| **Middleware** | Custom middleware | [backend/middleware.md](backend/middleware.md) |
| **Background Task** | Job patterns | [backend/background-task.md](backend/background-task.md) |
| **Test File** | pytest setup | [backend/test-file.md](backend/test-file.md) |

See [backend templates README](backend/README.md).

---

## Template Selection Guide

```
What are you writing?
│
├── Explaining an idea or mental model? ────────── → Concept
├── Documenting a tool, DB, or library? ────────── → Technology
├── Covering an AI-specific service? ───────────── → AI Tool
├── Describing a reusable design pattern? ──────── → Architecture Pattern
├── Summarizing a research paper? ──────────────── → Research Paper
├── Reference for an API? ────────────────────── → API
├── Guide for a development framework? ───────── → Framework
├── Designing a complete AI system? ──────────── → AI System Design
├── Production practices for a topic? ────────── → Production Guide
├── How to deploy something? ─────────────────── → Deployment Guide
├── Step-by-step learning guide? ─────────────── → Tutorial
├── Documenting a project you built? ─────────── → Case Study
├── Reviewing a production incident? ─────────── → Postmortem
├── Preparing for interviews? ────────────────── → Interview Topic
├── Quick reference card? ────────────────────── → Cheat Sheet
├── Diagnosing and fixing problems? ──────────── → Troubleshooting Guide
├── Reusable prompt template? ────────────────── → Prompt Pattern
└── Designing an agent workflow? ─────────────── → Agent Workflow
```

---

## See Also

- [Style Guide](../style-guide.md)
- [Naming Conventions](../naming-conventions.md)
- [Indexing Strategy](../indexing-strategy.md)
