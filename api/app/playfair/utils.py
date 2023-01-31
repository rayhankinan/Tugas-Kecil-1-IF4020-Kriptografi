from typing import List, NamedTuple, Type
from pydantic import conlist, validator
from .constants import MATRIX_DIMENSION, X_INDEX, J_INDEX
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

def generate_matrix(key: AlphabetStringType):
    base_matrix = [i for i in range (LENGTH_OF_ALPHABET)]
    del base_matrix[J_INDEX]

    key.replace('j', '')
    key = list(set(key))
    for char in key:
        byte = bytes(char)
        num = alphabet_ascii(byte)
        if num != -1:
            base_matrix.remove(num)
            base_matrix.insert(0, num)
    return base_matrix

def find_coord(key_matrix: PlayfairKeyType, num: int):
    for i in range (MATRIX_DIMENSION):
        for j in range (MATRIX_DIMENSION):
            if (key_matrix[i][j] == num):
                return (i, j)
    return (-1, -1)