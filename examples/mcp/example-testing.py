"""MCP server integration test pattern.

Run: python example-testing.py
"""

import subprocess
import sys
from pathlib import Path

from mcp_protocol import MiniMcpClient


def test_echo_roundtrip() -> None:
    here = Path(__file__).parent
    proc = subprocess.Popen(
        [sys.executable, "example-basic-mcp-server.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
        cwd=here,
    )
    client = MiniMcpClient(proc)
    client.initialize()
    tools = client.list_tools()
    assert any(t["name"] == "echo" for t in tools)
    result = client.call_tool("echo", {"text": "test"})
    assert result == "test"
    proc.terminate()
    print("PASS: echo roundtrip")


if __name__ == "__main__":
    test_echo_roundtrip()
