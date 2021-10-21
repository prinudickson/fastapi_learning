from fastapi import APIRouter, Depends, status, Response
from typing import List
import schemas, database
from sqlalchemy.orm import Session
import repository.blog as blog
from .oauth2 import get_current_user

router = APIRouter(
            prefix="/blog",
            tags=['Blog'])

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowBlog])
def all_blog(db: Session = Depends(database.get_db), current_user: schemas.User=Depends(get_current_user)):
    return blog.all_blog(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User=Depends(get_current_user)):
    return blog.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_200_OK)
def destroy(id, db: Session = Depends(database.get_db), current_user: schemas.User=Depends(get_current_user)):
    return blog.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User=Depends(get_current_user)):
    return blog.update(id, request, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id, response: Response, db: Session = Depends(database.get_db), current_user: schemas.User=Depends(get_current_user)):
    return blog.show(id, response, db)