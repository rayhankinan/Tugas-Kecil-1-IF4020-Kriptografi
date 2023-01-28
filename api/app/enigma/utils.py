from typing import List,  NamedTuple, Type
from pydantic import conint, conlist, validator
from .constants import NUM_OF_ROTORS
from ..utils import AlphabetCharType


class PlugboardConnection(NamedTuple):
    first_plug: AlphabetCharType
    second_plug: AlphabetCharType

    # TODO: Cek apakah first_plug tidak sama dengan second_plug


AlphabetListType: Type[List[str]] = conlist(
    AlphabetCharType,
    min_items=1,
    max_items=NUM_OF_ROTORS
)
RotorOrderListType: Type[List[int]] = conlist(
    conint(
        ge=0,
        lt=NUM_OF_ROTORS
    ),
    min_items=1,
    max_items=NUM_OF_ROTORS,
    unique_items=True
)
PlugboardConnectionListType: Type[List[PlugboardConnection]] = conlist(
    PlugboardConnection,
    unique_items=True
)
