from uuid import UUID
from pydantic import BaseModel
from passlib.hash import bcrypt

class User(BaseModel):
    id:UUID
    username:str
    password_hash:str

    @property
    def password(self) -> str:
        return getattr(self, 'password_hash', None)

    @password.setter
    def password(self, new_password:str) -> None:
        password_hash = bcrypt.using(rounds=10).hash(new_password)
        setattr(self, 'password_hash', password_hash)
