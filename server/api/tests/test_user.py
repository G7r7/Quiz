from fastapi.testclient import TestClient
from src.main import app
from src.schemas.user import UserCreate, UserLogged, UserLogin
from utils import create_user, get_logged_user, test_db

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

def test_user_list(test_db):
    create_user()
    response = TestClient(app).get("/users/list")
    assert response.status_code == 200

def test_user_me(test_db):
    user: UserLogged = get_logged_user()
    response = TestClient(app).post("/users/me", headers={"Authorization": f'Bearer {user["user_token"]}'})
    assert response.status_code == 200