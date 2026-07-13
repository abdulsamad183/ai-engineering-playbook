"""Prompt chaining — multi-step pipeline with intermediate outputs.

Run: python example-prompt-chaining.py
"""

from __future__ import annotations

import json
from dataclasses import dataclass


@dataclass
class ChainStep:
    name: str
    system: str
    extract_key: str | None = None  # key to pass to next step


ANALYZE_THEN_SUMMARIZE = [
    ChainStep(
        name="extract_facts",
        system="Extract key facts as a JSON array from the document. Output only JSON.",
        extract_key="facts",
    ),
    ChainStep(
        name="summarize",
        system="Summarize the following facts in 3 bullet points for an executive audience.",
        extract_key=None,
    ),
]


async def run_chain(document: str, llm_client, steps: list[ChainStep]) -> str:
    context = {"document": document}
    result = document

    for step in steps:
        user_content = result if step.name != "extract_facts" else context["document"]
        response = await llm_client.complete(
            system=step.system,
            user=user_content,
            temperature=0.1,
        )
        if step.extract_key:
            parsed = json.loads(response)
            result = json.dumps(parsed) if isinstance(parsed, list) else response
            context[step.extract_key] = parsed
        else:
            result = response

    return result


class MockLLM:
    async def complete(self, system: str, user: str, temperature: float = 0.0) -> str:
        if "JSON array" in system:
            return '["Revenue grew 23%", "Churn decreased to 2%", "New product launched in Q3"]'
        return "- Revenue grew 23% YoY\n- Churn improved to 2%\n- Q3 product launch successful"


async def main() -> None:
    doc = "Q3 report: Revenue grew 23%. Churn fell to 2%. We launched Product X."
    summary = await run_chain(doc, MockLLM(), ANALYZE_THEN_SUMMARIZE)
    print(summary)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
