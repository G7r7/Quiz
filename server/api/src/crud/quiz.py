from sqlalchemy.orm import Session
from .. import models 
from ..schemas import quiz as quizSchemas

def get_quiz(db: Session, quiz_id: int):
    return db.query(models.Quiz).filter(models.Quiz.id == quiz_id).first()

def get_all_quizs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Quiz).offset(skip).limit(limit).all()

def get_quizs(db: Session, user_id: int):
    return db.query(models.Quiz).all().where(models.User.id == user_id)

def create_quiz(db: Session, quiz: quizSchemas.QuizCreate):
    db_quiz = models.Quiz(quiz_name = quiz.name, user_id = quiz.user_id, date_creation = quiz.date_creation)
    db.add(db_quiz)
    db.commit()
    db.refresh(db_quiz)
    return db_quiz