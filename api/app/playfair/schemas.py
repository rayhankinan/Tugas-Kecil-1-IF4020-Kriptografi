from typing import List
from fastapi import File, Form, UploadFile
from pydantic import BaseModel


class PlayfairFileIn(BaseModel):
    key: List[List[str]] = Form()
    file: UploadFile = File()
