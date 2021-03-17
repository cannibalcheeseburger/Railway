from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,IntegerField,SubmitField,BooleanField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    username= StringField('username',validators=[InputRequired()])
    password= PasswordField('password',validators=[InputRequired()])
    remember = BooleanField('Remember Me')
    submit  = SubmitField('Login')


class RegisterForm(FlaskForm):
    username= StringField('username',validators=[InputRequired()])
    password= PasswordField('password',validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[InputRequired()])
    submit  = SubmitField('Sign Up')

class AvailForm(FlaskForm):
    date = StringField('date')

class BookForm(FlaskForm):
    train_id = StringField('train_id',validators=[InputRequired()])
    count = IntegerField('count',validators=[InputRequired()])