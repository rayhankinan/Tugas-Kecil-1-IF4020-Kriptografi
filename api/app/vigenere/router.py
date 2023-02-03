from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from .schemas import VigenereFileIn
from .services import encrypt_file_service, decrypt_file_service

vigenere_router = APIRouter(prefix="/vigenere")


@vigenere_router.post("/encrypt-file")
async def encrypt_file_handler(vigenere_file_in: VigenereFileIn = Depends()):
    iterable_file_content = await encrypt_file_service(vigenere_file_in.key, vigenere_file_in.file)
    response = StreamingResponse(
        content=iterable_file_content
    )
    return response


@vigenere_router.post("/decrypt-file")
async def decrypt_file_handler(vigenere_file_in: VigenereFileIn = Depends()):
    iterable_file_content = await decrypt_file_service(vigenere_file_in.key, vigenere_file_in.file)
    response = StreamingResponse(
        content=iterable_file_content
    )
    return response
