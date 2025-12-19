from pydantic import BaseModel
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mongodb_uri: str | None = None
    database_name: str = "ecommerce"
    jwt_secret: str = "change-me"
    recommender_url: str | None = None

    class Config:
        env_prefix = ""
        env_file = ".env"


class HealthResponse(BaseModel):
    status: str
