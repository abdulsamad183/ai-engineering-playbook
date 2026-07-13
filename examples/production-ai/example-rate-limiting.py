"""Token bucket rate limiter for AI API.

Run: python example-rate-limiting.py
"""

import time
from dataclasses import dataclass


@dataclass
class TokenBucket:
    capacity: int
    refill_per_sec: float
    tokens: float
    last: float

    @classmethod
    def create(cls, capacity: int, refill_per_sec: float) -> "TokenBucket":
        return cls(capacity=capacity, refill_per_sec=refill_per_sec, tokens=float(capacity), last=time.monotonic())

    def allow(self, cost: float = 1.0) -> bool:
        now = time.monotonic()
        elapsed = now - self.last
        self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_per_sec)
        self.last = now
        if self.tokens >= cost:
            self.tokens -= cost
            return True
        return False


if __name__ == "__main__":
    bucket = TokenBucket.create(capacity=5, refill_per_sec=1.0)
    for i in range(8):
        print(i, bucket.allow())
