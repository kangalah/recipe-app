from ..models import User
from flask import render_template,request
from app import app 

@app.route('/')
def index():
    return render_template('home.html') 

