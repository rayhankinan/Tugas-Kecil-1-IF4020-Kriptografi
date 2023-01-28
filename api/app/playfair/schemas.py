from fastapi import File, Form, UploadFile
from pydantic import BaseModel, validator
from .utils import ConvertChar, PlayfairKeyType


class PlayfairFileIn(BaseModel):
    key: PlayfairKeyType = Form()
    convert_character: ConvertChar = Form()
    file: UploadFile = File()

    # TODO: Cek apakah seluruh karakter pada matriks unik
