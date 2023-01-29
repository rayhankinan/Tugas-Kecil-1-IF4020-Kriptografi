import math
from typing import Callable, Coroutine, Type
from fastapi import UploadFile
from pydantic import conbytes, conint, constr
from .constants import OVERHEAD_ASCII
from .lib import alru_cache_typed

AllStringType: Type[str] = constr(min_length=1)
AllByteType: Type[bytes] = conbytes(
    min_length=1
)
AlphabetStringType: Type[str] = constr(
    min_length=1,
    regex=r"^[A-Za-z]+$",
    to_lower=True
)
AlphabetByteType: Type[bytes] = conbytes(
    min_length=1,
    to_lower=True
)
AlphabetCharType: Type[str] = constr(
    min_length=1,
    max_length=1,
    regex=r"^[A-Za-z]+$",
    to_lower=True
)
PositiveIntegerType: Type[int] = conint(gt=0)


async def apply_static_func_to_file(file: UploadFile, bytes_group: int = 1, func: Callable[[bytes], Coroutine[any, any, bytes]] = lambda x: x):
    while chunk := await file.read(bytes_group):
        yield await func(chunk)


async def apply_dynamic_func_to_file(file: UploadFile, bytes_group: int = 1, func: Callable[[bytes, int], Coroutine[any, any, bytes]] = lambda x, _: x):
    counter = 0
    while chunk := await file.read(bytes_group):
        yield await func(chunk, counter)
        counter += 1


@alru_cache_typed()
async def char_to_num(char: str):
    return ord(char)


@alru_cache_typed()
async def num_to_char(num: int):
    return chr(num)


@alru_cache_typed()
async def binary_to_num(binary: bytes):
    return int.from_bytes(binary, byteorder="big", signed=False)


@alru_cache_typed()
async def num_to_binary(num: int):
    length = math.ceil(num / (1 << 8))
    return num.to_bytes(length, byteorder="big", signed=False)
