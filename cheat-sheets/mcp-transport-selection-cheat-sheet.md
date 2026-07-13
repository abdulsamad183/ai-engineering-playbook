# MCP Transport Selection Cheat Sheet

| Need | Choose |
|------|--------|
| Local IDE / CLI tool | **STDIO** |
| Remote SaaS integration | **HTTP + SSE** or streamable HTTP |
| Bidirectional streaming | **WebSockets** (when host supports) |
| Air-gapped | **STDIO** subprocess only |

See [Transport Layer](../domains/mcp/mcp-transport-layer.md) · [Comparisons](../domains/mcp/mcp-comparison-guides.md).
