import asyncio

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