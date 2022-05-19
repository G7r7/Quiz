from fastapi.testclient import TestClient
from src.main import app
from src.schemas.quiz import Quiz, QuizCreate
from src.schemas.user import UserCreate, UserLogged
from tests.utils import get_logged_user
from utils import create_user, test_db

def test_postQuiz(test_db):
    user: UserLogged = get_logged_user()
    json: QuizCreate = QuizCreate(date_creation="2022-01-18", user_id=user['id'], quiz_name="Monsuperqui zz").json()
    response = TestClient(app).post("/quiz/", data=json, headers={'Authorization': "bearer" + user['user_token']})
    assert response.status_code == 200