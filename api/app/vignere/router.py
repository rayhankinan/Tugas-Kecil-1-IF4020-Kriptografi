from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from .schemas import VignereFileIn
from .services import encrypt_file_service, decrypt_file_service

vignere_router = APIRouter(prefix="/vignere")


@vignere_router.post("/encrypt-file")
async def encrypt_file_handler(vignere_file_in: VignereFileIn = Depends()):
    iterable_file_content = await encrypt_file_service(vignere_file_in.key, vignere_file_in.file)
    response = StreamingResponse(
        content=iterable_file_content,
        media_type=vignere_file_in.file.content_type
    )
    return response


@vignere_router.post("/decrypt-file")
async def decrypt_file_handler(vignere_file_in: VignereFileIn = Depends()):
    iterable_file_content = await decrypt_file_service(vignere_file_in.key, vignere_file_in.file)
    response = StreamingResponse(
        content=iterable_file_content,
        media_type=vignere_file_in.file.content_type
    )
    return response
