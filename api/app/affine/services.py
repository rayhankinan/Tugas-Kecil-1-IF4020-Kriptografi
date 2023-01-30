from fastapi import UploadFile
from ..utils import PositiveIntegerType, apply_static_func_to_file, num_to_binary
from ..constants import LENGTH_OF_ALPHABET, OVERHEAD_ASCII


async def encrypt_file_service(key: PositiveIntegerType, shift: PositiveIntegerType, file: UploadFile):
    async def encrypt_bytes(value: int):
        final_value = (key * value + shift) % LENGTH_OF_ALPHABET
        final_bytes = await num_to_binary(final_value + OVERHEAD_ASCII, 1)
        return final_bytes

    return apply_static_func_to_file(file, bytes_group=1, func=encrypt_bytes)


async def decrypt_file_service(key: PositiveIntegerType, shift: PositiveIntegerType, file: UploadFile):
    async def decrypt_bytes(value):
        final_value = (pow(key, -1, LENGTH_OF_ALPHABET)
                           * (value - shift)) % LENGTH_OF_ALPHABET
        final_bytes = await num_to_binary(final_value + OVERHEAD_ASCII, 1)
        return final_bytes

    return apply_static_func_to_file(file, bytes_group=1, func=decrypt_bytes)
