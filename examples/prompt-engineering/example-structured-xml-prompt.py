"""XML-structured prompt for reliable parsing.

Run: python example-structured-xml-prompt.py
"""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET


def build_xml_prompt(document: str, question: str) -> str:
    return f"""<task>
  <role>You are a precise document analyst.</role>
  <instructions>
    Answer the question using only information from the document.
    If the answer is not in the document, respond with "NOT_FOUND".
  </instructions>
  <document>
{document}
  </document>
  <question>{question}</question>
  <output_format>
    <answer>Your answer here</answer>
    <confidence>high|medium|low</confidence>
    <source_quote>Exact quote supporting the answer</source_quote>
  </output_format>
</task>"""


def parse_xml_response(response: str) -> dict:
    # Extract XML block from response (models may add preamble)
    match = re.search(r"<output_format>.*?</output_format>", response, re.DOTALL)
    if not match:
        raise ValueError("No output_format block in response")
    root = ET.fromstring(f"<root>{match.group()}</root>")
    fmt = root.find("output_format")
    return {
        "answer": fmt.findtext("answer", ""),
        "confidence": fmt.findtext("confidence", "low"),
        "source_quote": fmt.findtext("source_quote", ""),
    }


def main() -> None:
    doc = "The API rate limit is 100 requests per minute for free tier users."
    prompt = build_xml_prompt(doc, "What is the rate limit?")
    print(prompt[:300], "...")

    mock_response = """<output_format>
  <answer>100 requests per minute</answer>
  <confidence>high</confidence>
  <source_quote>The API rate limit is 100 requests per minute</source_quote>
</output_format>"""
    print(parse_xml_response(mock_response))


if __name__ == "__main__":
    main()
