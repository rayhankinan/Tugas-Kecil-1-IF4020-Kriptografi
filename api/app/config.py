from pydantic import BaseSettings, Field, Required
from functools import lru_cache


class Settings(BaseSettings):
    api_key: str = Field(default=Required)


@lru_cache()
def get_settings():
    return Settings()
