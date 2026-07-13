# MCP Message Types Cheat Sheet

| Type | Has `id` | Example methods |
|------|----------|-----------------|
| Request | Yes | `tools/call`, `initialize` |
| Response | Matches id | `result` or `error` |
| Notification | No | `initialized`, `tools/list_changed` |

**Error codes:** `-32600` invalid · `-32601` not found · `-32602` invalid params

See [Message Protocol](../domains/mcp/mcp-message-protocol.md).
