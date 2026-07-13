---
title: "MCP Core Concepts"
description: "MCP clients, servers, resources, prompts, tools, messages, sessions, capabilities, notifications."
domain: mcp
tags: [mcp, concepts, tools, resources, prompts, phase-9]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - mcp-message-protocol.md
  - mcp-tools.md
  - mcp-resources.md
  - mcp-prompts.md
keywords: [MCP concepts, capabilities, JSON-RPC]
author: hp
---

# MCP Core Concepts

## Overview

Section **4** of Phase 9.

| Component | Responsibility |
|-----------|----------------|
| **Client** | Protocol initiator in host process |
| **Server** | Capability provider |
| **Resources** | Context by URI (`file://`, custom scheme) |
| **Prompts** | Reusable prompt templates |
| **Tools** | Side-effecting or compute actions |
| **Messages** | JSON-RPC requests/responses/notifications |
| **Sessions** | Stateful binding over transport |
| **Capabilities** | Feature flags from `initialize` |
| **Registries** | In-server registration of handlers |
| **Notifications** | Server→client async events |
| **Requests** | Client→server with `id` |
| **Responses** | Result or error linked by `id` |

## Tools vs Resources vs Prompts

| Primitive | Read/Write | Purpose |
|-----------|------------|---------|
| **Resource** | Read (usually) | Context injection |
| **Prompt** | Read | Template messages |
| **Tool** | Execute | Actions, side effects |

## Navigation

- [MCP Tools](mcp-tools.md) · [Comparison Guides](mcp-comparison-guides.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 9 Section 4 |
