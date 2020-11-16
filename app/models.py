import flask
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Document):
    user_id = db.IntField(unique=True)
    username = db.StringField(max_length=35)
    email = db.StringField(max_length=50)
    password = db.StringField()
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def get_password(self, password):
        return check_password_hash(self.password, password)
    
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
    vote_id = db.StringField(unique=True)
    user_id = db.IntField()
    bunny_id = db.StringField()
    upvote = db.BooleanField()