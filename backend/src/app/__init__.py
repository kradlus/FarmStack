from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import home
from app.routers import auth


def create_app() -> FastAPI:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000",
            "http://127.0.0.1:3000"
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    app.include_router(home.router)
    app.include_router(auth.router)
    return app