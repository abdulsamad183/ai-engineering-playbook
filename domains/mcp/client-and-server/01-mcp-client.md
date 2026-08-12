---
title: "MCP Client"
description: "MCP client architecture — connection, discovery, capability negotiation, tool invocation, streaming, retries."
domain: mcp
tags: [mcp, client, connection, retry]
status: published
created: 2026-07-13
updated: 2026-07-13
version: "1.0"
related:
  - build-an-mcp-client.md
  - mcp-lifecycle.md
keywords: [MCP client, initialize, tools/call, reconnection]
author: hp
---

# MCP Client

## Overview

Section **5**.

```mermaid
flowchart TD
    START[Start] --> CONN[Connect transport]
    CONN --> INIT[initialize]
    INIT --> CAP[Cache capabilities]
    CAP --> LOOP[Request loop]
    LOOP --> TOOL[tools/call]
    LOOP --> RES[resources/read]
    LOOP --> PROM[prompts/get]
```

## Responsibilities

- Manage transport lifecycle (connect, reconnect)
- Send `initialize` / `initialized` handshake
- Cache `tools/list`, `resources/list`, `prompts/list`
- Invoke tools with timeout and retry policy
- Handle server notifications (`tools/list_changed`)
- Propagate errors to host with correlation IDs

## Retry Strategy

| Error | Action |
|-------|--------|
| Transport reset | Reconnect + re-initialize |
| Tool timeout | Retry if idempotent |
| Invalid params | No retry; fix schema |

## Python Example

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_client():
    params = StdioServerParameters(command="python", args=["server.py"])
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            result = await session.call_tool(tools.tools[0].name, arguments={})
            return result
```

## Navigation

- [Build an MCP Client](build-an-mcp-client.md)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-13 | Initial publication |
