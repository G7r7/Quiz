from typing import Union
from sqlalchemy.orm import Session
from .. import models 
from ..schemas import response as responseSchemas

def get_responses(db: Session, question_id: int):
    return db.query(models.Response).filter(models.Response.question_id == question_id)
