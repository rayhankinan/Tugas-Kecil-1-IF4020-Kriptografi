from fastapi import File, Form, UploadFile
from pydantic import BaseModel
from ..utils import AlphabetStringType


class VignereFileIn(BaseModel):
    key: AlphabetStringType = Form()
    file: UploadFile = File()
