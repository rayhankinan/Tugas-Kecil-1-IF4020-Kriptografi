from fastapi import UploadFile
from ..utils import apply_static_func_to_file


async def encrypt_file_service(key: bytes, file: UploadFile):
    # TODO: Add Extended Vignere Encryption
    return apply_static_func_to_file(file, )


async def decrypt_file_service(key: bytes, file: UploadFile):
    # TODO: Add Extended Vignere Decryption
    return apply_static_func_to_file(file, )
