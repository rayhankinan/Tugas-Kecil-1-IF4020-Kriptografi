from fastapi import File, Form, UploadFile
from pydantic import BaseModel
from ..utils import BinaryText


class ExtendedVignereFileIn(BaseModel):
    key: BinaryText = Form()
    file: UploadFile = File()
