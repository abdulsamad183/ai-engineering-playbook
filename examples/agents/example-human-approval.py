"""Human approval gate before destructive tool execution.

Run: python example-human-approval.py
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ApprovalStatus(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


@dataclass
class PendingAction:
    tool: str
    args: dict
    status: ApprovalStatus = ApprovalStatus.PENDING


class ApprovalQueue:
    def __init__(self) -> None:
        self._pending: dict[str, PendingAction] = {}

    def request(self, action_id: str, tool: str, args: dict) -> None:
        self._pending[action_id] = PendingAction(tool, args)

    def resolve(self, action_id: str, approved: bool) -> PendingAction | None:
        action = self._pending.get(action_id)
        if not action:
            return None
        action.status = ApprovalStatus.APPROVED if approved else ApprovalStatus.REJECTED
        return action


async def execute_with_approval(queue: ApprovalQueue, action_id: str, tool_fn, auto_approve_read: bool = True):
    action = queue._pending[action_id]
    if action.tool.startswith("read_") and auto_approve_read:
        return await tool_fn(**action.args)
    if action.status != ApprovalStatus.APPROVED:
        raise PermissionError("Action not approved")
    return await tool_fn(**action.args)
