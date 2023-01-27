from fastapi import File, Form, UploadFile
from pydantic import BaseModel


class VignereFileIn(BaseModel):
    key: str = Form(regex=r"^[A-Za-z]+$")
    file: UploadFile = File()
