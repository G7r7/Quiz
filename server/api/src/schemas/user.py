from pydantic import BaseModel

class UserBase(BaseModel):
    user_name: str

class UserCreate(UserBase):
    user_password: str

class UserLogin(UserBase):
    user_password: str

class UserLogged(UserBase):
    user_token: str
    id: int

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
