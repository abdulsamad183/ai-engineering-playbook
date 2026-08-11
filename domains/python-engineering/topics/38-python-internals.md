---
title: "Python Internals"
description: "Under the hood of CPython — bytecode, the GIL, objects, import system, and why it matters for performance."
domain: python-engineering
tags: [python, internals, cpython, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Python Internals

> Under the hood of CPython — bytecode, the GIL, objects, import system, and why it matters for performance.

## Definition

**Python internals** means how CPython represents programs and objects: source → bytecode → evaluation loop, object headers, the GIL, and the import machinery.

You don’t need to hack CPython daily — but internals explain performance, threading limits, and weird edge cases.

## Why engineers care

- Understand why threads ≠ CPU speedups
- Read `dis` output for hotspots
- Know dict/list over-allocation behavior
- Debug import/packaging mysteries

## Pipeline

```mermaid
flowchart LR
  Src[.py] --> Ast[AST]
  Ast --> Bc[Bytecode .pyc]
  Bc --> Eval[Evaluation loop]
  Eval --> Obj[PyObjects]
```

## Code examples

```python
import dis

def add(a, b):
    return a + b

dis.dis(add)                 # show bytecode
```

```python
x = 5
print(type(x), id(x))

# Small ints may be cached — don't rely on 'is' for values
a = 256
b = 256
print(a is b)                # often True — implementation detail
```

```python
def f(x, y=1):
    return x + y

print(f.__name__, f.__defaults__, f.__code__.co_argcount)
```

```python
import math
import sys
print("math" in sys.modules)
```

## GIL (short)

CPython’s GIL allows only one thread to execute Python bytecode at a time. I/O and many C extensions release it; pure-Python CPU loops don’t parallelize with threads.

## Dict/list internals (intuition)

- Lists: over-allocate capacity for amortized `append`
- Dicts: hash tables; insertion-ordered in modern CPython
- Strings: immutable; concatenation patterns matter

## Common misconceptions

- “Python is compiled or interpreted?” — both (bytecode + VM)
- “`is` means equality” — no, identity
- “Threads will use all cores for Python CPU” — not under GIL

---

## Continue

- **Previous:** [Memory Management](37-memory-management.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [Performance Optimization](39-performance-optimization.md)
- **AI production guide:** [Python for AI Engineering](../python-for-ai-engineering.md)
