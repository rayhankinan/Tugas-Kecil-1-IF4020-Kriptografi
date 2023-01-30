from fastapi import FastAPI, Depends, Request
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import request_validation_exception_handler
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from pydantic import ValidationError
from .dependencies import verify_api_key
from .vigenere.router import vigenere_router
from .extended_vigenere.router import extended_vigenere_router
from .auto_key_vigenere.router import auto_key_vigenere_router
from .affine.router import affine_router
from .hill.router import hill_router
from .playfair.router import playfair_router
from .enigma.router import enigma_router

app = FastAPI(
    title="API Tucil 1 Kripto",
    root_path="/api"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.add_middleware(
    GZipMiddleware,
    minimum_size=1000
)

app.include_router(
    vigenere_router,
    dependencies=[Depends(verify_api_key)]
)

app.include_router(
    extended_vigenere_router,
    dependencies=[Depends(verify_api_key)]
)

app.include_router(
    auto_key_vigenere_router,
    dependencies=[Depends(verify_api_key)]
)

app.include_router(
    affine_router,
    dependencies=[Depends(verify_api_key)]
)

app.include_router(
    hill_router,
    dependencies=[Depends(verify_api_key)]
)

app.include_router(
    playfair_router,
    dependencies=[Depends(verify_api_key)]
)

app.include_router(
    enigma_router,
    dependencies=[Depends(verify_api_key)]
)


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return await request_validation_exception_handler(request, exc)
