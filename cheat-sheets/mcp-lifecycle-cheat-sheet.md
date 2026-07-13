# MCP Lifecycle Cheat Sheet

| Stage | Method / Action |
|-------|-----------------|
| Connect | Open transport (STDIO / HTTP) |
| Initialize | `initialize` → capabilities |
| Ready | Client sends `initialized` notification |
| Discover | `tools/list`, `resources/list`, `prompts/list` |
| Use | `tools/call`, `resources/read`, `prompts/get` |
| Updates | Handle `*_list_changed` notifications |
| Shutdown | Close transport; drain in-flight |

See [MCP Lifecycle](../domains/mcp/mcp-lifecycle.md).
