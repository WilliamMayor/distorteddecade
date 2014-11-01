import os
from flask import Flask

from . import admin, public
from assets import assets


def create_app():
    app = Flask(__name__)
    app.config.from_object('dd.config')
    app.config.from_pyfile('.env', silent=True)
    for k in app.config:
        v = os.environ.get(k, None)
        if v is not None:
            app.config[k] = v

    assets.init_app(app)
    
    app.register_blueprint(admin.admin, url_prefix='/admin')
    app.register_blueprint(public.public)
    return app
