from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from .schemas import ExtendedVigenereFileIn
from .services import encrypt_file_service, decrypt_file_service

extended_vigenere_router = APIRouter(prefix="/extended-vigenere")


@extended_vigenere_router.post("/encrypt-file")
async def encrypt_file_handler(extended_vigenere_file_in: ExtendedVigenereFileIn = Depends()):
    iterable_file_content = await encrypt_file_service(extended_vigenere_file_in.key, extended_vigenere_file_in.file)
    response = StreamingResponse(
        content=iterable_file_content
    )
    return response


@extended_vigenere_router.post("/decrypt-file")
async def decrypt_file_handler(extended_vigenere_file_in: ExtendedVigenereFileIn = Depends()):
    iterable_file_content = await decrypt_file_service(extended_vigenere_file_in.key, extended_vigenere_file_in.file)
    response = StreamingResponse(
        content=iterable_file_content
    )
    return response
