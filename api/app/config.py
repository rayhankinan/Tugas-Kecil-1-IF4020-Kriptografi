from pydantic import BaseSettings, Field, Required
from async_lru import alru_cache


class Settings(BaseSettings):
    api_key: str = Field(default=Required)


@alru_cache()
async def get_settings():
    return Settings()
