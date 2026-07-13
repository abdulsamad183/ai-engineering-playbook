"""Session management — load/save conversation state with TTL semantics.

Run: python example-session-management.py
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
import json


@dataclass
class Session:
    session_id: str
    user_id: str
    phase: str = "idle"
    slots: dict[str, str] = field(default_factory=dict)
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def touch(self) -> None:
        self.updated_at = datetime.now(timezone.utc)

    def is_expired(self, ttl_hours: int = 24) -> bool:
        return datetime.now(timezone.utc) - self.updated_at > timedelta(hours=ttl_hours)


class SessionStore:
  """In-memory demo; production uses Redis."""

  def __init__(self) -> None:
      self._data: dict[str, Session] = {}

  def get(self, session_id: str) -> Session | None:
      s = self._data.get(session_id)
      if s and s.is_expired():
          del self._data[session_id]
          return None
      return s

  def save(self, session: Session) -> None:
      session.touch()
      self._data[session.session_id] = session

  def serialize(self, session: Session) -> str:
      return json.dumps({
          "session_id": session.session_id,
          "user_id": session.user_id,
          "phase": session.phase,
          "slots": session.slots,
      })


if __name__ == "__main__":
    store = SessionStore()
    s = Session("s1", "u1", phase="collecting_issue")
    s.slots["issue"] = "duplicate charge"
    store.save(s)
    loaded = store.get("s1")
    print(store.serialize(loaded))
