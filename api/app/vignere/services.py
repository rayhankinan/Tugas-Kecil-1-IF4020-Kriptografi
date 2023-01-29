from fastapi import UploadFile
from ..utils import AlphabetStringType, AlphabetByteType, apply_dynamic_func_to_file, binary_to_num, num_to_binary, char_to_num
from ..constants import LENGTH_OF_ALPHABET, OVERHEAD_ASCII


async def encrypt_file_service(key: AlphabetStringType, file: UploadFile):
    # TODO: Add Vignere Encryption
    async def encrypt_bytes(binary: AlphabetByteType, counter: int):
        raw_value = await binary_to_num(binary)
        initial_value = raw_value - OVERHEAD_ASCII
        index = counter % len(key)
        partitioned_key = await char_to_num(key[index])
        final_value = (initial_value + partitioned_key) % LENGTH_OF_ALPHABET
        final_bytes = await num_to_binary(final_value + OVERHEAD_ASCII)
        return final_bytes

    return apply_dynamic_func_to_file(file, bytes_group=1, func=encrypt_bytes)


async def decrypt_file_service(key: AlphabetStringType, file: UploadFile):
    # TODO: Add Vignere Decryption
    async def decrypt_bytes(binary: AlphabetByteType, counter: int):
        raw_value = await binary_to_num(binary)
        initial_value = raw_value - OVERHEAD_ASCII
        index = counter % len(key)
        partitioned_key = await char_to_num(key[index])
        final_value = (initial_value - partitioned_key) % LENGTH_OF_ALPHABET
        final_bytes = await num_to_binary(final_value + OVERHEAD_ASCII)
        return final_bytes

    return apply_dynamic_func_to_file(file, bytes_group=1, func=decrypt_bytes)
