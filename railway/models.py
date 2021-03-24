from railway import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

class Users(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    uid = db.Column(db.String(20))
    password = db.Column(db.String(20),nullable = False)
    balance = db.Column(db.Integer,default = 0)
    bookings = db.relationship('Booking',backref='user',lazy = True)
    def __repr__(self):
        return f"User('{self.uid}','{self.password}',{self.balance})"

class Trains(db.Model):
    train_id = db.Column(db.Integer,primary_key = True)
    source = db.Column(db.String(30),nullable = False)
    destination = db.Column(db.String(30),nullable = False)
    seats_total = db.Column(db.Integer,nullable = False)
    seats_res = db.Column(db.Integer,nullable = False)
    _type = db.Column(db.String(20),nullable = False)
    cost = db.Column(db.Integer,nullable = False)
    date = db.Column(db.String(20),nullable = False)
    def __repr__(self):
        return f"User({self.train_id},'{self.source}','{self.destination}',{self.seats_total},{self.seats_res},'{self._type}',{self.cost},'{self.date}')"

class Booking(db.Model):
    book_id = db.Column(db.Integer,primary_key = True)
    uid = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    train_id = db.Column(db.Integer,db.ForeignKey('trains.train_id'),nullable = False)
    num_booked = db.Column(db.Integer,nullable = False)
    def __repr__(self):
            return f"User({self.book_id},'{self.uid}',{self.train_id},{self.num_booked})"
