from fastapi import File, Form, UploadFile
from pydantic import BaseModel
from .utils import AffineKeyType, AffineShiftType


class AffineFileIn(BaseModel):
    key: AffineKeyType = Form()
    shift: AffineShiftType = Form()
    file: UploadFile = File()
