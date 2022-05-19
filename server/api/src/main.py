from src.routes import users, quiz, question, response
from src.database import database
from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import socketio
from src.database.get_db import get_db
from .routes import users, quiz, token
from .database import database
from . import models
from .utils.constant import app_socket
from .utils.oauth2 import oauth2_scheme, pwd_context, get_current_user

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*'],
)
app.include_router(users.router)
app.include_router(quiz.router)
app.include_router(question.router)
app.include_router(response.router)
app.include_router(token.router)


logged_routes=["/quiz/"]


app.mount("/ws", app_socket)
