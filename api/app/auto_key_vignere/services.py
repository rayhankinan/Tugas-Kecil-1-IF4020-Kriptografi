from collections import deque
from typing import Deque
from fastapi import UploadFile
from ..utils import AlphabetStringType, AlphabetByteType, apply_dynamic_func_to_file, binary_to_num, num_to_binary, char_to_num
from ..constants import LENGTH_OF_ALPHABET, OVERHEAD_ASCII


async def encrypt_file_service(key: AlphabetStringType, file: UploadFile):
    # TODO: Add Auto Key Vignere Encryption (Done)
    deq: Deque[int] = deque(maxlen=len(key) + 1)

    async def encrypt_bytes(binary: AlphabetByteType, counter: int):
        raw_value = await binary_to_num(binary)
        initial_value = raw_value - OVERHEAD_ASCII
        deq.append(initial_value)

        partitioned_key: int
        if counter < len(key):
            partitioned_key = await char_to_num(key[counter]) - OVERHEAD_ASCII
        else:
            partitioned_key = deq.popleft()

        final_value = (initial_value + partitioned_key) % LENGTH_OF_ALPHABET
        final_bytes = await num_to_binary(final_value + OVERHEAD_ASCII, 1)
        return final_bytes

    return apply_dynamic_func_to_file(file, bytes_group=1, func=encrypt_bytes)


async def decrypt_file_service(key: AlphabetStringType, file: UploadFile):
    # TODO: Add Auto Key Vignere Decryption (Done)
    deq: Deque[int] = deque(maxlen=len(key))

    async def decrypt_bytes(binary: AlphabetByteType, counter: int):
        raw_value = await binary_to_num(binary)
        initial_value = raw_value - OVERHEAD_ASCII

        partitioned_key: int
        if counter < len(key):
            partitioned_key = await char_to_num(key[counter]) - OVERHEAD_ASCII
        else:
            partitioned_key = deq.popleft()

        final_value = (initial_value - partitioned_key) % LENGTH_OF_ALPHABET
        deq.append(final_value)

        final_bytes = await num_to_binary(final_value + OVERHEAD_ASCII, 1)
        return final_bytes

    return apply_dynamic_func_to_file(file, bytes_group=1, func=decrypt_bytes)
