from typing import List, Union
from datetime import date
from numpy import number
from pydantic import BaseModel

class InvitationBase(BaseModel):
    url: str

class InvitationCreate(InvitationBase):
    quiz_id: int

class Invitation(InvitationBase):
    id: int
    quiz_id: int

    class Config:
        orm_mode = True
