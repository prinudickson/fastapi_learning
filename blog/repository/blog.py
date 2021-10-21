from fastapi import status, HTTPException
import schemas, models

def all_blog(db):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request:schemas.Blog, db):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id, db):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail= f"blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'deleted succesfully'

def update(id, request: schemas.Blog, db):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail= f"blog with id {id} not found")

    blog.update(request.dict())
    db.commit()
    return 'updated succesfully'

def show(id, response, db):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not available')
    return blog