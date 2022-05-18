from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from ..database.get_db import get_db
from ..schemas import question as questionSchemas
from ..crud import question as questionCrud

router = APIRouter()

@router.get("/question/list/{quiz_id}", response_model=List[questionSchemas.Question])
def get_questions(quiz_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = questionCrud.get_questions(db, skip=skip, limit=limit, quiz_id=quiz_id)
    return items

@router.post("/question/", response_model=questionSchemas.Question)
def create_question(question: questionSchemas.QuestionCreate, db: Session = Depends(get_db)):
    return questionCrud.create_question(db=db, question=question)