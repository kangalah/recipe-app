from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from datetime import datetime
from sqlalchemy.sql import func
from . import db


class Recipe(db.Model):
    
    __tablename__='recipes'
    
    id=db.Column(db.Integer, primary_key=True)
    recipe_title=db.Column(db.String, nullable=False)
    recipe_description=db.Column(db.String, nullable=False)
    is_public=db.Column(db.Boolean, nullable=False)
    image_filename=db.Column(db.String, default=None, nullable=True)
    image_url=db.Column(db.String, default=None, nullable=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
        
    def __init__(self, title, description, user_id, is_public, image_filename=None, image_url=None):
        self.recipe_title=title
        self.recipe_description=description
        self.is_public=is_public
        self.image_filename=image_filename
        self.image_url=image_url
        self.user_id=user_id
                
    def __repr__(self):
        return '<Title {}>'.format(self.title)

    
class User(UserMixin,db.Model):

    __tablename__='users'
    
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    username=db.Column(db.String(255))
    email=db.Column(db.String, unique=True, nullable=False)
    _password=db.Column(db.Binary(60), nullable=False)
    authenticated=db.Column(db.Boolean, default=False)
    email_confirmation_sent_on=db.Column(db.DateTime, nullable=True)
    email_confirmed=db.Column(db.Boolean, nullable=False)
    email_confirmed_on=db.Column(db.DateTime, nullable=True)

    def __init__(self, email, email_confirmation_sent_on=None,):
        self.email=email
        self.password=plaintext_password
        self.authenticated=False
        self.email_confirmation_sent_on=email_confirmation_sent_on
        self.email_confirmed=False
        self.email_confirmed_on=None
        

    @password.setter
    def set_password(self, plaintext_password):
    self._password=bcrypt.generate_password_hash(plaintext_password)


    def __repr__(self): 
        return '<User {}>'.format(self.name)

