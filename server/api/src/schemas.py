from typing import List, Union
from datetime import date

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
        
class QuizBase(BaseModel):
    
    name: str
    date_creation: date
    
class Quiz(QuizBase):
    id: str
    user_id: str
    
    class Config:
        orm_mode = True
        
