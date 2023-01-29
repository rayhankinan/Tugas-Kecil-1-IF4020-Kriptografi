from typing import Any, Dict
from fastapi import File, Form, UploadFile
from pydantic import BaseModel, validator
from .utils import AlphabetListType, PlugboardConnectionListType, RotorOrderListType


class EnigmaFileIn(BaseModel):
    rotor_order: RotorOrderListType = Form()
    notch_setting: AlphabetListType = Form()
    start_position: AlphabetListType = Form()
    list_of_plugboard: PlugboardConnectionListType = Form()
    file: UploadFile = File()

    # TODO: Cek apakah panjang list notch_setting dan start_position sama dengan panjang list rotor_order
    @validator("notch_setting")
    def same_length_notch_setting(cls, notch_setting: AlphabetListType, values: Dict[str, Any]):
        if len(notch_setting) != len(values["rotor_order"]):
            raise ValueError(
                "must be the same length as rotor_order"
            )
        return notch_setting

    @validator("start_position")
    def same_length_start_position(cls, start_position: AlphabetListType, values: Dict[str, Any]):
        if len(start_position) != len(values["rotor_order"]):
            raise ValueError(
                "must be the same length as rotor_order"
            )
        return start_position
