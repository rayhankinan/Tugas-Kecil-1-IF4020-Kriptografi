from typing import Any, Callable, Coroutine, List, Type, Union
from fastapi import UploadFile
from pydantic import conbytes, conint, constr
from .lib import alru_cache_typed
from .constants import LENGTH_OF_ALPHABET, OVERHEAD_ASCII, UPPERCASE_ASCII
from .playfair.constants import X_INDEX, J_INDEX

AllStringType: Type[str] = constr(min_length=1)
AllByteType: Type[bytes] = conbytes(
    min_length=1
)
AlphabetStringType: Type[str] = constr(
    min_length=1,
    regex=r"^[A-Za-z ]+$",
    to_lower=True,
    strip_whitespace=True
)
AlphabetCharType: Type[str] = constr(
    min_length=1,
    max_length=1,
    regex=r"^[A-Za-z]+$",
    to_lower=True
)
PositiveIntegerType: Type[int] = conint(gt=0)


async def apply_static_func_to_file(file: UploadFile, bytes_group: int = 1, func: Callable[[Union[int, List[int]]], Coroutine[Any, Any, bytes]] = lambda x: x):
    end_of_file: bool = False
    while not end_of_file:
        array_ascii: List[int] = []
        while len(array_ascii) != bytes_group:
            chunk = await file.read(1)
            if chunk == b'':
                end_of_file = True
                break

            num = await alphabet_ascii(chunk)
            if num != -1:
                array_ascii.append(num)

        if len(array_ascii) != 0:
            if (bytes_group == 1):
                yield await func(array_ascii[0])
            else:
                yield await func(array_ascii)

async def apply_static_playfair_to_file(file: UploadFile, func: Callable[[any], Coroutine[any, any, bytes]] = lambda x: x):
    end_of_file : bool = False
    while not end_of_file:
        array_ascii = []
        while len(array_ascii) != 2:
            chunk = await file.read(1)
            if chunk == b'':
                end_of_file = True
                if (len(array_ascii) == 1):
                    array_ascii.append(X_INDEX)
                break
            num = await alphabet_ascii(chunk)
            if num != -1:
                if (len(array_ascii) != 0 and num == array_ascii[0]):
                    array_ascii.append(X_INDEX)
                    yield await func(array_ascii)
                    array_ascii = []
                if num == J_INDEX:
                    if (num == array_ascii[0]):
                        array_ascii.append(X_INDEX)
                        yield await func(array_ascii)
                        array_ascii = []
                    array_ascii.append(J_INDEX - 1)
                else:
                    array_ascii.append(num)
        if len(array_ascii) == 2:
            yield await func(array_ascii)


async def apply_dynamic_func_to_file(file: UploadFile, bytes_group: int = 1, func: Callable[[Union[int, List[int]], int], Coroutine[Any, Any, bytes]] = lambda x, _: x):
    counter = 0
    end_of_file: bool = False
    while not end_of_file:
        array_ascii: List[int] = []
        while len(array_ascii) != bytes_group:
            chunk = await file.read(1)
            if chunk == b'':
                end_of_file = True
                break

            num = await alphabet_ascii(chunk)
            if num != -1:
                array_ascii.append(num)

        if len(array_ascii) != 0:
            if (bytes_group == 1):
                yield await func(array_ascii[0], counter)
                counter += 1
            else:
                yield await func(array_ascii, counter)
                counter += 1


async def apply_dynamic_extvig_to_file(file: UploadFile, bytes_group: int = 1, func: Callable[[bytes, int], Coroutine[Any, Any, bytes]] = lambda x, _: x):
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
async def num_to_binary(num: int, length: int):
    return num.to_bytes(length, byteorder="big", signed=False)


@alru_cache_typed()
async def alphabet_ascii(binary: bytes):
    num = await binary_to_num(binary)

    if OVERHEAD_ASCII <= num < OVERHEAD_ASCII + LENGTH_OF_ALPHABET:
        return num - OVERHEAD_ASCII
    elif UPPERCASE_ASCII <= num < UPPERCASE_ASCII + LENGTH_OF_ALPHABET:
        return num - UPPERCASE_ASCII
    else:
        return -1
