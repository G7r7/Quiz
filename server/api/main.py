from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from src.database import SessionLocal, engine
import src.models as models
import src.schemas.user
import src.crud.user
import src.schemas.quiz
import src.crud.quiz

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=src.schemas.user.UserCreate)
def create_user(user: src.schemas.user.UserCreate, db: Session = Depends(get_db)):
    return src.crud.user.create_user(db=db, user=user)


@app.get("/users/list", response_model=List[src.schemas.user.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = src.crud.user.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=src.schemas.user.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = src.crud.user.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/quiz/{quiz_id}", response_model=src.schemas.quiz.Quiz)
def get_quiz(quiz_id: int, db: Session = Depends(get_db)):
    list_quiz = src.crud.quiz.get_quiz(db, quiz_id)
    return list_quiz

@app.get("/quiz/list/{user_id}", response_model=List[src.schemas.quiz.Quiz])
def get_quizs(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = src.crud.quiz.get_quizs(db, skip=skip, limit=limit, user_id=user_id)
    return items

@app.post("/quiz/", response_model=src.schemas.quiz.Quiz)
def create_quiz(quiz: src.schemas.quiz.QuizCreate, db: Session = Depends(get_db)):
    return src.crud.quiz.create_quiz(db=db, quiz=quiz)