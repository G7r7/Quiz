from fastapi import FastAPI
from src.database import SessionLocal, engine
import src.models as models
from src.routes import users, quiz

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users.router)
app.include_router(quiz.router)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

