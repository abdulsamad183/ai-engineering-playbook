---
title: "Operators"
description: "Symbols and keywords that compute, compare, assign, and combine values — arithmetic through walrus and unpacking."
domain: python-engineering
tags: [python, fundamentals, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Operators

> Symbols and keywords that compute, compare, assign, and combine values — arithmetic through walrus and unpacking.

## Definition

An **operator** performs an operation on one or more operands. Python includes arithmetic, comparison, logical, bitwise, assignment, membership, identity, and the walrus operator.

## Uses

- Calculations (scores, budgets, sizes)
- Conditions for branching and loops
- Compact updates (`+=`)
- Membership tests (`in`)

## Categories

| Category | Examples |
|----------|----------|
| Arithmetic | `+ - * / // % **` |
| Comparison | `== != < > <= >=` |
| Logical | `and or not` |
| Bitwise | `& \| ^ ~ << >>` |
| Assignment | `= += -= *=` |
| Membership | `in` `not in` |
| Identity | `is` `is not` |
| Walrus | `:=` |

## Code examples

```python
a, b = 17, 5
print(a + b, a - b, a * b)   # 22 12 85
print(a / b)                  # 3.4 true division → float
print(a // b, a % b)          # 3 2 floor + remainder
print(a ** 2)                 # 289

print(0.1 + 0.2)              # float imprecision demo
```

```python
x = 10
print(x == 10, 1 < x <= 10)   # True True (chained compare)

skills = ["python", "rag"]
print("rag" in skills)

a = [1, 2]
b = [1, 2]
print(a == b, a is b)         # True False (value vs identity)
```

```python
count = 0
count += 1
first, *rest = [10, 20, 30]
print(first, rest)            # 10 [20, 30]

# Walrus: assign inside a condition (3.8+)
text = "token_count=128"
if (n := text.split("=")[-1]).isdigit():
    print("tokens:", int(n))
```

## Precedence tip

When unsure, **use parentheses**. `2 + 3 * 4` is `14`; `(2 + 3) * 4` is `20`.

---


## Worked example: token budget check

```python
prompt_tokens = 1200
reserved = 256
context_window = 8192
max_output = 512

remaining = context_window - prompt_tokens - reserved
ok = remaining >= max_output and prompt_tokens > 0
print("remaining", remaining, "ok", ok)

# Bit flags (advanced-ish but useful)
READ, WRITE, EXEC = 1, 2, 4
perms = READ | WRITE
print(bool(perms & WRITE), bool(perms & EXEC))
```

## Exercises

1. Predict results for `7 // 2`, `7 / 2`, `7 % 2`, `7 ** 2`.
2. Write a chained comparison that checks `0 <= x < 1`.
3. Demonstrate `==` vs `is` on two equal lists.


## Continue

- **Previous:** [Variables & Data Types](02-variables-data-types.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [Conditional Statements](04-conditional-statements.md)
- **AI production guide:** [Python for AI Engineering](../python-for-ai-engineering.md)
