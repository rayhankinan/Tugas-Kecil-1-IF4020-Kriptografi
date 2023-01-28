from typing import NamedTuple
from pydantic import constr, validator


class ConvertChar(NamedTuple):
    initial_char: constr(
        min_length=1,
        max_length=1,
        regex=r"^[A-Za-z]+$",
        to_lower=True
    )
    converted_char: constr(
        min_length=1,
        max_length=1,
        regex=r"^[A-Za-z]+$",
        to_lower=True
    )

    # TODO: Cek apakah initial_char berbeda dengan converted_char
