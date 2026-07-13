"""Application configuration."""

import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class DatabaseConfig:
    """Database configuration."""
    
    host: str = "localhost"
    port: int = 5432
    name: str = "codex"
    user: str = "postgres"
    password: str = ""


@dataclass
class RedisConfig:
    """Redis configuration."""
    
    host: str = "localhost"
    port: int = 6379
    db: int = 0


@dataclass
class AIConfig:
    """AI service configuration."""
    
    openai_api_key: str = ""
    model: str = "gpt-4"
    temperature: float = 0.7


@dataclass
class Settings:
    """Application settings."""
    
    app_name: str = "Codex Enterprise"
    app_version: str = "0.1.0"
    debug: bool = False
    secret_key: str = "change-me-in-production"
    
    database: DatabaseConfig = None
    redis: RedisConfig = None
    ai: AIConfig = None
    
    def __post_init__(self):
        """Initialize with environment variables."""
        self.database = DatabaseConfig(
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", "5432")),
            name=os.getenv("DB_NAME", "codex"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", ""),
        )
        self.redis = RedisConfig(
            host=os.getenv("REDIS_HOST", "localhost"),
            port=int(os.getenv("REDIS_PORT", "6379")),
        )
        self.ai = AIConfig(
            openai_api_key=os.getenv("OPENAI_API_KEY", ""),
        )
        self.secret_key = os.getenv("SECRET_KEY", self.secret_key)
        self.debug = os.getenv("DEBUG", "false").lower() == "true"
