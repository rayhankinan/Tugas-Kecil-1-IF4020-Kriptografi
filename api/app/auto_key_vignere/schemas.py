from fastapi import File, Form, UploadFile
from pydantic import BaseModel
from ..utils import AlphabetStringType


class AutoKeyVignereFileIn(BaseModel):
    auto_key: AlphabetStringType = Form()
    file: UploadFile = File()
