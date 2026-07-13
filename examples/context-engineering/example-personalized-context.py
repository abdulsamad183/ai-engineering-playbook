"""Personalized context — profile-driven context blocks.

Run: python example-personalized-context.py
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class UserProfile:
    user_id: str
    locale: str
    tier: str
    style: str
    opt_out: bool = False


def build_personalized_blocks(profile: UserProfile) -> list[str]:
    if profile.opt_out:
        return []
    return [
        f"<profile locale=\"{profile.locale}\" tier=\"{profile.tier}\" />",
        f"<preference>Respond in {profile.style} style.</preference>",
    ]


if __name__ == "__main__":
    p = UserProfile("u1", "en-GB", "enterprise", "concise")
    print(build_personalized_blocks(p))
