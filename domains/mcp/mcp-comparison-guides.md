---
title: "MCP Comparison Guides"
description: "MCP vs REST, function calling, transports, primitives, multi-server, authentication strategies."
domain: mcp
tags: [mcp, comparison, decision-matrix, phase-9]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - introduction-to-mcp.md
  - mcp-transport-layer.md
keywords: [MCP comparison, REST, STDIO, multi-server]
author: hp
---

# MCP Comparison Guides

## Overview

Decision matrices for MCP engineering choices.

---

## MCP vs REST

| Dimension | MCP | REST |
|-----------|-----|------|
| **Purpose** | AI capability protocol | General HTTP APIs |
| **Discovery** | `tools/list`, `resources/list` | OpenAPI / docs |
| **Session** | `initialize` negotiation | Stateless per request |
| **Primitives** | Tools, resources, prompts | Resources (nouns) only |
| **Host ecosystem** | IDE/agent native | Custom integration |
| **When to choose MCP** | Agent hosts, reusable servers | Public CRUD APIs |

---

## MCP vs Direct Function Calling

| Dimension | MCP | In-app functions |
|-----------|-----|------------------|
| **Coupling** | Loose; external servers | Tight; same codebase |
| **Reuse** | Cross-host server catalog | Per-app |
| **Latency** | Transport overhead | Minimal |
| **When to choose MCP** | Multiple integrations, third-party servers | Few static tools |

---

## STDIO vs HTTP vs WebSockets

| Transport | Latency | Remote | Complexity | Best for |
|-----------|---------|--------|------------|----------|
| **STDIO** | Low | No | Low | Local IDE tools |
| **HTTP+SSE** | Medium | Yes | Medium | Remote SaaS servers |
| **Streamable HTTP** | Medium | Yes | Medium | Modern remote MCP |
| **WebSockets** | Low | Yes | High | Bidirectional streaming |

---

## Resources vs Tools vs Prompts

| Primitive | Mutates state | Addressable | LLM invokes |
|-----------|---------------|-------------|-------------|
| **Resource** | No (read) | URI | Via host read |
| **Tool** | Often yes | Name | Model selects |
| **Prompt** | No | Name | Host fetches template |

---

## Single-Server vs Multi-Server

| Dimension | Single | Multi |
|-----------|--------|-------|
| **Complexity** | Low | Router + discovery |
| **Blast radius** | Large | Isolated per domain |
| **Scaling** | Monolith server | Scale per domain |
| **When** | Prototype | Production |

---

## Authentication Strategies

| Strategy | Complexity | UX | Enterprise fit |
|----------|------------|-----|----------------|
| API key | Low | Dev | Internal |
| OAuth | High | User consent | SaaS |
| mTLS | Medium | Transparent | Service mesh |

---

## Navigation

- [Transport Layer](mcp-transport-layer.md) · [Introduction](introduction-to-mcp.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Phase 9 comparisons |
