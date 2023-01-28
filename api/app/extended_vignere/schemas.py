from fastapi import File, Form, UploadFile
from pydantic import BaseModel, conbytes


class ExtendedVignereFileIn(BaseModel):
    key: conbytes(strip_whitespace=True, to_lower=True) = Form()
    file: UploadFile = File()
