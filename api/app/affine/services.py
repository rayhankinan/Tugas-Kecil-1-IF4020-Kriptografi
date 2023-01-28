from fastapi import UploadFile
from .utils import AffineKeyType, AffineShiftType
from ..utils import apply_static_func_to_file


async def encrypt_file_service(key: AffineKeyType, shift: AffineShiftType, file: UploadFile):
    # TODO: Add Affine Encryption
    return apply_static_func_to_file(file, )


async def decrypt_file_service(key: AffineKeyType, shift: AffineShiftType, file: UploadFile):
    # TODO: Add Affine Decryption
    return apply_static_func_to_file(file, )
