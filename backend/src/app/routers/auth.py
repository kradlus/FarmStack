from fastapi import APIRouter, status, Body
from fastapi.responses import JSONResponse

from app.models import LoginModel, RegisterModel

router:APIRouter = APIRouter(prefix="/auth")

@router.get("/login")
async def auth_login() -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_200_OK, content={
        "message":"Provide username and password"
    })

@router.post("/register")
async def auth_register(auth:RegisterModel = Body()) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={
        "message":f"User {auth.username} created!"
    })

@router.post("/login")
async def auth_login(auth:LoginModel = Body()) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_200_OK, content={
        "message":f"Logged In!",
        "token":"" # Implement
    })