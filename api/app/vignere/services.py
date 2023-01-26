from fastapi import UploadFile
from .schemas import VignereIn, VignereOut


async def encrypt_service(vignere_in: VignereIn) -> VignereOut:
    # TODO: Add Vignere Encryption
    pass


async def decrypt_service(vignere_in: VignereIn) -> VignereOut:
    # TODO: Add Vignere Decryption
    pass
