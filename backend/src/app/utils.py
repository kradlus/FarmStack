import secrets
from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from typing import Optional, Union
from passlib.hash import bcrypt
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta

from app.database import db_find_one
from app.models import FindOneModel, User, TokenData


SECRET_KEY = str(secrets.token_hex(16))
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def authenticate_user(username:str, hashed_password:str) -> Union[bool, User]:
    model = await db_find_one(FindOneModel(username=username))
    user:Optional[User] = None if not model else User(**model)
    if not user or not bcrypt.verify(hashed_password, user.password):
        return False
    return user

async def get_current_user(token:str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate":"Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        username:str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError as e:
        print(str(e))
        raise credentials_exception
    user = await db_find_one(FindOneModel(username=token_data.username))
    if not user:
        raise credentials_exception
    return User(**user)

async def get_current_active_user(current_user:User = Depends(get_current_user)) -> User:
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt