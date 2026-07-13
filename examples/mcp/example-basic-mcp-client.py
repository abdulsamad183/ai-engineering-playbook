"""Basic MCP-style client connecting to STDIO server.

Run: python example-basic-mcp-client.py
"""

import subprocess
import sys

from mcp_protocol import MiniMcpClient


def main() -> None:
    proc = subprocess.Popen(
        [sys.executable, "example-basic-mcp-server.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=__import__("pathlib").Path(__file__).parent,
    )
    client = MiniMcpClient(proc)
    info = client.initialize()
    print("Initialized:", info["serverInfo"]["name"])
    tools = client.list_tools()
    print("Tools:", [t["name"] for t in tools])
    out = client.call_tool("echo", {"text": "hello mcp"})
    print("Result:", out)
    proc.terminate()


if __name__ == "__main__":
    main()
