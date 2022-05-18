from fastapi import FastAPI
import socketio
from .routes import users, quiz, token
from .database import database
from . import models
from src.utils.constant import GlobalVar

app_socket = GlobalVar.APP_SOCKET

models.Base.metadata.create_all(bind=database.engine)


#TOKEN_COLLECTOR.start()

app = FastAPI()
app.include_router(users.router)
app.include_router(quiz.router)
app.include_router(token.router)


app.mount("/", app_socket)