from typing import List
from fastapi import Depends, APIRouter
from ..utils.quiz import Quiz
from ..utils.token import Token
from ..utils.constant import GlobalVar

MEM_QUIZ = GlobalVar.MEM_QUIZ

router = APIRouter()


@router.post("/token")
def generate_token(user_id: int,quiz_id: int, n:int = 32, m:int = 5):
    
    admin_token = Token(n)
    player_token = Token(m)
    
    quiz = Quiz(user_id, quiz_id, admin_token, player_token)
    
    MEM_QUIZ[(user_id, quiz_id)] = quiz
    
    return {"user_id": user_id,
            "quiz_id": quiz_id,
            "player_token": player_token.get_token(),
            "admin_token": admin_token.get_token()}
