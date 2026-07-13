# MCP Tool Design Checklist

- [ ] JSON Schema with `required` fields
- [ ] Clear description (model reads this)
- [ ] Bounded output size
- [ ] Timeout configured
- [ ] Idempotent flag / retry policy documented
- [ ] Permission class: read / write / destructive
- [ ] Errors return structured `isError` content
- [ ] No secrets in schema or responses

See [MCP Tools](../domains/mcp/mcp-tools.md).
