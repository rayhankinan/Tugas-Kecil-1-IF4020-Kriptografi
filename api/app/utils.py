from typing import Callable, Type
from fastapi import UploadFile
from pydantic import conbytes, conint, constr

AlphabetStringType: Type[str] = constr(regex=r"^[A-Za-z]+$", to_lower=True)
AlphabetCharType: Type[str] = constr(
    min_length=1,
    max_length=1,
    regex=r"^[A-Za-z]+$",
    to_lower=True
)
PositiveIntegerType: Type[int] = conint(gt=0)
BinaryText: Type[bytes] = conbytes()


async def apply_static_func_to_file(file: UploadFile, bytes_group: int = 1, func: Callable[[bytes], bytes] = lambda x: x):
    while chunk := await file.read(bytes_group):
        yield func(chunk)


async def apply_dynamic_func_to_file(file: UploadFile, bytes_group: int = 1, func: Callable[[bytes, int], bytes] = lambda x, _: x):
    counter = 0
    while chunk := await file.read(bytes_group):
        yield func(chunk, counter)
        counter += 1
