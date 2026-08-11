---
title: "Multithreading"
description: "Threads for overlapping I/O — ThreadPoolExecutor, shared state, locks, and GIL realities."
domain: python-engineering
tags: [python, threading, concurrency, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Multithreading

> Threads for overlapping I/O — ThreadPoolExecutor, shared state, locks, and GIL realities.

## Definition

A **thread** is a unit of execution within a process sharing memory. Python’s `threading` and `concurrent.futures.ThreadPoolExecutor` help run blocking I/O concurrently.

Due to the **GIL** (Global Interpreter Lock) in CPython, threads rarely speed up pure-Python CPU work, but they help with I/O waits.

## Uses

- Concurrent HTTP calls with blocking SDKs
- Background workers in simple apps
- Parallelizing I/O-bound preprocessing

## Code examples

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def fetch(n: int) -> str:
    time.sleep(0.2)                 # pretend network I/O
    return f"result-{n}"

t0 = time.perf_counter()
with ThreadPoolExecutor(max_workers=5) as pool:
    futures = [pool.submit(fetch, i) for i in range(5)]
    results = [f.result() for f in as_completed(futures)]
print(results)
print("elapsed", time.perf_counter() - t0)
```

```python
import threading

counter = 0
lock = threading.Lock()

def bump():
    global counter
    for _ in range(10000):
        with lock:                  # protect shared mutation
            counter += 1

threads = [threading.Thread(target=bump) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(counter)                      # 40000 if locked correctly
```

```python
import threading
tls = threading.local()

def work():
    tls.req_id = threading.get_ident()
    print("req", tls.req_id)
```

## Safety rules

1. Minimize shared mutable state
2. Use queues (`queue.Queue`) to pass messages
3. Don’t kill threads abruptly; use events/flags
4. Prefer `ThreadPoolExecutor` over manual threads

## Common mistakes

- Race conditions without locks
- Deadlocks (lock ordering)
- Using threads for CPU-bound Python loops

---

## Continue

- **Previous:** [Concurrency](33-concurrency.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [Multiprocessing](35-multiprocessing.md)
- **AI production guide:** [Python for AI Engineering](../python-for-ai-engineering.md)
