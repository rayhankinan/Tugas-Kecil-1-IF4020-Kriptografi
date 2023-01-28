from fastapi import File, Form, UploadFile
from pydantic import BaseModel, validator
from .utils import HillKey


class HillFileIn(BaseModel):
    key: HillKey = Form()
    file: UploadFile = File()

    # TODO: Cek apakah matriks kotak dan apakah matriks dapat diinvers
