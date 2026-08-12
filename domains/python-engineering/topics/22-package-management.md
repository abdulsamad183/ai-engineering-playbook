---
title: "Package Management"
description: "Install and pin dependencies with pip, requirements files, pyproject.toml, and lockfiles."
domain: python-engineering
tags: [python, pip, packaging, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-12
version: "1.1"
---

# Package Management

> Install and pin dependencies with pip, requirements files, pyproject.toml, and lockfiles.

## Definition

**Package management** is how you declare, install, upgrade, and lock third-party libraries so environments are reproducible.

## Uses

- Add FastAPI, OpenAI SDK, NumPy, pytest, …
- Reproduce CI and production installs
- Avoid “works on my machine” drift

## Key concepts

| Concept | Meaning |
|---------|---------|
| Distribution package | Installable project on PyPI |
| Requirement | Constraint like `httpx>=0.27` |
| Lockfile | Exact versions that were resolved |
| Extra | Optional dependency group (`dev`) |

## Code examples

```bash
# pip basics (inside a venv)
python -m pip install httpx
python -m pip install 'fastapi[standard]'
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
```

```toml
# pyproject.toml (modern packaging)
[project]
name = "myapp"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
  "fastapi>=0.115",
  "httpx>=0.27",
  "pydantic>=2.0",
]

[dependency-groups]
dev = ["pytest>=8.0", "ruff>=0.6"]
```

```bash
# uv sync example
uv sync
uv add pydantic
uv add --dev pytest
```

```text
# requirements style (apps)
fastapi==0.115.0
httpx==0.27.2
# pins for reproducibility; regenerate deliberately
```

## Version specifiers

```text
package==1.2.3    # exact
package>=1.2,<2   # compatible range
package~=1.2.3    # compatible release
```

## Best practices for AI apps

1. Pin transitive deps in deploy lockfiles
2. Separate runtime vs dev dependencies
3. Upgrade intentionally; run tests/evals after
4. Prefer official provider SDKs + small stack over mega-frameworks by default

## Common mistakes

- No pins in production
- Installing with multiple tools into one env chaotically
- Committing secrets in package config

---

## Continue

- **Previous:** [Virtual Environments](21-virtual-environments.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [Object-Oriented Programming](23-oop.md)
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

