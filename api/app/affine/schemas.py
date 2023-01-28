from fastapi import File, Form, UploadFile
from pydantic import BaseModel
from .utils import AffineKey, AffineShift


class AffineFileIn(BaseModel):
    key: AffineKey = Form()
    shift: AffineShift = Form()
    file: UploadFile = File()
