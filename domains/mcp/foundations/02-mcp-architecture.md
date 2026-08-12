---
title: "MCP Architecture"
description: "Complete MCP architecture — client, transport, protocol messages, server, tools, resources, prompts, external systems."
domain: mcp
tags: [mcp, architecture, client, server]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - introduction-to-mcp.md
  - mcp-transport-layer.md
  - mcp-message-protocol.md
keywords: [MCP architecture, transport, protocol layers]
author: hp
---

# MCP Architecture

## Overview

Section **2**.

```mermaid
flowchart TD
    C[MCP Client] --> TR[Transport Layer]
    TR --> PM[Protocol Messages JSON-RPC]
    PM --> S[MCP Server]
    S --> TL[Tools Layer]
    S --> RL[Resources Layer]
    S --> PL[Prompts Layer]
    TL --> EXT[External Systems APIs DB Files]
    RL --> EXT
```

## Layers

| Layer | Responsibility |
|-------|----------------|
| **Client** | Session, discovery, invoke, handle notifications |
| **Transport** | Framing, connection, streaming bytes |
| **Protocol** | JSON-RPC 2.0 messages, IDs, errors |
| **Server** | Route methods, enforce auth, register handlers |
| **Tools** | Executable functions with input/output schema |
| **Resources** | Readable URI-addressed content |
| **Prompts** | Templated prompt messages with arguments |
| **External** | DB, APIs, filesystem behind server impl |

## Message Flow

```mermaid
sequenceDiagram
    participant H as Host
    participant C as MCP Client
    participant S as MCP Server
    H->>C: use tool X
    C->>S: tools/call
    S->>S: validate + execute
    S-->>C: result / error
    C-->>H: observation
```

## Navigation

- [MCP Lifecycle](mcp-lifecycle.md) · [Core Concepts](mcp-core-concepts.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
