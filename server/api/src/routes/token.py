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

router = APIRouter()

@router.post("/token")
def generate_token(user_id: int,quiz_id: int, n:int = 32, m:int = 5):
    
    admin_token = Token(n)
    player_token = Token(m)
    
    quiz = Quiz(user_id, quiz_id, admin_token, player_token)
    
    mem_quiz[(user_id, quiz_id)] = quiz
    
    return {"user_id": user_id,
            "quiz_id": quiz_id,
            "player_token": player_token.get_token(),
            "admin_token": admin_token.get_token()}

@router.post("/tokenGen", response_model=TokenModel)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db = Depends(get_db) ):
    response = log_user(UserLogin(user_name=form_data.username, user_password=form_data.password), db=db)
    return {"access_token": response.user_token, "token_type": "bearer"}