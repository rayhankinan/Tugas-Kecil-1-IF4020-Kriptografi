from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import StreamingResponse
from .services import encrypt_service, decrypt_service

vignere_router = APIRouter(prefix="/vignere")


@vignere_router.post("/encrypt-file")
async def encrypt_handler(key: str = Form(regex=r"^[A-Za-z]+$"), file: UploadFile = File()):
    iterable_file_content = await encrypt_service(key, file)
    response = StreamingResponse(
        content=iterable_file_content,
        media_type=file.content_type
    )
    return response


@vignere_router.post("/decrypt-file")
async def decrypt_handler(key: str = Form(regex=r"^[A-Za-z]+$"), file: UploadFile = File()):
    iterable_file_content = await decrypt_service(key, file)
    response = StreamingResponse(
        content=iterable_file_content,
        media_type=file.content_type
    )
    return response
