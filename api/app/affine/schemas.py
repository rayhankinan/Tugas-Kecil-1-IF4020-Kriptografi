import math
from fastapi import File, Form, UploadFile
from pydantic import BaseModel, validator
from ..utils import PositiveIntegerType
from ..constants import LENGTH_OF_ALPHABET


class AffineFileIn(BaseModel):
    key: PositiveIntegerType = Form()
    shift: PositiveIntegerType = Form()
    file: UploadFile = File()

    # TODO: Cek apakah key relative prime dengan jumlah alphabet
    @validator("key")
    def relative_prime_key(cls, key: PositiveIntegerType):
        if math.gcd(key, LENGTH_OF_ALPHABET) != 1:
            raise ValueError(
                "must be relative prime to the length of alphabet"
            )
        return key
