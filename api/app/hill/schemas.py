from typing import List
from fastapi import File, Form, UploadFile
from pydantic import BaseModel


class HillFileIn(BaseModel):
    key: List[List[int]] = Form()
    file: UploadFile = File()
