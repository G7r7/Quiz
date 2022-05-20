import asyncio
from ..schemas import question as questionSchema
from ..schemas import response as responseSchema
from ..utils.player import Player

from typing import List


async def parse_token(sio, sid, data, list_tokens, token="token"):
    if token not in data.keys():
        await sio.emit("token_not_found", to=sid)
        return
    elif data[token] not in list_tokens:
        await sio.emit("invalid_token", to=sid)
        return
    else:
        return data[token]
    
async def parse_name(sio, sid, data):
    if "name" not in data.keys():
        await sio.emit("name_not_found", to=sid)
        return
    else:
        return data["name"]
    
def create_data_qr(question: questionSchema.Question, responses: List[responseSchema.Response]):
    res, responses_server = dict(), dict()
    res["question"] = {"content": question.content, "question_id": int(question.id), "number_question": int(question.number_question)}
    res["responses"] = []
    responses_server["responses_server"] = []
    for response in responses:
        res["responses"].append({"id": int(response.id), "content": response.content})
        responses_server["responses_server"].append({"id": int(response.id), "content": response.content, "is_true": bool(response.is_true)})
    return res, responses_server

def get_correct_responses(responses_server):
    return [response for response in responses_server["responses_server"] if response["is_true"]]

def calculate_score_player(player: Player, correct_response):
    player_response = player.current_question_responses[0]
    correct_response = [response["id"] for response in correct_response]
    if player_response in correct_response:
        player.add_score(1)
    
    player.current_question_responses.clear()
        
        
def get_distinct_responses(player, n):
    not_finished = True
    len_player_response = len(player.current_question_responses)
    distinct_responses = []
    for response in player.current_question_responses:
        if response not in distinct_responses:
            distinct_responses.append(response)
    return distinct_responses[-n:]