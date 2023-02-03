import json
from typing import Any, Dict, Set
from fastapi import File, Form, UploadFile
from pydantic import BaseModel, validator
from .utils import AlphabetListType, PlugboardConnectionListType, RotorOrderListType
from ..utils import AllStringType, AlphabetCharType


class EnigmaFileIn(BaseModel):
    rotor_order: RotorOrderListType = Form()
    notch_setting: AlphabetListType = Form()
    start_position: AlphabetListType = Form()
    # TODO: Migrate ini menjadi tipe json string
    list_of_plugboard: AllStringType = Form()
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

    @validator("list_of_plugboard")
    def parseable_plugboard(cls, list_of_plugboard: AllStringType):
        json_key: PlugboardConnectionListType = json.loads(list_of_plugboard)
        set_of_alphabet: Set[AlphabetCharType] = {}

        for connection in json_key:
            if connection.first_plug in set_of_alphabet:
                raise ValueError(
                    "plug only can be assigned once"
                )
            set_of_alphabet.add(connection.first_plug)

            if connection.second_plug in set_of_alphabet:
                raise ValueError(
                    "plug only can be assigned once"
                )
            set_of_alphabet.add(connection.second_plug)
