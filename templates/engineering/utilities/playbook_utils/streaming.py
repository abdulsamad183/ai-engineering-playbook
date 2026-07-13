"""SSE-style streaming helpers."""

from collections.abc import AsyncIterator, Iterator


async def stream_tokens(chunks: Iterator[str]) -> AsyncIterator[str]:
    for chunk in chunks:
        yield chunk
