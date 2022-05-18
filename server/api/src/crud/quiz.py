from typing import Union
from fastapi import Header
from sqlalchemy.orm import Session
from .. import models 
from ..schemas import quiz as quizSchemas
from ..utils import oauth2

def get_quiz(db: Session, quiz_id: int):
    return db.query(models.Quiz).filter(models.Quiz.id == quiz_id).first()

def get_quizs(db: Session, skip: int = 0, limit: int = 100, user_id: Union[int, None] = None):
    return db.query(models.Quiz).where(models.User.id == user_id).all()

def create_quiz(db: Session, quiz: quizSchemas.QuizCreate):
    db_quiz = models.Quiz(quiz_name = quiz.quiz_name, user_id = quiz.user_id, date_creation = quiz.date_creation)
    db.add(db_quiz)
    db.commit()
    db.refresh(db_quiz)
    response: quizSchemas.Quiz = quizSchemas.Quiz(id=db_quiz.id, quiz_name=db_quiz.quiz_name, user_id=db_quiz.user_id, date_creation=db_quiz.date_creation)
    return response