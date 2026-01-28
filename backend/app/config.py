from functools import lru_cache
from typing import List
import os
import sys

from pydantic import AnyHttpUrl, validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "E-commerce API"
    database_url: str = "postgresql+psycopg2://ecom_user:ecom_pass@localhost:5432/ecommerce"
    jwt_secret: str = "change-me-in-production"
    jwt_algorithm: str = "HS256"
    jwt_exp_minutes: int = 60 * 24
    cors_origins: List[AnyHttpUrl | str] = [
        "http://localhost:3000",
        "http://localhost:5173",
    ]
    recommender_url: str = "http://localhost:8000"
    
    @validator("jwt_secret")
    def validate_jwt_secret(cls, v):
        """Ensure JWT secret is changed in production"""
        if v == "change-me-in-production" and os.getenv("ENV", "development") == "production":
            print("ERROR: JWT_SECRET must be set in production! Using default is a security risk.")
            sys.exit(1)
        if len(v) < 32:
            print("WARNING: JWT_SECRET should be at least 32 characters long for security.")
        return v

    class Config:
        env_file = ".env"
        env_prefix = ""


@lru_cache
def get_settings() -> Settings:
    return Settings()
