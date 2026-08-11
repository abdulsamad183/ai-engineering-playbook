---
title: "Variables & Data Types"
description: "Names, objects, and Python's built-in data types — how values live in memory and how to choose the right type."
domain: python-engineering
tags: [python, fundamentals, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Variables & Data Types

> Names, objects, and Python's built-in data types — how values live in memory and how to choose the right type.

## Definition

A **variable** is a **name** bound to an **object**. Assignment (`name = value`) creates or rebinds the name. Python is **dynamically typed**: the same name can later point to a different type.

A **data type** describes what an object is (`int`, `str`, `list`, …) and which operations it supports.

## Uses

- Hold config, user input, model outputs, API payloads
- Pick types that match meaning (`bool` vs `0/1`)
- Understand mutability to avoid shared-state bugs

## Binding model

```mermaid
flowchart LR
  N[Name x] --> O[Object 42]
  N2[Rebind x] --> O2[Object hello]
```

```python
x = 42
y = x           # y refers to same int
x = "hello"     # x rebound; y still 42
print(y)        # 42
```

## Built-in types

| Category | Types | Mutable? |
|----------|-------|----------|
| Numeric | `int`, `float`, `complex` | No |
| Boolean | `bool` | No |
| Text | `str` | No |
| Sequences | `list`, `tuple`, `range` | only list |
| Sets | `set`, `frozenset` | only set |
| Mapping | `dict` | Yes |
| Null | `None` | No |
| Binary | `bytes`, `bytearray` | only bytearray |

## Code examples

```python
age = 30                      # int (arbitrary precision)
temp = 36.6                   # float
ready = True                  # bool
result = None                 # absence of value

name = "Samad"                # str (Unicode)
nums = [1, 2, 3]              # list — mutable
point = (10, 20)              # tuple — immutable
unique = {1, 2, 2}            # set → {1, 2}
user = {"id": 1, "role": "admin"}  # dict

# Always compare None with 'is'
if result is None:
    print("no result")

print(type(name), isinstance(name, str))
as_int = int("42")            # conversion; may raise ValueError
```

```python
# Mutability: aliases see in-place changes
a = [1, 2]
b = a
b.append(3)
print(a)          # [1, 2, 3]

c = a.copy()      # independent shallow copy
c.append(4)
print(a, c)       # [1, 2, 3] [1, 2, 3, 4]
```

## Naming conventions

```python
user_count = 10     # snake_case
MAX_RETRIES = 3      # constant by convention
_internal = True     # "private" by convention
```

## Common mistakes

- `== None` instead of `is None`
- Assuming floats are exact for money (use `decimal`)
- Mutating shared lists unintentionally

---


## Worked example: config object

```python
# Simple typed-ish config using plain variables + a dict
MODEL = "gpt-4.1-mini"
TEMPERATURE = 0.2
MAX_TOKENS = 512
FEATURES = {"rag": True, "tools": False}

def describe() -> str:
    return (
        f"model={MODEL} temp={TEMPERATURE} "
        f"max_tokens={MAX_TOKENS} rag={FEATURES['rag']}"
    )

print(describe())

# Prefer constants for values that shouldn't change by accident
# Prefer dict/dataclass when the shape grows
```

## Choosing types (decision guide)

| Need | Prefer |
|------|--------|
| Count / id | `int` |
| Measurement | `float` (or `Decimal` for money) |
| Flag | `bool` |
| Text | `str` |
| Ordered collection | `list` |
| Fixed record | `tuple` / dataclass |
| Unique ids | `set` |
| Keyed record / JSON | `dict` |
| Missing value | `None` |

## Exercises

1. Bind five values of different types; print `type(x)` for each.
2. Show that `a = b = []` shares one list (mutate via one name).
3. Convert `"3.14"` → `float` → `int` and explain the result.


## Continue

- **Previous:** [Python Basics](01-python-basics.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [Operators](03-operators.md)
- **AI production guide:** [Python for AI Engineering](../python-for-ai-engineering.md)
