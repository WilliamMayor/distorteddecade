from flask.ext.login import LoginManager

from models import User


manager = LoginManager()
manager.login_view = 'admin.signin'


@manager.user_loader
def load_user(uid):
    return User.query.get(int(uid))
