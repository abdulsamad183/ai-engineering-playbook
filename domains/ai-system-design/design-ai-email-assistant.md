---
title: "Design: AI Email Assistant"
description: "Email AI — classification, drafts, retrieval, calendar, summarization."
domain: ai-system-design
tags: [system-design, email, classification, calendar, phase-11]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - design-ai-crm-assistant.md
keywords: [email assistant, draft generation, inbox classification]
author: hp
---

# Design: AI Email Assistant

## Problem Statement

Triage inbox, draft replies, schedule meetings — with user approval before send.

## Architecture

```mermaid
flowchart TB
    INBOX[Email sync] --> CLASS[Classifier]
    CLASS --> SUM[Summarizer]
    CLASS --> DRAFT[Draft generator]
    DRAFT --> RAG[Contact/KB retrieval]
    DRAFT --> CAL[Calendar API]
    DRAFT --> APPROVE[User approval]
```

## Components

- **Ingestion** — Gmail/Outlook webhooks; incremental sync
- **Classification** — urgent, FYI, action required
- **Draft generation** — tone matching from sent history
- **Calendar** — propose slots via tool call

## Security

- OAuth scopes minimal; never auto-send without confirm

## Navigation

- [CRM Assistant](design-ai-crm-assistant.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 11 Section 12 |
