from fastapi import FastAPI
from src.routes import users, quiz
from src.database import database
from fastapi.middleware.cors import CORSMiddleware
import src.models

src.models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(users.router)
app.include_router(quiz.router)
app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*'],
)