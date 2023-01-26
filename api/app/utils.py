from typing import Callable
from fastapi import UploadFile


async def apply_static_func_to_file(file: UploadFile, bytes_group: int = 1, func: Callable[[bytes], bytes] = lambda x: x):
    while chunk := await file.read(bytes_group):
        yield func(chunk)

# TODO: Membuat iterable untuk mengaplikasikan dynamic func (digunakan pada auto-key dan enigma)
