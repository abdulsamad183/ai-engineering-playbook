---
title: "MCP Transport Layer"
description: "MCP transports — STDIO, HTTP, SSE, WebSockets, streaming, reconnection, comparison."
domain: mcp
tags: [mcp, transport, stdio, http, sse, websocket]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - mcp-architecture.md
  - mcp-comparison-guides.md
keywords: [STDIO, HTTP, SSE, WebSocket, transport]
author: hp
---

# MCP Transport Layer

## Overview

Section **10**.

| Transport | Use case | Pros | Cons |
|-----------|----------|------|------|
| **STDIO** | Local subprocess servers | Simple, secure local | Not remote |
| **HTTP + SSE** | Remote servers | Firewall-friendly | SSE complexity |
| **Streamable HTTP** | Modern remote | Unified stream | Newer spec |
| **WebSockets** | Bidirectional remote | Low latency | Infra overhead |

```mermaid
flowchart TB
    subgraph Local
        C1[Client] --> STDIO[STDIO pipes]
        STDIO --> S1[python server.py]
    end
    subgraph Remote
        C2[Client] --> HTTP[HTTP/SSE]
        HTTP --> S2[Remote MCP Server]
    end
```

## Reliability

- Keep-alive / heartbeat on long connections
- Exponential backoff reconnect
- Session re-`initialize` after transport drop

## Navigation

- [Message Protocol](mcp-message-protocol.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
