from rag.chunking import chunk_text


def test_chunk_text_produces_non_empty_chunks():
    text = " ".join(f"word{i}" for i in range(100))
    chunks = chunk_text(text, chunk_size=20, overlap=5)
    assert len(chunks) > 0
    assert all(chunk.strip() for chunk in chunks)
