from fastapi import File, Form, UploadFile
from pydantic import BaseModel, validator
from .utils import HillKeyType


class HillFileIn(BaseModel):
    key: HillKeyType = Form()
    file: UploadFile = File()

    # TODO: Cek apakah matriks kotak dan apakah matriks dapat diinvers
