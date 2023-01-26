from fastapi import Depends, Header, HTTPException, status
from .config import get_settings, Settings


async def verify_api_key(api_key: str = Header(), settings: Settings = Depends(get_settings)):
    if api_key != settings.api_key:
        raise HTTPException(status.HTTP_403_FORBIDDEN)
    return api_key
