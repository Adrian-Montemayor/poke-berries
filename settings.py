from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    """Settings management class"""
    flask_app: str
    flask_env: str

    class Config:
        flask_env = ".env"


@lru_cache()
def get_settings():
    """One instance and re-use the same settings object"""
    return Settings()

settings = get_settings()