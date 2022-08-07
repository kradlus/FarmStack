from fastapi import FastAPI
from routers import home

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(home.router)
    return app