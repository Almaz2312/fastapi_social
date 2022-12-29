from pydantic import BaseModel
from pydantic import EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class Profile(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True


class Follow_Schema(BaseModel):
    following_id: int

    class Config:
        orm_mode = True
