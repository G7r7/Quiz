from fastapi.testclient import TestClient
from src.main import app
from src.schemas.user import UserCreate

def test_postUser():
    json: UserCreate = UserCreate(user_name="Toto", user_password="titi").json()
    response = TestClient(app).post("/users/", data=json)
    assert response.status_code == 200