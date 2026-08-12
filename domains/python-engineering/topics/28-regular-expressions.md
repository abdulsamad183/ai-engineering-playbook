---
title: "Regular Expressions"
description: "Pattern matching on text with re — search, match, groups, substitution, and safe usage guidelines."
domain: python-engineering
tags: [python, regex, text, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-12
version: "1.1"
---

# Regular Expressions

> Pattern matching on text with re — search, match, groups, substitution, and safe usage guidelines.

## Definition

A **regular expression (regex)** is a pattern language for matching and extracting text. Python’s standard module is `re` (and the third-party `regex` package for advanced Unicode needs).

## Uses

- Validate simple formats (carefully)
- Extract fields from logs
- Light parsing when full grammars are overkill
- Redacting PII patterns in traces

## Core operations

| Function | Role |
|----------|------|
| `re.search` | First match anywhere |
| `re.match` | Match at start |
| `re.fullmatch` | Entire string |
| `re.findall` | All matches |
| `re.finditer` | Match objects iterator |
| `re.sub` | Substitute |
| `re.compile` | Precompile pattern |

## Code examples

```python
import re

text = "order id=A-123 status=paid"
m = re.search(r"id=([A-Z]-\d+)", text)
if m:
    print(m.group(1))  # A-123
```

```python
# Flags
print(re.findall(r"hi", "Hi hi HI", flags=re.IGNORECASE))

# Named groups + verbose flag (single-line pattern for clarity)
pattern = re.compile(
    r"(?P<key>[a-z_]+)=(?P<value>\S+)",
    re.VERBOSE,
)
print(pattern.search("max_tokens=512").groupdict())
```

```python
# Substitution / redaction
log = "user email=a@b.com ok"
redacted = re.sub(r"[\w.]+@[\w.]+", "<EMAIL>", log)
print(redacted)
```

```python
# Split
print(re.split(r"\s*,\s*", "a, b,c"))
```

```python
# Prefer raw strings for patterns
# Good: r"\d+"
# Confusing: "\\d+" vs accidental escape bugs
```

## Safety & performance

- Prefer simple string methods when enough (`in`, `startswith`, `split`)
- Avoid catastrophic backtracking on untrusted input
- Compile once if used in a hot loop

## Common mistakes

- Overcomplex regex for nested structures (use a parser)
- Forgetting raw strings
- Using regex as the only email validator (too naive or too strict)

---

## Continue

- **Previous:** [Type Hints](27-type-hints.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [Functional Programming](29-functional-programming.md)
- **AI production guide:** [Python for AI Engineering](../python-for-ai-engineering.md)

---

## AI engineering angle

This topic shows up constantly in AI codebases: training scripts, eval runners, FastAPI services, agent tools, and data cleanup jobs. Prefer clear `main()` entrypoints, typed interfaces, and small testable functions over notebook-only workflows.

## Production checklist

- [ ] Errors are explicit (no bare `except:`)
- [ ] Logging instead of leftover `print` in services
- [ ] Deterministic seeds where experiments need reproduction
- [ ] Resource cleanup via `with` / context managers
- [ ] Unit tests for pure helpers

## Practice exercises

1. Rewrite one snippet from this page as a function with type hints and a docstring.
2. Add a failing unit test, then make it pass.
3. Note one way this concept appears in RAG, agents, or LLM API clients.

## Interview prompts

**Q: When would you choose a different approach than the default shown here?**

A: Tie the answer to performance, readability, concurrency, or API boundaries — and give a concrete AI-engineering example (streaming responses, batch embedding, tool sandboxing).

## See also

- [Python hub](../README.md)
- [Python Frameworks](../../python-frameworks-libraries/README.md)
- [LLM Application Development](../../llm-application-development/README.md)

