from fastapi import Depends, Security, HTTPException, status
from fastapi.security.api_key import APIKeyCookie, APIKeyHeader, APIKeyQuery
from .config import get_settings, Settings


async def verify_api_key(
    api_key_cookie: str = Security(
        APIKeyCookie(
            name="access_token",
            auto_error=False
        )
    ),
    api_key_header: str = Security(
        APIKeyHeader(
            name="access_token",
            auto_error=False
        )
    ),
    api_key_query: str = Security(
        APIKeyQuery(
            name="access_token",
            auto_error=False
        )
    ),
    settings: Settings = Depends(get_settings)
):
    if api_key_cookie == settings.API_KEY:
        return api_key_cookie
    elif api_key_header == settings.API_KEY:
        return api_key_header
    elif api_key_query == settings.API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate API KEY"
        )
