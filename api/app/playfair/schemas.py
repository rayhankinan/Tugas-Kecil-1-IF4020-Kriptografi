from fastapi import File, Form, UploadFile
from pydantic import BaseModel, conlist, constr, validator
from .constants import MATRIX_DIMENSION
from .utils import ConvertChar


class PlayfairFileIn(BaseModel):
    key: conlist(
        conlist(
            constr(
                min_length=1,
                max_length=1,
                regex=r"^[A-Za-z]+$",
                to_lower=True
            ),
            min_items=MATRIX_DIMENSION,
            max_items=MATRIX_DIMENSION
        ),
        min_items=MATRIX_DIMENSION,
        max_items=MATRIX_DIMENSION
    ) = Form()
    convert_character: ConvertChar = Form()
    file: UploadFile = File()

    # TODO: Cek apakah seluruh karakter pada matriks unik
