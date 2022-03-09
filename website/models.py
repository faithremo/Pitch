from sqlalchemy import false
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    pitches = db.relationship('Pitch', backref='user', passive_deletes=True)
    
    class Pitch(db.model):
        id = db.Column(db.Integer, primary_key=True)
        text = db.column(db.Text, nullable=false)
        date_created = db.Column(db.DateTime(timezone=True), default=func.now())
        author =db.column(db.Integer, db.ForeinKey('user.id', ondelete="CASCADE"), nullable=False)