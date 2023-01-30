from typing import Type, List
from pydantic import conlist
from ..utils import PositiveIntegerType

HillKeyType: Type[List[List[int]]] = conlist(
    conlist(
        PositiveIntegerType,
        min_items=1
    ),
    min_items=1
)
