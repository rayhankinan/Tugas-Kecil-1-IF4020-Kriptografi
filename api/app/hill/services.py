import numpy as np
from struct import unpack
from typing import List
from fastapi import UploadFile
from .utils import HillKeyType
from ..utils import AllByteType, apply_static_func_to_file


async def encrypt_file_service(key: HillKeyType, file: UploadFile):
    # TODO: Add Hill Encryption
    async def encrypt_bytes(binary: AllByteType):
        ...
    return apply_static_func_to_file(file, )


async def decrypt_file_service(key: HillKeyType, file: UploadFile):
    # TODO: Add Hill Decryption
    async def decrypt_bytes(binary: AllByteType):
        ...
    return apply_static_func_to_file(file, )
