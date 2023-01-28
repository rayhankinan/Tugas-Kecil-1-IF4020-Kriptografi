from fastapi import File, Form, UploadFile
from pydantic import BaseModel, validator
from ..utils import PositiveIntegerType


class AffineFileIn(BaseModel):
    key: PositiveIntegerType = Form()
    shift: PositiveIntegerType = Form()
    file: UploadFile = File()

    # TODO: Cek apakah key relative prime dengan jumlah alfabet
