from collections import deque
from typing import Deque
from fastapi import UploadFile
from ..utils import AlphabetStringType, AlphabetByteType, apply_dynamic_func_to_file, binary_to_num, num_to_binary, char_to_num
from ..constants import LENGTH_OF_ALPHABET, OVERHEAD_ASCII


async def encrypt_file_service(key: AlphabetStringType, file: UploadFile):
    # TODO: Add Auto Key Vignere Encryption (Done)
    async def encrypt_bytes(binary: AlphabetByteType, counter: int):
        raw_value = await binary_to_num(binary)
        initial_value = raw_value - OVERHEAD_ASCII

        partitioned_key: int
        if counter < len(key):
            partitioned_key = await char_to_num(key[counter])
        else:
            await file.seek(counter - len(key))
            past_binary = await file.read(1)
            raw_key = await binary_to_num(past_binary)
            partitioned_key = raw_key - OVERHEAD_ASCII

        final_value = (initial_value + partitioned_key) % LENGTH_OF_ALPHABET
        final_bytes = await num_to_binary(final_value + OVERHEAD_ASCII, 1)
        return final_bytes

    return apply_dynamic_func_to_file(file, bytes_group=1, func=encrypt_bytes)


async def decrypt_file_service(key: AlphabetStringType, file: UploadFile):
    # TODO: Add Auto Key Vignere Decryption (Masih salah)
    deq: Deque[int] = deque(maxlen=len(key))

    async def decrypt_bytes(binary: AlphabetByteType, counter: int):
        raw_value = await binary_to_num(binary)
        initial_value = raw_value - OVERHEAD_ASCII

        partitioned_key: int
        if counter < len(key):
            partitioned_key = await char_to_num(key[counter])
        else:
            partitioned_key = deq.popleft()

        final_value = (initial_value - partitioned_key) % LENGTH_OF_ALPHABET
        deq.append(final_value)

        final_bytes = await num_to_binary(final_value + OVERHEAD_ASCII, 1)
        return final_bytes

    return apply_dynamic_func_to_file(file, bytes_group=1, func=decrypt_bytes)
