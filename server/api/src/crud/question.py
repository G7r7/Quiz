from typing import Union
from sqlalchemy.orm import Session
from .. import models 
from ..schemas import question as questionSchemas

def create_question(db: Session, question: questionSchemas.QuestionCreate):
    db_question = models.Question(content = question.content, quiz_id = question.quiz_id, number_question = question.number_question)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    response: questionSchemas.Question = questionSchemas.Question(id=db_question.id, content=db_question.content, quiz_id=db_question.quiz_id, number_question=db_question.number_question)
    return response
def get_questions(db: Session, quiz_id: int):
    return db.query(models.Question).filter(models.Question.quiz_id == quiz_id).order_by(models.Question.number_question.desc())
