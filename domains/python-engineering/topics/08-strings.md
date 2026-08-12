---
title: "Strings"
description: "Text in Python — creation, indexing, methods, formatting, encoding, and practical string processing."
domain: python-engineering
tags: [python, strings, fundamentals, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-12
version: "1.1"
---

# Strings

> Text in Python — creation, indexing, methods, formatting, encoding, and practical string processing.

## Definition

A **string** (`str`) is an **immutable sequence of Unicode characters**. Once created, you cannot change a character in place; “modifications” create new strings.

## Uses

- Prompts, messages, logs, file paths (prefer `pathlib` for paths)
- Parsing and formatting API payloads
- Normalization before embedding/tokenization

## Types / related text types

| Type | Meaning |
|------|---------|
| `str` | Unicode text |
| `bytes` | Raw bytes |
| `bytearray` | Mutable bytes |

## Creation & essentials

```python
s1 = "hello"
s2 = 'hello'                 # same
s3 = """multi
line"""                      # triple quotes
raw = r"C:\new\to"           # raw: backslashes kept
print(len(s1), s1[0], s1[-1])
print(s1[1:4])               # slicing "ell"
# s1[0] = "H"                # TypeError — immutable
```

## Methods you will use constantly

```python
text = "  Retrieval-Augmented Generation  "
print(text.strip())
print(text.lower())
print(text.replace("Generation", "Gen"))
print("Augmented" in text)
parts = "a,b,c".split(",")
print(parts, ",".join(parts))
print("score:42".partition(":"))
print("file.md".endswith(".md"))
print("42".isdigit())
```

## Formatting

```python
name, score = "rag", 0.87
# f-strings (preferred)
print(f"{name} score={score:.2%}")

# format / %
print("{}={}".format(name, score))
print("%s=%.2f" % (name, score))
```

## Encoding

```python
s = "café"
b = s.encode("utf-8")        # str → bytes
print(b)
print(b.decode("utf-8"))     # bytes → str

# Always know your encoding at I/O boundaries (files, HTTP)
```

## Practical patterns

```python
def normalize_query(q: str) -> str:
    q = q.strip().lower()
    q = " ".join(q.split())  # collapse whitespace
    return q

def truncate(s: str, n: int, suffix: str = "...") -> str:
    if len(s) <= n:
        return s
    return s[: n - len(suffix)] + suffix

print(normalize_query("  Hello   World "))
print(truncate("abcdefghijklmnopqrstuvwxyz", 10))
```

## Common mistakes

- Building huge strings with `+` in a loop → use `"".join(parts)` or io.StringIO
- Mixing `str` and `bytes`
- Using string paths instead of `pathlib.Path` for filesystem work

---


## Worked example: light PII mask

```python
def mask_email(text: str) -> str:
    parts = text.split()
    out = []
    for p in parts:
        if "@" in p and "." in p:
            name, _, domain = p.partition("@")
            out.append(name[:1] + "***@" + domain)
        else:
            out.append(p)
    return " ".join(out)

print(mask_email("contact me at ada@example.com thanks"))
```

## Exercises

1. Normalize whitespace + lowercase a query string.
2. Truncate a prompt preview to 80 chars with `...`.
3. Encode/decode a UTF-8 string containing non-ASCII characters.


## Continue

- **Previous:** [Scope & Namespaces](07-scope-namespaces.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [Lists](09-lists.md)
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

