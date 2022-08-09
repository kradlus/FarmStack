from uuid import UUID
from fastapi import status
from fastapi.exceptions import HTTPException 
from pydantic import BaseModel, validator
from passlib.hash import bcrypt

class User(BaseModel):
    id:UUID
    username:str
    password:str

class AuthModel(BaseModel):
    username:str
    password:str

class RegisterModel(AuthModel):
    @validator("password")
    @classmethod
    def password_validator(cls, v):
        if len(v) < 8:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"messaeg":"The password is too weak"}
            )
        # TODO: other security checks here
        return bcrypt.using(rounds=10).hash(v)

class LoginModel(AuthModel):
    pass