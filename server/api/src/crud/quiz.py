from typing import Union
from sqlalchemy.orm import Session
from .. import models 
from ..schemas import quiz as quizSchemas

def get_quiz(db: Session, quiz_id: int):
    return db.query(models.Quiz).filter(models.Quiz.id == quiz_id).first()

def get_quizs(db: Session, skip: int = 0, limit: int = 100, user_id: Union[int, None] = None):
    return db.query(models.Quiz).offset(skip).limit(limit).all().where(models.User.id == user_id)

def create_quiz(db: Session, quiz: quizSchemas.QuizCreate):
    db_quiz = models.Quiz(quiz_name = quiz.name, user_id = quiz.user_id, date_creation = quiz.date_creation)
    db.add(db_quiz)
    db.commit()
    db.refresh(db_quiz)
    return db_quiz