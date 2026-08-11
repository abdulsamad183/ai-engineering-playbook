---
title: "Multiprocessing"
description: "Process-based parallelism for CPU-bound work — pools, pickling, and process-safe patterns."
domain: python-engineering
tags: [python, multiprocessing, concurrency, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Multiprocessing

> Process-based parallelism for CPU-bound work — pools, pickling, and process-safe patterns.

## Definition

**Multiprocessing** runs code in **separate processes**, each with its own Python interpreter and GIL. Ideal for CPU-bound parallelism on multiple cores.

## Uses

- CPU-heavy tokenization/preprocessing
- Parallel offline evaluation
- Feature extraction when not already in native libs

## Tradeoffs

| Pros | Cons |
|------|------|
| True parallel CPU | Higher memory |
| Crash isolation | Pickling overhead |
| Bypass GIL | Harder shared state |

## Code examples

```python
from concurrent.futures import ProcessPoolExecutor

def cpu_heavy(n: int) -> int:
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=4) as pool:
        print(list(pool.map(cpu_heavy, [200000] * 4)))
```

```python
from multiprocessing import Process, Queue

def worker(q: Queue, x: int) -> None:
    q.put(x * x)

if __name__ == "__main__":
    q: Queue = Queue()
    p = Process(target=worker, args=(q, 7))
    p.start()
    p.join()
    print(q.get())
```

## Important constraints

1. Guard entrypoints with `if __name__ == "__main__":` (esp. Windows/mac spawn)
2. Arguments/results must be **picklable**
3. Prefer `ProcessPoolExecutor` for simple map/submit patterns
4. Shared memory exists but keep it rare

## vs threads vs async

- Network fan-out → async/threads
- Pure Python CPU → processes
- NumPy/PyTorch often already release GIL / use their own threads

## Common mistakes

- Forgetting `__main__` guard → infinite process spawn
- Huge payloads over queues
- Assuming processes share memory like threads

---

## Continue

- **Previous:** [Multithreading](34-multithreading.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [Asynchronous Programming](36-asynchronous-programming.md)
- **AI production guide:** [Python for AI Engineering](../python-for-ai-engineering.md)
