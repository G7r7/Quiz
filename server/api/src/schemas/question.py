from typing import List, Union
from datetime import date
from numpy import number
from pydantic import BaseModel

class QuestionBase(BaseModel):
    number_question: int
    content: str

class QuestionCreate(QuestionBase):
    quiz_id: int

class Question(QuestionBase):
    id: int
    quiz_id: int

    class Config:
        orm_mode = True
