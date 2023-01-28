from fastapi import File, Form, UploadFile
from pydantic import BaseModel, constr


class VignereFileIn(BaseModel):
    key: constr(regex=r"^[A-Za-z]+$") = Form()
    file: UploadFile = File()
