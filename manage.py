from flask import Flask
from app import create_app,db
from flask_script import Manager, Server
from app.models import User
from app import templates
from app import app 



app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db)
    

if __name__ == '__main__':
    manager.run()



