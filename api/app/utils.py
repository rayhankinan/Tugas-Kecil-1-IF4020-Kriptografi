from typing import Callable
from fastapi import UploadFile


async def apply_static_func_to_file(file: UploadFile, bytes_group: int = 1, func: Callable[[bytes], bytes] = lambda x: x):
    while chunk := await file.read(bytes_group):
        yield func(chunk)


async def apply_dynamic_func_to_file(file: UploadFile, bytes_group: int = 1, func: Callable[[bytes, int], bytes] = lambda x, _: x):
    counter = 0
    while chunk := await file.read(bytes_group):
        yield func(chunk, counter)
        counter += 1
