from src import avail,all_trains,booking,all_booked,cancel
from flask import Flask
from flask import render_template
from flask import request, redirect


app = Flask(__name__)

@app.route('/')
def home():
    rows = all_trains.all_trains()
    return render_template('home.html',rows = rows)

@app.route('/all')
def allTrains():
    rows = all_trains.all_trains()
    return render_template('all.html',rows = rows)

@app.route('/avail',methods=['POST','GET'])
def available():
    dat = request.form['date']
    rows = avail.Avail(dat)
    return render_template('avail.html',rows = rows)



@app.route('/all_booked')
def booked():
    rows = all_booked.all_book()
    return render_template('all_booked.html',rows = rows)

@app.route('/book')
def bookings():
    rows = all_trains.all_trains()
    return render_template('home.html',rows = rows)

@app.route('/cancel')
def cancelling():
    rows = all_trains.all_trains()
    return render_template('home.html',rows = rows)


if __name__ == "__main__":
    app.run()

