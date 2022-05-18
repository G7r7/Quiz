from sqlalchemy.orm import Session
from .. import models 
from ..schemas import user as userSchemas
import hashlib, uuid

def get_user(db: Session, user_id: int) : 
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: userSchemas.UserCreate):
    salt = "salé"
    hash = hashlib.sha512(user.user_password.encode() + salt.encode()).hexdigest()
    db_user = models.User(user_name=user.user_name, user_password=hash)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    response: userSchemas.User = userSchemas.User(id=db_user.id, user_name=db_user.user_name)
    return response