from app import create_app,db
from flask_script import Manager,Server,Shell
from app.models import *

app =create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User )



if __name__ == '__main__':
    manager.run()
