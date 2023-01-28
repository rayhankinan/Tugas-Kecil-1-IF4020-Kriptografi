from fastapi import File, Form, UploadFile
from pydantic import BaseModel
from .utils import VignereAutoKeyType


class AutoKeyVignereFileIn(BaseModel):
    auto_key: VignereAutoKeyType = Form()
    file: UploadFile = File()
