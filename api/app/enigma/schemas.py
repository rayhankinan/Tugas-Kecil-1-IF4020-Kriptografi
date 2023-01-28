from fastapi import File, Form, UploadFile
from pydantic import BaseModel, conint, conlist, constr, validator
from .constants import NUM_OF_ROTORS
from .utils import PlugboardConnection


class EnigmaFileIn(BaseModel):
    rotor_order: conlist(
        conint(
            ge=0,
            lt=NUM_OF_ROTORS
        ),
        min_items=1,
        max_items=NUM_OF_ROTORS,
        unique_items=True
    ) = Form()
    notch_setting: conlist(
        constr(
            min_length=1,
            max_length=1,
            regex=r"^[A-Za-z]+$",
            to_lower=True
        ),
        min_items=1,
        max_items=NUM_OF_ROTORS
    ) = Form()
    start_position: conlist(
        constr(
            min_length=1,
            max_length=1,
            regex=r"^[A-Za-z]+$",
            to_lower=True
        ),
        min_items=1,
        max_items=NUM_OF_ROTORS
    ) = Form()
    plugboard: conlist(PlugboardConnection, unique_items=True) = Form()
    file: UploadFile = File()

    # TODO: Cek apakah panjang list notch_setting dan start_position sama dengan panjang list rotor_order
