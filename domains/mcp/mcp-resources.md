---
title: "MCP Resources"
description: "MCP resources — static/dynamic, URI design, metadata, discovery, pagination, access control, caching."
domain: mcp
tags: [mcp, resources, URI, discovery]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - mcp-core-concepts.md
  - ../context-engineering/retrieval-context.md
keywords: [MCP resources, resource URI, resources/read]
author: hp
---

# MCP Resources

## Overview

Section **7**. Resources provide **addressable context** to hosts without executing tools.

## Types

| Type | Example URI | Use |
|------|-------------|-----|
| **Static** | `config://app/settings` | Fixed config blob |
| **Dynamic** | `db://reports/daily` | Generated on read |
| **File** | `file:///project/README.md` | Filesystem servers |

## URI Design

- Use hierarchical schemes: `tenant://acme/policy/refund`
- Include version in path or metadata when content changes
- Document MIME type in resource metadata

## Operations

- `resources/list` — discovery (paginate cursors)
- `resources/read` — fetch content by URI
- `resources/subscribe` — notifications on change (if supported)

## Access Control

Filter `resources/list` by authenticated principal. Never leak URIs the caller cannot read.

## Caching

Client caches by `(uri, etag)` with TTL; invalidate on `resources/list_changed` notification.

## Navigation

- [MCP Prompts](mcp-prompts.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
