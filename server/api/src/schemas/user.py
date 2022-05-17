from numpy import number
from pydantic import BaseModel

class UserBase(BaseModel):
    user_name: str

class UserCreate(UserBase):
    user_password: str

class User(UserBase):
    id: number

    class Config:
        orm_mode = True
