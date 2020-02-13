from app import creat_app
from app .models import User

@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User)