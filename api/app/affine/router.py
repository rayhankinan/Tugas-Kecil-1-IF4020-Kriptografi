from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from .schemas import AffineFileIn
from .services import encrypt_file_service, decrypt_file_service

affine_router = APIRouter(prefix="/affine")


@affine_router.post("/encrypt-file")
async def encrypt_file_handler(affine_file_in: AffineFileIn = Depends()):
    iterable_file_content = await encrypt_file_service(affine_file_in.key, affine_file_in.shift, affine_file_in.group, affine_file_in.file)
    response = StreamingResponse(
        content=iterable_file_content,
        media_type=affine_file_in.file.content_type
    )
    return response


@affine_router.post("/decrypt-file")
async def decrypt_file_handler(affine_file_in: AffineFileIn = Depends()):
    iterable_file_content = await decrypt_file_service(affine_file_in.key, affine_file_in.shift, affine_file_in.group, affine_file_in.file)
    response = StreamingResponse(
        content=iterable_file_content,
        media_type=affine_file_in.file.content_type
    )
    return response
