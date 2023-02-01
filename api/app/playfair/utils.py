import numpy
from typing import List, Type
from pydantic import conlist
from ..lib import alru_cache_typed
from .constants import MATRIX_DIMENSION, J_INDEX
from ..utils import PositiveIntegerType, AlphabetStringType, alphabet_ascii
from ..constants import LENGTH_OF_ALPHABET

PlayfairKeyType: Type[List[List[int]]] = conlist(
    conlist(
        PositiveIntegerType,
        min_items=MATRIX_DIMENSION,
        max_items=MATRIX_DIMENSION
    ),
    min_items=MATRIX_DIMENSION,
    max_items=MATRIX_DIMENSION
)


@alru_cache_typed()
async def generate_matrix(key: AlphabetStringType):
    set_key = []
    base_matrix = [i for i in range(LENGTH_OF_ALPHABET)]
    del base_matrix[J_INDEX]

    key = key.replace('j', '')
    key = key.replace(' ', '')

    for char in key:
        byte = bytes(char, 'utf-8')
        num = await alphabet_ascii(byte)
        if num not in set_key and num != -1:
            set_key.append(num)
    for ascii in base_matrix:
        if ascii not in set_key:
            set_key.append(ascii)

    return set_key


def find_coord(key_matrix: numpy.ndarray, num: int):
    for i in range(MATRIX_DIMENSION):
        for j in range(MATRIX_DIMENSION):
            if (key_matrix[i][j] == num):
                return (i, j)
    return (-1, -1)
