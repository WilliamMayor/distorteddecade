from flask_wtf import Form
from wtforms import (
    StringField, PasswordField, TextAreaField, HiddenField, BooleanField)
from wtforms.validators import DataRequired, Optional
from wtforms.ext.dateutil.fields import DateTimeField


class SigninForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class IntroForm(Form):
    text = TextAreaField('Intro', validators=[DataRequired()])


class UserForm(Form):
    uid = HiddenField(validators=[Optional()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Optional()])


class BioForm(Form):
    bid = HiddenField()
    name = StringField('Name')
    role = StringField('Role')
    image = StringField('Image')
    text = TextAreaField('Bio')


class GigForm(Form):
    gid = HiddenField()
    name = StringField('Name')
    where = StringField('Where')
    url = StringField('URL')
    when = DateTimeField('When')
    hide = BooleanField('Hidden')
    private = BooleanField('Private')


class EmbedForm(Form):
    eid = HiddenField()
    name = StringField('Name')
    code = StringField('Code')
