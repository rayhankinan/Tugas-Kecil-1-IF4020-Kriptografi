from fastapi import File, Form, UploadFile
from pydantic import BaseModel


class AffineFileIn(BaseModel):
    key: int = Form(gt=0)
    shift: int = Form(gt=0)
    file: UploadFile = File()
