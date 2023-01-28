from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from .schemas import EnigmaFileIn
from .services import encrypt_file_service, decrypt_file_service

enigma_router = APIRouter(prefix="/enigma")


@enigma_router.post("/encrypt-file")
async def encrypt_file_handler(enigma_file_in: EnigmaFileIn = Depends()):
    iterable_file_content = await encrypt_file_service(enigma_file_in.rotor_order, enigma_file_in.notch_setting, enigma_file_in.start_position, enigma_file_in.list_of_plugboard, enigma_file_in.file)
    response = StreamingResponse(
        content=iterable_file_content,
        media_type=enigma_file_in.file.content_type
    )
    return response


@enigma_router.post("/decrypt-file")
async def decrypt_file_handler(enigma_file_in: EnigmaFileIn = Depends()):
    iterable_file_content = await decrypt_file_service(enigma_file_in.rotor_order, enigma_file_in.notch_setting, enigma_file_in.start_position, enigma_file_in.list_of_plugboard, enigma_file_in.file)
    response = StreamingResponse(
        content=iterable_file_content,
        media_type=enigma_file_in.file.content_type
    )
    return response
