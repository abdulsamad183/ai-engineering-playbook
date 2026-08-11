---
title: "Secure Tool Use"
description: "How to let models call tools without handing over the kingdom."
domain: ai-security-guardrails
tags: [ai-security-guardrails]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Secure Tool Use

> How to let models call tools without handing over the kingdom.

## Definition

Tools should be typed, authenticated as the user, allowlisted, rate-limited, and preferably idempotent. High-impact actions require confirmation or out-of-band approval. Arguments must be validated like any public API.

## Why it matters

Most catastrophic LLM incidents will be tool incidents.

## How it works

```mermaid
sequenceDiagram
  participant U as User
  participant A as Agent
  participant T as Tool API
  U->>A: Goal
  A->>T: Restricted call
  T-->>A: Result
  A->>U: Propose irreversible action
  U->>A: Confirm
  A->>T: Execute
```

## Key principles

1. **User-scoped credentials** — Never god-mode API keys in the agent.
2. **Confirm irreversible acts** — Delete/pay/email externally.
3. **Argument validation** — JSON schema + server checks.

## Common applications

| Application | Description |
|-------------|-------------|
| MCP tools | Careful server exposure |
| Browser tools | Domain allowlists |
| DB tools | Read-only roles by default |

## Common mistakes

- Exposing raw SQL/shell tools broadly
- Trusting model-chosen URLs without SSRF controls

## Further reading

- [MCP](../mcp/README.md)
- [AI Agents](../ai-agents/README.md)
