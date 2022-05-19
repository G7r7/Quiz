import json
import typing
from fastapi.testclient import TestClient
import pytest
from src.main import app
from src.models import User
from src.schemas.quiz import Quiz, QuizCreate
from src.schemas.user import UserCreate, UserLogged, UserLogin
from src import models
from src.database.database import engine

@pytest.fixture()
def test_db():
    models.Base.metadata.create_all(bind=engine)
    yield
    models.Base.metadata.drop_all(bind=engine)

def create_user() -> User:
    json: UserCreate = UserCreate(user_name="Toto", user_password="titi").json()
    response: User = TestClient(app).post("/users/", data=json)
    return response

def log_user() -> UserLogged:
    json: UserLogin = UserLogin(user_name="Toto", user_password="titi").json()
    response: UserLogged = TestClient(app).post("/users/login", data=json)
    return response

def get_logged_user() -> UserLogged:
    create_user()
    return json.loads(log_user().content)

