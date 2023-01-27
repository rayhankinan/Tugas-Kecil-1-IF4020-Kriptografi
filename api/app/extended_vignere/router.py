from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import StreamingResponse
from .services import encrypt_file_service, decrypt_file_service

extended_vignere_router = APIRouter(prefix="/extended-vignere")


@extended_vignere_router.post("/encrypt-file")
async def encrypt_file_handler(key: bytes = Form(), file: UploadFile = File()):
    iterable_file_content = await encrypt_file_service(key, file)
    response = StreamingResponse(
        content=iterable_file_content,
        media_type=file.content_type
    )
    return response


@extended_vignere_router.post("/decrypt-file")
async def decrypt_file_handler(key: bytes = Form(), file: UploadFile = File()):
    iterable_file_content = await decrypt_file_service(key, file)
    response = StreamingResponse(
        content=iterable_file_content,
        media_type=file.content_type
    )
    return response
