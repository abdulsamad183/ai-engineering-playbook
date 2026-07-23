# GitHub Actions Templates

> Reusable CI/CD workflows for Python AI projects.

---

## Workflows

| File | Purpose |
|------|---------|
| `python-ci.yml` | Lint (ruff), test (pytest), Docker build, Trivy scan |
| `deploy.yml` | Deployment workflow_dispatch stub |

---

## Usage

Copy `.github/workflows/` into your repository root. Customize Python version and build context.

---

## Related

- [FastAPI starter CI](../fastapi-starter/.github/workflows/ci.yml)
- [Git and GitHub Workflow](../../../domains/foundations/git-github-workflow.md)
