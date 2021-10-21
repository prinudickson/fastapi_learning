from fastapi import APIRouter, Depends
import schemas, database
from sqlalchemy.orm import Session
import repository.user as user
from .oauth2 import get_current_user

router = APIRouter(
            prefix='/user',
            tags=['Users'])

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db), current_user: schemas.User=Depends(get_current_user)):
    return user.create_user(request, db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id:int, db: Session = Depends(database.get_db), current_user: schemas.User=Depends(get_current_user)):
    return user.get_user(id, db)   