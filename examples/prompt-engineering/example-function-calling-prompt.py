"""Function-calling prompt pattern — tools in system, structured tool selection.

Run: python example-function-calling-prompt.py
"""

from __future__ import annotations

import json
from typing import Any


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_knowledge_base",
            "description": "Search internal docs for policy answers",
            "parameters": {
                "type": "object",
                "properties": {"query": {"type": "string"}},
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "create_support_ticket",
            "description": "Escalate to human support",
            "parameters": {
                "type": "object",
                "properties": {
                    "subject": {"type": "string"},
                    "priority": {"type": "string", "enum": ["low", "medium", "high"]},
                },
                "required": ["subject", "priority"],
            },
        },
    },
]

SYSTEM_PROMPT = """You are a customer support agent for Acme SaaS.

Use tools when needed:
- search_knowledge_base: for policy and how-to questions
- create_support_ticket: when the user requests a human or issue is unresolved

If you can answer from conversation alone, respond directly without tools.
Never invent refund amounts or SLA commitments not in tool results.
"""


def build_chat_request(user_message: str) -> dict[str, Any]:
  return {
      "messages": [
          {"role": "system", "content": SYSTEM_PROMPT},
          {"role": "user", "content": user_message},
      ],
      "tools": TOOLS,
      "tool_choice": "auto",
      "temperature": 0.2,
  }


def parse_tool_call(response: dict[str, Any]) -> tuple[str | None, dict | None]:
    """Extract first tool call from OpenAI-style response."""
    choice = response.get("choices", [{}])[0]
    message = choice.get("message", {})
    tool_calls = message.get("tool_calls")
    if not tool_calls:
        return message.get("content"), None
    tc = tool_calls[0]
    return None, {
        "name": tc["function"]["name"],
        "arguments": json.loads(tc["function"]["arguments"]),
    }


if __name__ == "__main__":
    req = build_chat_request("I was charged twice on invoice 8842. Can you help?")
    print(json.dumps(req, indent=2)[:500])

    mock_response = {
        "choices": [{
            "message": {
                "tool_calls": [{
                    "function": {
                        "name": "search_knowledge_base",
                        "arguments": json.dumps({"query": "duplicate charge refund policy"}),
                    }
                }]
            }
        }]
    }
    content, tool = parse_tool_call(mock_response)
    print("tool:", tool)
