from typing import Union
from sqlalchemy.orm import Session
from .. import models 
from ..schemas import response as responseSchemas

def create_response(db: Session, response: responseSchemas.ResponseCreate):
    db_response = models.Response(content = response.content, question_id = response.question_id, is_true = response.is_true)
    db.add(db_response)
    db.commit()
    db.refresh(db_response)
    response: responseSchemas.Response = responseSchemas.Response(id=db_response.id, content=db_response.content, question_id=db_response.question_id, is_true=db_response.is_true)
    return response