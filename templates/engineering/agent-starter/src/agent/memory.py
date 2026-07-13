"""Short-term memory buffer."""

from collections import deque


class Memory:
    def __init__(self, max_items: int = 20) -> None:
        self._items: deque[str] = deque(maxlen=max_items)

    def add(self, item: str) -> None:
        self._items.append(item)

    def recall(self) -> list[str]:
        return list(self._items)
