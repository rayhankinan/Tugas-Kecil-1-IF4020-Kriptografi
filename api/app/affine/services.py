from fastapi import UploadFile
from .utils import repeat_add, repeat_subtract
from ..utils import PositiveIntegerType, AlphabetByteType, apply_static_func_to_file, binary_to_num, num_to_binary
from ..constants import LENGTH_OF_ALPHABET, OVERHEAD_ASCII


async def encrypt_file_service(key: PositiveIntegerType, shift: PositiveIntegerType, group: PositiveIntegerType, file: UploadFile):
    # TODO: Add Affine Encryption (Done)
    async def encrypt_bytes(binary: AlphabetByteType):
        raw_value = await binary_to_num(binary)
        initial_value = await repeat_subtract(raw_value, group, OVERHEAD_ASCII)
        modulo = await repeat_add(1, group, LENGTH_OF_ALPHABET)
        encrypted_value = (key * initial_value + shift) % modulo
        final_value = await repeat_add(encrypted_value, group, OVERHEAD_ASCII)
        final_bytes = await num_to_binary(final_value, group)
        return final_bytes

    return apply_static_func_to_file(file, bytes_group=group, func=encrypt_bytes)


async def decrypt_file_service(key: PositiveIntegerType, shift: PositiveIntegerType, group: PositiveIntegerType, file: UploadFile):
    # TODO: Add Affine Decryption (Done)
    async def decrypt_bytes(binary: AlphabetByteType):
        raw_value = await binary_to_num(binary)
        initial_value = await repeat_subtract(raw_value, group, OVERHEAD_ASCII)
        modulo = await repeat_add(1, group, LENGTH_OF_ALPHABET)
        decrypted_value = (pow(key, -1, modulo)
                           * (initial_value - shift)) % modulo
        final_value = await repeat_add(decrypted_value, group, OVERHEAD_ASCII)
        print(final_value)
        final_bytes = await num_to_binary(final_value, group)
        return final_bytes

    return apply_static_func_to_file(file, bytes_group=group, func=decrypt_bytes)
