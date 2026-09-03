import os
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # App
    APP_NAME: str = "PhishGuard Enterprise AI Monorepo"
    DEBUG: bool = False
    SECRET_KEY: str = "phishguard-enterprise-secret-key-2026-safe-production"

    # Database
    # Jika di Vercel, gunakan /tmp/phishguard.db karena sistem file read-only
    DATABASE_URL: str = (
        "sqlite+aiosqlite:////tmp/phishguard.db"
        if os.getenv("VERCEL") or os.getenv("AWS_LAMBDA_FUNCTION_NAME")
        else "sqlite+aiosqlite:///./phishguard.db"
    )

    # Redis (rate limiting + cache)
    REDIS_URL: str = "memory://"  # in-memory rate limiting default

    # CORS
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://localhost:3000",
        "https://mocherik.github.io",
        "https://*.github.io",
        "https://*.vercel.app",
        "*"
    ]

    # External Threat Intelligence APIs
    PHISHTANK_API_KEY: str = ""
    GOOGLE_SAFE_BROWSING_API_KEY: str = ""
    OPENPHISH_FEED_URL: str = "https://openphish.com/feed.txt"
    VIRUSTOTAL_API_KEY: str = ""

    # File upload limits
    MAX_FILE_SIZE_MB: int = 10
    ALLOWED_FILE_EXTENSIONS: List[str] = [
        ".pdf", ".doc", ".docx", ".xls", ".xlsx",
        ".ppt", ".pptx", ".txt", ".eml", ".msg",
    ]

    # NLP Model
    NLP_MODEL_NAME: str = "distilbert-base-uncased"
    NLP_MODEL_PATH: str = "./models/phish_nlp"

    # JWT
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 hari

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
