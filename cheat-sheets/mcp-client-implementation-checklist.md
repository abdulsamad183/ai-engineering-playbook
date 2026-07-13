# MCP Client Implementation Checklist

- [ ] Transport connect with timeout
- [ ] `initialize` + `initialized` handshake
- [ ] Capability cache with TTL
- [ ] Handle `*_list_changed` notifications
- [ ] Retry only idempotent tools
- [ ] Reconnect + re-initialize on transport drop
- [ ] Correlation IDs in logs
- [ ] Multi-server routing if applicable

See [Build an MCP Client](../domains/mcp/build-an-mcp-client.md).
