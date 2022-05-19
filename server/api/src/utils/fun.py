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
    res["question"] = {"content": question.content, "question_id": question.id, "number_question": question.number_question}
    res["responses"] = []
    responses_server["responses_server"] = []
    for response in responses:
        res["responses"].append({"id": response.id, "content": response.content})
        responses_server["responses_server"].append({"id": response.id, "content": response.content, "is_true": response.is_true})
    return res, responses_server

def get_correct_responses(responses_server):
    return [response["id"] for response in responses_server.values() if response["is_true"]]

def calculate_score_player(player: Player, correct_response):
    player_response = player.current_question_responses[-1]
    if player_response in correct_response:
        player.add_score(1)
    player.current_question_responses.clear()
        