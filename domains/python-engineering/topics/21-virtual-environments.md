---
title: "Virtual Environments"
description: "Isolate project dependencies with venv, virtualenv, and uv — why isolation matters and how to use it daily."
domain: python-engineering
tags: [python, venv, tooling, tutorial]
status: published
created: 2026-08-11
updated: 2026-08-11
version: "1.0"
---

# Virtual Environments

> Isolate project dependencies with venv, virtualenv, and uv — why isolation matters and how to use it daily.

## Definition

A **virtual environment** is an isolated Python runtime directory with its own `python` / `pip` and installed packages. It prevents Project A’s dependencies from breaking Project B.

## Uses

- Keep AI projects (torch, fastapi, langchain) from colliding
- Reproduce installs per project
- Safe experimentation without polluting system Python

## Types / tools

| Tool | Notes |
|------|-------|
| `venv` | Standard library (recommended baseline) |
| `virtualenv` | Third-party predecessor |
| `uv venv` / `uv sync` | Modern fast tooling |
| Conda | Common in data science; different model |

```mermaid
flowchart TB
  Sys[System Python] --> V1[venv project A]
  Sys --> V2[venv project B]
  V1 --> PA[packages A]
  V2 --> PB[packages B]
```

## Code examples

```bash
# Create with stdlib venv
python3 -m venv .venv

# Activate (Linux/macOS)
source .venv/bin/activate

# Activate (Windows PowerShell)
# .venv\Scripts\Activate.ps1

# Confirm
which python
python -c "import sys; print(sys.prefix)"

# Deactivate
deactivate
```

```bash
# uv workflow (fast)
uv venv .venv
source .venv/bin/activate
uv pip install fastapi httpx
```

```bash
# Useful hygiene
echo ".venv/" >> .gitignore
python -m pip install --upgrade pip
```

## Rules of thumb

1. **One venv per project**
2. **Never sudo pip install into system Python** for app work
3. **Commit lockfiles**, not the venv folder
4. Document Python version (`.python-version` or `requires-python`)

## Common mistakes

- Installing packages while venv is inactive
- Checking `.venv` into git
- Mixing conda base env for everything

---

## Continue

- **Previous:** [Modules & Packages](20-modules-packages.md)
- **Hub:** [Python topics](../README.md)
- **Next:** [Package Management](22-package-management.md)
- **AI production guide:** [Python for AI Engineering](../python-for-ai-engineering.md)
