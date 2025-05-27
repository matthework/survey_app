import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:password@db:5432/surveydb")
    AUTH0_DOMAIN: str = os.getenv("AUTH0_DOMAIN")
    API_AUDIENCE: str = os.getenv("API_AUDIENCE")
    ALGORITHMS: str = os.getenv("ALGORITHMS", "RS256")

settings = Settings()