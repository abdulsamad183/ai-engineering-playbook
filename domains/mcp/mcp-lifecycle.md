---
title: "MCP Lifecycle"
description: "MCP session lifecycle — discovery, capability negotiation, initialization, requests, streaming, termination."
domain: mcp
tags: [mcp, lifecycle, session, initialization, phase-9]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - mcp-client.md
  - mcp-server.md
keywords: [MCP lifecycle, initialize, capability negotiation]
author: hp
---

# MCP Lifecycle

## Overview

Section **3** of Phase 9.

```mermaid
stateDiagram-v2
    [*] --> ClientStartup
    ClientStartup --> Connect: open transport
    Connect --> Initialize: initialize request
    Initialize --> Negotiated: capabilities exchanged
    Negotiated --> Active: tools/list resources/list
    Active --> Request: tools/call resources/read
    Request --> Active: response
    Active --> Streaming: optional stream
    Streaming --> Active
    Active --> Notify: server notifications
    Active --> Terminated: close
    Terminated --> [*]
```

## Stages

| Stage | Actions |
|-------|---------|
| **Client startup** | Load server config, spawn or connect |
| **Discovery** | Resolve server endpoint / command |
| **Capability negotiation** | `initialize` with protocol version |
| **Session init** | `initialized` notification from client |
| **Requests** | list/call/read/get operations |
| **Streaming** | Partial results for long operations |
| **Updates** | `list_changed` notifications |
| **Termination** | Close transport, cleanup |

## Navigation

- [MCP Client](mcp-client.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 9 Section 3 |
