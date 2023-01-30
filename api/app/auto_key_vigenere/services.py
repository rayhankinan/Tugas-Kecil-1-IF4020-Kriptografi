from collections import deque
from typing import Deque
from fastapi import UploadFile
from ..utils import AlphabetStringType, apply_dynamic_func_to_file, num_to_binary, char_to_num
from ..constants import LENGTH_OF_ALPHABET, OVERHEAD_ASCII


async def encrypt_file_service(key: AlphabetStringType, file: UploadFile):
    deq: Deque[int] = deque(maxlen=len(key)+1)

    async def encrypt_bytes(value: int, counter: int):
        deq.append(value)
        partitioned_key: int
        if counter < len(key):
            partitioned_key = await char_to_num(key[counter]) - OVERHEAD_ASCII
        else:
            partitioned_key = deq.popleft()

        final_value = (value + partitioned_key) % LENGTH_OF_ALPHABET
        final_bytes = await num_to_binary(final_value + OVERHEAD_ASCII, 1)
        return final_bytes

    return apply_dynamic_func_to_file(file, bytes_group=1, func=encrypt_bytes)


async def decrypt_file_service(key: AlphabetStringType, file: UploadFile):
    deq: Deque[int] = deque(maxlen=len(key))

    async def decrypt_bytes(value: int, counter: int):
        partitioned_key: int
        if counter < len(key):
            partitioned_key = await char_to_num(key[counter]) - OVERHEAD_ASCII
        else:
            partitioned_key = deq.popleft()

        final_value = (value - partitioned_key) % LENGTH_OF_ALPHABET
        deq.append(final_value)

        final_bytes = await num_to_binary(final_value + OVERHEAD_ASCII, 1)
        return final_bytes

    return apply_dynamic_func_to_file(file, bytes_group=1, func=decrypt_bytes)
