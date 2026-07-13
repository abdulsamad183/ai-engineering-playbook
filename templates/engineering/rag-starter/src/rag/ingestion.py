"""Document ingestion — swap loaders for PDF, HTML, Markdown."""

from pathlib import Path


def load_documents(path: str) -> list[dict[str, str]]:
    root = Path(path)
    docs: list[dict[str, str]] = []
    for file in root.glob("**/*"):
        if file.suffix.lower() in {".txt", ".md"}:
            docs.append({"id": str(file), "text": file.read_text(), "source": str(file)})
    return docs
