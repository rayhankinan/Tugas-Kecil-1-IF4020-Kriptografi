from typing import Type, List
from pydantic import conint, conlist

HillKey: Type[List[List[int]]] = conlist(
    conlist(
        conint(ge=0),
        min_items=1
    ),
    min_items=1
)
