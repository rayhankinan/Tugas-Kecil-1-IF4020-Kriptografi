from typing import List, NamedTuple, Type
from pydantic import conlist, validator
from .constants import MATRIX_DIMENSION
from ..utils import AlphabetCharType


class ConvertChar(NamedTuple):
    initial_char: AlphabetCharType
    converted_char: AlphabetCharType

    # TODO: Cek apakah initial_char berbeda dengan converted_char


PlayfairKeyType: Type[List[List[int]]] = conlist(
    conlist(
        AlphabetCharType,
        min_items=MATRIX_DIMENSION,
        max_items=MATRIX_DIMENSION
    ),
    min_items=MATRIX_DIMENSION,
    max_items=MATRIX_DIMENSION
)
