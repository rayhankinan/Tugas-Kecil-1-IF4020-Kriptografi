from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from .schemas import AutoKeyVignereFileIn
from .services import encrypt_file_service, decrypt_file_service

auto_key_vignere_router = APIRouter(prefix="/auto-key-vignere")


@auto_key_vignere_router.post("/encrypt-file")
async def encrypt_file_handler(auto_key_vignere_file_in: AutoKeyVignereFileIn = Depends()):
    iterable_file_content = await encrypt_file_service(auto_key_vignere_file_in.key, auto_key_vignere_file_in.file)
    response = StreamingResponse(
        content=iterable_file_content,
        media_type=auto_key_vignere_file_in.file.content_type
    )
    return response


@auto_key_vignere_router.post("/decrypt-file")
async def decrypt_file_handler(auto_key_vignere_file_in: AutoKeyVignereFileIn = Depends()):
    iterable_file_content = await decrypt_file_service(auto_key_vignere_file_in.key, auto_key_vignere_file_in.file)
    response = StreamingResponse(
        content=iterable_file_content,
        media_type=auto_key_vignere_file_in.file.content_type
    )
    return response
