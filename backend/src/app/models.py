from fastapi import status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, validator, Field
from passlib.hash import bcrypt
from bson.objectid import ObjectId
from typing import Union


class AuthModel(BaseModel):
    username: str
    password: str


class User(AuthModel):
    id: ObjectId = Field(..., alias="_id")
    disabled: Union[bool, None] = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

    @validator("id")
    @classmethod
    def id_validator(cls, v) -> str:
        if not ObjectId.is_valid(v):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"message": "ObjectId invalid"},
            )
        return str(v)


class RegisterModel(AuthModel):
    @validator("password")
    @classmethod
    def password_validator(cls, v):
        if len(v) < 8:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"messaeg": "The password is too weak"},
            )
        # TODO: other security checks here
        return bcrypt.using(rounds=10).hash(v)


class LoginModel(AuthModel):
    pass


class SearchModel(BaseModel):
    class Config:
        orm_mode = True


class FindOneUsernameModel(SearchModel):
    username: str


class FindOneUserModel(SearchModel):
    user: str

    def __str__(self) -> str:
        return self.user


class TokenData(BaseModel):
    username: Union[str, None] = None


class Token(BaseModel):
    access_token: Union[str, None]
    token_type: Union[str, None]
