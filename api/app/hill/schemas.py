import numpy as np
from fastapi import File, Form, UploadFile
from pydantic import BaseModel, validator
from .utils import HillKeyType


class HillFileIn(BaseModel):
    key: HillKeyType = Form()
    file: UploadFile = File()

    # TODO: Cek apakah matriks berbentuk kotak dan apakah matriks dapat diinvers
    @validator("key")
    def check_matrix(cls, key: HillKeyType):
        matrix = np.array(key)
        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError(
                "must be a square matrix"
            )
        if np.linalg.det(matrix) == 0:
            raise ValueError(
                "must be a non singular matrix"
            )
        return key
