from pydantic import BaseSettings, Field, Required
from .lib import alru_cache_typed


class Settings(BaseSettings):
    API_KEY: str = Field(default=Required)


@alru_cache_typed()
async def get_settings():
    return Settings()
