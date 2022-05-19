from pytest import skip
from ..utils.constant import mem_quiz, sio
from ..utils.fun import *
from ..utils.player import Player
from ..database.get_db import get_db
from ..crud import question as questionCrud
from ..crud import response as responseCrud

@sio.event
async def new_room_added(sid, data):
    await sio.emit("new_room_added", data=data)
    
    
@sio.event
async def connect(sid, environ, auth):
    
    data = dict()
    i = 0
    for quiz in mem_quiz.quizs.values():
        data[i] = {"player_token": quiz.player_token, "quiz_name": quiz.name}
    await sio.emit("all_rooms", {"data": {i : {"player_token": player_token, "quiz_name": mem_quiz} for i, player_token in zip(range(len(mem_quiz.quizs)), mem_quiz.player_tokens())}})


@sio.event
async def enter_quiz(sid, data):
    
    recieved_token = await parse_token(sio, sid, data, list_tokens=mem_quiz.player_tokens(), token="player_token")
    
    if recieved_token is None:
        return
    
    player_name = await parse_name(sio, sid, data)
    
    if player_name is None:
        return
    
    
        
    quiz = mem_quiz[recieved_token]
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
        await sio.emit("new_player_joined", to=recieved_token)

            

        
@sio.event
async def start_quiz(sid, data):
    
    recieved_player_token = await parse_token(sio, sid, data, list_tokens=mem_quiz.player_tokens(), token="player_token")
    
    if recieved_player_token is None:
        return
    
    recieved_admin_tokens = await parse_token(sio, sid, data, list_tokens=mem_quiz.admin_tokens(), token="admin_token")
    
    if recieved_admin_tokens is None:
        return

    if recieved_player_token is not None and recieved_admin_tokens is not None:
        
        quiz = mem_quiz[recieved_player_token]
        mem_quiz.play_quiz(quiz)
        
        await sio.emit("start_quiz", room=recieved_player_token)
        
        db =  next(get_db())
        
        quiz_id = quiz.id
        list_questions = questionCrud.get_questions(db, quiz_id)
        
        for question in list_questions:
            
            list_response = responseCrud.get_responses(db, question.id)
            data_to_send, response = create_data_qr(question, list_response)
            await sio.emit("send_question", {"data": data_to_send}, room=recieved_player_token, skip_sid=sid)
            
            
            # Sleep
            await sio.sleep(10)
            # Calculate score of each player
            await sio.emit("stop_sending", room=recieved_player_token, skip_sid=sid)
            
            correct_response = get_correct_responses(response)
            
            for player in quiz.players:
                calculate_score_player(player, correct_response)
                
            await sio.emit("correct_response", room=recieved_player_token, skip_sid=sid)
            
            await sio.sleep(5)
            
            await sio.emit("next_question", room=recieved_player_token, skip_sid=sid)
            
        # Broadcast Winner
        
        winner = quiz.get_winners()
        
        await sio.emit("winner",{"name": winner.name}, room=recieved_player_token, skip_sid=sid)
        
        await sio.sleep(5)
        
        # Clean infos in mem_quiz
        mem_quiz.end_quiz(quiz)
    
        

@sio.event
async def receive_response(sid, data):
    player = mem_quiz.get_player_from_sid()
    player.add_response(data)
    