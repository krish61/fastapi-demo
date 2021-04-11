from fastapi.exceptions import HTTPException
from app import models

def get_logged_in_user(db, user_email):
    user = db.query(models.User).filter(models.User.email==user_email).first()
    return user

def get_all_blogs(db):
    blogs = db.query(models.Blog).all()
    return blogs

def create_blog(db, title, body, user):
    new_blog = models.Blog(title=title, body=body, user_id=user.id, created_by=user)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_single_blog(db, blog_id):
    blog = db.query(models.Blog).filter(models.Blog.id==blog_id).first()
    if blog is None:
        raise HTTPException(status_code=404, detail=f"No Blog found with the {blog_id} id")
    return blog

def update_blog(db, title, blog_id):
    blog = db.query(models.Blog).filter(models.Blog.id==blog_id)
    if not blog.first():
        raise HTTPException(status_code=400,detail="Blog not Found")
    blog.update({'title': title})
    db.commit()
    return "done"

def delete_blog(db, blog_id):
    db.query(models.Blog).filter(models.Blog.id==blog_id).delete(synchronize_session=False)
    db.commit()
    return {'detail':'Blog deleted Successfully'}