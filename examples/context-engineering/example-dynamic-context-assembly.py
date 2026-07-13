"""Dynamic context assembly — intent-based policy resolver.

Run: python example-dynamic-context-assembly.py
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ContextRequest:
    user_id: str
    message: str
    tier: str


INTENT_KEYWORDS = {
    "billing": ["invoice", "charge", "refund", "payment"],
    "technical": ["error", "sso", "login", "api"],
}


def detect_intent(message: str) -> str:
    lower = message.lower()
    for intent, keywords in INTENT_KEYWORDS.items():
        if any(k in lower for k in keywords):
            return intent
    return "general"


def resolve_policy_blocks(req: ContextRequest) -> list[str]:
    intent = detect_intent(req.message)
    blocks = ["<base_policy>Always be accurate.</base_policy>"]
    if req.tier == "enterprise":
        blocks.append("<sla>99.9% uptime SLA applies.</sla>")
    if intent == "billing":
        blocks.append("<billing_policy>Refunds in 3 business days.</billing_policy>")
    elif intent == "technical":
        blocks.append("<tech_playbook>Check SSO metadata first.</tech_playbook>")
    return blocks


if __name__ == "__main__":
    req = ContextRequest("u1", "duplicate charge on invoice", "enterprise")
    print("\n".join(resolve_policy_blocks(req)))
