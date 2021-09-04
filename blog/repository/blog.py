from .. import models
from fastapi import status, HTTPException


def get_all(db):
    blogs = db.query(models.Blog).all()
    return blogs


def create_blog(request, db):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_blog(blog_id, db):
    blogs = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {blog_id} is not available")
    return blogs


def delete_blog(blog_id, db):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {blog_id} is not available")
    blog.delete(synchronize_session=False)
    db.commit()
    return "done"


def update_blog(blog_id, request, db):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {blog_id} is not available")
    blog.update(request.dict())
    db.commit()
    return "blog is updated in the db"

