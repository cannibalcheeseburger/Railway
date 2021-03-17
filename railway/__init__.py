from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://database.db'

db = SQLAlchemy(app)

from railway import routes