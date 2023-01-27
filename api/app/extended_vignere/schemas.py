from fastapi import File, Form, UploadFile
from pydantic import BaseModel


class ExtendedVignereFileIn(BaseModel):
    key: bytes = Form()
    file: UploadFile = File()
