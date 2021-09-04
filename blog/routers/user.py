from fastapi import APIRouter, Depends
from typing import List
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create_user(request, db)


@router.get("/{user_id}", response_model=schemas.ShowUser)
def show_user(user_id: int, db: Session = Depends(database.get_db)):
    return user.get_user(user_id, db)


@router.get("/", response_model=List[schemas.ShowUser])
def show_all_users(db: Session = Depends(database.get_db)):
    return user.get_all_users(db)
