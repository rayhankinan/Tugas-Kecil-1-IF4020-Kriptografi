from fastapi import UploadFile
from ..utils import apply_static_func_to_file
from .utils import HillKey


async def encrypt_file_service(key: HillKey, file: UploadFile):
    # TODO: Add Hill Encryption
    return apply_static_func_to_file(file, )


async def decrypt_file_service(key: HillKey, file: UploadFile):
    # TODO: Add Hill Decryption
    return apply_static_func_to_file(file, )
