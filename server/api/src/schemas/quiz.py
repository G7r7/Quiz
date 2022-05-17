from typing import List, Union
from datetime import date
from pydantic import BaseModel
        
class QuizBase(BaseModel):
    name: str
    date_creation: date

class QuizCreate(QuizBase):
    user_id: int
    
class Quiz(QuizBase):
    id: str
    user_id: int
    
    class Config:
        orm_mode = True
        
