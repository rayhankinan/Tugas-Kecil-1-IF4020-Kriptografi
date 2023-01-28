from fastapi import UploadFile
from .utils import HillKeyType
from ..utils import apply_static_func_to_file


async def encrypt_file_service(key: HillKeyType, file: UploadFile):
    # TODO: Add Hill Encryption
    return apply_static_func_to_file(file, )


async def decrypt_file_service(key: HillKeyType, file: UploadFile):
    # TODO: Add Hill Decryption
    return apply_static_func_to_file(file, )
