"""FastAPI + MCP-style JSON-RPC endpoint co-hosted.

Run: uvicorn example-fastapi-mcp:app --port 8080
Then: curl -X POST http://127.0.0.1:8080/mcp -H 'Content-Type: application/json' \\
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from mcp_protocol import MiniMcpServer

mcp = MiniMcpServer("fastapi-mcp")
mcp.register_tool(
    "health_check",
    {"description": "Health check tool", "inputSchema": {"type": "object", "properties": {}}},
    lambda _: "ok",
)

app = FastAPI(title="MCP + REST")


@app.get("/health")
async def health() -> dict:
    return {"status": "healthy"}


@app.post("/mcp")
async def mcp_endpoint(request: Request) -> JSONResponse:
    body = await request.json()
    resp = mcp.handle(body)
    return JSONResponse(resp or {"jsonrpc": "2.0", "id": body.get("id"), "error": {"code": -32600, "message": "Invalid request"}})
