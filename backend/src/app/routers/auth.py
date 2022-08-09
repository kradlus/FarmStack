from fastapi import APIRouter, status, Body
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from app.models import LoginModel, RegisterModel, FindOneModel, User
from app.database import db_insert_one, db_find_one
from passlib.hash import bcrypt
from typing import Optional

router:APIRouter = APIRouter(prefix="/auth")

@router.post("/register")
async def auth_register(auth:RegisterModel = Body()) -> JSONResponse:
    await db_insert_one(auth)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={
        "message":f"User {auth.username} created!"
    })

@router.post("/login")
async def auth_login(auth:LoginModel = Body()) -> JSONResponse:
    model = await db_find_one(FindOneModel.from_orm(auth))
    user:Optional[User] = None if not model else User(**model)
    if not user or not bcrypt.verify(auth.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message":"Invalid username or password"}
        )
    return JSONResponse(status_code=status.HTTP_200_OK, content={
        "token":"" # Implement
    })
