"""Versioned prompt loader — treats prompts as software artifacts.

Run: python example-prompt-loader.py
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PromptTemplate:
    name: str
    version: str
    system: str
    user: str

    def render(self, **variables: str) -> tuple[str, str]:
        system = self.system.format(**variables)
        user = self.user.format(**variables)
        return system, user


class PromptRepository:
    def __init__(self, base_dir: Path):
        self._base = base_dir
        self._cache: dict[str, PromptTemplate] = {}

    def load(self, name: str, version: str = "1.0") -> PromptTemplate:
        key = f"{name}@{version}"
        if key in self._cache:
            return self._cache[key]

        path = self._base / name / f"v{version}.txt"
        if not path.exists():
            raise FileNotFoundError(f"Prompt not found: {path}")

        content = path.read_text()
        system, _, user = content.partition("---USER---")
        template = PromptTemplate(
            name=name,
            version=version,
            system=system.strip(),
            user=user.strip(),
        )
        self._cache[key] = template
        return template


# Demo with inline template (production: load from files)
CLASSIFICATION_V1 = PromptTemplate(
    name="classification",
    version="1.0",
    system="""You classify user feedback into exactly one category.
Categories: bug, feature_request, question, praise
Respond with JSON: {{"category": "<category>", "confidence": <0-1>}}""",
    user="Feedback: {feedback}",
)


async def classify_feedback(feedback: str, llm_client) -> dict:
    system, user = CLASSIFICATION_V1.render(feedback=feedback)
    # Production: call LLM with system + user messages
    response = await llm_client.complete(system=system, user=user, temperature=0.0)
    return response


if __name__ == "__main__":
    repo = PromptRepository(Path("prompts/production"))
    tpl = CLASSIFICATION_V1
    s, u = tpl.render(feedback="The export button crashes on large files.")
    print("=== SYSTEM ===")
    print(s)
    print("=== USER ===")
    print(u)
