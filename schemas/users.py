from pydantic import BaseModel
from pydantic import EmailStr
from typing import Optional


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class Profile(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True


class Follow_Schema(BaseModel):
    following_id: int

    class Config:
        orm_mode = True


class ShowFollow(BaseModel):
    following_id: int
    follower_id: int

    class Config:
        orm_mode = True
