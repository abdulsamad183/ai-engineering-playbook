# MCP Engineering Examples

> Phase 9 patterns. See [MCP Handbook](../../domains/mcp/README.md).

Uses a minimal `mcp_protocol.py` to demonstrate JSON-RPC patterns without requiring the full MCP SDK.

| Example | Pattern |
|---------|---------|
| [mcp_protocol.py](mcp_protocol.py) | Shared mini server/client |
| [example-basic-mcp-server.py](example-basic-mcp-server.py) | STDIO server |
| [example-basic-mcp-client.py](example-basic-mcp-client.py) | STDIO client |
| [example-tool-registration.py](example-tool-registration.py) | Tool registry |
| [example-resource-registration.py](example-resource-registration.py) | Resource URIs |
| [example-prompt-registration.py](example-prompt-registration.py) | Prompt templates |
| [example-stdio-transport.py](example-stdio-transport.py) | STDIO transport |
| [example-http-transport.py](example-http-transport.py) | HTTP JSON-RPC |
| [example-streaming-transport.py](example-streaming-transport.py) | Progress streaming |
| [example-multi-server-client.py](example-multi-server-client.py) | Multi-server routing |
| [example-authentication.py](example-authentication.py) | API key auth |
| [example-logging.py](example-logging.py) | Structured logging |
| [example-testing.py](example-testing.py) | Integration test |
| [example-fastapi-mcp.py](example-fastapi-mcp.py) | FastAPI co-host |

```bash
cd examples/mcp
python example-basic-mcp-client.py
python example-testing.py
```

FastAPI (optional): `pip install fastapi uvicorn` then `uvicorn example-fastapi-mcp:app --port 8080`
