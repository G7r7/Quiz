
from fastapi import FastAPI

api_server = FastAPI()


@api_server.get("/")
def read_root():
    return {"Hello": "World"}
