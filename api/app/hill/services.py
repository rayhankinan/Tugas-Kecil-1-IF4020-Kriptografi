import numpy as np
import json
from struct import unpack
from typing import List
from fastapi import UploadFile
from .utils import HillKeyType
from ..utils import AllByteType, AllStringType, apply_static_func_to_file, binary_to_num
from ..constants import LENGTH_OF_ALPHABET, OVERHEAD_ASCII


async def encrypt_file_service(key: AllStringType, file: UploadFile):
    # TODO: Add Hill Encryption (Not finished)
    json_key: HillKeyType = json.loads(key)
    key_matrix = np.array(json_key)

    async def encrypt_bytes(binary: AllByteType):
        if len(binary) < len(json_key):
            return binary

        byte_list: List[bytes] = list(
            unpack(f">{len(json_key)}c", binary)
        )
        num_list: List[int] = []
        for byte in byte_list:
            num = await binary_to_num(byte)
            num_list.append(num)
        raw_vector = np.array(num_list)

        remove_overhead = np.vectorize(lambda x: round(x) - OVERHEAD_ASCII)
        initial_vector: np.ndarray = remove_overhead(raw_vector)

        final_vector: np.ndarray = np.matmul(key_matrix, initial_vector)

        modulo = np.vectorize(lambda x: round(x) % LENGTH_OF_ALPHABET)
        final_modulo_array: np.ndarray = modulo(final_vector)

        add_overhead = np.vectorize(lambda x: round(x) + OVERHEAD_ASCII)
        result_array: np.ndarray = add_overhead(final_modulo_array)
        final_bytes = result_array.astype("uint8").tobytes()

        return final_bytes

    return apply_static_func_to_file(file, bytes_group=len(json_key), func=encrypt_bytes)


async def decrypt_file_service(key: AllStringType, file: UploadFile):
    # TODO: Add Hill Decryption (Not finished)
    json_key: HillKeyType = json.loads(key)
    key_matrix = np.array(json_key)

    async def decrypt_bytes(binary: AllByteType):
        if len(binary) < len(json_key):
            return binary

        byte_list: List[bytes] = list(
            unpack(f">{len(json_key)}c", binary)
        )
        num_list: List[int] = []
        for byte in byte_list:
            num = await binary_to_num(byte)
            num_list.append(num)
        raw_vector = np.array(num_list)

        remove_overhead = np.vectorize(lambda x: round(x) - OVERHEAD_ASCII)
        initial_vector: np.ndarray = remove_overhead(raw_vector)

        determinant: float = np.linalg.det(key_matrix)
        adjoint_matrix = determinant * np.linalg.inv(key_matrix)
        inverse_modulo = np.vectorize(
            lambda x: pow(round(determinant), -1, LENGTH_OF_ALPHABET) * x
        )
        inverse_matrix: np.ndarray = inverse_modulo(adjoint_matrix)
        modulo = np.vectorize(lambda x: round(x) % LENGTH_OF_ALPHABET)
        inverse_modulo_matrix: np.ndarray = modulo(inverse_matrix)

        final_vector: np.ndarray = np.matmul(
            inverse_modulo_matrix,
            initial_vector
        )

        final_modulo_array: np.ndarray = modulo(final_vector)

        add_overhead = np.vectorize(lambda x: round(x) + OVERHEAD_ASCII)
        result_array: np.ndarray = add_overhead(final_modulo_array)
        final_bytes = result_array.astype("uint8").tobytes()

        return final_bytes

    return apply_static_func_to_file(file, bytes_group=len(json_key), func=decrypt_bytes)
