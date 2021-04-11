from typing import List
from fastapi.param_functions import Depends
from app.hashing import Hash
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from app import schemas, models, database

router = APIRouter(tags=['users'], prefix='/user')
get_db = database.get_db
session = database.Session

@router.post("/", status_code=201)
async def create_user(request: schemas.UserSchema, db:session=Depends(get_db)):
    users = db.query(models.User).filter(models.User.email==request.email)
    if users.first():
        raise HTTPException(status_code=400, detail="Email Already exists")
    hashed_password = Hash().hash_password(request.password)
    user = models.User(name=request.name, password=hashed_password, email=request.email)
    db.add(user)
    db.commit()
    db.refresh(user)
    # return new_blog
    return user

@router.get("/", response_model=List[schemas.ShowUsers])
async def all_users(db:session=Depends(get_db)):
    users = db.query(models.User).all()
    return users
