from fastapi import UploadFile
from ..utils import AlphabetStringType, AlphabetByteType, apply_dynamic_func_to_file, apply_dynamic_extvig_to_file, binary_to_num, num_to_binary, char_to_num
from ..constants import LENGTH_OF_ALPHABET, OVERHEAD_ASCII


async def encrypt_file_service(key: AlphabetStringType, file: UploadFile):
    async def encrypt_bytes(value: int, counter: int):
        index = counter % len(key)
        partitioned_key = await char_to_num(key[index]) - OVERHEAD_ASCII
        final_value = (value + partitioned_key) % LENGTH_OF_ALPHABET
        final_bytes = await num_to_binary(final_value + OVERHEAD_ASCII, 1)
        return final_bytes

    return apply_dynamic_func_to_file(file, bytes_group=1, func=encrypt_bytes)


async def decrypt_file_service(key: AlphabetStringType, file: UploadFile):
    async def decrypt_bytes(value: int, counter: int):
        index = counter % len(key)
        partitioned_key = await char_to_num(key[index]) - OVERHEAD_ASCII
        final_value = (value - partitioned_key) % LENGTH_OF_ALPHABET
        final_bytes = await num_to_binary(final_value + OVERHEAD_ASCII, 1)
        return final_bytes

    return apply_dynamic_func_to_file(file, bytes_group=1, func=decrypt_bytes)
