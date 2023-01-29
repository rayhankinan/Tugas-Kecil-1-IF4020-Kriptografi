from fastapi import UploadFile
from ..utils import AlphabetStringType, apply_dynamic_func_to_file


async def encrypt_file_service(key: AlphabetStringType, file: UploadFile):
    # TODO: Add Vignere Encryption
    return apply_dynamic_func_to_file(file, )


async def decrypt_file_service(key: AlphabetStringType, file: UploadFile):
    # TODO: Add Vignere Decryption
    return apply_dynamic_func_to_file(file, )
