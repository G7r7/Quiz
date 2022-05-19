from fastapi.testclient import TestClient
from src.main import app
from src.schemas.user import UserCreate, UserLogin
from utils import create_user, test_db

def test_postUser(test_db):
    json: UserCreate = UserCreate(user_name="Toto", user_password="titi").json()
    response = TestClient(app).post("/users/", data=json)
    assert response.status_code == 200

def test_login(test_db):
    create_user()
    json: UserLogin = UserLogin(user_name="Toto", user_password="titi").json()
    response = TestClient(app).post("/users/login", data=json)
    assert response.status_code == 200

def test_incorrect_login(test_db):
    create_user()
    json: UserLogin = UserLogin(user_name="Toti", user_password="titi").json()
    response = TestClient(app).post("/users/login", data=json)
    assert response.status_code == 401

def test_incorrect_password(test_db):
    create_user()
    json: UserLogin = UserLogin(user_name="Toto", user_password="tii").json()
    response = TestClient(app).post("/users/login", data=json)
    assert response.status_code == 401