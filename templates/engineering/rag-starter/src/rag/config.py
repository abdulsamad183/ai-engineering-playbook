from pydantic_settings import BaseSettings, SettingsConfigDict


class RAGSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    chunk_size: int = 512
    chunk_overlap: int = 64
    top_k: int = 5
    rerank_top_n: int = 3
    embedding_model: str = "text-embedding-3-small"
    vector_backend: str = "memory"
