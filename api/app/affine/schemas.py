import math
import asyncio
from typing import Any, Dict
from fastapi import File, Form, UploadFile
from pydantic import BaseModel, validator
from .utils import repeat_add
from ..utils import PositiveIntegerType
from ..constants import LENGTH_OF_ALPHABET


class AffineFileIn(BaseModel):
    group: PositiveIntegerType = Form()
    key: PositiveIntegerType = Form()
    shift: PositiveIntegerType = Form()
    file: UploadFile = File()

    # TODO: Cek apakah key relative prime dengan modulo
    @validator("key")
    def relative_prime_key(cls, key: PositiveIntegerType, values: Dict[str, Any]):
        modulo = asyncio.run(
            repeat_add(1, values["group"], LENGTH_OF_ALPHABET)
        )
        if math.gcd(key, modulo) != 1:
            raise ValueError(
                "must be relative prime to the modulo"
            )
        return key

    # TODO: Cek apakah key lebih kecil dari modulo
    @validator("shift")
    def smaller_than_modulo(cls, shift: PositiveIntegerType, values: Dict[str, Any]):
        modulo = asyncio.run(
            repeat_add(1, values["group"], LENGTH_OF_ALPHABET)
        )
        if shift > modulo:
            raise ValueError(
                "must be smaller than modulo"
            )
        return shift
