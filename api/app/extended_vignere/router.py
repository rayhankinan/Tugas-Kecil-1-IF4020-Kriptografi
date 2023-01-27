from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from .schemas import ExtendedVignereFileIn
from .services import encrypt_file_service, decrypt_file_service

extended_vignere_router = APIRouter(prefix="/extended-vignere")


@extended_vignere_router.post("/encrypt-file")
async def encrypt_file_handler(extended_vignere_file_in: ExtendedVignereFileIn = Depends()):
    iterable_file_content = await encrypt_file_service(extended_vignere_file_in.key, extended_vignere_file_in.file)
    response = StreamingResponse(
        content=iterable_file_content,
        media_type=extended_vignere_file_in.file.content_type
    )
    return response


@extended_vignere_router.post("/decrypt-file")
async def decrypt_file_handler(extended_vignere_file_in: ExtendedVignereFileIn = Depends()):
    iterable_file_content = await decrypt_file_service(extended_vignere_file_in.key, extended_vignere_file_in.file)
    response = StreamingResponse(
        content=iterable_file_content,
        media_type=extended_vignere_file_in.file.content_type
    )
    return response
