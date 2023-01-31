from fastapi import UploadFile
from typing import List
from .utils import PlayfairKeyType, generate_matrix
from ..utils import apply_static_func_to_file, apply_static_playfair_to_file, AlphabetStringType


async def encrypt_file_service(key: AlphabetStringType, file: UploadFile):

    key_matrix : PlayfairKeyType = generate_matrix(key)
    # TODO: Add Playfair Encryption
    async def encrypt_bytes(bigram: List[int]):
        pass
    return apply_static_playfair_to_file(file, func=encrypt_bytes)


async def decrypt_file_service(key: AlphabetStringType, file: UploadFile):
    # TODO: Add Playfair Decryption
    async def decrypt_bytes(bigram: List[int]):
        pass
    return apply_static_func_to_file(file, bytes_group=2, func=decrypt_bytes)
