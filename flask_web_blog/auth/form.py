from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Email, Required, Length, Regexp, EqualTo, ValidationError

from models import User


class LoginForm(FlaskForm):
    email = StringField('email',validators=[Required(),Length(1,100),Email()])
    password=PasswordField('password',validators=[Required()])
    remember_me=BooleanField('keep me logged in')
    submit=SubmitField('login')
class RegistrationForm(FlaskForm):
    email=StringField('email',validators=[Required(),Length(1,100),Email()])
    username=StringField('username',validators=[Required(),Length(1,100),
            Regexp('^[a-zA-Z][a-zA-Z0-9_.]*$',0,'user must have only letters number,'
                                                'dots or underscores')])
    password=PasswordField('password',validators=[Required(),EqualTo('password2',message='password must match')])
    password2=PasswordField('confirm password',validators=[Required()])
    submit=SubmitField('Register')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('email already registered.')
    def validate_username(self,field):
        if User.query.filter_by(uname=field.data).first():
            raise ValidationError('username alreasy to use')