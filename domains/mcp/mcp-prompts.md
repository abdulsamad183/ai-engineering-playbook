---
title: "MCP Prompts"
description: "MCP prompt registry — templates, parameters, metadata, versioning, discovery, validation."
domain: mcp
tags: [mcp, prompts, templates, registry]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - ../prompt-engineering/prompt-templates-guide.md
  - mcp-core-concepts.md
keywords: [MCP prompts, prompts/get, parameterized prompts]
author: hp
---

# MCP Prompts

## Overview

Section **8**. Prompts become **protocol assets** — discoverable, versioned templates servers expose via `prompts/list` and `prompts/get`.

## Prompt as Protocol Asset

```mermaid
flowchart LR
    REG[Prompt Registry on Server] --> LIST[prompts/list]
    LIST --> GET[prompts/get with args]
    GET --> MSG[Rendered messages]
    MSG --> HOST[Host injects into LLM]
```

## Features

| Feature | Description |
|---------|-------------|
| **Registry** | Named prompts with descriptions |
| **Parameters** | JSON Schema for template variables |
| **Metadata** | Tags, version, audience |
| **Validation** | Reject missing required args |
| **Reuse** | Same prompt across hosts |

## Example

Server exposes `code-review` prompt with `language` and `diff` parameters — host fetches rendered messages instead of duplicating template strings.

## Navigation

- [MCP Tools](mcp-tools.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
