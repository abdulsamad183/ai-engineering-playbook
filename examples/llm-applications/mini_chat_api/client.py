"""Client for mini_chat_api. Start server.py first."""
from __future__ import annotations

import json
import urllib.request

URL = "http://127.0.0.1:8765/v1/chat"


def chat(content: str) -> str:
    req = urllib.request.Request(
        URL,
        data=json.dumps({"messages": [{"role": "user", "content": content}]}).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=5) as resp:  # noqa: S310
        return json.loads(resp.read().decode())["reply"]


if __name__ == "__main__":
    print(chat("hello from mini chat api"))
