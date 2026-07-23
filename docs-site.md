# Documentation site (MkDocs Material)

> Browse the playbook as a website with sidebar navigation, search, and Mermaid diagrams.

**Live site:** https://abdulsamad183.github.io/ai-engineering-playbook/

---

## How it works

| Piece | Role |
|-------|------|
| `docs/` | Symlinks into `domains/`, `meta/`, `cheat-sheets/`, etc. (content stays in place) |
| `mkdocs.yml` | Theme, nav tabs, search, Mermaid |
| `hooks/strip_frontmatter.py` | Hides YAML frontmatter on pages |
| `.github/workflows/docs.yml` | Deploys to GitHub Pages on every `main` push |

---

## Local preview

```bash
python -m venv .venv-docs
source .venv-docs/bin/activate
pip install -r requirements-docs.txt
mkdocs serve
```

Open http://127.0.0.1:8000

## Build

```bash
mkdocs build
```

Output: `site/` (gitignored).

---

## Deploy / GitHub Pages (one-time)

After the first workflow run creates the `gh-pages` branch:

1. GitHub repo → **Settings** → **Pages**
2. **Build and deployment** → Source: **Deploy from a branch**
3. Branch: **`gh-pages`** / folder **`/` (root)**
4. Save — site is live in ~1 minute

Pushing to `main` redeploys automatically.

---

## Navigation

Top tabs: Home · Start · Foundations · LLM Systems · Retrieval & Agents · Production · Research & Career · Toolkit · Meta

Use the search box (header) to find any page — all Markdown under the symlinked trees is indexed even if not listed in the sidebar.
