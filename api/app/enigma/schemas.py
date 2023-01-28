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
