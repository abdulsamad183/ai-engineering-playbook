"""Vision / multimodal request with OpenAI.

Run: python example-vision-request.py path/to/image.png
"""

from __future__ import annotations

import base64
import os
import sys
from pathlib import Path

from openai import AsyncOpenAI

client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])


def encode_image(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("utf-8")


async def describe_image(image_path: Path, model: str = "gpt-4o") -> str:
    b64 = encode_image(image_path)
    response = await client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this image for a RAG caption."},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/png;base64,{b64}"},
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    return response.choices[0].message.content or ""


async def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("sample.png")
    if not path.exists():
        print("Provide an image path: python example-vision-request.py image.png")
        return
    print(await describe_image(path))


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
