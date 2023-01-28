from fastapi import UploadFile
from .utils import VignereAutoKeyType
from ..utils import apply_dynamic_func_to_file


async def encrypt_file_service(auto_key: VignereAutoKeyType, file: UploadFile):
    # TODO: Add Auto Key Vignere Encryption
    return apply_dynamic_func_to_file(file, )


async def decrypt_file_service(auto_key: VignereAutoKeyType, file: UploadFile):
    # TODO: Add Auto Key Vignere Decryption
    return apply_dynamic_func_to_file(file, )
