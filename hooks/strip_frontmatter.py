"""Strip YAML frontmatter so pages render cleanly in MkDocs."""


def on_page_markdown(markdown: str, **kwargs) -> str:
    if not markdown.startswith("---"):
        return markdown
    end = markdown.find("\n---", 3)
    if end == -1:
        return markdown
    # Skip past closing --- and following newline
    rest = markdown[end + 4 :]
    return rest.lstrip("\n")
