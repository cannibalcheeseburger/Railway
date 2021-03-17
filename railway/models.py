from railway import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Users(db.Model,UserMixin):
    uid = db.Column(db.String(20),primary_key = True)
    password = db.Column(db.String(20),nullable = False)
    balance = db.Column(db.Integer,default = 0)

class Trains(db.Model):
    uid = db.Column(db.String,primary_key = True)
    password = db.Column(db.String,nullable = False)
    balance = db.Column(db.Integer,default = 0)
class Booking(db.Model):
    book_id = db.Column(db.Integer,primary_key = True)
    uid = db.Column(db.String(20),nullable = False)
    train_id = db.Column(db.Integer,nullable = False)
    num_booked = db.Column(db.Integer,nullable = False)
