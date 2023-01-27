from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from .dependencies import verify_api_key
from .exceptions import CryptoException
from .vignere.router import vignere_router
from .extended_vignere.router import extended_vignere_router
from .auto_key_vignere.router import auto_key_vignere_router
from .affine.router import affine_router

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
    vignere_router,
    dependencies=[Depends(verify_api_key)]
)

app.include_router(
    extended_vignere_router,
    dependencies=[Depends(verify_api_key)]
)

app.include_router(
    auto_key_vignere_router,
    dependencies=[Depends(verify_api_key)]
)

app.include_router(
    affine_router,
    dependencies=[Depends(verify_api_key)]
)


@app.exception_handler(CryptoException)
async def crypto_exception_handler(request: Request, exc: CryptoException):
    pass
