from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import socketio
from .routes import users, quiz, token
from .database import database
from . import models
from .utils.constant import app_socket
from .utils.oauth2 import oauth2_scheme, pwd_context

models.Base.metadata.create_all(bind=database.engine)

#TOKEN_COLLECTOR.start()

app = FastAPI()
app.include_router(users.router)
app.include_router(quiz.router)
app.include_router(token.router)

app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*'],
)

app.mount("/", app_socket)
