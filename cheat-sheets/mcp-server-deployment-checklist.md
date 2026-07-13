# MCP Server Deployment Checklist

- [ ] Health endpoint (HTTP) or process supervisor (STDIO)
- [ ] Graceful shutdown with request drain
- [ ] Structured JSON logging + request_id
- [ ] Secrets from env / vault
- [ ] Per-tool timeouts
- [ ] Resource limits (CPU, memory)
- [ ] CI tests for tool contracts
- [ ] Capability change notifications on deploy

See [Build an MCP Server](../domains/mcp/build-an-mcp-server.md) · [Production MCP](../domains/mcp/production-mcp.md).
