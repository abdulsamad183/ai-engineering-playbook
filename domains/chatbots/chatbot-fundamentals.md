---
title: "Chatbot Fundamentals"
description: "Types of chatbots and the components every serious chat product needs."
domain: chatbots
tags: [chatbots]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Chatbot Fundamentals

> Types of chatbots and the components every serious chat product needs.

## Definition

Chatbots range from FAQ trees to open-domain assistants to task-oriented agents. Core components: NLU/routing, dialogue state, response generation, integrations, and analytics.

## Why it matters

Chat is a UX, not an architecture. Many products should be forms-with-AI, not endless chat.

## How it works

```mermaid
flowchart LR
  FAQ[FAQ / retrieval bot] --> Hybrid[Hybrid assistant]
  Hybrid --> Task[Task-oriented agent]
  Task --> Open[Open assistant]
```

## Key principles

1. **Scope the job** — Support deflection ≠ general AGI chat.
2. **Design escape hatches** — Handoff to humans.
3. **Measure outcomes** — Resolution, not just CSAT of fluff.

## Common applications

| Application | Description |
|-------------|-------------|
| Customer support | Grounded answers |
| Internal helpdesk | Permissioned tools |
| Onboarding | Guided workflows |

## Common mistakes

- No handoff path when the bot fails
- Unbounded chit-chat that burns tokens

## Further reading

- [Dialogue & memory](dialogue-and-memory.md)
- [LLM Application Development](../llm-application-development/README.md)
