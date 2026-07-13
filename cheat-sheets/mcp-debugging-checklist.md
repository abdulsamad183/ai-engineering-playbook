# MCP Debugging Checklist

| Symptom | Check |
|---------|-------|
| Tool not found | Stale `tools/list` cache; `list_changed` |
| Hang after restart | Re-`initialize` session |
| Invalid params | Schema vs model output; log args |
| Transport reset | STDIO stderr on stdout? proxy timeout |
| Auth failures | Token scope; initialize context |
| Retry storm | Circuit breaker; idempotency |

See [MCP Engineering Mistakes](../domains/mcp/mcp-engineering-mistakes.md).
