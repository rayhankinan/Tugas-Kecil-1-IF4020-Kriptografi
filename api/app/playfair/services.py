from fastapi import UploadFile
from typing import List
from .constants import MATRIX_DIMENSION
from .utils import PlayfairKeyType, generate_matrix, find_coord
from ..utils import apply_static_func_to_file, apply_static_playfair_to_file, num_to_binary, AlphabetStringType


async def encrypt_file_service(key: AlphabetStringType, file: UploadFile):

    key_matrix : PlayfairKeyType = generate_matrix(key)
    # TODO: Add Playfair Encryption
    async def encrypt_bytes(bigram: List[int]):
        index_fi = find_coord(key_matrix, bigram[0])
        index_se = find_coord(key_matrix, bigram[1])
        if index_fi[0] == index_se[0]:
            encrypt_byte_fi = key_matrix[index_fi[0]][(index_fi[1] + 1) % MATRIX_DIMENSION]
            encrypt_byte_se = key_matrix[index_se[0]][(index_se[1] + 1) % MATRIX_DIMENSION]
        elif index_fi[1] == index_se[1]:
            encrypt_byte_fi = key_matrix[(index_fi[0] + 1) % MATRIX_DIMENSION][index_fi[1]]
            encrypt_byte_se = key_matrix[(index_se[0] + 1) % MATRIX_DIMENSION][index_se[1]]
        else:
            encrypt_byte_fi = key_matrix[index_fi[0]][index_se[1]]
            encrypt_byte_se = key_matrix[index_se[0]][index_fi[1]]
        encrypt_byte_fi = num_to_binary(encrypt_byte_fi, 1)
        encrypt_byte_se = num_to_binary(encrypt_byte_se, 2)
        return encrypt_byte_fi << 8 | encrypt_byte_se

    return apply_static_playfair_to_file(file, func=encrypt_bytes)


async def decrypt_file_service(key: AlphabetStringType, file: UploadFile):
    # TODO: Add Playfair Decryption
    async def decrypt_bytes(bigram: List[int]):
        pass
    return apply_static_func_to_file(file, bytes_group=2, func=decrypt_bytes)
