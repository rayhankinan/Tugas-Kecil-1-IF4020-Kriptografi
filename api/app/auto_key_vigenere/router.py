from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from .schemas import AutoKeyVigenereFileIn
from .services import encrypt_file_service, decrypt_file_service

auto_key_vigenere_router = APIRouter(prefix="/auto-key-vigenere")


@auto_key_vigenere_router.post("/encrypt-file")
async def encrypt_file_handler(auto_key_vigenere_file_in: AutoKeyVigenereFileIn = Depends()):
    iterable_file_content = await encrypt_file_service(auto_key_vigenere_file_in.key, auto_key_vigenere_file_in.file)
    response = StreamingResponse(
        content=iterable_file_content
    )
    return response


@auto_key_vigenere_router.post("/decrypt-file")
async def decrypt_file_handler(auto_key_vigenere_file_in: AutoKeyVigenereFileIn = Depends()):
    iterable_file_content = await decrypt_file_service(auto_key_vigenere_file_in.key, auto_key_vigenere_file_in.file)
    response = StreamingResponse(
        content=iterable_file_content
    )
    return response
