from typing import Type
from pydantic import conint

AffineKey: Type[int] = conint(gt=0)
AffineShift: Type[int] = conint(gt=0)
