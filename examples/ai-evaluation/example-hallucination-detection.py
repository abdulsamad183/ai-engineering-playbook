"""Hallucination detection — citation and support checks.

Run: python example-hallucination-detection.py
"""

import re


def unsupported_citations(answer: str, valid_ids: set[str]) -> list[str]:
    cited = set(re.findall(r"\[(\w+)\]", answer))
    return sorted(cited - valid_ids)


def unsupported_claim_heuristic(answer: str, context: str) -> float:
    """Simplified: fraction of answer bigrams not in context."""
    def bigrams(text: str) -> set[tuple[str, str]]:
        words = text.lower().split()
        return {(words[i], words[i + 1]) for i in range(len(words) - 1)}

    a, c = bigrams(answer), bigrams(context)
    if not a:
        return 0.0
    return len(a - c) / len(a)


def main() -> None:
    answer = "Refunds take 30 days [policy-1]. See also [fake-9]."
    print("bad citations:", unsupported_citations(answer, {"policy-1"}))
    ctx = "Refunds accepted within 30 days with receipt."
    print("unsupported ratio:", unsupported_claim_heuristic("Refunds take 30 days", ctx))


if __name__ == "__main__":
    main()
