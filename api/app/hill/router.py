from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from .schemas import HillFileIn
from .services import encrypt_file_service, decrypt_file_service

hill_router = APIRouter(prefix="/hill")


@hill_router.post("/encrypt-file")
async def encrypt_file_handler(hill_file_in: HillFileIn = Depends()):
    iterable_file_content = await encrypt_file_service(hill_file_in.key, hill_file_in.file)
    response = StreamingResponse(
        content=iterable_file_content,
        media_type=hill_file_in.file.content_type
    )
    return response


@hill_router.post("/decrypt-file")
async def decrypt_file_handler(hill_file_in: HillFileIn = Depends()):
    iterable_file_content = await decrypt_file_service(hill_file_in.key, hill_file_in.file)
    response = StreamingResponse(
        content=iterable_file_content,
        media_type=hill_file_in.file.content_type
    )
    return response
