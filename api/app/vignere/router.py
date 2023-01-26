from fastapi import APIRouter, Depends, Form
from .schemas import VignereIn, VignereOut
from .services import encrypt_service, decrypt_service

router = APIRouter(
    prefix="/vignere",
    tags=["vignere"]
)


@router.post("/encrypt", response_model=VignereOut)
async def encrypt_handler(vignere_in: VignereIn = Depends()):
    result = await encrypt_service(vignere_in)
    return result


@router.post("/decrypt", response_model=VignereOut)
async def decrypt_handler(vignere_in: VignereIn = Depends()):
    result = await decrypt_service(vignere_in)
    return result
