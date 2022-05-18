from typing import Union
from sqlalchemy.orm import Session
from .. import models 
from ..schemas import question as questionSchemas

def get_questions(db: Session, quiz_id: int):
    return db.query(models.Question).filter(models.Question.quiz_id == quiz_id).order_by(models.Question.number_question.desc())
