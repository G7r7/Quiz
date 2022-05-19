from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from ..database.get_db import get_db
from ..schemas import response as responseSchemas
from ..crud import response as responseCrud

router = APIRouter()

@router.post("/response/", response_model=responseSchemas.Response)
def create_response(response: responseSchemas.ResponseCreate, db: Session = Depends(get_db)):
    return responseCrud.create_response(db=db, response=response)