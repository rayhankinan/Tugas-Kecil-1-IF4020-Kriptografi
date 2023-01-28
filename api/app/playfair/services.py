from fastapi import UploadFile
from .utils import PlayfairKeyType
from ..utils import apply_static_func_to_file


async def encrypt_file_service(key: PlayfairKeyType, file: UploadFile):
    # TODO: Add Playfair Encryption
    return apply_static_func_to_file(file, )


async def decrypt_file_service(key: PlayfairKeyType, file: UploadFile):
    # TODO: Add Playfair Decryption
    return apply_static_func_to_file(file, )
