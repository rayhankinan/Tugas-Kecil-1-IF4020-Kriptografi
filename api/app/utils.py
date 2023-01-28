import math
from typing import Callable, Type
from fastapi import UploadFile
from pydantic import conbytes, conint, constr
from .constants import OVERHEAD_ASCII

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


def alphabet_to_num(char: str):
    return ord(char) - OVERHEAD_ASCII


def num_to_alphabet(num: int):
    return chr(num + OVERHEAD_ASCII)


def binary_to_num(binary: bytes):
    return int.from_bytes(binary, byteorder="big", signed=False)


def num_to_binary(num: int):
    length = math.ceil(num / (1 << 8))
    return num.to_bytes(length, byteorder="big", signed=False)
