from fastapi import UploadFile
from ..utils import BinaryText, apply_dynamic_func_to_file


async def encrypt_file_service(key: BinaryText, file: UploadFile):
    # TODO: Add Extended Vignere Encryption
    return apply_dynamic_func_to_file(file, )


async def decrypt_file_service(key: BinaryText, file: UploadFile):
    # TODO: Add Extended Vignere Decryption
    return apply_dynamic_func_to_file(file, )
