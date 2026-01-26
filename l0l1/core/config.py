from typing import Optional, List
from pydantic_settings import BaseSettings
from pydantic import Field
import os


class Settings(BaseSettings):
    # Database
    database_url: str = Field(default="sqlite:///./l0l1.db", validation_alias="DATABASE_URL")

    # AI Model Configuration
    default_provider: str = Field(default="openai", validation_alias="L0L1_AI_PROVIDER")
    openai_api_key: Optional[str] = Field(default=None, validation_alias="OPENAI_API_KEY")
    anthropic_api_key: Optional[str] = Field(default=None, validation_alias="ANTHROPIC_API_KEY")

    # Model Settings
    embedding_model: str = Field(default="text-embedding-3-small", validation_alias="L0L1_EMBEDDING_MODEL")
    completion_model: str = Field(default="gpt-4o-mini", validation_alias="L0L1_COMPLETION_MODEL")

    # Vector Database
    vector_db_path: str = Field(default="./data/vector", validation_alias="L0L1_VECTOR_DB_PATH")

    # Knowledge Graph
    knowledge_graph_path: str = Field(default="./data/kg", validation_alias="L0L1_KNOWLEDGE_GRAPH_PATH")

    # Background Tasks
    redis_url: str = Field(default="redis://localhost:6379/0", validation_alias="REDIS_URL")

    # Workspace Settings
    workspace_data_dir: str = Field(default="./workspaces", validation_alias="L0L1_WORKSPACE_DIR")

    # PII Detection
    enable_pii_detection: bool = Field(default=True, validation_alias="L0L1_ENABLE_PII_DETECTION")
    pii_entities: List[str] = Field(
        default=["PERSON", "EMAIL_ADDRESS", "PHONE_NUMBER", "SSN", "CREDIT_CARD", "IP_ADDRESS"],
        validation_alias="L0L1_PII_ENTITIES"
    )

    # Continuous Learning
    enable_learning: bool = Field(default=True, validation_alias="L0L1_ENABLE_LEARNING")
    learning_threshold: float = Field(default=0.8, validation_alias="L0L1_LEARNING_THRESHOLD")

    # API Settings
    api_host: str = Field(default="0.0.0.0", validation_alias="L0L1_API_HOST")
    api_port: int = Field(default=8000, validation_alias="L0L1_API_PORT")

    # CORS Settings
    cors_origins: List[str] = Field(
        default=["http://localhost:3000", "http://localhost:8000"],
        validation_alias="L0L1_CORS_ORIGINS"
    )

    # Logging
    log_level: str = Field(default="INFO", validation_alias="L0L1_LOG_LEVEL")

    model_config = {
        "env_file": ".env",
        "case_sensitive": False,
        "extra": "ignore",
    }


settings = Settings()
