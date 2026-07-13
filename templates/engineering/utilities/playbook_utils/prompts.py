"""Load parameterized prompts from templates/engineering/prompts/."""

from pathlib import Path


def load_prompt(name: str, **variables: str) -> str:
    path = Path(__file__).resolve().parents[2] / "prompts" / f"{name}.md"
    text = path.read_text()
    for key, value in variables.items():
        text = text.replace(f"{{{{{key}}}}}", value)
    return text
