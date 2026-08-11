---
title: "Package Management"
description: "Install and pin dependencies with pip, requirements files, pyproject.toml, and lockfiles."
domain: python-engineering
tags: [python, pip, packaging, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
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
