"""Minimal MCP-style JSON-RPC 2.0 helpers for playbook examples.

Not a full MCP SDK — demonstrates protocol patterns from domains/mcp/.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class JsonRpcError(Exception):
    code: int
    message: str

    def to_dict(self) -> dict:
        return {"code": self.code, "message": self.message}


def read_message(stream) -> dict | None:
    line = stream.readline()
    if not line:
        return None
    return json.loads(line)


def write_message(stream, payload: dict) -> None:
    stream.write(json.dumps(payload) + "\n")
    stream.flush()


def make_response(req_id: int, result: Any) -> dict:
    return {"jsonrpc": "2.0", "id": req_id, "result": result}


def make_error(req_id: int, error: JsonRpcError) -> dict:
    return {"jsonrpc": "2.0", "id": req_id, "error": error.to_dict()}


Handler = Callable[[dict], Any]


class MiniMcpServer:
  """STDIO JSON-RPC server with tools, resources, prompts registries."""

  def __init__(self, name: str) -> None:
      self.name = name
      self._tools: dict[str, dict] = {}
      self._tool_handlers: dict[str, Callable] = {}
      self._resources: dict[str, dict] = {}
      self._resource_handlers: dict[str, Callable] = {}
      self._prompts: dict[str, dict] = {}
      self._prompt_handlers: dict[str, Callable] = {}
      self._methods: dict[str, Handler] = {
          "initialize": self._initialize,
          "tools/list": self._tools_list,
          "tools/call": self._tools_call,
          "resources/list": self._resources_list,
          "resources/read": self._resources_read,
          "prompts/list": self._prompts_list,
          "prompts/get": self._prompts_get,
      }

  def register_tool(self, name: str, schema: dict, handler: Callable) -> None:
      self._tools[name] = schema
      self._tool_handlers[name] = handler

  def register_resource(self, uri: str, meta: dict, handler: Callable) -> None:
      self._resources[uri] = meta
      self._resource_handlers[uri] = handler

  def register_prompt(self, name: str, meta: dict, handler: Callable) -> None:
      self._prompts[name] = meta
      self._prompt_handlers[name] = handler

  def _initialize(self, params: dict) -> dict:
      return {
          "protocolVersion": "2024-11-05",
          "serverInfo": {"name": self.name, "version": "1.0.0"},
          "capabilities": {"tools": {}, "resources": {}, "prompts": {}},
      }

  def _tools_list(self, _params: dict) -> dict:
      tools = [
          {"name": n, "description": s.get("description", ""), "inputSchema": s.get("inputSchema", {})}
          for n, s in self._tools.items()
      ]
      return {"tools": tools}

  def _tools_call(self, params: dict) -> dict:
      name = params.get("name")
      args = params.get("arguments", {})
      if name not in self._tool_handlers:
          raise JsonRpcError(-32602, f"Unknown tool: {name}")
      content = self._tool_handlers[name](args)
      return {"content": [{"type": "text", "text": str(content)}], "isError": False}

  def _resources_list(self, _params: dict) -> dict:
      resources = [{"uri": u, **m} for u, m in self._resources.items()]
      return {"resources": resources}

  def _resources_read(self, params: dict) -> dict:
      uri = params.get("uri")
      if uri not in self._resource_handlers:
          raise JsonRpcError(-32602, f"Unknown resource: {uri}")
      text = self._resource_handlers[uri]()
      return {"contents": [{"uri": uri, "mimeType": "text/plain", "text": text}]}

  def _prompts_list(self, _params: dict) -> dict:
      prompts = [{"name": n, **m} for n, m in self._prompts.items()]
      return {"prompts": prompts}

  def _prompts_get(self, params: dict) -> dict:
      name = params.get("name")
      args = params.get("arguments", {})
      if name not in self._prompt_handlers:
          raise JsonRpcError(-32602, f"Unknown prompt: {name}")
      messages = self._prompt_handlers[name](args)
      return {"messages": messages}

  def handle(self, message: dict) -> dict | None:
      if "method" not in message:
          return None
      req_id = message.get("id")
      if req_id is None:
          return None  # notification — ignore in mini server
      method = message["method"]
      params = message.get("params", {})
      try:
          if method not in self._methods:
              raise JsonRpcError(-32601, f"Method not found: {method}")
          result = self._methods[method](params)
          return make_response(req_id, result)
      except JsonRpcError as e:
          return make_error(req_id, e)
      except Exception as e:
          return make_error(req_id, JsonRpcError(-32000, str(e)))

  def serve_stdio(self) -> None:
      while True:
          msg = read_message(sys.stdin)
          if msg is None:
              break
          resp = self.handle(msg)
          if resp:
              write_message(sys.stdout, resp)


class MiniMcpClient:
  """Minimal client for subprocess STDIO servers."""

  def __init__(self, process) -> None:
      self._proc = process
      self._id = 0

  def request(self, method: str, params: dict | None = None) -> dict:
      self._id += 1
      payload = {"jsonrpc": "2.0", "id": self._id, "method": method, "params": params or {}}
      write_message(self._proc.stdin, payload)
      resp = read_message(self._proc.stdout)
      if resp is None:
          raise RuntimeError("Server closed connection")
      if "error" in resp:
          raise RuntimeError(resp["error"]["message"])
      return resp["result"]

  def initialize(self) -> dict:
      return self.request("initialize", {"clientInfo": {"name": "mini-client", "version": "1.0"}})

  def list_tools(self) -> list[dict]:
      return self.request("tools/list")["tools"]

  def call_tool(self, name: str, arguments: dict) -> str:
      result = self.request("tools/call", {"name": name, "arguments": arguments})
      return result["content"][0]["text"]
