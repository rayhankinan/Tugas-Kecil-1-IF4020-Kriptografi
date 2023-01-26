from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from .dependencies import verify_api_key
from .exceptions import CryptoException

app = FastAPI(
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    dependencies=[Depends(verify_api_key)],
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


@app.exception_handler(CryptoException)
async def crypto_exception_handler(request: Request, exc: CryptoException):
    pass
