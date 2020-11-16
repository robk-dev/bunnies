import flask
from app import db

class User(db.Document):
    user_id = db.IntField(unique=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)
    email = db.StringField(max_length=50)
    password = db.StringField(max_length=30)
    
class Bunny(db.Document):
    bunny_id = db.StringField(unique=True, max_length=20)
    name = db.StringField(max_length=50)
    bio = db.StringField(max_length=120)
    score = db.StringField(max_length=20)
    origin = db.StringField(max_length=50)
    
class Carrot(db.Document):
    carrot_id = db.StringField(unique=True)
    name = db.StringField(max_length=50)
    description = db.StringField(max_length=120)
    taste = db.StringField(max_length=20)
    texture = db.StringField(max_length=20)
    
class Vote(db.Document):
    vote_id = db.IntField(unique=True)
    user_id = db.IntField(unique=True)
    bunny_id = db.StringField(unique=True, max_length=20)
    upvote = db.BooleanField()