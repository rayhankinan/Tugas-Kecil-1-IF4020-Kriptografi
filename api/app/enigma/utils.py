from typing import NamedTuple
from pydantic import constr


class PlugboardConnection(NamedTuple):
    first_plug: constr(
        min_length=1,
        max_length=1,
        regex=r"^[A-Za-z]+$",
        to_lower=True
    )
    second_plug: constr(
        min_length=1,
        max_length=1,
        regex=r"^[A-Za-z]+$",
        to_lower=True
    )
