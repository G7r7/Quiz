from fastapi.testclient import TestClient
from src.main import app
from src.schemas.quiz import Quiz, QuizCreate
from src.schemas.user import UserCreate, UserLogged
from tests.utils import get_logged_user

# def test_postQuiz():
#     user: UserLogged = get_logged_user()
#     json: QuizCreate = QuizCreate(date_creation="2022-01-18", user_id=user['id'], name="Monsuperqui zz").json()
#     response = TestClient(app).post("/quiz/", data=json, headers={'Authorization': user['user_token']})
#     assert response.status_code == 200