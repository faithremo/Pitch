from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.column(db.string(100),unique=True)
    username = db.column(db.string(100),unique=True)
    password = db.column(db.string(100))
    date_created =db.Column(db.DateTime(timezone=True), default=func.now())
    
