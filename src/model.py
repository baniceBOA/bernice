from .server import db
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime


class User(db.Model):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String,)
    password = Column(String)
    email = Column(String)
    post = relationship('Post', back_populates='user')


class Post(db.Model):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey('User.username'))
    user = relationship('User',back_populates='post')
    category = relationship('Category', back_populates='posts')
    html = Column(String)
    date = Column(DateTime,default=datetime.now)

class Category(db.Model):
    __tablename__ = 'Category'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    post_id = Column(Integer, ForeignKey('Post.id'))
    posts = relationship('Post', back_populates='category')
    

db.create_all()

