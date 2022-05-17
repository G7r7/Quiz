from typing import List, Union
from datetime import date
from pydantic import BaseModel

class ResponseBase(BaseModel):
    content: str
    is_true: bool

class ResponseCreate(ResponseBase):
    question_id: int

class Response(ResponseBase):
    id: int
    question_id: int

    class Config:
        orm_mode = True
