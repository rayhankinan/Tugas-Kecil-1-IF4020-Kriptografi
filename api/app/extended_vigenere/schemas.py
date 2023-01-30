from fastapi import File, Form, UploadFile
from pydantic import BaseModel
from ..utils import AllStringType


class ExtendedVigenereFileIn(BaseModel):
    key: AllStringType = Form()
    file: UploadFile = File()
