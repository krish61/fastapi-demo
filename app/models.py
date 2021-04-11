from app.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__="blogs"
    id = Column(Integer,primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("userss.id"))    #tablename.id
    created_by = relationship("User", back_populates="blogs")
    
class User(Base):
    __tablename__="userss"
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    blogs = relationship('Blog', back_populates='created_by')
