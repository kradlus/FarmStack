from fastapi import APIRouter, status, Body
from fastapi.responses import JSONResponse

from app.models import RegisterModel

router:APIRouter = APIRouter(prefix="/auth")

@router.get("/login")
async def auth_login():
    return JSONResponse(status_code=status.HTTP_200_OK, content={
        "message":"Provide username and password"
    })

@router.post("/register")
async def auth_login(auth:RegisterModel = Body()):
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={
        "message":f"User {auth.username} created!"
    })