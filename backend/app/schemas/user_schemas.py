from pydantic import BaseModel
from typing import Optional

class UserInDB(BaseModel):
    username: str
    hashed_password: str

class User(BaseModel):
    username: str

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class ChangePassword(BaseModel):
    username: str
    old_password: str
    new_password: str

class LoginData(BaseModel):
    username: str
    password: str