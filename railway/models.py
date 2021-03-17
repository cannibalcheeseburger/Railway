from railway import db

class Users(db.Model):
    uid = db.Column(db.String,primary_key = True)
    password = db.Column(db.String,nullable = False)
    balance = db.Column(db.Integer,default = 0)

class Trains(db.Model):
    uid = db.Column(db.String,primary_key = True)
    password = db.Column(db.String,nullable = False)
    balance = db.Column(db.Integer,default = 0)
class Booking(db.Model):
    book_id = db.Column(db.Integer,primary_key = True)
    uid = db.Column(db.String,nullable = False)
    train_id = db.Column(db.Integer,nullable = False)
    num_booked = db.Column(db.Integer,nullable = False)
