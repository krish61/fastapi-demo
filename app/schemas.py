from app.database import Base
from typing import List, Optional
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str


class UserSchema(BaseModel):
    name:str=...
    email:str
    password:str

class ShowUsers(BaseModel):
    name:str
    email:str

    class Config:
        orm_mode = True

class Login(BaseModel):
    email:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None

class ShowBlog(Blog):
    user_id:Optional[int]=None
    created_by=ShowUsers
    class Config:
        orm_mode = True
