import numpy as np
import json
import math
from fastapi import File, Form, UploadFile
from pydantic import BaseModel, validator
from .utils import HillKeyType
from ..utils import AllStringType
from ..constants import LENGTH_OF_ALPHABET


class HillFileIn(BaseModel):
    key: AllStringType = Form()
    file: UploadFile = File()

    # TODO: Cek apakah matriks berbentuk kotak dan apakah matriks dapat diinvers
    @validator("key")
    def check_matrix(cls, key: AllStringType):
        json_key: HillKeyType = json.loads(key)
        matrix = np.array(json_key)
        determinant = round(np.linalg.det(matrix))

        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError(
                "must be a square matrix"
            )
        if determinant == 0:
            raise ValueError(
                "must be a non singular matrix"
            )
        if math.gcd(determinant, LENGTH_OF_ALPHABET) != 1:
            raise ValueError(
                "determinant must be relative prime to the length of alphabet"
            )
        return key
