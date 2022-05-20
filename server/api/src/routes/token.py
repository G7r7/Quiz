from typing import List
from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from src.schemas.user import UserLogin
from ..database.get_db import get_db
from src.utils.oauth2 import log_user
from ..utils.quiz import Quiz
from ..utils.token import Token
from ..utils.constant import mem_quiz
from ..utils.oauth2 import Token as TokenModel
from ..crud import quiz as quizCrud
from ..database.get_db import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/token")
def generate_token(user_id: int,quiz_id: int, n:int = 32, m:int = 5, db: Session = Depends(get_db)):
    
    admin_token = Token(n)
    player_token = Token(m)
    
    list_quiz = quizCrud.get_quiz(db, quiz_id)

    
    quiz = Quiz(user_id, quiz_id, admin_token, player_token, name=list_quiz.quiz_name)
    
    mem_quiz[(user_id, quiz_id)] = quiz
    
    return {"user_id": user_id,
            "quiz_id": quiz_id,
            "quiz_name": quiz.name,
            "player_token": player_token.get_token(),
            "admin_token": admin_token.get_token()}


@router.post("/tokenGen", response_model=TokenModel)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db = Depends(get_db) ):
    response = log_user(UserLogin(user_name=form_data.username, user_password=form_data.password), db=db)
    return {"access_token": response.user_token, "token_type": "bearer"}