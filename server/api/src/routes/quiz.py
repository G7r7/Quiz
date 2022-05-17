from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from main import get_db, app
import schemas.quiz
import crud.quiz

router = APIRouter()

@router.get("/quiz/{quiz_id}", response_model=schemas.quiz.Quiz)
def get_quiz(quiz_id: int, db: Session = Depends(get_db)):
    list_quiz = crud.quiz.get_quiz(db, quiz_id)
    return list_quiz

@router.get("/quiz/list/{user_id}", response_model=List[schemas.quiz.Quiz])
def get_quizs(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.quiz.get_quizs(db, skip=skip, limit=limit, user_id=user_id)
    return items

@router.post("/quiz/", response_model=schemas.quiz.Quiz)
def create_quiz(quiz: schemas.quiz.QuizCreate, db: Session = Depends(get_db)):
    return crud.quiz.create_quiz(db=db, quiz=quiz)