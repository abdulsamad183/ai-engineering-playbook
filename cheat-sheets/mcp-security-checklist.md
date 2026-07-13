# MCP Security Checklist

- [ ] TLS on remote transports
- [ ] Auth at connection + per-tool RBAC
- [ ] Input validation (JSON Schema)
- [ ] Output sanitization before LLM context
- [ ] Sandboxed subprocess / container for STDIO servers
- [ ] No unconstrained shell tools
- [ ] Tenant isolation on shared servers
- [ ] Audit log for write tools
- [ ] HITL for destructive operations

See [MCP Security](../domains/mcp/mcp-security.md).
