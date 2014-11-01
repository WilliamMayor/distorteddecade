from flask import g
from flask.ext.login import LoginManager, current_user

from models import User


manager = LoginManager()
manager.login_view = 'admin.signin'


@manager.user_loader
def load_user(id):
    return User.query.get(int(id))