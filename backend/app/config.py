from functools import lru_cache
from typing import List

from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "E-commerce API"
    database_url: str = "postgresql+psycopg2://ecom_user:ecom_pass@postgres:5432/ecommerce"
    jwt_secret: str = "change-me"
    jwt_algorithm: str = "HS256"
    jwt_exp_minutes: int = 60 * 24
    cors_origins: List[AnyHttpUrl | str] = [
        "http://localhost:3000",
        "http://localhost:5173",
    ]
    recommender_url: str = "http://recommender:8000"

    class Config:
        env_file = ".env"
        env_prefix = ""


@lru_cache
def get_settings() -> Settings:
    return Settings()
