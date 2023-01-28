from fastapi import File, Form, UploadFile
from pydantic import BaseModel
from ..utils import PositiveIntegerType


class AffineFileIn(BaseModel):
    key: PositiveIntegerType = Form()
    shift: PositiveIntegerType = Form()
    file: UploadFile = File()
