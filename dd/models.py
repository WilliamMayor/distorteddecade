import datetime

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
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
        return unicode(self.id)

    def is_editable(self):
        return self.email != 'mail@williammayor.co.uk'

    def is_deletable(self):
        return self.is_editable()

    def __repr__(self):
        return '<User %r>' % (self.username)

    def as_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }


class Intro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.date.today)

    def __iter__(self):
        for p in self.text.split('\n'):
            if p:
                yield p
