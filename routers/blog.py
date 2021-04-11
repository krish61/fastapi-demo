from fastapi.exceptions import HTTPException
from sqlalchemy.orm import session
from starlette.responses import Response
from app import models, schemas, database, oauth
from handlers import blog_handlers
from typing import List
from fastapi import APIRouter, Depends

router = APIRouter(tags=['blogs'], prefix='/blogs')

get_db = database.get_db
session = database.Session
@router.get("/", response_model=List[schemas.ShowBlog])
async def all_blogs(db:session=Depends(get_db),current_user: schemas.UserSchema = Depends(oauth.get_current_user)):
    blogs = blog_handlers.get_all_blogs(db)
    return blogs

@router.post("/", status_code=201, response_model=schemas.ShowBlog)
async def create_blog(request: schemas.Blog, db:session=Depends(get_db),current_user: schemas.UserSchema = Depends(oauth.get_current_user)):
    logged_in_user = blog_handlers.get_logged_in_user(db, current_user.email)
    blog = blog_handlers.create_blog(db, request.title, request.body, logged_in_user)
    return blog

@router.get("{id}/", status_code=200, response_model=schemas.ShowBlog)
async def single_blog(id:int, response:Response, db:session=Depends(get_db)):
    blog = blog_handlers.get_single_blog(db, id)
    return blog

@router.put("{id}", status_code=200)
async def update_blog(id:int, request: schemas.Blog, db:session=Depends(get_db)):
    blog = blog_handlers.update_blog(db, request.title, request.body, id)
    return blog

@router.delete("{id}/", status_code=204)
async def delete_blog(id:int, response:Response, db:session=Depends(get_db)):
    blog = blog_handlers.delete_blog(db, id)
    return blog