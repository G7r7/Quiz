from fastapi import FastAPI
from .routes import users, quiz
from .database import database
from . import models

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(users.router)
app.include_router(quiz.router)
