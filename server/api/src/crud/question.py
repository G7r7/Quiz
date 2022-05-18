from typing import Union
from sqlalchemy.orm import Session
from .. import models 
from ..schemas import question as questionSchemas

# def get_quiz(db: Session, quiz_id: int):
#     return db.query(models.Quiz).filter(models.Quiz.id == quiz_id).first()

def get_questions(db: Session, skip: int = 0, limit: int = 100, quiz_id: Union[int, None] = None):
    return db.query(models.Question).where(models.Quiz.id == quiz_id).all()

def create_question(db: Session, question: questionSchemas.QuestionCreate):
    db_question = models.Question(content = question.content, quiz_id = question.quiz_id, number_question = question.number_question)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    response: questionSchemas.Question = questionSchemas.Question(id=db_question.id, content=db_question.content, quiz_id=db_question.quiz_id, number_question=db_question.number_question)
    return response