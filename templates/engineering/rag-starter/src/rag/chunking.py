"""Chunking strategies — swap for semantic or recursive chunkers."""


def chunk_text(text: str, *, chunk_size: int = 512, overlap: int = 64) -> list[str]:
    words = text.split()
    chunks: list[str] = []
    step = max(1, chunk_size - overlap)
    for i in range(0, len(words), step):
        piece = " ".join(words[i : i + chunk_size])
        if piece:
            chunks.append(piece)
    return chunks
