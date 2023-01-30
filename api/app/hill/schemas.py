import numpy as np
import json
from fastapi import File, Form, UploadFile
from pydantic import BaseModel, validator
from .utils import HillKeyType
from ..utils import AllStringType


class HillFileIn(BaseModel):
    key: AllStringType = Form()
    file: UploadFile = File()

    # TODO: Cek apakah matriks berbentuk kotak dan apakah matriks dapat diinvers
    @validator("key")
    def check_matrix(cls, key: AllStringType):
        json_key: HillKeyType = json.loads(key)
        matrix = np.array(json_key)

        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError(
                "must be a square matrix"
            )
        if np.linalg.det(matrix) == 0:
            raise ValueError(
                "must be a non singular matrix"
            )
        return key
