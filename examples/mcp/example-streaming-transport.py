"""Streaming pattern — progress chunks for long-running tools.

Run: python example-streaming-transport.py
"""

import asyncio


async def long_job(query: str, emit) -> dict:
    for i in range(3):
        await emit({"progress": i + 1, "total": 3, "message": f"Processing {query} step {i+1}"})
        await asyncio.sleep(0.1)
    return {"status": "done", "query": query}


async def main() -> None:
    chunks: list[dict] = []

    async def emit(chunk: dict) -> None:
        chunks.append(chunk)
        print("CHUNK:", chunk)

    result = await long_job("report", emit)
    print("FINAL:", result)
    print(f"Received {len(chunks)} progress notifications")


if __name__ == "__main__":
    asyncio.run(main())
