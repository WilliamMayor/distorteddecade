from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, HiddenField
from wtforms.validators import DataRequired
from flask_wtf.html5 import URLField


class SigninForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class BioForm(Form):
    bid = HiddenField()
    name = StringField('Name')
    role = StringField('Role')
    image = StringField('Image')
    text = TextAreaField('Bio')
