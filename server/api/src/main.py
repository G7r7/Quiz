from src.routes import users, quiz, question, response
from src.database import database
from fastapi import Depends, FastAPI, Request
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
import socketio
from .routes import users, quiz, token
from .database import database
from . import models
from .utils.constant import app_socket

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

app.mount("/ws", app_socket)
