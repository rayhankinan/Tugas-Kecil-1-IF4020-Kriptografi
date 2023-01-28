from typing import Type
from pydantic import constr

VignereAutoKeyType: Type[str] = constr(regex=r"^[A-Za-z]+$", to_lower=True)
