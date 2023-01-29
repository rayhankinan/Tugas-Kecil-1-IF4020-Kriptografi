from fastapi import UploadFile
from ..utils import AllStringType, AllByteType, apply_dynamic_func_to_file, binary_to_num, num_to_binary, char_to_num
from ..constants import LENGTH_OF_ASCII


async def encrypt_file_service(key: AllStringType, file: UploadFile):
    # TODO: Add Extended Vignere Encryption
    async def encrypt_bytes(binary: AllByteType, counter: int):
        raw_value = await binary_to_num(binary)
        index = counter % len(key)
        partitioned_key = await char_to_num(key[index])
        final_value = (raw_value + partitioned_key) % LENGTH_OF_ASCII
        final_bytes = await num_to_binary(final_value)
        return final_bytes

    return apply_dynamic_func_to_file(file, bytes_group=1, func=encrypt_bytes)


async def decrypt_file_service(key: AllStringType, file: UploadFile):
    # TODO: Add Extended Vignere Decryption
    async def decrypt_bytes(binary: AllByteType, counter: int):
        raw_value = await binary_to_num(binary)
        index = counter % len(key)
        partitioned_key = await char_to_num(key[index])
        final_value = (raw_value - partitioned_key) % LENGTH_OF_ASCII
        final_bytes = await num_to_binary(final_value)
        return final_bytes

    return apply_dynamic_func_to_file(file, bytes_group=1, func=decrypt_bytes)
