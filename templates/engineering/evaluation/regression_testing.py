"""Regression test runner for golden datasets."""

from dataclasses import dataclass


@dataclass
class RegressionCase:
    name: str
    input: str
    expected_substrings: list[str]


def run_regression(fn, cases: list[RegressionCase]) -> list[tuple[str, bool]]:
    results: list[tuple[str, bool]] = []
    for case in cases:
        output = fn(case.input)
        ok = all(s in output for s in case.expected_substrings)
        results.append((case.name, ok))
    return results
