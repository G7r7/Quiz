from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from ..database.get_db import get_db
from ..schemas import user as userSchemas
from ..crud import user as userCrud

router = APIRouter()

@router.post("/users/", response_model=userSchemas.User)
def create_user(user: userSchemas.UserCreate, db: Session = Depends(get_db)):
    return userCrud.create_user(db=db, user=user)

@router.get("/users/list", response_model=List[userSchemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = userCrud.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/users/{user_id}", response_model=userSchemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = userCrud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
