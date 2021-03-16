from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,IntegerField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    username= StringField('username',validators=[InputRequired()])
    password= PasswordField('password',validators=[InputRequired()])

class RegisterForm(FlaskForm):
    username= StringField('username',validators=[InputRequired()])
    password= PasswordField('password',validators=[InputRequired()])

class AvailForm(FlaskForm):
    date = StringField('date')

class BookForm(FlaskForm):
    train_id = StringField('train_id',validators=[InputRequired()])
    count = IntegerField('count',validators=[InputRequired()])