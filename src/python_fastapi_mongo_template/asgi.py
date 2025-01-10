from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from .router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


asgi = FastAPI(lifespan=lifespan)
asgi.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
asgi.include_router(router)


@asgi.exception_handler(HTTPException)
def _(request: Request, exc: HTTPException):
    return JSONResponse({"message": exc.detail, "details": repr(exc)}, exc.status_code)


@asgi.exception_handler(ValidationError)
def _(request: Request, exc: ValidationError):
    return JSONResponse(
        {
            "message": "Validation failed",
            "details": repr(exc.errors(include_url=False)),
        },
        422,
    )


@asgi.exception_handler(Exception)
def _(request: Request, exc: Exception):
    return JSONResponse(
        {"message": "An unexpected error has ocurred", "details": repr(exc)},
        500,
    )
