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
        raw_matrix = key_matrix[0:len(binary)][0:len(binary)]

        byte_list: List[bytes] = list(
            unpack(f">{len(binary)}c", binary)
        )
        num_list: List[int] = []
        for byte in byte_list:
            num = await binary_to_num(byte)
            num_list.append(num)
        raw_vector = np.vstack(num_list)

        remove_overhead = np.vectorize(lambda x: x - OVERHEAD_ASCII)
        initial_matrix: np.ndarray = remove_overhead(raw_matrix)
        initial_vector: np.ndarray = remove_overhead(raw_vector)

        final_vector = initial_matrix @ initial_vector
        final_array = final_vector.transpose()

        modulo = np.vectorize(lambda x: x % LENGTH_OF_ALPHABET)
        final_modulo_array: np.ndarray = modulo(final_array)

        add_overhead = np.vectorize(lambda x: x + OVERHEAD_ASCII)
        result_array: np.ndarray = add_overhead(final_modulo_array)
        final_bytes = result_array.astype("uint8").tobytes()

        return final_bytes

    return apply_static_func_to_file(file, bytes_group=len(key), func=encrypt_bytes)


async def decrypt_file_service(key: AllStringType, file: UploadFile):
    # TODO: Add Hill Decryption (Not finished)
    json_key: HillKeyType = json.loads(key)
    key_matrix = np.array(json_key)

    async def decrypt_bytes(binary: AllByteType):
        raw_matrix = key_matrix[0:len(binary)][0:len(binary)]

        byte_list: List[bytes] = list(
            unpack(f">{len(binary)}c", binary)
        )
        num_list: List[int] = []
        for byte in byte_list:
            num = await binary_to_num(byte)
            num_list.append(num)
        raw_vector = np.vstack(num_list)

        remove_overhead = np.vectorize(lambda x: x - OVERHEAD_ASCII)
        initial_matrix: np.ndarray = remove_overhead(raw_matrix)
        initial_vector: np.ndarray = remove_overhead(raw_vector)

        determinant: float = np.linalg.det(initial_matrix)
        adjoint_matrix = determinant * np.linalg.inv(initial_matrix)
        inverse_modulo = np.vectorize(
            lambda x: pow(determinant, -1, LENGTH_OF_ALPHABET) * x
        )
        inverse_matrix: np.ndarray = inverse_modulo(adjoint_matrix)

        final_vector = inverse_matrix @ initial_vector
        final_array = final_vector.transpose()

        modulo = np.vectorize(lambda x: x % LENGTH_OF_ALPHABET)
        final_modulo_array: np.ndarray = modulo(final_array)

        add_overhead = np.vectorize(lambda x: x + OVERHEAD_ASCII)
        result_array: np.ndarray = add_overhead(final_modulo_array)
        final_bytes = result_array.astype("uint8").tobytes()

        return final_bytes

    return apply_static_func_to_file(file, bytes_group=len(key), func=decrypt_bytes)
