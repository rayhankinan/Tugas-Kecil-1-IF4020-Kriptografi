from fastapi import File, Form, UploadFile
from pydantic import BaseModel


class AutoKeyVignereFileIn(BaseModel):
    auto_key: str = Form(regex=r"^[A-Za-z]+$")
    file: UploadFile = File()
