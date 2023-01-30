import numpy as np
import json
from struct import unpack
from typing import List
from fastapi import UploadFile
from .utils import HillKeyType
from ..utils import AllStringType, apply_static_func_to_file
from ..constants import LENGTH_OF_ALPHABET, OVERHEAD_ASCII


async def encrypt_file_service(key: AllStringType, file: UploadFile):
    # TODO: Add Hill Encryption (Done)
    json_key: HillKeyType = json.loads(key)
    key_matrix = np.array(json_key)

    async def encrypt_bytes(values: List[int]):
        raw_vector = np.array(values)
        add_overhead = np.vectorize(lambda x: round(x) + OVERHEAD_ASCII)
        final_bytes: bytes

        if raw_vector.size < len(json_key):
            result_array: np.ndarray = add_overhead(raw_vector)
            final_bytes = result_array.astype("uint8").tobytes()
        else:
            final_vector: np.ndarray = np.matmul(key_matrix, raw_vector)

            modulo = np.vectorize(lambda x: round(x) % LENGTH_OF_ALPHABET)
            final_modulo_array: np.ndarray = modulo(final_vector)

            result_array: np.ndarray = add_overhead(final_modulo_array)
            final_bytes = result_array.astype("uint8").tobytes()

        return final_bytes

    return apply_static_func_to_file(file, bytes_group=len(json_key), func=encrypt_bytes)


async def decrypt_file_service(key: AllStringType, file: UploadFile):
    # TODO: Add Hill Decryption (Done)
    json_key: HillKeyType = json.loads(key)
    key_matrix = np.array(json_key)

    async def decrypt_bytes(values: List[int]):
        raw_vector = np.array(values)
        add_overhead = np.vectorize(lambda x: round(x) + OVERHEAD_ASCII)
        final_bytes: bytes

        if raw_vector.size < len(json_key):
            result_array: np.ndarray = add_overhead(raw_vector)
            final_bytes = result_array.astype("uint8").tobytes()
        else:
            determinant: float = np.linalg.det(key_matrix)
            adjoint_matrix = determinant * np.linalg.inv(key_matrix)
            inverse_determinant: int = pow(
                round(determinant),
                -1,
                LENGTH_OF_ALPHABET
            )
            inverse_modulo = np.vectorize(lambda x: inverse_determinant * x)
            inverse_matrix: np.ndarray = inverse_modulo(adjoint_matrix)

            final_vector: np.ndarray = np.matmul(inverse_matrix, raw_vector)

            modulo = np.vectorize(lambda x: round(x) % LENGTH_OF_ALPHABET)
            final_modulo_array: np.ndarray = modulo(final_vector)

            add_overhead = np.vectorize(lambda x: round(x) + OVERHEAD_ASCII)
            result_array: np.ndarray = add_overhead(final_modulo_array)
            final_bytes = result_array.astype("uint8").tobytes()

        return final_bytes

    return apply_static_func_to_file(file, bytes_group=len(json_key), func=decrypt_bytes)
