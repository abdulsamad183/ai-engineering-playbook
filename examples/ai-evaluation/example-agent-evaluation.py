"""Agent evaluation — tool trace accuracy.

Run: python example-agent-evaluation.py
"""


def tool_sequence_accuracy(actual: list[str], expected: list[str]) -> float:
    if not expected:
        return 1.0
    matches = sum(1 for a, e in zip(actual, expected) if a == e)
    return matches / len(expected)


def task_completion(final_state: dict, goal: dict) -> float:
    return 1.0 if final_state.get("status") == goal.get("status") else 0.0


def main() -> None:
    trace = ["search", "read_file", "summarize"]
    golden = ["search", "read_file", "summarize"]
    print("tool accuracy:", tool_sequence_accuracy(trace, golden))
    print("task complete:", task_completion({"status": "done"}, {"status": "done"}))


if __name__ == "__main__":
    main()
