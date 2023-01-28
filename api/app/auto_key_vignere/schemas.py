from fastapi import File, Form, UploadFile
from pydantic import BaseModel, constr


class AutoKeyVignereFileIn(BaseModel):
    auto_key: constr(regex=r"^[A-Za-z]+$", to_lower=True) = Form()
    file: UploadFile = File()
