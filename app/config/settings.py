from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # Database settings (from Laravel .env)
    DATABASE_URL: str = "mysql+pymysql://root:root@localhost:3308/if-stage-db"

    # JWT/Auth settings
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # App settings
    APP_NAME: str = "IF-Py-Dash"
    DEBUG: bool = True

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()