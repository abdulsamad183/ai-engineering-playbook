# MCP Transport Selection Cheat Sheet

| Need | Choose |
|------|--------|
| Local IDE / CLI tool | **STDIO** |
| Remote SaaS integration | **HTTP + SSE** or streamable HTTP |
| Bidirectional streaming | **WebSockets** (when host supports) |
| Air-gapped | **STDIO** subprocess only |

See [Transport Layer](../domains/mcp/transport-and-auth/01-mcp-transport-layer.md) · [Comparisons](../domains/mcp/production/05-mcp-comparison-guides.md).
