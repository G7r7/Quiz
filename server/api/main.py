from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session



import socketio

import json
import asyncio

import uvicorn

import src.crud as crud
import src.models as models
import src.schemas as schemas
from src.database import SessionLocal, engine

from src.utils.memory_quiz import *
from src.utils.token import *
from src.utils.quiz import *
from src.utils.fun import *
from src.utils.token_collector import TokenCollector

#models.Base.metadata.create_all(bind=engine)
MEM_QUIZ = MemoryQuiz()

TOKEN_COLLECTOR = TokenCollector(mem=MEM_QUIZ, interval=1)
#TOKEN_COLLECTOR.start()

app = FastAPI()

sio = socketio.AsyncServer(logger=True, engineio_logger=True, async_mode='asgi', cors_allowed_origins="*")
app_socket = socketio.ASGIApp(sio)


@sio.event
async def enter_quiz(sid, data):
    
    recieved_token = await parse_token(sio, sid, data, list_tokens=MEM_QUIZ.player_tokens())
    player_name = await parse_name(sio, sid, data)
    
    if recieved_token is None or player_name is None:
        return
        
    quiz = MEM_QUIZ[recieved_token]
    if not quiz.open_to_register:
        await sio.emit("quiz_closed_to_register", to=sid)
        return
        
    player = Player(sid, player_name)
                
    if player in quiz.players:
        await sio.emit("user_already_joined", to=sid)
    else:
        quiz.add_player(player)
        sio.enter_room(sid, recieved_token)
        await sio.emit("quizjoin", to=sid)

            

        
@sio.event
async def start_quiz(sid, data):
    
    recieved_player_token = await parse_token(sio, sid, data, list_tokens=MEM_QUIZ.player_tokens(), token="player_token")
    recieved_admin_tokens = await parse_token(sio, sid, data, list_tokens=MEM_QUIZ.admin_tokens(), token="admin_token")

    if recieved_player_token is not None and recieved_admin_tokens is not None:
        
        quiz = MEM_QUIZ[recieved_player_token]
        MEM_QUIZ.play_quiz(quiz)
        
        await sio.emit("start_quiz", room=recieved_admin_tokens, skip_sid=sid)
        
        list_questions = ""
        create_question = lambda x : x
        
        for question in list_questions:
            
            data_question = create_question(question)
            await sio.emit("send_question", room=recieved_admin_tokens, skip_sid=sid, data=data_question)
            
            # Sleep
            # Calculate score of each player
            # Pass to next question
            
        # Broadcast Winner
        # Clean infos in MEM_QUIZ
        MEM_QUIZ.end_quiz(quiz)
        
    else:
        await sio.emit("not_auth_to_start_quiz", to=sid)
            
        

@sio.event
async def receive_response(sid, data):
    player = MEM_QUIZ.get_player_from_sid()
    player.add_response(data)
    
    


@app.post("/token")
def generate_token(user_id: int,quiz_id: int, n:int = 32, m:int = 5):
    
    admin_token = Token(n)
    player_token = Token(m)
    
    quiz = Quiz(user_id, quiz_id, admin_token, player_token)
    
    MEM_QUIZ[(user_id, quiz_id)] = quiz
    
    return {"user_id": user_id,
            "quiz_id": quiz_id,
            "player_token": player_token.get_token(),
            "admin_token": admin_token.get_token()}































app.mount("/", app_socket)

if __name__ == "__main__":
    try:
        uvicorn.run("main:app")
        print("Je suis là")
    except Exception as e:
        TOKEN_COLLECTOR.stop()
        TOKEN_COLLECTOR.join()
        raise(e)