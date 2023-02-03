from fastapi import UploadFile
from .utils import RotorOrderListType, AlphabetListType, PlugboardConnectionListType
from ..utils import apply_dynamic_func_to_file, AllStringType


async def encrypt_file_service(rotor_order: RotorOrderListType, notch_setting: AlphabetListType, start_position: AlphabetListType, list_of_plugboard: AllStringType, file: UploadFile):
    # TODO: Add Enigma Encryption
    return apply_dynamic_func_to_file(file, )


async def decrypt_file_service(rotor_order: RotorOrderListType, notch_setting: AlphabetListType, start_position: AlphabetListType, list_of_plugboard: AllStringType, file: UploadFile):
    # TODO: Add Enigma Decryption
    return apply_dynamic_func_to_file(file, )
