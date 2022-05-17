from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from ..database.get_db import get_db
from ..schemas import quiz as quizSchemas
from ..crud import quiz as quizCrud

router = APIRouter()

@router.get("/quiz/{quiz_id}", response_model=quizSchemas.Quiz)
def get_quiz(quiz_id: int, db: Session = Depends(get_db)):
    list_quiz = quizCrud.get_quiz(db, quiz_id)
    return list_quiz

@router.get("/quiz/list/{user_id}", response_model=List[quizSchemas.Quiz])
def get_quizs(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = quizCrud.get_quizs(db, skip=skip, limit=limit, user_id=user_id)
    return items

@router.post("/quiz/", response_model=quizSchemas.Quiz)
def create_quiz(quiz: quizSchemas.QuizCreate, db: Session = Depends(get_db)):
    return quizCrud.create_quiz(db=db, quiz=quiz)