from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField,SubmitField
from wtforms.validators import Required,Length

from config import db


class loginForm(FlaskForm):
    username=StringField(
        '用户名',
        validators=[
            Required(),
            Length(50)
        ]
    )
    passwd=PasswordField(
        '密码',
        validators=[
            Length(8),
        ]
    )
    submit=SubmitField(
        '提交'
    )
