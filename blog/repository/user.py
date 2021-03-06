from fastapi import status, HTTPException
from .. import models
from ..hashing import Hash


def create_user(request, db):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(user_id, db):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User id {user_id} is not there in the db")
    return user


def get_all_users(db):
    users = db.query(models.User).all()
    return users
