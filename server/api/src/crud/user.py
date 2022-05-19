from fastapi import HTTPException
from sqlalchemy.orm import Session
from .. import models 
from ..schemas import user as userSchemas
from ..utils import oauth2

def get_user(db: Session, user_id: int) : 
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_name(db: Session, user_name: str) : 
    resp = db.query(models.User).filter(models.User.user_name == user_name).first()
    return resp

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: userSchemas.UserCreate):
    hash = oauth2.get_password_hash(user.user_password)
    db_user = models.User(user_name=user.user_name, user_password=hash)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    response: userSchemas.User = userSchemas.User(id=db_user.id, user_name=db_user.user_name)
    return response
