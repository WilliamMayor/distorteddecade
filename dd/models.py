import datetime

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()


class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    
    def check_password(self, candidate):
        return bcrypt.check_password_hash(self.password, candidate)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.uid)

    def __repr__(self):
        return '<User %r>' % (self.username)


class Intro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)

    def __iter__(self):
        for p in self.text.split('\n'):
            if p:
                yield p


class Bio(db.Model):
    bid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    role = db.Column(db.Text)
    image = db.Column(db.Text)
    text = db.Column(db.Text)

    def split_text(self):
        for p in self.text.split('\n'):
            if p:
                yield p
