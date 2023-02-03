from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from .schemas import PlayfairFileIn
from .services import encrypt_file_service, decrypt_file_service

playfair_router = APIRouter(prefix="/playfair")


@playfair_router.post("/encrypt-file")
async def encrypt_file_handler(playfair_file_in: PlayfairFileIn = Depends()):
    iterable_file_content = await encrypt_file_service(playfair_file_in.key, playfair_file_in.file)
    response = StreamingResponse(
        content=iterable_file_content
    )
    return response


@playfair_router.post("/decrypt-file")
async def decrypt_file_handler(playfair_file_in: PlayfairFileIn = Depends()):
    iterable_file_content = await decrypt_file_service(playfair_file_in.key, playfair_file_in.file)
    response = StreamingResponse(
        content=iterable_file_content
    )
    return response
