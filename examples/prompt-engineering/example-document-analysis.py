"""Document analysis pipeline — extract, classify, summarize in one chain.

Run: python example-document-analysis.py
"""

from __future__ import annotations

import json
from dataclasses import dataclass


@dataclass
class AnalysisResult:
    doc_type: str
    entities: dict
    summary: str
    risk_flags: list[str]


EXTRACT_PROMPT = """Extract entities from the document as JSON:
{"parties": [], "dates": [], "amounts": [], "obligations": []}
Output only JSON."""

CLASSIFY_PROMPT = """Classify document type. Choose one: contract, invoice, report, correspondence, other.
Output JSON: {"doc_type": "...", "confidence": 0.0-1.0}"""

SUMMARIZE_PROMPT = """Summarize in 3 bullets for a legal ops reviewer. Flag risks as a JSON array in field risk_flags.
Output JSON: {"summary": "...", "risk_flags": []}"""


async def analyze_document(document: str, llm) -> AnalysisResult:
    entities_raw = await llm.complete(EXTRACT_PROMPT, document, temperature=0.0)
    entities = json.loads(entities_raw)

    classify_raw = await llm.complete(
        CLASSIFY_PROMPT,
        f"Entities: {json.dumps(entities)}\n\nDocument:\n{document[:4000]}",
        temperature=0.0,
    )
    doc_type = json.loads(classify_raw)["doc_type"]

    summary_raw = await llm.complete(
        SUMMARIZE_PROMPT,
        document[:6000],
        temperature=0.1,
    )
    parsed = json.loads(summary_raw)

    return AnalysisResult(
        doc_type=doc_type,
        entities=entities,
        summary=parsed["summary"],
        risk_flags=parsed.get("risk_flags", []),
    )


class MockLLM:
    async def complete(self, system: str, user: str, temperature: float = 0.0) -> str:
        if "entities" in system.lower():
            return '{"parties": ["Acme Corp", "Beta LLC"], "dates": ["2026-01-15"], "amounts": ["$50,000"], "obligations": ["Net 30 payment"]}'
        if "Classify" in system:
            return '{"doc_type": "contract", "confidence": 0.94}'
        return '{"summary": "- Master services agreement\\n- $50K value, Net 30\\n- Effective Jan 15, 2026", "risk_flags": ["auto-renewal clause"]}'


async def main() -> None:
    doc = "MASTER SERVICES AGREEMENT between Acme Corp and Beta LLC. Effective January 15, 2026. Fee: $50,000. Payment Net 30. Auto-renewal unless 60-day notice."
    result = await analyze_document(doc, MockLLM())
    print(result)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
