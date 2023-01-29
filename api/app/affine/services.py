from fastapi import UploadFile
from ..utils import PositiveIntegerType, apply_static_func_to_file, binary_to_num, num_to_binary
from ..constants import LENGTH_OF_ALPHABET, OVERHEAD_ASCII


async def encrypt_file_service(key: PositiveIntegerType, shift: PositiveIntegerType, file: UploadFile):
    # TODO: Add Affine Encryption (Baru bisa lower alphabet)
    async def encrypt_bytes(binary: bytes):
        raw_value = await binary_to_num(binary)
        initial_value = raw_value - OVERHEAD_ASCII
        final_value = (key * initial_value + shift) % LENGTH_OF_ALPHABET
        final_bytes = await num_to_binary(final_value + OVERHEAD_ASCII)
        return final_bytes

    return apply_static_func_to_file(file, bytes_group=1, func=encrypt_bytes)


async def decrypt_file_service(key: PositiveIntegerType, shift: PositiveIntegerType, file: UploadFile):
    # TODO: Add Affine Decryption (Baru bisa lower alphabet)
    async def decrypt_bytes(binary: bytes):
        raw_value = await binary_to_num(binary)
        initial_value = raw_value - OVERHEAD_ASCII
        final_value = (
            pow(key, -1, LENGTH_OF_ALPHABET) * (initial_value - shift)
        ) % LENGTH_OF_ALPHABET
        final_bytes = await num_to_binary(final_value + OVERHEAD_ASCII)
        return final_bytes

    return apply_static_func_to_file(file, bytes_group=1, func=decrypt_bytes)
