from fastapi import APIRouter, status, Body, Depends
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

from app.models import Token, RegisterModel, User
from app.database import DBManager
from app.utils import authenticate_user, create_access_token, get_db_creds

db = DBManager(get_db_creds())
router:APIRouter = APIRouter(prefix="/auth")

@router.post("/register")
async def auth_register(auth:RegisterModel = Body()) -> JSONResponse:
    await db.db_insert_one(auth)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={
        "message":f"User {auth.username} created!"
    })

@router.post("/login", response_model=Token)
async def auth_login(form_data: OAuth2PasswordRequestForm = Depends()) -> JSONResponse:    
    user:User = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message":"Invalid username or password"}
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return JSONResponse(status_code=status.HTTP_200_OK, content={
        "token":access_token, "token_type":"bearer"
    })
