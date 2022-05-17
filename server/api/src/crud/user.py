from sqlalchemy.orm import Session
from .. import models 
from ..schemas import user as userSchemas
import hashlib
import os

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: userSchemas.UserCreate):
    hash = hashlib.pbkdf2_hmac(
        'sha256', # The hash digest algorithm for HMAC
        user.password.encode('utf-8'), # Convert the password to bytes
        'mysaltysalt', # Provide the salt
        100000 # It is recommended to use at least 100,000 iterations of SHA-256 
    )
    db_user = models.User(user_name=user.user_name, user_password=hash)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user