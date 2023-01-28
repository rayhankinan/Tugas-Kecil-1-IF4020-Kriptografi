from typing import Type
from pydantic import conint

AffineKeyType: Type[int] = conint(gt=0)
AffineShiftType: Type[int] = conint(gt=0)
