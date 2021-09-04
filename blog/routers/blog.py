from fastapi import APIRouter, Depends, status
from typing import List
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import blog
from ..oauth2 import get_current_user

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)


@router.get("/", response_model=List[schemas.ShowBlog])
def get_all(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db),  current_user: schemas.User = Depends(get_current_user)):
    return blog.create_blog(request, db)


@router.get("/{blog_id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(blog_id: int, db: Session = Depends(database.get_db),  current_user: schemas.User = Depends(get_current_user)):
    return blog.get_blog(blog_id, db)


@router.delete("/{blog_id}")
def delete_blog(blog_id: int, db: Session = Depends(database.get_db),  current_user: schemas.User = Depends(get_current_user)):
    return blog.delete_blog(blog_id, db)


@router.put("/blog/{blog_id}", status_code=status.HTTP_202_ACCEPTED)
def update(blog_id: int, request: schemas.Blog, db: Session = Depends(database.get_db),  current_user: schemas.User = Depends(get_current_user)):
    return blog.update_blog(blog_id, request, db)
