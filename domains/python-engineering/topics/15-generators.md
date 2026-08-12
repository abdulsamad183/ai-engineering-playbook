---
title: "Generators"
description: "Lazy sequences with yield — generator functions, generator expressions, and streaming pipelines."
domain: python-engineering
tags: [python, generators, fundamentals, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-12
version: "1.1"
---

# Generators

> Lazy sequences with yield — generator functions, generator expressions, and streaming pipelines.

## Definition

A **generator** is a function that uses `yield` to produce a sequence of values lazily. Calling it returns a **generator iterator** without running the body until you iterate.

Generator expressions `(expr for x in xs)` create anonymous generators.

## Uses

- Stream large files / token batches / API pages
- Pipeline transforms with low memory
- Infinite sequences with care (`itertools.count`)

## Types

| Kind | How |
|------|-----|
| Generator function | `def f(): yield ...` |
| Generator expression | `(x for x in xs)` |
| `yield from` | Delegate to sub-iterator |

```mermaid
flowchart LR
  Call[Call generator fn] --> G[Generator object]
  G -->|next| Y[Run to next yield]
  Y --> G
  G -->|done| S[StopIteration]
```

## Code examples

```python
def countdown(n: int):
    while n > 0:
        yield n
        n -= 1

g = countdown(3)
print(next(g), next(g), next(g))
print(list(countdown(3)))
```

```python
def read_lines(path: str):
    with open(path, encoding="utf-8") as f:
        for line in f:
            yield line.rstrip("\n")

# Composition: pipeline
def non_empty(lines):
    for line in lines:
        if line.strip():
            yield line

def numbered(lines):
    for i, line in enumerate(lines, 1):
        yield f"{i}: {line}"

# Example with in-memory data instead of file
sample = ["a", "", "b"]
pipe = numbered(non_empty(iter(sample)))
print(list(pipe))
```

```python
# yield from
def concat(a, b):
    yield from a
    yield from b

print(list(concat([1, 2], [3])))
```

```python
# Generator expression
squares = (n * n for n in range(5))
print(sum(squares))
# sum(squares) again → 0 because exhausted
```

```python
# send / generator as coroutine (advanced peek)
def accumulator():
    total = 0
    while True:
        x = yield total
        if x is None:
            break
        total += x

acc = accumulator()
next(acc)                 # prime
print(acc.send(5))
print(acc.send(3))
```

## vs lists

| | Generator | List |
|---|-----------|------|
| Memory | Lazy | Eager |
| Reusable | No (one-shot) | Yes |
| Indexing | No | Yes |
| Len | No (generally) | Yes |

## Common mistakes

- Expecting generators to restart automatically
- Using generators when you need random access / len

---

## Continue

- **Previous:** [Iterators & Iterables](14-iterators-iterables.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [Lambda Functions](16-lambda-functions.md)
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

